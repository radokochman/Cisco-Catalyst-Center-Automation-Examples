import requests
import json

USER = "devnetuser"
PASSWORD = "Cisco123!"
AUTH = requests.auth.HTTPBasicAuth(USER, PASSWORD)
AUTH_RESPONSE = requests.post(
    "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token",
    auth=AUTH,
    verify=False,
)

TOKEN = json.loads(AUTH_RESPONSE.text)["Token"]

HEADERS = {"X-Auth-Token": TOKEN}

BASE_URL = "https://sandboxdnac.cisco.com/dna/intent/api/v1"
RESOURCE = "/network-device"

call_response = requests.get(BASE_URL + RESOURCE, headers=HEADERS, verify=False)
devices = json.loads(call_response.text)["response"]

for device in devices:
    RESOURCE = f"/interface/network-device/{device['id']}"
    call_response = requests.get(BASE_URL + RESOURCE, headers=HEADERS, verify=False)
    interfaces = json.loads(call_response.text)["response"]

    print(f"Interfaces on {device['hostname']}:")

    for interface in interfaces:
        print(
            f"\tName: {interface['portName']}, Status: {interface['status']}, "
            f"Port mode: {interface['portMode']}, Speed: {interface['speed']}"
        )
