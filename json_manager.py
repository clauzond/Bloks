import json


def load_file(filename,player_name='blank',fulldir=""):
    # Renvoie une liste, dont le ième élément est l'item d'ID i (item=dictionnaire)
    if fulldir=="":
        filedir = f'savestates/{player_name}/{filename}.json'
    else:
        filedir = fulldir
    f = open(filedir,'r',encoding='utf-8-sig')

    data = json.load(f)

    f.close()

    return(data)


def save_file(data,filename,player_name='blank'):
    # Sauvegarde l'inventaire
    filedir = f'savestates/{player_name}/{filename}.json'

    f = open(filedir,'w',encoding='utf-8')

    data = json.dump(data,f)

    f.close()

    return