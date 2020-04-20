import json_manager as jm

class Player():

    def __init__(self,player_dic,attribut_dic,spell_dic,inventory_dic,x=100,y=100):

        self.player_dic = player_dic
        self.attribut_dic = attribut_dic
        self.spell_dic = spell_dic
        self.inventory_dic = inventory_dic

        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

    def __repr__(self):
        s = ''
        s += 'player_dic : '+str(self.player_dic)
        s += '\n'
        s += 'attribut_dic : '+str(self.attribut_dic)
        s += '\n'
        s += 'spell_dic : '+str(self.spell_dic)
        s += '\n'
        s += 'x,y : '+str(self.x)+','+str(self.y)
        s += '\n'
        s += 'vx,vy : '+str(self.vx)+','+str(self.vy)

        return(s)

    def save(self):
        jm.save_file(data=self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.spell_dic,filename='spell_dic',player_name=self.player_dic['name'])
        jm.save_file(data=self.inventory_dic,filename='inventory_dic',player_name=self.player_dic['name'])




if __name__=='__main__':
    from dictionnaires import dictionnaires_vierge
    player_dic,attribut_dic,spell_dic,inventory_dic = dictionnaires_vierge()
    player = Player(player_dic,attribut_dic,spell_dic,inventory_dic,0,0)