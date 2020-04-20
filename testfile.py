def n_to_coord(n):
    # transforme un nombre 11 (commence à 0) en coordonnées, on a donc 11 -> (ligne 1,colonne 2)

    ligne = n//10 + 1
    colonne = n - (n//10)*10 + 1

    print(ligne,colonne)

def append(d):


    for i in range(6,63):
        item = {'id': int(i), 'name': f'Item {i}', 'description': f'Description item {i}', 'owned': int(i), 'sellprice': int(i), 'itemlevel': 0, 'image': 'img/item.gif', 'stats':{}}



        d['itemlist'].append(item)
        d['total_items'] += 1
        d['owned_distinct_items'] += 1
    return(d)


def v2_append(d):
    d['owned_distinct_items'] = 0
    d['total_items'] = 0
    for i in range(0,63):
        item = {'id': int(i), 'name': f'Item {i}', 'description': f'Description item {i}', 'owned': int(i), 'sellprice': int(i), 'itemlevel': 0, 'image': 'img/item.gif', 'stats':{}}
        d['itemlist'][i] = item
        if i>0:
            d['owned_distinct_items'] += 1
        d['total_items']+=1
    return(d)