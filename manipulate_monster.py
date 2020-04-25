# On fera une version d'un monstre par tranche de 5 niveaux
# Avec suffisamment de monstres, cela suffira à trouver des monstres divers d'un niveau proche de celui du joueur

# Un monstre est représenté par son dictionnaire


# Cette fonction va ajouter des stats au mob avec des pourcentages
# Si le mob est elite ou légendaire, cette fonction ne changera rien
def rarify_monster(monster_dic):
    if monster_dic['category'] in ['Elite','Legendary','42']:
        return(monster_dic)


    for stat in monster_dic['stats'].keys():
        from random import random

        r = random() * 100

        if r<1:

        elif r<5:

        elif r<10:


        elif r<25: