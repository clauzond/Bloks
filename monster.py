# La classe commune à tous les monstres
# Les monstres sont des sous-classes de celle-ci

class Monster():

    def __init__(self,_name,_description,_level,_category,_imagedir,_element,_statsdic):


        dic = {
        'name':_name,
        'description':_description,
        'level':_level,
        'category':_category, # catéforie = Friendly, Common, Elite, Legendary ou 42
        'image':_imageidr,
        'element':_element, # element = Force,Agilité,Intelligence ou Chance
        'stats':_statsdic # contient toutes les stats nécessaires dans stats_window.py
        }


        self.dic = dic



    # applique un bonus ou un malus
    def boost(self,attribut,valeur):

        if attribut in self.dic['stats']:
            self.dic['stats'][attribut] += valeur
        else:
            self.dic['stats'][attribut] = valeur

    # calcule les dommages infligés (avec les stats actuels) par le monstre
    # pas de sort pour les monstres pour le moment
    def calculate_damage(self):
        import manipulate_stats as ms

        ms.calculate_damage_monster(stat_dic = self.dic['stats'],element=self.dic['element'])