import requests
import json
import sys
import os
TOKEN = sys.argv[1]
INVITE_LINK = sys.argv[2]
PROXY = { 'http' : sys.argv[3] } 
url = 'https://discordapp.com/api/v6/invite/'+INVITE_LINK
headers = {"content-type": "application/json", "Authorization": TOKEN }

r = requests.post(url,headers=headers, proxies=PROXY)
if r.status_code == 200:
    print("Token:"+"'"+TOKEN[-25]+"'"+" Joined the server")
else:
    print('error, something went wrong.')
    print('Make sure your token is correct | https://discordhelp.net/discord-token')
    print(r.json())
