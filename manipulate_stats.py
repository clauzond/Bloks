from tkinter import *
import classtooltip as ctt
import dictionnaires




# Transférer les attributs de "attribut_dic" et des items de "player_dic['equipped_list']" vers player_dic['stats']
# Les statistiques de "attribut_dic" resteront ceux donnés par les level_up et par l'attribuation manuelle
# Comme ça, les statistiques réelles du joueur sont toujours contenu dedans
def calculate_playerstats(attribut_dic,player_dic):
    player_dic['stats'] = {}

    # attribut_dic vers player_dic['stats']
    attribut_liste = list(attribut_dic.keys())
    for i in range(len(attribut_liste)):
        attribut = attribut_liste[i]
        attribut_level = attribut_dic[attribut]['level']
        player_dic['stats'][attribut] = attribut_level


    # equipped_list vers player_dic['stats']

    equipped_list = player_dic['equipped_list']


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
                    if this_stat in player_dic['stats']:
                        player_dic['stats'][this_stat] += this_value
                    # Sinon, on la crée, en l'initialisant à la valeur voulue
                    else:
                        player_dic['stats'][this_stat] = this_value

    return(player_dic)



def calculate_damage_player(player_stats,monster_stats,player_itemlist,multiplicateur_defense=1):
    # itemlist sera la "equipped_list" du joueur

    # mult item attribut : de base, 10% pour tout de base
    mi_f = mi_a = mi_i = mi_c = 0.1
    # mult base attribut (par défault, 25%)
    mb_a = mb_c = 0.20
    mb_f = mb_i = 0.25

    dmg_fixe = player_stats['Dommage fixe']
    dmg_f = player_stats['Dommage force']
    dmg_a = player_stats['Dommage agilité']
    dmg_i = player_stats['Dommage intelligence']
    dmg_c = player_stats['Dommage chance']

    f = player_stats['Force']
    a = player_stats['Agilité']
    i = player_stats['Intelligence']
    c = player_stats['Chance']

    res_fixe = monster_stats['Résistance fixe']
    res_f = monster_stats['Résistance force']
    res_a = monster_stats['Résistance agilité']
    res_i = monster_stats['Résistance intelligence']
    res_c = monster_stats['Résistance chance']


    for item in player_itemlist:
        # l'item avec lequel on tape doit avoir un attribut 'multiplicateurs'

        # on vérifie que l'item a bien la clef 'multiplicateurs'
        if 'multiplicateurs' in item:
            mi_f += item['multiplicateurs']['Force']
            mi_a += item['multiplicateurs']['Agilité']
            mi_i += item['multiplicateurs']['Intelligence']
            mi_c += item['multiplicateurs']['Chance']

    dmg_fixe = multiplicateur_defense*dmg_fixe - res_fixe
    if dmg_fixe < 0:
        dmg_fixe = 0
    dmg_force =   multiplicateur_defense*(mi_f*(mb_f*f + dmg_f)) - res_f
    if dmg_force < 0:
        dmg_force = 0
    dmg_agilite = multiplicateur_defense*(mi_a*(mb_a*a + dmg_a)) - res_a
    if dmg_agilite < 0:
        dmg_agilite = 0
    dmg_intelligence = multiplicateur_defense*(mi_i*(mb_i*i + dmg_i)) - res_i
    if dmg_intelligence < 0:
        dmg_intelligence = 0
    dmg_chance = multiplicateur_defense*(mi_c*(mb_c*c + dmg_c)) - res_c
    if dmg_chance < 0:
        dmg_chance = 0



    # dommage_fixe + [somme pour tous les attributs de [(multiplicateur_item) * (multiplicateur_attribut*attribut + dommage_attribut) ]
    dmg_tot = dmg_fixe + dmg_force + dmg_agilite + dmg_intelligence + dmg_chance
    return(dmg_tot)


# Le monstre va taper à [(multiplicateur_stat)*(stat_principale) + dommage de la stat principale]
def calculate_damage_monster(monster_stats,player_stats,element,multiplicateur_defense):
    # Element = Force, Agilité, Intelligence ou Chance

    stat = monster_stats[element]
    dmg_stat = monster_stats['Dommage fixe'] + monster_stats[f'Dommage {element.lower()}']

    res = player_stats['Résistance fixe'] + player_stats[f'Résistance {element.lower()}']

    if element == "Force":
        multiplicateur_stat = 0.25
    elif element == "Agilité":
        multiplicateur_stat = 0.25
    elif element == "Intelligence":
        multiplicateur_stat = 0.25
    elif element == "Chance":
        multiplicateur_stat = 0.25

    dommage_total = (multiplicateur_defense)*(dmg_stat + stat * multiplicateur_stat) - res
    if dommage_total < 0:
        dommage_total = 0

    return(dommage_total)


# Calculate le multiplicateur de défense du joueur, lorsque celui-ci est en état de défense
# La force augmente ce multiplicateur
def player_multiplicateur_defense(player_stats,attacking=True,receiving=False):
    from fonctions_maths import function_multiplicateur_defense

    mult = function_multiplicateur_defense(player_stats['Force'],attacking,receiving)
    return(mult)


def spellbar_progress(player_stats):
    """
    Calcule le pourcentage (entre 0 et 100) de la barre de spell à remplir par attaque du joueur.

    Formule : function_mana_spellbar(Mana + 0.25 * Intelligence)
    (voir détails pour la fonction dans fonctions_maths.function_mana_spellbar)
    """
    from fonctions_maths import function_mana_spellbar
    mana = player_stats['Mana'] + 0.25*player_stats['Intelligence']

    return(function_mana_spellbar(mana))


def chance_fuite(player_stats,monster_stats):
    """
    Calcule les chances de fuite (entre 0 et 1) du joueur.

    Formule : function_fuite(Agilité_joueur,Agilité_monstre)
    (voir détails pour la fonction dans fonctions_maths.function_fuite)
    """
    from fonctions_maths import function_fuite
    x_player = player_stats['Agilité']
    x_monster = monster_stats['Agilité']

    return(function_fuite(x_player=x_player,x_monster=x_monster))