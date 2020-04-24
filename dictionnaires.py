from tkinter import PhotoImage

def load_images():
    """
    images des attributs en 30x30
    images des sorts en 50x50
    """
    neutre=PhotoImage(file="img/neutre.gif")
    star=PhotoImage(file="img/star.gif")
    xp=PhotoImage(file='img/xp.gif')
    xpblanc=PhotoImage(file='img/xpblanc.gif')
    xpnoir=PhotoImage(file='img/xpnoir.gif')
    starnoir=PhotoImage(file='img/starnoir.gif')
    nothing=PhotoImage(file='img/nothing.gif')
    vide=PhotoImage(file="img/vide.gif")

    friendly = PhotoImage(file='img/monster.gif')
    common = PhotoImage(file='img/monster.gif')
    elite = PhotoImage(file='img/monster.gif')
    legendary = PhotoImage(file='img/monster.gif')
    _42 = PhotoImage(file='img/monster.gif')


    money=PhotoImage(file='img/kamas.gif')


    img_dic = {     'xp':xp,
                    'xpblanc':xpblanc,
                    'xpnoir':xpnoir,
                    'star':star,
                    'Neutre':neutre,
                    'starnoir':starnoir,
                    'money':money,
                    'nothing':nothing,
                    "Friendly":friendly,
                    "Common":common,
                    "Elite":elite,
                    "Legendary":legendary,
                    "42":_42,
                    "vide":vide
                }


    return(img_dic)



    return(img_dic)


def load_spell_dic():
    import manipulate_json as jm

    return(jm.load_file(fulldir='ressources/template/spell_dic.json'))

def load_attribut_dic():
    import manipulate_json as jm

    return(jm.load_file(fulldir='ressources/template/attribut_dic.json'))

def load_player_dic():
    import manipulate_json as jm

    return(jm.load_file(fulldir='ressources/template/player_dic.json'))

def load_inventory_dic():
    import manipulate_json as jm

    return(jm.load_file(fulldir='ressources/template/inventory_dic.json'))


def dictionnaires_vierge(loadimg=False,loadspelltip=False,loadspellname=False,loadlevelupdics=False):
    if loadimg:
        return(load_images())

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