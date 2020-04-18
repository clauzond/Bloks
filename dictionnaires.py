from tkinter import PhotoImage


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
                    'spell6':spell
                }


    return(img_dic)



    return(img_dic)

def load_attribut_tips():
    dic = { 'HP':'',
            'Mana':'',
            'Force':'',
            'Agilité':'',
            'Intelligence':'',
            'Chance':''
            }

    namelist = list(dic.keys())

    for name in namelist:
        fich = open(f'tooltips/attribut/{name}.txt',mode='r',encoding='utf-8')
        textlist=fich.readlines()

        s = ""
        for ligne in textlist:
            s+=ligne

        dic[name] = s
        fich.close()

    return(dic)


def load_spell(type):
    dic = { 'spell1':'Nom du premier sort',
            'spell2':'Nom du deuxième sort',
            'spell3':'Nom du troisième sort',
            'spell4':'Nom du quatrième sort',
            'spell5':'Nom du cinquième sort',
            'spell6':'Nom du sixième sort'
            }

    if type=='tip':
        namelist = list(dic.keys())

        for name in namelist:
            fich = open(f'tooltips/spell/{name}.txt',mode='r',encoding='utf-8')
            textlist=fich.readlines()

            s = ""
            for ligne in textlist:
                s+=ligne

            dic[name] = s
            fich.close()

        return(dic)

    elif type=='name':
        return(dic)

    elif type=='bind':
        namelist=list(dic.keys())

        for name in namelist:
            dic[name] = 'None'
        dic['active'] = ['spell1','spell2','spell3']
        return(dic)

    elif type=='blank':
        l = list(dic.keys())
        for x in l:
            dic[x] = 0
        return(dic)

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


def dictionnaires_vierge(loadcolor=False,loadimg=False,loadattributtip=False,loadspelltip=False,loadspellname=False):
    if loadimg:
        return(load_images())

    elif loadcolor:
        return(load_colors())

    elif loadattributtip:
        return(load_attribut_tips())

    elif loadspelltip:
        return(load_spell('tip'))

    elif loadspellname:
        return(load_spell('name'))

    else:
        attribut_dic = {'HP':0,
                        'Mana':0,
                        'Force':0,
                        'Agilité':0,
                        'Intelligence':0,
                        'Chance':0
                        }
        player_dic = {  "name":'Blue Dragon',
                        "level":1,
                        "current_xp":0,
                        "max_xp":10,
                        "attribut_point":3,
                        "spell_point":2
                        }

        spell_dic = load_spell('blank')

        spellbind_dic = load_spell('bind')


        return(player_dic,attribut_dic,spell_dic,spellbind_dic)