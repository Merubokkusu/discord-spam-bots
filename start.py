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
p = None

def printWarning(input):
    print("====")
    print("WARNING! " + input)
    print("====")

account_creator_completed = open("account_creator_completed.txt", 'a+').read().splitlines()
account_verify_completed = open("account_verify_completed.txt", 'a+').read().splitlines()
emailList = open("combolist.txt", 'a+').read().splitlines()
    
if os.path.exists('tokens.txt'):
    userToken = open("tokens.txt").read().splitlines()
    printWarning("EDIT YOUR CONFIG.PY BEFORE USING!\n-=Using tokens.txt=-\n")
else:
    printWarning("EDIT YOUR CONFIG.PY BEFORE USING!")

if os.path.exists('combolist.txt'):
    emailList = open("combolist.txt").read().splitlines()
else:
    emailList = None

if os.path.exists('proxies.txt'):
    proxy_list = open("proxies.txt").read().splitlines()
else:
    file = open('proxies.txt','a')
    for i in emailList:
        file.writelines("localhost" + '\n')
    proxy_list = open("proxies.txt").read().splitlines()

def incrementProxyNumber():
    global proxy_number
    if(proxy_number < len(proxy_list)):
        proxy_number =+ 1
    else:
        proxy_number = 0

if os.path.exists('tokens.txt'):
    tokenV = open("tokens.txt").read().splitlines()
else:
    tokenV = None

if len(sys.argv) < 2:
    print("   +=================+")
    print("Type one of the following numbers to launch that spammmer")
    print("   +========- Server Spammers -=========+")
    print("1 : Text Spammer - Write your own text to spam")
    print("2 : Image Spammer - Spam random images in a selected folder")
    print("3 : Insult Spammer - Picks insults online and spams them")
    print("   +========- DM Spammers -=========+")
    print("4 : Text Spammer - Write your own text to spam")
    print("5 : Image Spammer - Spam random images in a selected folder")
    print("6 : Insult Spammer - Picks insults online and spams them")
    print("   +========- Other -=========+")
    print("7 : Join Server - Join the server thats written in the config")
    print("   +========- Account Creator -=========+")
    print("8 : Account creator - Create bulk accounts")
    print("9 : Account verifier - Verify accounts")
    print("   +=================+")

    in_pick = float(input("Select a bot: "))
else:
    in_pick = float(sys.argv[1])
    spam_text = sys.argv[2]

if in_pick == 1:
    if os.path.exists('text.txt'):
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/server/discord_text_spam.py',token,'null',proxy_list[proxy_number]])
            incrementProxyNumber()
            sleep(1)
    else:
        if spam_text == None:
            spam_text = input("Write spam text : ")
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/server/discord_text_spam.py',token,spam_text,proxy_list[proxy_number]])
            incrementProxyNumber()
            sleep(1)

if in_pick == 2:
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots/server/discord_image_spam.py', token,proxy_list[proxy_number]])
        incrementProxyNumber()

if in_pick == 3:
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots/server/discord_insult_spam.py', token,proxy_list[proxy_number]])
        incrementProxyNumber()

#DM Spammers
if in_pick == 4:
    if os.path.exists('text.txt'):
        if not os.path.exists('dm_spam_text.txt'):
            file = open('dm_spam_text.txt','w')
            file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
            file.close()
        for token in userToken:
            p = subprocess.Popen([pythonCommand,'bots/DM/discord_text_spam_dm.py',token,'null',proxy_list[proxy_number]])
            incrementProxyNumber()
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
            incrementProxyNumber()
            sleep(2.5)

if in_pick == 5:
    if not os.path.exists('dm_spam_image.txt'):
        file = open('dm_spam_image.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand, 'bots/DM/discord_image_spam_dm.py', token,proxy_list[proxy_number]])
        incrementProxyNumber()

if in_pick == 6:
    if not os.path.exists('dm_spam_insult.txt'):
        file = open('dm_spam_insult.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen([pythonCommand,'bots/DM/discord_insult_spam_dm.py', token,proxy_list[proxy_number]])
        incrementProxyNumber()

if in_pick == 7:	
    for token in userToken:
        if userToken == False:
            enp = token.split(':')
            p = subprocess.Popen([pythonCommand,'bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser,proxy_list[proxy_number]])
            incrementProxyNumber()
            sleep(joinSpeed)	
        else:	
            p = subprocess.Popen([pythonCommand,'bots/misc/joinServer2.0.py',token,inviteLink,proxy_list[proxy_number]])	
            incrementProxyNumber()	
            sleep(joinSpeed)

if in_pick == 8:
    if(captchaAPI == ""):
        printWarning("This requires an API key from https://2captcha.com/")
    elif(emailList is None):
        printWarning("You need to create the combolist.txt-file!")
    else:
        for combo in emailList:
            enp = combo.split(':')
            currentEmail = enp[0]
            print("Starting account creation for: " + currentEmail)
            if(currentEmail in account_creator_completed):
                print("Account already created: " + currentEmail)
            else:
                p = subprocess.Popen([pythonCommand, 'bots/misc/account-creator/account_creator.py', enp[0], enp[1], proxy_list[proxy_number]])
                incrementProxyNumber()
                sleep(joinSpeed)
if in_pick == 9:
    if(captchaAPI == ""):
        printWarning("This requires an API key from https://2captcha.com/")
    elif not os.path.exists('tokens.txt'):
        printWarning("You need to create the tokens.txt-file!")
    elif not os.path.exists('combolist.txt'):
        printWarning("You need to create the combolist.txt-file!")
    elif (mailServer == ""):
        printWarning("mailServer is not set in the config!")
    else:
        for tokens in tokenV:
            enp = tokens.split(':')
            currentEmail = enp[0]
            print("Starting account verification for: " + currentEmail)
            if currentEmail in account_verify_completed:
                print("Account already verified: " + currentEmail)
            else:
                p = subprocess.Popen([pythonCommand,'bots/misc/account-creator/account_verify.py', enp[0], enp[1], proxy_list[proxy_number], enp[2]])
                incrementProxyNumber()
                sleep(joinSpeed)
                p.wait()

if p:
    p.wait()
