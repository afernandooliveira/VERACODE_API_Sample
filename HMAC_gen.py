import sys
import pprint
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

auth=RequestsAuthPluginVeracodeHMAC()

hmac = vars(auth)

for item in hmac:
    print(item, ':', hmac[item] )