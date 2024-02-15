#
# Middleware to connect with QRNG SeQure Quantum device, fetch 256 bits of randomness 
# and upload it to Thales CipherTrust Manager.
# Written by Matias Bendel 
# v1.0
#

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend
from urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
import requests
import random
import base64
import time
import re
import os

size=32
numpack=1
coding = "latin-1"
token=random.randint(100000,999999)

# Bearer token required
headers = {'Authorization': 'XXXXXX'}
data = {'request_type': 'data', 'package_size': size, 'package_total': numpack, 'output_type': 'base64'}

# Connecting to SeQure Quantum API REST - API endpoint required
response = requests.post('XXXX', headers=headers, data=data)
if (response):
    print("Connection to SeQure Quantum............................success")
    time.sleep(1)
else:
    print("Connection to SeQure Quantum: Error\nExit program.")
    sys.exit(0) 
    
# JSON mapping
data = str(response.content).split('"')[1::2]
# Taking only the second object that belongs to the key
base64_string = data[2]
# Decode/encode
decoded_bytes = base64.b64decode(base64_string.encode(coding))
decoded_string = decoded_bytes.decode(coding)
key_material = bytes(decoded_string,coding)

# Checking key length
key_material_len = len(key_material)
if key_material_len > 32:
    print("Error: AES not retrieved or greater that 32 bytes long. Exit program.")
    sys.exit(0)
elif key_material_len < 32:
    print("Error: AES not retrieved or less than 32 bytes long. Exit program.")
    sys.exit(0)
else:
    print("AES retrieved and length is 32 bytes....................success")
    time.sleep(1)

# --------------------

# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
# Call CipherTrust API and retrieve API Key - Ciphertrust credentials required
data = {"name": "XXX", "password": "XXXX"}
# Ciphertrust IP address required
response = requests.post('https://<CM IP address>/api/v1/auth/tokens', json=data, verify=False)
data = str(response.content).split('"')[1::2]
api_key = data[1]

if (api_key):
    print("Connection to CipherTrust Manager.......................success")
    time.sleep(1)
else:
    print("Connection to CipherTrust Manager: Error\nExit program.")
    sys.exit(0) 
    
# Create in CipherTrust a new secret with KDK cryptographic material 
headers = {'Authorization': f'Bearer {api_key}'}
data = { "name": f"AES_Quantum_Key_{token}", "usageMask": 12, "algorithm": "aes", "meta": { "ownerId": "local|admin" }, "state": "Pre-Active", "material": key_material.hex(), "aliases": [ { "alias": f"AES_Quantum_Key_{token}", "type": "string" } ] }
# Ciphertrust IP address required
response = requests.post('https://<CM IP address>/api/v1/vault/keys2', headers=headers, json=data, verify=False)

if (response):
    print(f"AES_Quantum_Key_{token} uploaded to CipherTrust..........success")
    time.sleep(1)
else:
    print("Key uploaded to CipherTrust: Error\nExit program.")
    sys.exit(0) 

# End
os.system('pause')
