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
# Peut renvoyer le nouveau pourcentage des dégâts d'attaques
# ou le nouveau pourcentage des dégâts reçus
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
# Renvoie un nombre entre 10 et 50 (10% ou 50%)
def function_mana_spellbar(x):
    y = 10 + x*0.25
    if y>=50:
        y = 50
    return(y)

# La fonction détermine le pourcentage de chance de fuire
# L'agilité fera augmenté ces chances, mais l'agilité de l'adversaire les fera baisser
# Renvoie un nombre entre 0 et 1 (pourcentage)
def function_fuite(x_player,x_monster):
    if x_monster==0:
        return(1)
    # J'utilise la formule des générations 1 et 2 de Pokémon, en adaptant sachant que 32 = 255/8
    # Au lieu de 255, on prend 7200
    # Au lieu de 32 on prend 900 (car 7200/900 = 8)
    B = ((1/4)*x_monster)%7200
    F = ((x_player)*900)/B
    if F>7200:
        return(1)
    else:
        return(F/7200)



if __name__ == '__main__':
    fun = function_fuite
    l = []
    for i in range(0,100,1):
        l.append(f"{fun(i,257):0.2f}")
    print(l)
