import sys
import requests
import json
import pprint
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com"
headers = {"User-Agent": "Python HMAC Example"}
user_id = "ebb305ed-f214-45e0-b55e-2f34a0447b25"

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/api/authn/v2/users/"+user_id, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        pprint.pprint(data)
        
    else:
        print(response.status_code)
