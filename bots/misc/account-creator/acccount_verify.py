#
# acccount_verify.py
# @author Merubokkusu
# @created 2019-03-04T19:25:41.012Z-05:00
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified 2020-01-23T02:08:15.630Z-05:00
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
sys.path.append("././.")
from config import *

account_Email = sys.argv[1]
account_Password = sys.argv[2]
PROXY = sys.argv[3]
TOKEN = sys.argv[4]
foundLink = False
API_KEY = captchaAPI
site_key = '6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn' 

proxy = {
        'http': 'http://'+PROXY
}

class MyHTMLParser(HTMLParser): # From https://stackoverflow.com/a/3075561/6058560

    def handle_starttag(self, tag, attrs):
        global verifyLink
        if tag == "a":
           for name, value in attrs:
               if name == "href":
                       if str.startswith(value,'https://discordapp.com/verify'):
                                verifyLink = str(value)
def sendEmail():
        url = 'https://discordapp.com/api/v6/auth/verify/resend'
        print(url)
        headers = {"content-type": "application/json", "Authorization": TOKEN }

        r = requests.post(url,headers=headers,proxies=proxy)
        if r.status_code == 200 or 204:
                print("Token:"+"'"+TOKEN[-25]+"'"+" had the email resent.")
                checkEmail()
        else:
                print(r.status_code)
                print('error, something went wrong.')
                print('Make sure your token is correct | https://discordhelp.net/discord-token')
def checkEmail():
        foundLink = False
        pop_conn = poplib.POP3_SSL(mailServer)
        pop_conn.user(account_Email)
        pop_conn.pass_(account_Password)

        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        messages = ['\n'.join(map(bytes.decode, mssg[1])) for mssg in messages]
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]

        for message in messages:
                if(str.startswith(message['from'],"Discord") & foundLink == False):
                        print("FOUND " + '"'+ message['subject'] +'"')
                        foundLink = True
                        for part in message.walk():
                                if part.get_content_type():
                                        body = part.get_payload(decode=True)
                                        thisbody = str(body)
                                        MyHTMLParser().feed(thisbody)                                      
        if(foundLink == False):
                print("couldnt find email, waiting two seconds")
                time.sleep(2)
                pop_conn.quit() 
                checkEmail()
        else:
                pop_conn.quit()
                verifyAccount()

def verifyAccount():
        url = 'https://discordapp.com/'
        print(verifyLink)
        s = requests.Session()
        captcha_id = s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url)).text.split('|')[1]
        recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
        print("solving ref captcha...")
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
                sleep(5)
                recaptcha_answer = s.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
        recaptcha_answer = recaptcha_answer.split('|')[1]
        headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        "content-type": "application/json",
        "Connection": "keep-alive",
        }

        payload = {
                "token": verifyLink[:36],
                "captcha_key": recaptcha_answer,}
        r = requests.post(verifyLink,data=json.dumps(payload),headers=headers, proxies=proxy)
        print(r.status_code)
        print(r.content)

sendEmail()
