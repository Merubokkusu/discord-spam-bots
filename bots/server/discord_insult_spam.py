#
# discord_insult_spam.py
# @author Merubokkusu
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2019
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified Mon Mar 18 2019 15:02:50 GMT-0400 (Eastern Daylight Time)
#

import urllib.request
import discord
import asyncio
import random
import os
import sys
import subprocess
import aiohttp
from bs4 import BeautifulSoup
sys.path.append("./.")
from config import *

if(os.path.exists("proxies.txt")):
    conn = aiohttp.ProxyConnector(proxy="http://"+sys.argv[2])
    client = discord.Client(connector=conn)
else:
    client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    while not client.is_closed:
        html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
        soup = BeautifulSoup(html,"html.parser")
        insult_text = soup.find('h1')
        print(insult_text.text)
        await client.send_message(discord.Object(id=DiscordChannel), insult_text.text)
        await asyncio.sleep(SpamSpeed) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it
    
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
