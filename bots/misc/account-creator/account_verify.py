#
# acccount_verify.py
# @author Merubokkusu
# @created 2019-03-04T19:25:41.012Z-05:00
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified 2021-03-09T17:43:27.010Z-05:00
#

import requests
import json
import sys
import os
import poplib
import time
from email import parser
from html.parser import HTMLParser
from time import sleep
from twocaptcha import TwoCaptcha
sys.path.append("././.")
from config import captchaAPI, mailServer

account_Email = sys.argv[1]
account_Password = sys.argv[2]
PROXY = sys.argv[3]
TOKEN = sys.argv[4]
foundLink = False
#API_KEY = captchaAPI
solver = TwoCaptcha(captchaAPI)
site_key = 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34' 
currentAcc = account_Email.split("@", 1)[0]
checkedTimes = 0

proxy = {
    'http': 'http://'+PROXY
}

def resolve(url):
    s = requests.Session()
    url = s.get(url).url
    if 'https://discord.com/verify' in url:
        return url
    else:
        return None

class MyHTMLParser(HTMLParser): # From https://stackoverflow.com/a/3075561/6058560

    def handle_starttag(self, tag, attrs):
        global verifyLink
        if tag == "a":
           for name, value in attrs:
               if name == "href":
                    if 'click.discord.com/ls/click' in value:
                        verifyLinkObscured = str(value)
                        resolveObscuredLink = resolve(verifyLinkObscured)
                        if resolveObscuredLink is not None:
                            verifyLink = resolve(verifyLinkObscured)
                            print(currentAcc, "VERIFY LINK: ", verifyLink)

def sendEmail():
    url = 'https://discord.com/api/v6/auth/verify/resend'
    headers = {"content-type": "application/json", "authorization": TOKEN }

    r = requests.post(url, headers=headers, proxies=proxy)

    if(r.status_code == 200 or 204):
        print(currentAcc, "Token: '" + TOKEN[-25] + "' had the email resent.")
        sleep(5) # should sleep some here 
        checkEmail()
    elif(r.status_code == 429):
        print(currentAcc, r.status_code, 'ERROR, TOO MANY REQUESTS')
    else:
        print(currentAcc, r.status_code, 'ERROR, something went wrong. Make sure your user token is correct | https://discordhelp.net/discord-token')

def checkEmail():
    global checkedTimes
    foundLink = False
    pop_conn = poplib.POP3_SSL(mailServer)
    pop_conn.user(account_Email)
    pop_conn.pass_(account_Password)

    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    messages = ['\n'.join(map(bytes.decode, mssg[1])) for mssg in messages]
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]

    for message in messages:
        if(str.startswith(message['from'],"Discord") & foundLink == False):
            print(currentAcc, "FOUND " + '"'+ message['subject'] +'"')
            foundLink = True
            for part in message.walk():
                if part.get_content_type():
                    body = part.get_payload(decode=True)
                    thisbody = str(body)
                    MyHTMLParser().feed(thisbody)
            #pop_conn.dele(len(pop_conn.list()[1])) # Delete newest email when found
            break # No ne ed to look for more emails

    if(foundLink == False):
        checkedTimes += 1
        print(currentAcc, "Couldnt find email, waiting two seconds:", account_Email)
        time.sleep(2)
        pop_conn.quit()
        if checkedTimes >= 10:
            print(currentAcc, "Couldnt find email after 10 retries, stopping!")
            exit()
        checkEmail()
    elif(foundLink == True):
        pop_conn.quit()
        verifyAccount()

def verifyAccount():
    discordUrl = 'https://discordapp.com/'
    print(currentAcc, "Starting verification")
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
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        "content-type": "application/json",
        "Connection": "keep-alive",
    }
    payload = {
        "token": verifyLink[33:],
        "captcha_key": recaptcha_answer,
    }
    r = requests.post("https://discord.com/api/v6/auth/verify", data=json.dumps(payload), headers=headers, proxies=proxy)
    if(r.status_code == 200):
        fileCompleted = open('account_verify_completed.txt','a+')
        fileCompleted.writelines(account_Email + '\n')
        print(currentAcc, ": Account verification completed!")
    else:
        print(currentAcc, "Account verification failed! Either already verified or wrong token. Error: ", r.status_code)

sendEmail()