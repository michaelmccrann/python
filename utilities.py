#!/usr/bin/env python3

import urllib.request
import urllib.parse
import os
import hashlib 
import requests
from jinja2 import Template
from collections import namedtuple

Person      = namedtuple('Person', 'id name username email phone password')
TestData    = namedtuple('TestData', 'OrderDate Region Rep Item Units UnitCost Total')

def get_test_data(spreadsheet_row):

  return TestData ( 
    OrderDate=      spreadsheet_row[0].value, 
    Region=         spreadsheet_row[1].value, 
    Rep=            spreadsheet_row[2].value, 
    Item=           spreadsheet_row[3].value, 
    Units=          spreadsheet_row[4].value, 
    UnitCost=       spreadsheet_row[5].value, 
    Total=          spreadsheet_row[6].value
  )

def get_person(data):
  return Person(data['id'], data['name'], data['username'], data['email'], data['phone'], None) 
  
def md5ChecksumFile(filePath):
  with open(filePath, 'rb') as fh:
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)

  return m.hexdigest()

def md5ChecksumData(data):
    m = hashlib.md5(data)
    return m.hexdigest()    

def get_base_url(base_url_template, server):
  template = Template(base_url_template)
  return template.render(server=server)

def get_full_url(base_url, resource):
  # print (base_url)
  # print (resource)
  template = Template("{{ base_url }}/{{ resource }}")
  return template.render(base_url=base_url, resource=resource)


def download_file(file_url, download_dir):

  url_parsed = urllib.parse.urlparse(file_url)
  full_pathname = os.path.abspath(os.path.join(download_dir, os.path.split(url_parsed.path)[1]))

  r = requests.get(file_url)
  if r.status_code != 200:
    raise Exception('Download did not return 200 status code')

  download_write_required=True
  if os.path.exists(full_pathname):
    print ("File exists checking md5sums")
    if md5ChecksumData(r.content) == md5ChecksumFile(full_pathname):
      download_write_required=False

  if download_write_required:
    with open(full_pathname,'wb') as output_file:
      print ("Writing file")
      output_file.write(r.content)
  else:
    print("No download write required")
      
  return full_pathname
