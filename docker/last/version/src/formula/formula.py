#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool
import os
import shutil
import requests

def Run():
    url = 'https://registry.hub.docker.com/v2/repositories/library/alpine/tags/'
    resp = requests.get(url=url)
    data = resp.json()

    version = 'latest'
    for key in data['results']:
        if  key['name'] != 'latest':
            version = key['name']
            break
        
    print('Executando o docker-compose com a versão {}'.format(version))
    current_directory = os.path.dirname(os.path.abspath(__file__))
    dest_file = os.path.join(current_directory, 'temp-docker-compose.yml')

    shutil.copy2('docker-compose.yml', dest_file)

    fin = open(dest_file, "rt")
    data = fin.read()
    #TODO substituir alpine pela última versão
    data = data.replace('${image-version}', version)

    fin.close()

    fin = open(dest_file, "wt")
    fin.write(data)
    fin.close()

    os.system('docker-compose -f {} run app sh'.format(dest_file))