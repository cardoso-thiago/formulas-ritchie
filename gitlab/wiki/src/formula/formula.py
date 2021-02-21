#!/usr/bin/python3
import requests, re, sys, subprocess, os
from colored import fg, attr
from bs4 import BeautifulSoup
import inquirer

def Run():
    url = 'https://cardoso-thiago.gitlab.io/site-antora-demo/'
    redirect = requests.get(url)
    location = re.search('<script>location="(.*)"</script>', redirect.text).group(1)
    page = requests.get(url + location)
    soup = BeautifulSoup(page.content, 'html.parser')
    article = soup.find('article')

    dict_links = {} 
    for link in article.find_all('a'):
        finalUrl = url + location.replace('main.html', link.get('href')) 
        if not finalUrl in dict_links.values():
            dict_links[link.get_text()] = finalUrl

    gitlab_links = [
    inquirer.List('gitlab_links', 
        message = "Qual página você quer visualizar?",
        choices = dict_links,
        carousel = True
        ),
    ]

    user_selection = inquirer.prompt(gitlab_links)
    url_selection = dict_links.get(user_selection["gitlab_links"])
    print(f"{fg(2)}Abrindo a url {url_selection}{attr(0)}")
    open_url(url_selection)

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