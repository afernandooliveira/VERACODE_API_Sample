import sys
import requests
import pprint
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr"
headers = {"User-Agent": "Python HMAC Example"}

workspaceId = "1cbd5fb1-c35c-4c2e-834e-1348e7f57ee4"

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/v3/workspaces/"+workspaceId+"/issues", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        pprint.pprint(data)
        
    else:
        print(response.status_code)
