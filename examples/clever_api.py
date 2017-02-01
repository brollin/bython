#!/usr/bin/env python

import requests
import json

response = requests.get('https://api.clever.com/v1.1/students',headers={'Authorization':'Bearer DEMO_TOKEN'})

print('status code:',response.status_code)

json_loads = json.loads(response.text)

with open('out.json','w') as f:
    f.write(json.dumps(json_loads))



