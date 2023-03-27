import sys
import requests
import json
import pprint
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com"
headers = {"User-Agent": "Python HMAC Example"}
org_id = "ORG_ID" # Informe o ORG_ID, que pode ser obtido executando uma chamada a API_SELF


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/api/authn/v2/users?org_id="+org_id, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        pprint.pprint(data)
        
    else:
        print(response.status_code)
