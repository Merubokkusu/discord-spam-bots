#
# start.py
# @author Merubokkusu
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2019
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified Tue Mar 05 2019 02:11:47 GMT-0500 (Eastern Standard Time)
#

import sys
import subprocess
import os
from time import sleep
from config import *

proxy_number = 0
spam_text = None

if os.path.exists('tokens.txt'):
    userToken = open("tokens.txt").read().splitlines()
    w1 = "EDIT YOUR CONFIG.PY BEFORE USING!\n-=Using tokens.txt=-\n"
else:
    w1 = "EDIT YOUR CONFIG.PY BEFORE USING!\n"

if os.path.exists('proxies.txt'):
    proxy_list = open("proxies.txt").read().splitlines()
else:
    proxy_list = []
    for token in userToken:
        proxy_list.append('localhost')

if os.path.exists('combolist.txt'):
    emailList = open("combolist.txt").read().splitlines()
if os.path.exists('token_gen.txt'):
    tokenV = open("token_gen.txt").read().splitlines()

if len(sys.argv) < 2:
    for char in w1:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(0.5)
    print("Type one of the following numbers to launch that spammmer")
    print("       +========-Server Spammers-=========+")
    print("1 : Text Spammer - Write your own text to spam")
    print("2 : Image Spammer - Spam random images in a selected folder")
    print("3 : Insult Spammer - Picks insults online and spams them")
    print("         +========-DM Spammers-=========+      ")
    print("4 : Text Spammer - Write your own text to spam")
    print("5 : Image Spammer - Spam random images in a selected folder")
    print("6 : Insult Spammer - Picks insults online and spams them")
    print("           +========-Other-=========+")
    print("7 : Join Server - Join the server thats written in the config")
    print("           +========-Account Creator-=========+")
    print("8 : Account creator - Create bulk accounts")
    print("9 : Account verifier - Verify accounts")

    in_pick = float(input("Select a bot: "))
else:
    in_pick = float(sys.argv[1])
    spam_text = sys.argv[2]


if in_pick == 1:
    if os.path.exists('text.txt'):
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/server/discord_text_spam.py',token,'null',proxy_list[proxy_number]])
            proxy_number += 1
            sleep(1)
    else:
        if spam_text == None:
            spam_text = input("Write spam text : ")
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/server/discord_text_spam.py',token,spam_text,proxy_list[proxy_number]])
            proxy_number += 1
            sleep(1)

if in_pick == 2:
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots/server/discord_image_spam.py', token,proxy_list[proxy_number]])
        proxy_number += 1

if in_pick == 3:
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots/server/discord_insult_spam.py', token,proxy_list[proxy_number]])
        proxy_number += 1

#DM Spammers
if in_pick == 4:
    if os.path.exists('text.txt'):
        if not os.path.exists('dm_spam_text.txt'):
            file = open('dm_spam_text.txt','w')
            file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
            file.close()
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/DM/discord_text_spam_dm.py',token,'null',proxy_list[proxy_number]])
            proxy_number += 1
            sleep(2.5)
    else:
        if not os.path.exists('dm_spam_text.txt'):
            file = open('dm_spam_text.txt','w')
            file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
            file.close()
        if spam_text == None:
            spam_text = input("Write spam text : ")
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/DM/discord_text_spam_dm.py',token,spam_text,proxy_list[proxy_number]])
            proxy_number += 1
            sleep(2.5)

if in_pick == 5:
    if not os.path.exists('dm_spam_image.txt'):
        file = open('dm_spam_image.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots/DM/discord_image_spam_dm.py', token,proxy_list[proxy_number]])
        proxy_number += 1

if in_pick == 6:
    if not os.path.exists('dm_spam_insult.txt'):
        file = open('dm_spam_insult.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots/DM/discord_insult_spam_dm.py', token,proxy_list[proxy_number]])
        proxy_number += 1

if in_pick == 7:
    for token in userToken:
        if userToken == False:
            enp = token.split(':')
            p = subprocess.Popen([pythonCommand,'bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser,proxy_list[proxy_number]])
            proxy_number += 1
            sleep(joinSpeed)
        else:
            p = subprocess.Popen([pythonCommand,'bots/misc/joinServer2.0.py',token,inviteLink,proxy_list[proxy_number]])
            proxy_number += 1
            sleep(joinSpeed)

if in_pick == 8:
    if(captchaAPI == ""):
        print("This requires an API key from https://2captch9a.com/")
    else:
        for combo in emailList:
            enp = combo.split(':')
            p = subprocess.Popen([pythonCommand,'bots/misc/account-creator/account_creator.py',enp[0],enp[1],proxy_list[proxy_number]])
            proxy_number += 1
            sleep(joinSpeed)
if in_pick == 9:
    if(captchaAPI == ""):
        print("This requires an API key from https://2captcha.com/")
    else:
        for combo in emailList:
            for tknv in tokenV:
                enp = combo.split(':')
                p = subprocess.Popen([pythonCommand,'bots/misc/account-creator/account_verify.py',enp[0],enp[1],proxy_list[proxy_number],tknv])
                proxy_number += 1
                sleep(joinSpeed)

p.wait()
