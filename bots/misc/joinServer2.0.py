import requests
import json
import sys
import os
TOKEN = sys.argv[0]
INVITE_LINK = sys.argv[1]
PROXY = sys.argv[2]
url = 'https://discordapp.com/api/v6/invite/'+INVITE_LINK+'?with_counts=true'

headers = {"content-type": "application/json", "Authorization": TOKEN }
try:
    r = requests.post(url,headers=headers, proxies=PROXY)
except requests.RequestException as e:
    print("Server join error. Make sure the invite link is 6 digits and not the full URL.")
else:
    print("Joined Server")