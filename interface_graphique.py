from tkinter import *

class Main_Window():

    def __init__(self,player_name):


        self.main_window = Tk()


        self.main_window.title("Bloks")
        self.main_window.resizable(False, False)
        self.main_window.iconbitmap("img/icone.ico")

        self.main_window.option_add('*Font','Constantia 12')
        self.main_window.option_add('*Button.relief','flat')
        self.main_window.option_add('*Button.overRelief','ridge')
        self.main_window.option_add('*justify','left')
        self.backgroundcolor='#8BD8BD'
        self.foregroundcolor='#243665'
        self.main_window.option_add('*background',self.backgroundcolor)
        self.main_window.option_add('*foreground',self.foregroundcolor)
        self.main_window.option_add('*compound','left')

        #self.main_window.configure(bg='gray')
        self.main_window.attributes("-fullscreen", True)



        # Actuellement : 1280 * 720
        #self.main_canvas = Canvas(self.main_window,width=16*80,height=9*80)
        #self.main_canvas.pack(expand=True,fill="both")

        # Actuellement : 1280 * 560
        self.game_canvas = Canvas(self.main_window,width=16*80,height=7*80)
        self.game_canvas.pack(expand=True,fill="both")
        self.game_canvas.update()

        height = self.game_canvas.winfo_height()
        width = self.game_canvas.winfo_width()

        import outputbox
        self.outputbox = outputbox.OutputBox(canvas=self.game_canvas,x=width-300,y=height-300-200,height=300,width=300)
        self.outputbox.show()

        self.myMap = None
        self.combat = False

        import manipulate_json as jm
        self.player_dic = jm.load_file(filename='player_dic',player_name=player_name)
        self.spell_dic = jm.load_file(filename='spell_dic',player_name=player_name)
        self.attribut_dic = jm.load_file(filename='attribut_dic',player_name=player_name)
        self.inventory_dic = jm.load_file(filename='inventory_dic',player_name=player_name)

        self.draw_menu()


    # Une fonction qui DOIT ne rien renvoyer
    # Elle sera utilisée régulièrement, quand un changement est effectué "globalement dans les dictionnaires", mais pas réellement dans le disque
    def save_all(self,*args):
        import manipulate_stats as ms

        self.player_dic = ms.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)

        import manipulate_json as jm

        jm.save_file(self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])
        jm.save_file(self.inventory_dic,filename='inventory_dic',player_name=self.player_dic['name'])
        jm.save_file(self.spell_dic,filename='spell_dic',player_name=self.player_dic['name'])

        self.outputbox.add_text('Everything has been saved')


    # Une fonction qui DOIT ne rien renvoyer
    def reload_everything(self,*args):
        import manipulate_stats as ms

        self.player_dic = ms.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)

        import manipulate_json as jm

        self.player_dic = jm.load_file(filename='player_dic',player_name=self.player_dic['name'])
        self.spell_dic = jm.load_file(filename='spell_dic',player_name=self.player_dic['name'])
        self.attribut_dic = jm.load_file(filename='attribut_dic',player_name=self.player_dic['name'])
        self.inventory_dic = jm.load_file(filename='inventory_dic',player_name=self.player_dic['name'])

        #self.outputbox.add_text('Everything has been loaded')





    ## Menu canvas related functions ##

    def draw_menu(self):
        height = self.game_canvas.winfo_height()


        self.StatsButton = Button(self.game_canvas,text="Stats",command=self.openstatwindow)
        self.StatsButton.place(x=50,y=height-50,anchor='s')


        self.AttributButton = Button(self.game_canvas,text="Attributs",command=self.openattributwindow)
        self.AttributButton.place(x=50+150,y=height-50,anchor='s')

        self.SpellButton = Button(self.game_canvas,text="Spells",command=self.openspellwindow)
        self.SpellButton.place(x=50+300,y=height-50,anchor='s')

        self.InventoryButton = Button(self.game_canvas,text="Inventaire",command=self.openinventorywindow)
        self.InventoryButton.place(x=50+450,y=height-50,anchor='s')

        self.LevelupButton = Button(self.game_canvas,text="Level Up",command=self.openlevelupwindow)
        self.LevelupButton.place(x=50+600,y=height-50,anchor='s')


    def openstatwindow(self):
        import stats_window as sw

        x = self.game_canvas.winfo_width() / 4
        y = self.game_canvas.winfo_height() / 4 - 100

        w = sw.StatsWindow(toplevel=True)
        w.show(stat_dic=self.player_dic['stats'],name=self.player_dic['name'],level=self.player_dic['level'],image_dir=self.player_dic['image'],rel_x=x,rel_y=y)

    def openspellwindow(self):
        import spell_window as spw

        x = self.game_canvas.winfo_width() / 4
        y = self.game_canvas.winfo_height() / 4 - 100

        w = spw.SpellWindow(toplevel=True)
        w.show(player_dic=self.player_dic,spell_dic=self.spell_dic,function=self.save_all,rel_x=x,rel_y=y)

    def openinventorywindow(self):
        import inventory_window as iw

        x = self.game_canvas.winfo_width() / 4
        y = self.game_canvas.winfo_height() / 4 - 100

        w = iw.InventoryWindow(toplevel=True,player_dic=self.player_dic,inventory_dic=self.inventory_dic,attribut_dic=self.attribut_dic,function = self.save_all,rel_x=x,rel_y=y)

    def openattributwindow(self):
        import attribut_window as aw

        x = self.game_canvas.winfo_width() / 4
        y = self.game_canvas.winfo_height() / 4 - 100

        w = aw.AttributWindow(toplevel=True)
        w.show(player_dic=self.player_dic,attribut_dic=self.attribut_dic,function=self.save_all,rel_x=x,rel_y=y)

    def openlevelupwindow(self):
        import levelup_window as luw

        x = self.game_canvas.winfo_width() / 4
        y = self.game_canvas.winfo_height() / 4 - 100

        w = luw.Levelup_Window(toplevel=True,player_dic=self.player_dic,attribut_dic=self.attribut_dic,function = self.save_all,rel_x=x,rel_y=y)



    ## Map-related functions ##
    import manipulate_map as mm
    def load_map(self,mapdir,mapname,tilename,imgdir):
        self.myMap = mm.load_map(mapdir,mapname,tilename,imgdir)


    def load_player(self,player_imgdir):
        import manipulate_showplayer as msp
        self.player_image = PhotoImage(file=player_imgdir)
        self.showplayer = msp.ShowPlayer(window=self.main_window,
                                    draw_map_function = self.draw_map,
                                    game_canvas = self.game_canvas,
                                    player_photoimage = self.player_image,
                                    outputbox=self.outputbox,
                                    x_limit = self.myMap.x_limit,
                                    y_limit = self.myMap.y_limit)





    def test(self,event):
        self.outputbox.add_text(text=f"{event.x},{event.y}")

    def clear_map(self):
        self.game_canvas.delete('all')


    # La fonction draw_map doit prendre en argument seulement les x,y du bloc tout en haut à gauche de l'écran
    # Attention : x et y sont en "numéro de bloc"
    # 1,1 correspond donc au bloc en haut à gauche ligne 1 colonne 1
    # Ainsi, si x_debut = 0.5, on ne voit affiché que la moitié (en x) du bloc en haut à gauche
    def draw_map(self,x_debut,y_debut):
        if self.myMap is None:
            return()

        self.myMap.draw_map(canvas=self.game_canvas,x_debut=x_debut,y_debut=y_debut)

    def draw_player(self,x_debut,y_debut):
        self.showplayer.draw(x_map = x_debut, y_map = y_debut)

        self.game_canvas.bind_all('<Left>',self.showplayer.move_left)
        self.game_canvas.bind_all('<Right>',self.showplayer.move_right)
        self.game_canvas.bind_all('<space>',self.showplayer.jump)
        self.game_canvas.bind_all('<Down>',self.showplayer.go_down)
        self.game_canvas.bind_all('<Up>',self.showplayer.check_usable)

        self.game_canvas.bind_all('<Button-1>',self.test)

        pass


    def move_left(self):
        pass
    def move_right(self):
        pass
    def move_up(self):
        pass
    def move_down(self):
        pass



    ## Combat-related functions ##
    def show_combat(self,monster_dic):
        import healthbar
        import speedbar
        import outputbox

        # Désactive tous les boutons de Menu inutiles
        self.AttributButton.config(state=DISABLED)
        self.SpellButton.config(state=DISABLED)
        self.InventoryButton.config(state=DISABLED)
        self.LevelupButton.config(state=DISABLED)

        self.combat = True
        self.playerturn = False

        self.monster_dic = monster_dic

        # Ces 3 dictionnaires pourront bouger en plein combat, et sont recréés pour les manipuler
        self.player_stats = player_dic['stats']
        self.equipped_list = player_dic['equipped_list']

        # self.game_canvas

        xl = 20
        y_label = 20

        self.player_label = Label(self.game_canvas,
                                text=f"{self.player_dic['name']}",font="Constantia 13 bold")
        self.player_label.place(x=xl,y=y_label)

        y_healthbar = y_label + 25

        hpmax = self.player_stats['HP']
        self.player_healthbar = healthbar.HealthBar(canvas=self.game_canvas,length=200,height=25,maximum=hpmax,x=xl,y=y_healthbar,color="red")
        self.player_healthbar.show()

        self.bind_player_tooltip()

        height = self.game_canvas.winfo_height()
        width = self.game_canvas.winfo_width()

        x_monster_label = width - 220
        self.monster_label = Label(self.game_canvas,
                                text=f"{self.monster_dic['name']}",font="Constantia 13 bold")
        self.monster_label.place(x=x_monster_label+200, y=y_label,anchor='ne')

        hpmax = self.monster_dic['stats']['HP']
        self.monster_healthbar = healthbar.HealthBar(canvas=self.game_canvas,length=200,height=25,maximum=hpmax,x=x_monster_label,y=y_healthbar,color="red",special="right")
        self.monster_healthbar.show()
        self.bind_monster_tooltip()

        # joueur en or, à gauche
        # monstre en rouge, à droite
        speed1=self.player_stats['Agilité']
        speed2=self.monster_dic['stats']['Agilité']
        x_speedbar = (xl + x_monster_label)/2 + 90
        self.speedbar = speedbar.SpeedBar(canvas=self.game_canvas,x=x_speedbar,y=20,length=200,max1=100,max2=100,speed1=speed1,speed2=speed2,color1="#FFFFFF",color2="red",backgroundcolor=self.backgroundcolor,bordercolor=self.foregroundcolor)
        self.speedbar.show()




        # self.game_canvas
        self.playbutton = Button(self.game_canvas,text="PLAY",command=self.play_combat_loop)
        self.playbutton.place(x=width-400,y=height-50,anchor='s')

        self.attackbutton = Button(self.game_canvas,text="ATTACK",state=DISABLED,command=self.player_attack)
        self.attackbutton.place(x=width-250,y=height-50,anchor='s')


        self.defendbutton = Button(self.game_canvas,text="Quit",state=DISABLED,command=self.player_defend)
        self.defendbutton.place(x=width-100,y=height-50,anchor='s')

        self.order = None


    def bind_player_tooltip(self):
        import stats_window as sw
        toolTip = sw.StatsWindow(widget = self.player_healthbar.widget)
        def enter(event):
            toolTip.show(stat_dic=self.player_stats,name=self.player_dic['name'],level=self.player_dic['level'],image_dir=self.player_dic['image'],category='')
        def leave(event):
            toolTip.hidetip()
        self.player_healthbar.widget.bind('<Enter>', enter)
        self.player_healthbar.widget.bind('<Leave>', leave)


    def bind_monster_tooltip(self):
        import stats_window as sw
        toolTip = sw.StatsWindow(widget = self.monster_healthbar.widget)
        def enter(event):
            toolTip.show(stat_dic=self.monster_dic['stats'],name=self.monster_dic['name'],level=self.monster_dic['level'],image_dir=self.monster_dic['image'],category=self.monster_dic['category'],x_relative=-500)
        def leave(event):
            toolTip.hidetip()
        self.monster_healthbar.widget.bind('<Enter>', enter)
        self.monster_healthbar.widget.bind('<Leave>', leave)

    def play_combat_loop(self):
        self.order = self.speedbar.order

        if self.order == "wait":
            self.main_window.after(20,self.play_combat_loop)

        elif self.order == None:

            self.order = self.speedbar.lets_go()

            self.playbutton.config(state=DISABLED)
            self.main_window.after(20,self.play_combat_loop)

        # Tour du monstre
        elif self.order == 2:
            self.order = None
            self.speedbar.order = None
            self.main_window.after(500,self.monster_attack)

            self.main_window.after(2000,self.play_combat_loop)

        # Tour du joueur
        elif self.order == 1:
            self.playerturn = True
            self.attackbutton.config(state=NORMAL)
            self.defendbutton.config(state=NORMAL)

        elif self.order == "stop":
            self.hide_combat()




    def refresh_speed_player(self):
        if not self.combat:
            return

        speed1 = self.player_stats['Agilité']

        if speed1 > self.speedbar.id_speed1:
            self.speedbar.set_speed1(speed1)
            self.outputbox.add_text(f"{self.player_dic['name']} a accéléré !")
        elif speed1 < self.speedbar.id_speed1:
            self.speedbar.set_speed1(speed1)
            self.outputbox.add_text(f"{self.player_dic['name']} a été ralenti !")


    def refresh_speed_monster(self):
        if not self.combat:
            return

        speed2 = self.monster_dic['stats']['Agilité']

        if speed2 > self.speedbar.id_speed2:
            self.speedbar.set_speed2(speed2)
            self.outputbox.add_text(f"{self.monster_dic['name']} a accéléré !")
        elif speed2 < self.speedbar.id_speed1:
            self.speedbar.set_speed2(speed2)
            self.outputbox.add_text(f"{self.monster_dic['name']} a été ralenti !")


    def player_defend(self):
        self.outputbox.add_text("Touche de défense, momentannément changée")
        self.player_wincombat()

    def player_attack(self):
        if (not self.combat) or (not self.playerturn):
            return
        import manipulate_stats as ms

        damage = ms.calculate_damage_player(player_stats = self.player_stats,monster_stats = self.monster_dic['stats'],player_itemlist=self.equipped_list)

        self.monster_healthbar.take_hit(damage)
        if damage>1:
            s='s'
        else:
            s=''
        self.outputbox.add_text(f"{self.monster_dic['name']} a subi {damage:0.1f} dommage{s}")
        self.monster_dic['stats']['HP'] -= damage

        if self.monster_dic['stats']['HP'] < 0:
            self.outputbox.add_text(f"{self.monster_dic['name']} a été vaincu !")
            self.player_wincombat()

        else:
            self.order = None
            self.playerturn = False
            self.speedbar.order = None
            self.attackbutton.config(state=DISABLED)
            self.defendbutton.config(state=DISABLED)
            self.play_combat_loop()


    def monster_attack(self):
        if not self.combat:
            return
        import manipulate_stats as ms

        damage = ms.calculate_damage_monster(monster_stats=self.monster_dic['stats'],player_stats = self.player_stats,element=self.monster_dic['element'])

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
            self.order = None
            self.speedbar.order = None
            #self.playbutton.config(state=NORMAL)

    def player_wincombat(self):
        self.speedbar.order = "stop"
        self.playerturn = False
        self.outputbox.add_text(f"Vous gagnez A IMPLEMENTER points d'expérience !")
        self.playbutton.config(text="Quitter le combat")
        self.playbutton.config(state=NORMAL)
        self.attackbutton.config(state=DISABLED)
        self.defendbutton.config(state=DISABLED)

    def player_losecombat(self):
        self.speedbar.order = "stop"
        self.playerturn = False
        self.outputbox.add_text(f"Vous êtes mort...")
        self.playbutton.config(text="Quitter le combat")
        self.playbutton.config(state=NORMAL)
        self.attackbutton.config(state=DISABLED)
        self.defendbutton.config(state=DISABLED)

    def hide_combat(self):
        self.player_healthbar.hidetip()
        self.monster_healthbar.hidetip()
        self.speedbar.hidetip()
        self.player_label.destroy()
        self.monster_label.destroy()

        self.attackbutton.destroy()
        self.defendbutton.destroy()
        self.playbutton.destroy()

        self.player_stats = None
        self.equipped_list = None
        self.combat = False
        self.playerturn = False
        self.player_stats = None
        self.monster_dic = None

        self.AttributButton.config(state=NORMAL)
        self.SpellButton.config(state=NORMAL)
        self.InventoryButton.config(state=NORMAL)
        self.LevelupButton.config(state=NORMAL)


if __name__ == "__main__":
    global w
    import manipulate_json as jm
    import manipulate_map as mm

    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')
    monster_dic = jm.load_file(fulldir="ressources/template/monster/slime_bleu.json")

    mapdir = "img/stock/_tiles/Tiled software"
    mapname = "my_first_map"
    tilename = "bloks"

    imgdir = "img/stock/_tiles/non resized"



    w = Main_Window(player_dic['name'])

    #w.show_combat(monster_dic=monster_dic)

    w.load_map(mapdir,mapname,tilename,imgdir)
    w.draw_map(0.33,0)

    player_imgdir = "img/stock/platformer graphics/Player/p1_stand.png"
    w.load_player(player_imgdir=player_imgdir)
    w.draw_player(0.33,0)


    w.main_window.focus_force()
    w.main_window.mainloop()