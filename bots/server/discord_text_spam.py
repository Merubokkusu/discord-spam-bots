#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import discord
import asyncio
import sys
import random
import os
import subprocess
sys.path.append("./.")
from config import *

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
        p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=True)
        p.wait()
    client.run(enp[0],enp[1], bot=False) 
else: 
    client.run(token, bot=False)