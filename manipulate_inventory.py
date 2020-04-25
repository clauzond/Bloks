
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


