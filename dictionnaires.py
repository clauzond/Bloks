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


def dictionnaires_vierge(loadcolor=False,loadimg=False,loadattributtip=False,loadspelltip=False,loadspellname=False,loadlevelupdics=False):
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

    elif loadlevelupdics:
        return(load_levelupdics())

    else:
        attribut_dic = {'HP':3,
                        'Mana':3,
                        'Force':3,
                        'Agilité':3,
                        'Intelligence':3,
                        'Chance':3
                        }
        player_dic = {  "name":'Blue Dragon',
                        "level":4,
                        "current_xp":20,
                        "max_xp":100,
                        "total_xp":390,
                        "attribut_point":15,
                        "spell_point":3
                        }

        spell_dic = load_spell('blank')

        spellbind_dic = load_spell('bind')


        return(player_dic,attribut_dic,spell_dic,spellbind_dic)