# Retourne la liste des passifs
def get_passive_list(spell_dic):

    passive_list = []

    # On regarde les 9 sorts
    for i in range(1,9):
        this_spell = spell_dic[f"spell{i}"]
        passive_list.append( this_spell['passive'] )

    return(passive_list)


def cast_spell(spell_number,player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):
    spell_number = int(spell_number)
    if spell_number==1:
        spell1(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==2:
        spell2(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==3:
        spell3(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==4:
        spell4(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==5:
        spell5(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==6:
        spell8(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==7:
        spell7(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)
    elif spell_number==8:
        spell8(player_stats=player_stats,monster_dic=monster_dic,spell_dic=spell_dic,outputbox=outputbox,function=function)



# Fonction qui sert à effectuer le sort 1
def spell1(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell2(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell3(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell4(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell5(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell6(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell7(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()

# Fonction qui sert à effectuer le sort 1
def spell8(player_stats,monster_dic,spell_dic,outputbox,function = lambda:None):

    # Quand on a tout terminé, on exécute "function"
    function()
