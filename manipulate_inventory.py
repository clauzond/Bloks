
# NOTE : le tri est purement visuel, et n'importe pas du tout pour la fonction inventaire
# Ajoute "item" à l'inventaire du joueur avec le nom correspondant
# Trie, puis sauvegarde l'inventaire
def add_item_to_inventory(item,player_name):
    import manipulate_json as jm
    inventory_dic = jm.load_file(filename="inventory_dic",player_name=player_name)
    inventory_dic['itemlist'].append(item)

    # On trie l'inventaire par id
    inventory_dic['itemlist'] = sorted(inventory_dic['itemlist'], key = lambda x: x['id'])

    # Si on veut pouvoir préciser un dossier de save spécial
    #if savedir != "":
    #    jm.save_file(inventory_dic,fulldir=savedir)

    jm.save_file(inventory_dic,filename="inventory_dic",player_name=player_name)


# Donne la liste de TOUS les items qui se trouvent dans mypath
def template_itemlist():
    import manipulate_json as jm
    mypath = "ressources/template/items"

    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


    itemlist = []

    for filename in onlyfiles:
        mydir = f"{mypath}/{filename}"
        item = jm.load_file(fulldir=mydir)
        itemlist.append(item)

    return(itemlist)

# Transforme un item, avec des probabilités, pour lui donner plus de stats sur des lignes déjà existantes
def rarify_item(item,chance):
    from random import random

    rarete = 0
    facteur_luck = chance**(1/3)

    # Pour chaque attribut dans les stats
    for attribut in item['stats'].keys():
        # On fait un choix random entre 0 et 100
        r = random()*100

        # 1% de x2 ; 5% de x1.5 ; 10% de x1.25 ; 25% de x1.1
        if r<(1+facteur_luck) :
            rarete += 10
            item['stats'][attribut] = round(item['stats'][attribut] * 2,1)
        elif r<(5+facteur_luck):
            rarete += 5
            item['stats'][attribut] = round(item['stats'][attribut] * 1.5,1)
        elif r<(10+facteur_luck):
            rarete += 3
            item['stats'][attribut] = round(item['stats'][attribut] * 1.25,1)
        elif r<(25+facteur_luck):
            rarete += 1
            item['stats'][attribut] = round(item['stats'][attribut] * 1.1,1)


    # Pour chaque multiplicateur dans les multiplicateurs
    for (mult,value) in item['multiplicateurs'].items():
        # On fait un choix random entre 0 et 100
        r = random() * 100

        # 1% de +0.5 ; 5% de +0.25 ; 10% de +0.1
        if r<(1+facteur_luck):
            rarete += 10
            item['stats'][mult] += 0.5
        elif r<(5+facteur_luck):
            rarete += 5
            item['stats'][mult] += 0.25
        elif r<(10+facteur_luck):
            rarete += 3
            item['stats'][mult] += 0.1

    # Le prix augmente selon la rareté obtenue
    item['sellprice'] += round(item['sellprice'] * (rarete/10),1)

    return(item)