#
# discord_text_spam.py
# @author Merubokkusu
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2019
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified Mon Mar 18 2019 15:02:46 GMT-0400 (Eastern Daylight Time)
#

import discord
import asyncio
import sys
import random
import os
import subprocess
import aiohttp
import socket
sys.path.append("./.")
from config import *

if(os.path.exists("proxies.txt")):
    conn = aiohttp.ProxyConnector(proxy="http://"+sys.argv[3])
    client = discord.Client(connector=conn)
else:
    client = discord.Client()
token = sys.argv[1]
global spam_text
spam_text = sys.argv[2]

@client.event
async def on_ready():
    spam_text = sys.argv[2]
    print("Started Text Spam")
    while not client.is_closed:
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

        await client.send_message(discord.Object(id=DiscordChannel), spam_text)
        await asyncio.sleep(SpamSpeed) 
        print(client.user.name + ' sent ' + spam_text)

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
        if sys.platform == "win32":
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
            p.wait()
        else:
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=False)
            p.wait()
    client.run(token, bot=False)
