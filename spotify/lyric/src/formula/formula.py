#!/usr/bin/python3
from colored import fg, attr
from distutils.util import strtobool
from SwSpotify import spotify
import sys, subprocess, os

def Run():
    artist = spotify.artist()
    song = spotify.song()

    print(f"{fg(7)}Abrindo letra para {fg(2)}{song}{fg(7)} de {fg(2)}{artist}{attr(0)}")
    open_url('https://genius.com/{}-{}-lyrics'.format(format_to_genius(artist), format_to_genius(song)))

def format_to_genius(value):
    live_music_tag = " - Live"
    live_music_tag2 = " (Live"

    if live_music_tag in value:
        value = value.split(live_music_tag)[0]
    if live_music_tag2 in value:
        value = value.split(live_music_tag2)[0]

    value = value.replace("(", "")
    value = value.replace(")", "")
    value = value.replace(".", "")
    value = value.replace("'", "")
    value = value.replace("´", "")
    value = value.replace("&", "and")
    return value.replace(" ", "-")

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