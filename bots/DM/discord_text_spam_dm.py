#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import discord
import asyncio
import sys
import os
import time
import random
import subprocess
import aiohttp
sys.path.append("./.")
from config import *

if(os.path.exists("proxies.txt")):
    conn = aiohttp.ProxyConnector(proxy="http://"+sys.argv[3])
    client = discord.Client(connector=conn)
else:
    client = discord.Client()
token = sys.argv[1]
UserList = []
emojiList = [':smile:',':laughing:',':slight_smile:',':hot_pepper:',':smirk:']#You can configure these to your likings 
enp = []



@client.event
async def on_ready():
    spam_text = sys.argv[2]
    print("Started Text Spam with " + client.user.name)
    for server in client.servers:
        if ScanAllServers == False:
            if(server.id == DiscordServer):
                UserList = list(server.members)
        else:
            UserList = list(server.members)
    if HeavyScrape == False:                
        for member in UserList:
            if(member.id != client.user.id):
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
                if member.id in text: 
                    print(member.name + ' was already messaged')
                else:
                    try:
                        await client.send_message(member,spam_text+" "+random.choice(emojiList)+random.choice(emojiList))
                        print('Sent message to '+ member.name)
                        file = open('dm_spam_text.txt','a')
                        file.writelines(member.id + '\n')
                        file.close()
                        for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                            sys.stdout.flush()
                            await asyncio.sleep(1)
                        sys.stdout.write("\rComplete!                    \n")
                    except Exception:
                        print('Something went wrong (;3;) relaunching...') 
    else:
        while not client.is_closed:
            member = random.choice(UserList)
            if(member.id != client.user.id):
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
                    print(member.name + ' was already messaged')
                else:
                    try:
                        await client.send_message(member,spam_text+" "+random.choice(emojiList)+random.choice(emojiList))
                        print('Sent message to '+ member.name)
                        file = open('dm_spam_text.txt','a')
                        file.writelines(member.id + '\n')
                        file.close()
                        for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                            sys.stdout.flush()
                            await asyncio.sleep(1)
                        sys.stdout.write("\rComplete!                    \n")
                    except Exception:
                        print('Something went wrong (;3;) relaunching...')             


if ':' in token: 
    enp = token.split(':')
    if autojoinServer == True:
        if sys.platform == "win32":
            p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=True)
            p.wait()
        else:
            p = subprocess.Popen(['python','bots\misc\joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=False)
            p.wait() 
    client.run(enp[0],enp[1], bot=False) 
else: 
    if autojoinServer == True:
        p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
        p.wait() 
    client.run(token, bot=False)
