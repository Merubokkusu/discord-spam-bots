#
# discord_insult_spam.py
# @author Merubokkusu
# @description 
# @created 2020-09-02T15:28:56.184Z-04:00
# @last-modified 2021-03-09T17:18:46.689Z-05:00
#

import urllib.request
import discum
import random
import os
import sys
import subprocess
import time
from bs4 import BeautifulSoup
sys.path.append("./.")
from config import *

token = sys.argv[1]
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
        bot = discum.Client(email=email,password=password, token="none",log=discumLog)
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

while True:
    html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
    soup = BeautifulSoup(html,"html.parser")
    insult_text = soup.find('h1')
    print(insult_text.text)
    bot.sendMessage(DiscordChannel, insult_text.text)
    time.sleep(SpamSpeed) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it
