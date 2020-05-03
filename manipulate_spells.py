# Retourne la liste des passifs
def get_passive_list(spell_dic):

    passive_list = []

    # On regarde les 9 sorts
    for i in range(1,9):
        this_spell = spell_dic[f"spell{i}"]
        passive_list.append( this_spell['passive'] )

    return(passive_list)

# Fonction qui sert à effectuer le sort 1
def spell1(player_dic,monster_dic,spell_dic,outputbox,function = lambda None):




    # Quand on a tout terminé, on exécute "function"
    function()
