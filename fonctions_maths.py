from math import *

# L'important c'est que d'avoir trop de speed n'est pas broken comparé à pas beaucoup de speed
# Avec cette fonction, au mieux on joue 2 fois plus vite
# Il ne faudrait pas non plus que jouer full agilité permet d'outspeed tout le monde à ce point !
def function_speed(x):
    y = log(10+x)
    return(y)


# La fonction pour la chance : très peu au début, mais augmente quand même raisonnablement
def function_chance(x):
    y = x**(1/3)
    return(y)


# La fonction pour déterminer combien fait gagner la force au multiplicateur de défense
# La valeur en sortie doit être entre 0 et 0.
def function_multiplicateur_defense(x,attacking=True,receiving=False):
    y = x/1000
    if y>0.25:
        y=0.25
    y += 0.4
    if attacking:
        return(y)
    elif receiving:
        return(1 - y*0.5)

# La fonction détermine le nombre de pourcentage de barre de spell gagnée par attaque
# Par défaut, on veut 10% par attaque et maximum 50% pour +200 mana
def function_mana_spellbar(x):
    y = 10 + x*0.25
    if y>=50:
        y = 50
    return(y)

if __name__ == '__main__':
    fun = function_mana_spellbar
    l = []
    for i in range(0,200,1):
        l.append(f"{fun(i):0.1f}")
    print(l)
