import logging
import requests
from requests.auth import HTTPBasicAuth
import json

logging.basicConfig(level=logging.INFO)

HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = f'http://{HOST}/restconf/api/running/'

def set_interface_config():
    url = BASE_URL + 'interfaces/interface/GigabitEthernet3'
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }

    data = {
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet3",
            "description": "Changed through Restconf",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.0.10.3",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    response = requests.put(url, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=json.dumps(data))
    return "Success" if response.status_code == 204 else f"Error: {response.status_code}"

print(set_interface_config())



