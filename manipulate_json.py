# coding: utf-8
import json
import os, os.path


def load_file(filename='',player_name='blank',fulldir=""):
    """
    Renvoie le contenu du ficher
    Option 1 : on remplit "fulldir" pour accéder directement au fichier
    Option 2 : on remplit "filename" et "player_name" pour accéder à savestates/player_name/filename.json
    """
    if fulldir=="":
        filedir = f'savestates/{player_name}/{filename}.json'
    else:
        filedir = fulldir
    f = open(filedir,'r',encoding='utf-8-sig')
    data = json.load(f)
    f.close()
    return(data)


def save_file(data,filename="",player_name='blank',fulldir=""):
    """
    Sauvegarde le contenu du ficher et ne renvoie rien
    Option 1 : on remplit "fulldir" pour accéder directement au fichier
    Option 2 : on remplit "data, "filename" et "player_name" pour sauvegarder data dans savestates/player_name/filename.json
    """
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