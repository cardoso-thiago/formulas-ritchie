#!/usr/bin/python3
import requests, re, sys, subprocess, os
from colored import fg, attr
from bs4 import BeautifulSoup

def Run():
    url = 'https://cardoso-thiago.gitlab.io/site-antora-demo/'
    redirect = requests.get(url)
    location = re.search('<script>location="(.*)"</script>', redirect.text).group(1)
    page = requests.get(url + location)
    soup = BeautifulSoup(page.content, 'html.parser')
    article = soup.find('article')
    count = 0
    dict_links = {} 
    for link in article.find_all('a'):
        finalUrl = url + location.replace('main.html', link.get('href')) 
        if not finalUrl in dict_links.values():
            count+=1
            dict_links[count] = finalUrl
            print("[{}] - {}".format(count, link.get_text()))
    user_selection = get_user_selection(dict_links)
    url_selection = dict_links.get(user_selection)
    print(f"{fg(2)}Abrindo a url {url_selection}{attr(0)}")
    open_url(url_selection)

def get_user_selection(dict_links):
    if sys.version_info.major == 2:
        selection = raw_input()
    elif sys.version_info.major == 3:
        selection = input()

    try:
        if int(selection) < 1:
            print(f"{fg(1)}Insira uma opção maior que 0:{attr(0)}")
            return get_user_selection(dict_links)
        elif int(selection) > len(dict_links):
            print(f"{fg(1)}Insira uma opção menor ou igual a {str(len(dict_links))}:{attr(0)}")
            return get_user_selection(dict_links)
        else:
            return int(selection)
    except ValueError:
        print(f"{fg(1)}Insira um valor entre 1 e {str(len(dict_links))}:{attr(0)}")
        return get_user_selection(dict_links)

def open_url(url):
    if sys.platform == 'win32':
        os.startfile(url)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', url])
    else:
        try:
            with open(os.devnull, 'wb') as dn:
                subprocess.Popen(['xdg-open', url], cwd="/", stdout=dn, stderr=dn)
        except OSError:
            print(f"{fg(1)}Erro ao executar o comando, abra a url {url} no seu navegador.{attr(0)}")