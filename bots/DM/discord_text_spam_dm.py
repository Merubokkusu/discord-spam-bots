#
# discord_text_spam_dm.py
# @author Merubokkusu
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2021
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
#

import discum
import json
import sys
import os
import time
import random
import subprocess
import requests
sys.path.append("./.")
from config import *

token = sys.argv[1]
global spam_text
spam_text = sys.argv[2]
global bot # Declaring discum global
if(os.path.exists("proxies.txt")):
    pnp = sys.argv[3].split(':')
if ':' in token: # Email and pass check (Seeing if there is a basic combo list)
    enp = token.split(':')
    email = enp[0] 
    password = enp[1]
    if autojoinServer == True:
        if sys.platform == "win32":
            p = subprocess.Popen(['python','bots/misc/joinServer.py',email,password,inviteLink,useBrowser],shell=True)
            p.wait()
        else:
            p = subprocess.Popen(['python','bots\misc\joinServer.py',email,password,inviteLink,useBrowser],shell=False)
            p.wait() 
    if(os.path.exists("proxies.txt")): # Checking root folder for proxies
        bot = discum.Client(email=email,password=password, token="none", proxy_host=pnp[0], proxy_port=pnp[1], log=discumLog)
    else:
        bot = discum.Client(email=email,password=password, token="none", log=discumLog)
else:
    if autojoinServer == True:   
        if sys.platform == "win32":
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
            p.wait()
        else:
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=False)
            p.wait()
    if(os.path.exists("proxies.txt")):

        bot = discum.Client(token=token, proxy_host=pnp[0], proxy_port=pnp[1], log=discumLog)
    else:
        bot = discum.Client(token=token,log=discumLog)

@bot.gateway.command
def memberTest(resp):
	guild_id = DiscordServer
	channel_id = DiscordChannel
	if resp.event.ready_supplemental:
		bot.gateway.fetchMembers(guild_id, channel_id)
	if bot.gateway.finishedMemberFetching(guild_id):
		bot.gateway.removeCommand(memberTest)
		bot.gateway.close()


bot.gateway.run()



emojiList = [':smile:',':laughing:',':slight_smile:',':hot_pepper:',':smirk:']#You can configure these to your likings 



while True:
    print("Started Text DM Spam")
    if HeavyScrape == False:                
        for member in bot.gateway.session.guild(DiscordServer).members:
            print(member)
            if os.path.exists('text.txt'):
                if textRandom == False and textFull == False:
                    lines = open('text.txt').read().splitlines()
                    spam_text = lines[0]
                elif textFull == True:
                    with open('text.txt', 'r', encoding='utf-8') as spamtextfile:
                        spam_text = spamtextfile.read()
                else:
                    lines = open('text.txt').read().splitlines()
                    spam_text = random.choice(lines)
            userNames = open('dm_spam_text.txt');
            text = userNames.read().strip().split()
            if member in text: 
                print(member + ' was already messaged')
            else:
                try:
                    dmChannel = json.loads(bot.createDM([member]).content)
                    bot.sendMessage(str(dmChannel['id']),spam_text+" "+random.choice(emojiList)+random.choice(emojiList))
                    print('Sent message to '+ member)
                    file = open('dm_spam_text.txt','a')
                    file.writelines(member + '\n')
                    file.close()
                    for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                        sys.stdout.write("\r")
                        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                        sys.stdout.flush()
                        time.sleep(1)
                    sys.stdout.write("\rComplete!                    \n")
                except Exception:
                    print('Something went wrong (;3;) relaunching...') 
                    time.sleep(8)
    else:
        member = random.choice(bot.gateway.session.guild(DiscordServer).members)
        if os.path.exists('text.txt'):
            if textRandom == False:
                lines = open('text.txt').read().splitlines()
                spam_text = lines[0]
            else:
                lines = open('text.txt').read().splitlines()
                spam_text = random.choice(lines)
        userNames = open('dm_spam_text.txt');
        text = userNames.read().strip().split()
        if member.id in text: 
            print(member + ' was already messaged')
        else:
            try:
                dmChannel = json.loads(bot.createDM([member]).content)
                bot.sendMessage(str(dmChannel['id']),spam_text+" "+random.choice(emojiList)+random.choice(emojiList))
                print('Sent message to '+ member)
                file = open('dm_spam_text.txt','a')
                file.writelines(member + '\n')
                file.close()
                for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\rComplete!                    \n")
            except Exception:
                print('Something went wrong (;3;) relaunching...')    
                time.sleep(8)
        
