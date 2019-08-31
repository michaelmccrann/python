#!/usr/bin/env python3

import yaml

with open('data/data.yaml') as f:
    
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        
        for k, v in doc.items():
            print(k, "->", v)


            https://developer.github.com/v3/activity/events/#list-public-events