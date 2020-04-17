from tkinter import PhotoImage


def load_images():
    agilite=PhotoImage(file="img/agilite.gif")
    force=PhotoImage(file="img/force.gif")
    chance=PhotoImage(file="img/chance.gif")
    intelligence=PhotoImage(file="img/intelligence.gif")
    hp=PhotoImage(file="img/hp.gif")
    mana=PhotoImage(file="img/mana.gif")
    neutre=PhotoImage(file="img/neutre.gif")
    star=PhotoImage(file="img/star.gif")

    liste=[agilite,force,chance,intelligence,hp,mana,neutre,star]
    liste2=['Agilité','Force','Chance','Intelligence','HP','Mana','Neutre','Star']

    dic = {}
    for i in range(len(liste)):
        dic[liste2[i]] = liste[i]
    return(dic)