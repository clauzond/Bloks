from tkinter import *

class Main_Window():

    def __init__(self,player_name):


        self.main_window = Tk()


        self.main_window.title("Bloks")
        self.main_window.resizable(False, False)
        self.main_window.iconbitmap("img/icone.ico")

        self.main_window.option_add('*Font','Constantia 12')
        self.main_window.option_add('*Button.activebackground','darkgray')
        self.main_window.option_add('*Button.activeforeground','darkgray')
        self.main_window.option_add('*Button.relief','groove')
        self.main_window.option_add('*Button.overRelief','ridge')
        self.main_window.option_add('*justify','left')
        self.main_window.option_add('*background','lightgray')
        self.main_window.option_add('*compound','left')

        self.main_window.configure(bg='gray')
        self.main_window.attributes("-fullscreen", True)



        # Actuellement : 1280 * 720
        self.main_canvas = Canvas(self.main_window,width=16*80,height=9*80)
        self.main_canvas.pack(expand=True)

        # Actuellement : 1280 * 560
        self.game_canvas = Canvas(self.main_canvas,width=16*80,height=7*80)
        self.game_canvas.pack(expand=True,side=TOP,fill=BOTH)
        self.game_canvas.update()

        self.menu_canvas = Canvas(self.main_canvas,width=8*80,height=2*80)
        self.menu_canvas.pack(expand=True,side=LEFT,fill=BOTH)
        self.menu_canvas.update()

        self.other_canvas = Canvas(self.main_canvas,width=8*80,height=2*80)
        self.other_canvas.pack(expand=True,side=RIGHT,fill=BOTH)
        self.other_canvas.update()

        self.combat = False
        self.exploration = False

        import manipulate_json as jm
        self.player_dic = jm.load_file(filename='player_dic',player_name=player_name)
        self.spell_dic = jm.load_file(filename='spell_dic',player_name=player_name)
        self.attribut_dic = jm.load_file(filename='attribut_dic',player_name=player_name)
        self.inventory_dic = jm.load_file(filename='inventory_dic',player_name=player_name)

        self.draw_menu_canvas()



    def save_all(self):
        import manipulate_stats as ms

        self.player_dic = manipulate_stats.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)

        import manipulate_json as jm

        jm.save_file(self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])
        jm.save_file(self.inventory_dic,filename='inventory_dic',player_name=self.player_dic['name'])
        jm.save_file(self.spell_dic,filename='spell_dic',player_name=self.player_dic['name'])

        print('Everything has been saved !')


    def reload_everything(self,*args):
        print("Everything was loaded")
        self.player_dic = jm.load_file(filename='player_dic',player_name=self.player_dic['name'])
        self.spell_dic = jm.load_file(filename='spell_dic',player_name=self.player_dic['name'])
        self.attribut_dic = jm.load_file(filename='attribut_dic',player_name=self.player_dic['name'])
        self.inventory_dic = jm.load_file(filename='inventory_dic',player_name=self.player_dic['name'])


    ## Menu canvas related functions ##

    def draw_menu_canvas(self):
        self.StatsButton = Button(self.menu_canvas,text="Stats",command=self.openstatwindow)
        self.StatsButton.pack(fill='both',expand=True,side=LEFT)

        self.AttributButton = Button(self.menu_canvas,text="Attributs",command=self.openattributwindow)
        self.AttributButton.pack(fill='both',expand=True,side=LEFT)

        self.SpellButton = Button(self.menu_canvas,text="Spells",command=self.openspellwindow)
        self.SpellButton.pack(fill='both',expand=True,side=LEFT)

        self.InventoryButton = Button(self.menu_canvas,text="Inventaire",command=self.openinventorywindow)
        self.InventoryButton.pack(fill='both',expand=True,side=LEFT)

        self.LevelupButton = Button(self.menu_canvas,text="Level Up",command=self.openlevelupwindow)
        self.LevelupButton.pack(fill='both',expand=True,side=LEFT)

    def openstatwindow(self):
        import stats_window as sw

        w = sw.StatsWindow(toplevel=True)
        w.show(stat_dic=self.player_dic['stats'],name=self.player_dic['name'],level=self.player_dic['level'],image_dir=self.player_dic['image'])

    def openspellwindow(self):
        import spell_window as spw

        w = spw.SpellWindow(toplevel=True)
        w.show(player_dic=self.player_dic,spell_dic=self.spell_dic,function=self.reload_everything)

    def openinventorywindow(self):
        import inventory_window as iw

        w = iw.InventoryWindow(toplevel=True,player_dic=self.player_dic,inventory_dic=self.inventory_dic,attribut_dic=self.attribut_dic,function = self.reload_everything)

    def openattributwindow(self):
        import attribut_window as aw

        w = aw.AttributWindow(toplevel=True)
        w.show(player_dic=self.player_dic,attribut_dic=self.attribut_dic,function=self.reload_everything)

    def openlevelupwindow(self):
        import levelup_window as luw

        w = luw.Levelup_Window(toplevel=True,player_dic=self.player_dic,attribut_dic=self.attribut_dic,function = self.reload_everything)




    ## Combat-related functions ##
    def show_combat(self,monster_dic):
        import healthbar
        import speedbar
        import outputbox

        #a = Frame(self.game_canvas,width=100).place(x=16*75,y=7*75)

        self.combat = True
        self.playerturn = False

        self.monster_name = monster_dic['name']

        self.monster_element = monster_dic['element']



        # Ces 3 dictionnaires pourront bouger en plein combat, et sont recréés pour les manipuler
        self.player_stats = player_dic['stats']
        self.monster_stats = monster_dic['stats']
        self.equipped_list = player_dic['equipped_list']

        # self.game_canvas
        hpmax = self.player_stats['HP']
        self.player_healthbar = healthbar.HealthBar(canvas=self.game_canvas,length=100,maximum=hpmax,x=500,y=470,color="red")
        self.player_healthbar.show()

        hpmax = self.monster_stats['HP']
        self.monster_healthbar = healthbar.HealthBar(canvas=self.game_canvas,length=100,maximum=hpmax,x=100,y=470,color="red")
        self.monster_healthbar.show()

        # monstre en rouge, joueur en jaune
        speed1=self.monster_stats['Agilité']
        speed2=self.player_stats['Agilité']
        self.speedbar = speedbar.SpeedBar(canvas=self.game_canvas,x=5,y=200,length=200,max1=100,max2=100,speed1=speed1,speed2=speed2,color1="red",color2="yellow",bg="gray")
        self.speedbar.show()


        x = self.game_canvas.winfo_width() - 300 - 2
        y = self.game_canvas.winfo_height() - 200 - 2
        self.outputbox = outputbox.OutputBox(canvas=self.game_canvas,x=x,y=y,height=200,width=300)
        self.outputbox.show()

        # self.other_canvas
        self.playbutton = Button(self.other_canvas,text="PLAY",command=self.play_combat)
        self.playbutton.pack(expand=False,fill='x',padx=2,pady=5)

        self.attackbutton = Button(self.other_canvas,text="ATTACK",state=DISABLED,command=self.player_attack)
        self.attackbutton.pack(expand=False,fill='x',padx=2,pady=5)


        self.defendbutton = Button(self.other_canvas,text="DEFEND",state=DISABLED,command=self.player_defend)
        self.defendbutton.pack(expand=False,fill='x',padx=2,pady=5)


    def play_combat2(self):
        self.order = self.speedbar.order

        if self.order == None:
            print("Attendez !")
        # Tour du monstre
        elif self.order == 1:
            self.monster_attack()

            self.play_combat()


        # Tour du joueur
        elif self.order == 2:
            self.playerturn = True
            self.attackbutton.config(state=NORMAL)
            self.defendbutton.config(state=NORMAL)

    def play_combat(self):

        self.order = self.speedbar.lets_go()

        self.playbutton.config(state=DISABLED)
        self.main_window.after(2000,self.play_combat2)





    def refresh_speed_player(self):
        if not self.combat:
            return

        speed2 = self.player_stats['Agilité']

        if speed2 > self.speedbar.id_speed2:
            self.speedbar.set_speed2(speed2)
            self.outputbox.add_text(f"{self.player_dic['name']} a accéléré !")
        elif speed2 < self.speedbar.id_speed2:
            self.speedbar.set_speed2(speed2)
            self.outputbox.add_text(f"{self.player_dic['name']} a été ralenti !")


    def refresh_speed_monster(self):
        if not self.combat:
            return

        speed1 = self.monster_stats['Agilité']

        if speed1 > self.speedbar.id_speed1:
            self.speedbar.set_speed1(speed1)
            self.outputbox.add_text(f"{self.monster_name} a accéléré !")
        elif speed1 < self.speedbar.id_speed1:
            self.speedbar.set_speed1(speed1)
            self.outputbox.add_text(f'{self.monster_name} a été ralenti !')


    def player_defend(self):
        print("Touche de défense - inutile")

    def player_attack(self):
        if (not self.combat) or (not self.playerturn):
            return
        import manipulate_stats as ms

        damage = ms.calculate_damage_player(player_stats = self.player_stats,monster_stats = self.monster_stats,player_itemlist=self.equipped_list)

        self.monster_healthbar.take_hit(damage)
        if damage>1:
            s='s'
        else:
            s=''
        self.outputbox.add_text(f'{self.monster_name} a subi {damage:0.1f} dommage{s}')
        self.monster_stats['HP'] -= damage

        if self.monster_stats['HP'] < 0:
            self.outputbox.add_text(f'{self.monster_name} a été vaincu !')
            self.player_wincombat()

        else:
            self.playerturn = False
            self.attackbutton.config(state=DISABLED)
            self.defendbutton.config(state=DISABLED)
            #self.playbutton.config(state=NORMAL)
            self.play_combat()


    def monster_attack(self):
        if not self.combat:
            return
        import manipulate_stats as ms

        damage = ms.calculate_damage_monster(monster_stats=self.monster_stats,player_stats = self.player_stats,element=self.monster_element)

        self.player_healthbar.take_hit(damage)
        self.player_stats['HP'] -= damage
        if damage>1:
            s='s'
        else:
            s=''
        self.outputbox.add_text(f"{self.player_dic['name']} a subi {damage:0.1f} dommage{s}")


        if self.player_stats['HP'] < 0:
            self.outputbox.add_text(f"{self.player_dic['name']} a été vaincu !")
            self.player_losecombat()

        else:
            pass
            #self.playbutton.config(state=NORMAL)

    def player_wincombat(self):
        print('Gagné')

    def player_losecombat(self):
        print('Perdu')

    def hide_combat(self):
        self.player_healthbar.hidetip()
        self.monster_healthbar.hidetip()
        self.speedbar.hidetip()
        self.outputbox.hidetip()

        self.combat = False
        self.player_stats = None
        self.monster_stats = None


if __name__ == "__main__":
    import manipulate_json as jm

    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')
    monster_dic = jm.load_file(fulldir="ressources/template/monster/slime_bleu.json")





    w = Main_Window(player_dic['name'])

    w.show_combat(monster_dic=monster_dic)

#    w.outputbox.add_text("Salut\nCeci\nest\nun\ntest")
    #w.speedbar.start()
    #w.healthbar.take_hit(1000)


    w.main_window.focus_force()
    w.main_window.mainloop()