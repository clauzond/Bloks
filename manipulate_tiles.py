import manipulate_json as jm

def load_map_with_used_objects(map_by_layer,used_objects):
    """
    Enlève les objects utilisés de la map
    """
    for layer_nbr in range(len(used_objects)):
        for used_item in used_objects[layer_nbr]:
            map_by_layer[layer_nbr][used_item[0]][used_item[1]] = map_by_layer[0][used_item[0]][used_item[1]]
    return(map_by_layer)

def add_used_item(layer,li,go,player_name,myMap):
    """
    Ajoute un item utilisé au json "used_objects" ; ne fait rien s'il est déjà présent
    """
    used_objects = jm.load_file(filename="used_objects",player_name=player_name)
    if [li,go] not in used_objects[layer]:
        used_objects[layer].append([li,go])
        jm.save_file(data=used_objects,filename="used_objects",player_name=player_name)
        myMap.used_objects = used_objects
        myMap.map_by_layer[layer][li][go] = myMap.map_by_layer[0][li][go]


def use_disappearing_item(layer,li,go,taglist,player_name,myMap):
    if "keyYellow" in taglist:
        add_used_item(layer=layer,li=li,go=go,player_name=player_name,myMap=myMap)


