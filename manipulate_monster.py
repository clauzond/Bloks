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



# Trouve un encounter random parmi un dossier donné qui contient tous les monstres
# Le level du mob devra être aux alentours de celui du joueur, sachant ques les mobs Elite et Legendary et 42 ont moins de chance de tomber
def random_encounter(player_dic,dossier):
    pass


# Calcule les drops que va lacher un monstre (les drops sont dans 'drop_list', si elle est vide/inexistante alors rien ne se passe)
# Les dropchance seront précisés dans l'item en question, dans une clé sur dictionnaire 'dropchance'
# Ce(s) drop(s) sera(seront) rarifié(s) au hasard à l'aide de la fonction manipulate_inventory.rarify_item(item,chance)
def random_drop(monster_dic,chance):
    pass