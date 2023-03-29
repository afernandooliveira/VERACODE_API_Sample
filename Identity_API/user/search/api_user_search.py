import sys
import requests
import json
import pprint
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com"
headers = {"User-Agent": "Python HMAC Example"}
api_id = "api_id"                   # string
login_enabled = "login_enabled"     # boolean {true or false}
login_status = "login_status"       # string  {active, failed, locked, or never}
org_id = "org_id"                   # string  {pode ser obtido executando API self}
org_name = "org_name"               # string
role_id = "role_id"                 # string
saml_user = "saml_user"             # boolean {true or false}
search_term = "search_term"         # string  {Keyword to search for users using the username, first name, last name, and email address fields.}
team_id = "team_id"                 # string
user_type = "user_type"             # string { api, for API service account, or user, for human user account}


if __name__ == "__main__":

    try:
        # Sample for more than one parameter
        # response = requests.get(api_base + "/api/authn/v2/users/search?"+"login_status="+login_status+"&org_id="+org_id, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
        response = requests.get(api_base + "/api/authn/v2/users/search?"+"org_id="+org_id, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Whoops!")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        pprint.pprint(data)
        
    else:
        print(response.status_code)
