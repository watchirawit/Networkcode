#!/usr/bin/env python3
from urllib import response
import requests

from requests.auth import HTTPBasicAuth

requests.get('http://api.github.com/user', auth=HTTPBasicAuth('user', 'password'))

response = requests.get('http://api.github.com/user', auth=('user', 'password'))

print('Respones.status_code:'+ str(response.status_code))
if response.status_code == 200:
    print('Login successfull: ' + response.text)


    