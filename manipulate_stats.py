from tkinter import *
import classtooltip as ctt
import dictionnaires




# Transférer les attributs de "attribut_dic" vers les attributs de bases du joueur
def baseattribut_to_playerstats(attribut_dic,player_dic):

    attribut_liste = list(attribut_dic.keys())[:6]

    for i in range(len(attribut_liste)):
        attribut = attribut_liste[i]
        attribut_level = attribut_dic[attribut]['level']

        player_dic['stats']['base'][attribut] = attribut_level

    return(player_dic)


# Transférer les statistiques donnés par les items équippés vers les attributs du joueur
def equipped_list_attributs_to_playerstats(player_dic):
    equipped_list = player_dic['equipped_list']
    player_dic['stats']['byitems'] = {}



    for i in range(len(equipped_list)):
        if len(equipped_list[i])>0:
            stats = equipped_list[i]['stats']

            if len(stats)>0:

                statkey_list = list(stats.keys())
                statvalue_list = list(stats.values())

                for i in range(len(statkey_list)):
                    this_stat = statkey_list[i]
                    this_value = statvalue_list[i]
                    # Si la statistique existe, on rajoute à celle existante
                    if this_stat in player_dic['stats']['byitems']:
                        player_dic['stats']['byitems'][this_stat] += this_value
                    # Sinon, on la crée, en l'initialisant à la valeur voulue
                    else:
                        player_dic['stats']['byitems'][this_stat] = this_value
    return(player_dic)


# Additionner toutes les statistiques 'base' et 'byitems' en une seule 'total'
def total_playerstats(player_dic):
    total = {"HP":0,
"Mana":0,
"Force":0,
"Agilité":0,
"Intelligence":0,
"Chance":0,
"Dommage fixe":0,
"Dommage force":0,
"Dommage agilité":0,
"Dommage intelligence":0,
"Dommage chance":0,
"Résistance fixe":0,
"Résistance force":0,
"Résistance agilité":0,
"Résistance intelligence":0,
"Résistance chance":0}

    base = player_dic['stats']['base']
    byitems = player_dic['stats']['byitems']

    keys = list(total.keys())
    for key in keys:
        if key in base:
            if key in byitems:
                total[key] = base[key] + byitems[key]
            else:
                total[key] = base[key]
        else:
            if key in byitems:
                total[key] = byitems[key]
    player_dic['stats']['total'] = total
    return(player_dic)

# Transférer les attributs de "total" vers attribut_dic
def total_to_attribut_dic(player_dic,attribut_dic):
    total = total_playerstats(player_dic)['stats']['total']

    keys = list(total.keys())
    for key in keys:
        attribut_dic[key]['level'] = total[key]
    return(attribut_dic)
