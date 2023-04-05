import sys
import requests
import pprint
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr"
headers = {"User-Agent": "Python HMAC Example"}

workspaceId = "9197948e-5a0b-4409-8ac5-3424350a6507"

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/v3/workspaces/"+workspaceId+"/agents", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        pprint.pprint(data)
        
    else:
        print(response.status_code)
