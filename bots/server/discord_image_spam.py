#
# discord_image_spam.py
# @author Merubokkusu
# @description 
# @created 2020-09-02T15:28:56.184Z-04:00
# @last-modified 2020-11-15T11:52:43.172Z-05:00
#

import random
import os
import sys
import subprocess
import time
import discum
sys.path.append("./.")
from config import *

token = sys.argv[1]
global bot # Declaring discum global
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
        bot = discum.Client(email=email,password=password, token="none", proxy_host=sys.argv[3])
    else:
        bot = discum.Client(email=email,password=password, token="none")
else:
    if autojoinServer == True:   
        if sys.platform == "win32":
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
            p.wait()
        else:
            p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=False)
            p.wait()
    if(os.path.exists("proxies.txt")):
        bot = discum.Client(token=token, proxy_host=sys.argv[3])
    else:
        bot = discum.Client(token=token)

while True:
    UpImage = random.choice(os.listdir(DirPictures)) 
    print(DirPictures+UpImage)
    bot.sendFile(DiscordChannel, DirPictures + UpImage)
    time.sleep(SpamSpeed) # Changes how fast the images are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )
        