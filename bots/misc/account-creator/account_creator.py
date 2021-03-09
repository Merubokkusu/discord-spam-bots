#
# account_creator.py
# @author Merubokkusu
# @created 2020-01-14T22:58:46.871Z-05:00
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified 2021-03-09T17:45:06.061Z-05:00
#

import requests
import json
import sys
import os
from time import sleep
from twocaptcha import TwoCaptcha
sys.path.append("././.")
from config import captchaAPI

account_Email = sys.argv[1]
account_Password = sys.argv[2]
PROXY = sys.argv[3]
#API_KEY = captchaAPI # Your 2captcha API KEY in the config file
solver = TwoCaptcha(captchaAPI)
site_key = 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34' 
discordUrl = "https://discordapp.com/api/v6/auth/register"
currentAcc = account_Email.split("@", 1)[0]

def create():
    proxy = {
        'http': 'http://'+PROXY
    }

    # s = requests.Session()
    # captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url)).text.split('|')[1]
    # recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    # print(currentAcc, "Trying to solve captcha...")
    # while 'CAPCHA_NOT_READY' in recaptcha_answer:
    #     sleep(5)
    #     recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
    #     print(currentAcc, "2captcha: Not ready, please wait...")
    # print(currentAcc, "2captcha: ", recaptcha_answer.split('|')[0])
    # recaptcha_answer = recaptcha_answer.split('|')[1]
    recaptcha_answer = solver.hcaptcha(sitekey=site_key,url=discordUrl)

    #This is the main login.
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        "content-type": "application/json",
        "Connection": "keep-alive",
    }

    payload = {
        "email": account_Email,
        "username": account_Email.split("@", 1)[0],
        "password": account_Password,
        "invite": None,
        "consent": True,
        "gift_code_sku_id": None,
        "captcha_key": recaptcha_answer,
    }

    # Post register to discord
    r = requests.post(discordUrl, data=json.dumps(payload), headers=headers, proxies=proxy)
    
    sleep(0.5)
    if(r.status_code == 201 or 200 or 202):
        file = open('tokens.txt','a')
        fileCompleted = open('account_creator_completed.txt','a+')
        if 'message' in r.json():
            print(currentAcc, ": Discord:", r.json()['message'], 'Retry in seconds: ', r.json()['retry_after'])
        if 'email' in r.json():
            print(currentAcc, ': ', r.json()['email'])
            fileCompleted.writelines(account_Email + '\n')
            print(currentAcc, ": Account creation completed!")
        if 'token' in r.json():
            file.writelines(account_Email + ":" + account_Password + ":" + r.json()['token'] + '\n')
            fileCompleted.writelines(account_Email + '\n')
            print(currentAcc, ": Account creation completed!")
    
create()
