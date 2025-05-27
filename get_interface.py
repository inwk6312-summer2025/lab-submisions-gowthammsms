import logging
import requests
from requests.auth import HTTPBasicAuth
import json

logging.basicConfig(level=logging.INFO)

HOST = '192.168.1.101'  # Replace as needed
USER = 'student'
PASS = 'Meilab123'
BASE_URL = f'http://{HOST}/restconf/api/running/'

def get_interfaces(endpoint):
    url = BASE_URL + endpoint
    headers = {'Accept': 'application/vnd.yang.data+json'}
    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), headers=headers)
    if response.status_code == 200:
        return json.dumps(response.json(), indent=4)
    else:
        return f"Error: {response.status_code}"

print(get_interfaces('interfaces'))
