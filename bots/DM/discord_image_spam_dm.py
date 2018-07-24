#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import discord
import asyncio
import random
import os
import sys
import subprocess
sys.path.append("./.")
from config import *

client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    for server in client.servers:
        if ScanAllServers == False:
            if(server.id == DiscordServer):
                UserList = list(server.members)
        else:
            UserList = list(server.members)
            
    if HeavyScrape == False:                  
        for member in UserList:
            if(member.id != client.user.id):
                userNames = open('dm_spam_image.txt');
                text = userNames.read().strip().split()
                if member.id in text: 
                    print(member.name + ' was already messaged')
                else:
                    try:
                        UpImage = random.choice(os.listdir(DirPictures)) 
                        await client.send_file(member, DirPictures + UpImage)
                        print('Sent '+UpImage +' To '+ member.name)
                        file = open('dm_spam_image.txt','a')
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
                userNames = open('dm_spam_image.txt');
                text = userNames.read().strip().split()
                if member.id in text: 
                    print(member.name + ' was already messaged')
                else:
                    try:
                        UpImage = random.choice(os.listdir(DirPictures)) 
                        await client.send_file(member, DirPictures + UpImage)
                        print('Sent '+UpImage +' To '+ member.name)
                        file = open('dm_spam_image.txt','a')
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
        p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=True)
        p.wait()
    client.run(enp[0],enp[1], bot=False) 
else: 
    client.run(token, bot=False)