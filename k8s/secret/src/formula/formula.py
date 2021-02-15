#!/usr/bin/python3
from colored import fg, attr
import shutil
import os
import sys

def Run(name, namespace, user, password):
    print(f"{fg(3)}Gerando o arquivo {name}.yml{attr(0)}")

    dest_file = os.path.join(get_download_path(), '{}.yml'.format(name))
    if os.path.isfile(dest_file):
        print(f"{fg(1)}O arquivo {dest_file} já existe. Deseja sobrescrever? (y/n) {attr(0)}")
        overwrite = get_user_confirmation()

        if not overwrite:
            print(f"{fg(3)}Processo interrompido pelo usuário. Nenhum arquivo foi gerado.{attr(0)}")
            return

    shutil.copy2('formula/secret-model.yml', dest_file) 
    
    fin = open(dest_file, "rt")
    data = fin.read()
    data = data.replace('${secret.name}', name)
    data = data.replace('${secret.namespace}', namespace)
    data = data.replace('${secret.user}', user)
    data = data.replace('${secret.password}', password)
    fin.close()

    fin = open(dest_file, "wt")
    fin.write(data)
    fin.close()

    print(f"{fg(2)}Arquivo gerado no caminho: {attr(0)}" + dest_file)

def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def get_user_confirmation():
    if sys.version_info.major == 2:
        confirmation = raw_input()
    elif sys.version_info.major == 3:
        confirmation = input()

    if confirmation.lower() == 'y':
        return True
    elif  confirmation.lower() == 'n':
        return False
    else:
        print(f"{fg(1)}Insira uma opção válida: (y/n) {attr(0)}")
        return get_user_confirmation()