#!/usr/bin/env python3

import yaml
from jinja2 import Template

uri_template_str="{{ protocol | default('https')}}://{{ api_server }}:{{ port | default(443) }}/{{ resource }}"
#uri_template_str="{{ protocol }}://{{ api_server }}:{{ port | default(443)/{{ resource }}"


with open('data/app.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    template = Template(uri_template_str)

    server=data['environments']['prod']['api_server']
    resource=data['apis']['my_api']['delete_api']['resource']
    print(template.render(api_server=server, resource=resource))


