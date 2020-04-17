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
                    'spell':spell
                }


    return(img_dic)



    return(img_dic)

def load_tooltips():
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
    dic = { 'Spell 1':0,
            'Spell 2':0,
            'Spell 3':0,
            'Spell 4':0,
            'Spell 5':0,
            'Spell 6':0
            }

    if type=='tip':
        namelist = list(dic.keys())

        for name in namelist:
            fich = open(f'tooltips/{name}.txt',mode='r',encoding='utf-8')
            textlist=fich.readlines()

            s = ""
            for ligne in textlist:
                s+=ligne

            dic[name] = s
            fich.close()

        return(dic)

    else:
        return(dic)



def dictionnaires_vierge(loadcolor=False,loadimg=False,loadtooltip=False,loadspelltip=False):
    if loadimg:
        img_dic = load_images()
        return(img_dic)

    elif loadcolor:
        color_dic = {   'HP':'#FF1E1E',
                        'Mana':'#02AFFD',
                        'Force':'#815633',
                        'Agilité':'#2A6E2C',
                        'Intelligence': '#D13800',
                        'Chance':'#398A89'
                    }
        return(color_dic)

    elif loadtooltip:
        return(load_tooltips())

    elif loadspelltip:
        return(load_spell('tip'))

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
                        "skill_point":2
                        }

        spell_dic = load_spell('blank')


        return(player_dic,attribut_dic,spell_dic)