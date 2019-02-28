#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import discord
import asyncio
import random
import os
import sys
import subprocess
import aiohttp
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
    print("Started Image Spam")
    while not client.is_closed:
            UpImage = random.choice(os.listdir(DirPictures)) 
            print(UpImage)
            await client.send_file(discord.Object(id=DiscordChannel), DirPictures + UpImage)
            await asyncio.sleep(SpamSpeed) # Changes how fast the images are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )

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