# coding: utf-8
import json
import os, os.path


def load_file(filename='',player_name='blank',fulldir=""):
    # Renvoie une liste, dont le ième élément est l'item d'ID i (item=dictionnaire)
    if fulldir=="":
        filedir = f'savestates/{player_name}/{filename}.json'
    else:
        filedir = fulldir
    f = open(filedir,'r',encoding='utf-8-sig')
    data = json.load(f)
    f.close()
    return(data)


def save_file(data,filename="",player_name='blank',fulldir=""):
    # Sauvegarde l'inventaire
    if fulldir=="":
        filedir = f'savestates/{player_name}/{filename}.json'
    else:
        filedir=fulldir

    directory = "/".join(filedir.split('/')[:-1])
    if not os.path.exists(directory):
        os.mkdir(directory)
    f = open(filedir,'w+',encoding='utf-8-sig')
    data = json.dump(data,f,ensure_ascii=False)
    f.close()
    return