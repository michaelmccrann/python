#!/usr/bin/env python3

import yaml

with open('data/app.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print (type(data))
    print(data['environments']['prod']['api_server'])
    
print (data)    