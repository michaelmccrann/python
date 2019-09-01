#!/usr/bin/env python3

import yaml
from jinja2 import Template
import requests
import json
import utilities

with open('data/app.yml') as f:
     data = yaml.load(f, Loader=yaml.FullLoader)

api = data['apis']['test_data_api']
env = data['environments']['test_data']

base_url = utilities.get_base_url(data['global']['base_url_template'], env['api_server'])

resource_template_str = api['all_users']['url_template']
url = utilities.get_full_url(base_url, resource_template_str)

print (url)

r = requests.get(url)
print(r.status_code)

for user in json.loads(r.text):
  p = utilities.get_person(user)
  print (p)
  if p.password:
    print (p)
  #print (user)

