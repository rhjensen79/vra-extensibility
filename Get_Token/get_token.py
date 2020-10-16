#A simple reusable function for autentification with api.mgmt.cloud.vmware.com
#and getting a bearer token.
#To use "import authenticate" at the top of your script (in same folder)
#and run as token = authenticate.authentificate(api_token)

import json
import requests

def authentificate(api_token):
    api_url_base = 'https://api.mgmt.cloud.vmware.com/'             #Base URL

    url = api_url_base+"iaas/api/login"
    headers = {'Content-Type': 'application/json'}
    payload = "{\n\t\"refreshToken\": \""+api_token+"\"\n}"

    response = requests.post(url, headers=headers, data = payload)

    if response.status_code == 200:
        data = response.json()
        token = (data['token'])
        return token
    else:
        return ("Error code : ",response.status_code)