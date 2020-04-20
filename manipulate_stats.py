from tkinter import *
import classtooltip as ctt
import dictionnaires



# Transférer les attributs de "attribut_dic" vers les attributs de bases du joueur
def baseattribut_to_playerstats(attribut_dic,player_dic):

    attribut_liste = list(attribut_dic.keys())

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