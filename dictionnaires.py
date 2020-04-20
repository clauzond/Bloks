from tkinter import PhotoImage


def load_levelupdics():
    dic = {'max_xp':[],'attribut_gain':{},'attribut_point_gain':[],'spell_point_gain':[]}

    # load max_xp
    fich = open('ressources/levelup/max_xp.txt','r',encoding='utf-8')
    liste = fich.readlines()
    fich.close()

    mylist = [0] # pour le niveau 0
    for i in range(len(liste)):
        x = liste[i].replace('\n','').split('|')[1]
        mylist.append(int(x))
    dic['max_xp'] = mylist

    # load attribut_gain
    fich = open('ressources/levelup/attribut_gain.txt','r',encoding='utf-8')
    liste = fich.readlines()
    fich.close()

    mydic = {'HP':[0],'Mana':[0],'Force':[0],'Agilité':[0],'Chance':[0],'Intelligence':[0]}
    for i in range(len(liste)):
        xliste = liste[i].replace('\n','').split('|')[1:]

        for elem in xliste:
            nom = str(elem[:-1])
            x = elem[-1] # les attributs gagnés par level seront < 10
            mydic[nom].append(int(x))

    dic['attribut_gain'] = mydic

    # load attribut_point_gain
    fich = open('ressources/levelup/attribut_point_gain.txt','r',encoding='utf-8')
    liste = fich.readlines()
    fich.close()

    mylist = [0] # pour le niveau 0
    for i in range(len(liste)):
        x = liste[i].replace('\n','').split('|+')[1]
        mylist.append(int(x))
    dic['attribut_point_gain'] = mylist

    # load spell_point_gain
    fich = open('ressources/levelup/spell_point_gain.txt','r',encoding='utf-8')
    liste = fich.readlines()
    fich.close()

    mylist = [0] # pour le niveau 0
    for i in range(len(liste)):
        x = liste[i].replace('\n','').split('|+')[1]
        mylist.append(int(x))
    dic['spell_point_gain'] = mylist

    return(dic)

def load_images():
    """
    images des attributs en 30x30
    images des sorts en 50x50
    """
    agilite=PhotoImage(file="img/agilite.gif")
    force=PhotoImage(file="img/force.gif")
    chance=PhotoImage(file="img/chance.gif")
    intelligence=PhotoImage(file="img/intelligence.gif")
    hp=PhotoImage(file="img/hp.gif")
    mana=PhotoImage(file="img/mana.gif")
    neutre=PhotoImage(file="img/neutre.gif")
    star=PhotoImage(file="img/star.gif")
    xp=PhotoImage(file='img/xp.gif')
    xpblanc=PhotoImage(file='img/xpblanc.gif')
    xpnoir=PhotoImage(file='img/xpnoir.gif')
    player=PhotoImage(file='img/player.gif')
    starnoir=PhotoImage(file='img/starnoir.gif')

    spell=PhotoImage(file='img/spell.gif')
    money=PhotoImage(file='img/kamas.gif')

    item_default=PhotoImage(file='img/item.gif')

    img_dic = {     'HP':hp,
                    'Mana':mana,
                    'Force':force,
                    'Agilité':agilite,
                    'Intelligence':intelligence,
                    'Chance':chance,
                    'xp':xp,
                    'xpblanc':xpblanc,
                    'xpnoir':xpnoir,
                    'star':star,
                    'Neutre':neutre,
                    'player':player,
                    'starnoir':starnoir,
                    'spell1':spell,
                    'spell2':spell,
                    'spell3':spell,
                    'spell4':spell,
                    'spell5':spell,
                    'spell6':spell,
                    'spell7':spell,
                    'spell8':spell,
                    'item':item_default,
                    'money':money
                }


    return(img_dic)



    return(img_dic)

def load_colors():
    color_dic = {   'HP':'#FF1E1E',
                    'Mana':'#02AFFD',
                    'Force':'#815633',
                    'Agilité':'#2A6E2C',
                    'Intelligence': '#D13800',
                    'Chance':'#398A89',
                    'spell1':'#4C652B',
                    'spell2':'#4C652B',
                    'spell3':'#4C652B',
                    'spell4':'#4C652B',
                    'spell5':'#4C652B',
                    'spell6':'#4C652B'
                }
    return(color_dic)

def load_spell_dic():
    import json_manager as jm

    return(jm.load_file(filename='spell_dic',player_name='template',fulldir='ressources/template/spell_dic.json'))

def load_attribut_dic():
    import json_manager as jm

    return(jm.load_file(filename='attribut_dic',player_name='template',fulldir='ressources/template/attribut_dic.json'))

def load_player_dic():
    import json_manager as jm

    return(jm.load_file(filename='player_dic',player_name='template',fulldir='ressources/template/player_dic.json'))

def load_inventory_dic():
    import json_manager as jm

    return(jm.load_file(filename='inventory_dic',player_name='template',fulldir='ressources/template/inventory_dic.json'))


def dictionnaires_vierge(loadcolor=False,loadimg=False,loadspelltip=False,loadspellname=False,loadlevelupdics=False):
    if loadimg:
        return(load_images())

    elif loadcolor:
        return(load_colors())

    elif loadlevelupdics:
        return(load_levelupdics())

    else:
        attribut_dic = load_attribut_dic()

        player_dic = load_player_dic()
        #spell_dic = load_spell('blank')

        #spellbind_dic = load_spell('bind')

        spell_dic = load_spell_dic()

        inventory_dic = load_inventory_dic()
        return(player_dic,attribut_dic,spell_dic,inventory_dic)