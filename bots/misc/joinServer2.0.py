#
# joinServer2.0.py
# @author Merubokkusu
# @created Thu Feb 07 2019 15:20:35 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2019
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified Tue Mar 05 2019 02:14:17 GMT-0500 (Eastern Standard Time)
#

import requests
import json
import sys
import os
TOKEN = sys.argv[1]
INVITE_LINK = sys.argv[2]
PROXY = { 'http' : sys.argv[3] } 
url = 'https://discordapp.com/api/v6/invite/'+INVITE_LINK+'?with_counts=true'
print(url)
headers = {"content-type": "application/json", "Authorization": TOKEN }

r = requests.post(url,headers=headers, proxies=PROXY)
if r.status_code == 200:
    print("Token:"+"'"+TOKEN[-25]+"'"+" Joined the server")
else:
    print('error, something went wrong.')
    print('Make sure your token is correct | https://discordhelp.net/discord-token')
    print(r.json())