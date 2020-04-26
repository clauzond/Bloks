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

fun = function_agilite
l = []
for i in range(0,100,1):
    l.append(f"{fun(i):0.1f}")
print(l)

