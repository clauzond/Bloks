class Player():

    def __init__(self,player_dic,attribut_dic,spell_dic,spellbind_dic,x,y):

        self.player_dic = player_dic
        self.attribut_dic = attribut_dic
        self.spell_dic = spell_dic
        self.spellbind_dic = spellbind_dic

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
        s += 'x,y : '+str(self.x)+','+str(self.y)
        s += '\n'
        s += 'vx,vy : '+str(self.vx)+','+str(self.vy)

        return(s)



if __name__=='__main__':
    from dictionnaires import dictionnaires_vierge
    player_dic,attribut_dic = dictionnaires_vierge()
    player = Player(player_dic,attribut_dic,0,0)