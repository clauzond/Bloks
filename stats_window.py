from tkinter import *
import classtooltip as ctt
import dictionnaires


class StatsWindow():


    def __init__(self,toplevel="",widget=""):
        self.toplevel = toplevel
        self.widget = widget
        self.stats_window = None

    def hidetip(self):
        tw = self.stats_window
        c = self.stats_canvas
        self.stats_canvas = None
        self.stats_window = None
        if tw:
            c.destroy()
            tw.destroy()

    # anystat_dic correspond au dictionnaire stats contenu dans "player_dic" ou dans "monster_dic"
    def show(self,stat_dic,name,level,image_dir,category=''):
        if self.stats_window:
            return

        if type(self.widget)==str:
            if self.toplevel:
                self.stats_window = Toplevel()
                self.stats_window.wm_overrideredirect(1)
                self.stats_window.focus_force()
            else:
                self.stats_window = Tk()

            self.bold_font13 = "Constantia 13 bold"
            self.bold_font16 = "Constantia 16 bold"
            self.classic_font12 = "Constantia 12"
            self.classic_font16 = "Constantia 16"

            self.underline_font12 = "Constantia 12 bold underline"
            self.bold_font12 = "Constantia 12 bold"
            self.classic_font12 = "Constantia 12"

        else:
            x, y, cx, cy = self.widget.bbox("insert")
            x = x + self.widget.winfo_rootx() + 12
            y = y + cy + self.widget.winfo_rooty() + 40
            self.stats_window = Toplevel(self.widget)

            self.stats_window.wm_overrideredirect(1)
            self.stats_window.wm_geometry("+%d+%d" % (x, y))

            self.bold_font13 = "Constantia 8 bold"
            self.bold_font16 = "Constantia 9 bold"
            self.classic_font16 = "Constantia 9"
            self.classic_font12 = "Constantia 12"

            self.underline_font12 = "Constantia 8 bold underline"
            self.bold_font12 = "Constantia 6 bold"
            self.classic_font12 = "Constantia 6"



        self.stats_window.title("Stats")
        self.stats_window.resizable(False, False)
        self.stats_window.iconbitmap("img/icone.ico")

        self.stats_window.option_add('*Font','Constantia 12')
        self.stats_window.option_add('*Button.activebackground','darkgray')
        self.stats_window.option_add('*Button.activeforeground','darkgray')
        self.stats_window.option_add('*Button.relief','groove')
        self.stats_window.option_add('*Button.overRelief','ridge')
        self.stats_window.option_add('*justify','left')
        self.stats_window.option_add('*bg','lightgray')
        self.stats_window.option_add('*compound','left')


        self.stats_canvas = Canvas(self.stats_window)
        self.stats_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.stat_dic = stat_dic
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)


        itsimage = PhotoImage(file=image_dir)
        name_label = Label(self.stats_canvas,
                        text=str(name),
                        fg='black',font=self.bold_font13,image=itsimage)
        name_label.grid(row=0, column=0)

        level_label = Label(self.stats_canvas,
                        text=str(level),
                        fg='black',font=self.bold_font13,image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=1)

        if len(category)>0 :
            category_label = Label(self.stats_canvas,
                                text = str(category),
                                fg='black',font=self.bold_font13,image=self.img_dic[category])
            category_label.grid(row=0,column=2)

        Frame(self.stats_canvas,height=10).grid(row=1)

        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        stat_name_list = list(self.stat_dic.keys())
        stat_value_list = list(self.stat_dic.values())

        import manipulate_json as jm
        attribut_dic = jm.load_file(fulldir="ressources/template/attribut_dic.json")


        imglist=[]
        ligne,colonne = 1,0
        k1 = 2
        k2 = 0
        for i in range(len(stat_name_list)):

            attribut_name = str(stat_name_list[i])
            attribut_value = int(stat_value_list[i])
            color = str(attribut_dic[attribut_name]['color'])
            imglist.append( PhotoImage(file=attribut_dic[attribut_name]['image']) )

            l1=Label(self.stats_canvas,
                    text=f"{attribut_name} : {attribut_value}",
                    fg=color,font=self.bold_font12,
                    image=imglist[i])
            l1.grid(row=ligne+k1,column=colonne+k2,padx=10,sticky=W)

            ctt.CreateToolTip(l1,attribut_dic[attribut_name]['description'])

            ligne += 1

            if i==5:
                ligne = 2
                colonne = 1
            if i==10:
                ligne = 2
                colonne = 2


        if type(self.widget)==str:
            # Séparateur suivi du bouton 'Confirmer'
            Frame(self.stats_canvas,height=10).grid(row=i+k1+1)
            Button(self.stats_canvas,text="Confirmer",command=self.confirm).grid(row=i+k1+2,column=0,columnspan=10)


        self.stats_window.mainloop()


    def confirm(self):
        self.stats_window.destroy()



def Tooltip(stat_dic,name,level,image_dir,category='',toplevel='',widget=''):
    toolTip = StatsWindow(widget=widget)
    def enter(event):
        toolTip.show(stat_dic=stats,name=name,level=level,image_dir=image_dir,category=category)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

if __name__ == "__main__" :
    #player_dic,b,c,d = dictionnaires.dictionnaires_vierge()

    import manipulate_json as jm
    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')

    stats = player_dic['stats']
    name = player_dic['name']
    level = player_dic['level']
    img_dir = player_dic['image']


    a=0

    if a==0:

        w=StatsWindow(toplevel=False)
        w.show(stat_dic=stats,name=name,level=level,image_dir=img_dir,category='Elite')

    else:
        w = Tk()

        w.title("Un petit test")
        w.resizable(False,False)
        w.iconbitmap("img/icone.ico")

        w.option_add('*Font','Constantia 12')
        w.option_add('*Button.activebackground','darkgray')
        w.option_add('*Button.activeforeground','darkgray')
        w.option_add('*Button.relief','groove')
        w.option_add('*Button.overRelief','ridge')
        w.option_add('*justify','left')
        w.option_add('*bg','lightgray')
        w.option_add('*compound','left')


        wc = Canvas(w,width=100,height=100)
        wc.pack(fill=BOTH,expand=True,padx=20,pady=20)

        l = Label(w,text="Bonjour")
        l.pack()

        Tooltip(widget=l,stat_dic=stats,name=name,level=level,image_dir=img_dir,category='Elite')

        w.mainloop()