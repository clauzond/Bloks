import manipulate_json as jm

class Player():

    def __init__(self,player_dic,attribut_dic,spell_dic,inventory_dic,x=100,y=100):

        self.player_dic = player_dic
        self.attribut_dic = attribut_dic
        self.spell_dic = spell_dic
        self.inventory_dic = inventory_dic

        self.fighting_stat_dic = {}


        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

    def __repr__(self):
        s = ''

        s += 'x,y : '+str(self.x)+','+str(self.y)
        s += '\n'
        s += 'vx,vy : '+str(self.vx)+','+str(self.vy)

        return(s)

    def save(self):
        import manipulate_stats as ms

        self.sort_inventory()

        self.player_dic = ms.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)

        jm.save_file(data=self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.spell_dic,filename='spell_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.inventory_dic,filename='inventory_dic',player_name=self.player_dic['name'])

    def load(self):
        import manipulate_stats as ms

        self.player_dic = jm.load_file(filename='player_dic',player_name=self.player_dic['name'])
        self.spell_dic = jm.load_file(filename='spell_dic',player_name=self.player_dic['name'])
        self.attribut_dic = jm.load_file(filename='attribut_dic',player_name=self.player_dic['name'])
        self.inventory_dic = jm.load_file(filename='inventory_dic',player_name=self.player_dic['name'])


    def sort_inventory(self):
        # On trie l'inventaire par id
        self.inventory_dic['itemlist'] = sorted(inventory_dic['itemlist'], key = lambda x: x['id'])




if __name__=='__main__':
    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')

    player = Player(player_dic,attribut_dic,spell_dic,inventory_dic,0,0)