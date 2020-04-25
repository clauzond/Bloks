from tkinter import *
import classtooltip as ctt
import dictionnaires

class AttributWindow():

    def __init__(self,toplevel="",widget=""):

        self.toplevel = toplevel
        self.widget = widget
        self.attribut_window = None


    def hidetip(self):
        tw = self.attribut_window
        c = self.attribut_canvas
        self.attribut_canvas = None
        self.attribut_window = None
        if tw:
            c.destroy()
            tw.destroy()



    def show(self,player_dic,attribut_dic,function=None):
        if self.attribut_window:
            return

        self.function = function

        if type(self.widget)==str:
            if self.toplevel:
                self.attribut_window = Toplevel()
                self.attribut_window.wm_overrideredirect(1)
                self.attribut_window.focus_force()
            else:
                self.attribut_window = Tk()

        else:
            x, y, cx, cy = self.widget.bbox("insert")
            x = x + self.widget.winfo_rootx() + 12
            y = y + cy + self.widget.winfo_rooty() + 40
            self.attribut_window = Toplevel(self.widget)

            self.attribut_window.wm_overrideredirect(True)
            self.attribut_window.wm_geometry("+%d+%d" % (x, y))




        self.attribut_window.title("Attributs")
        self.attribut_window.resizable(False, False)
        self.attribut_window.iconbitmap("img/icone.ico")

        self.attribut_window.option_add('*Font','Constantia 12')
        self.attribut_window.option_add('*Button.activebackground','darkgray')
        self.attribut_window.option_add('*Button.activeforeground','darkgray')
        self.attribut_window.option_add('*Button.relief','groove')
        self.attribut_window.option_add('*Button.overRelief','ridge')
        self.attribut_window.option_add('*justify','left')
        self.attribut_window.option_add('*bg','lightgray')
        self.attribut_window.option_add('*compound','left')


        self.attribut_canvas = Canvas(self.attribut_window)
        self.attribut_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.player_dic = player_dic
        self.attribut_dic = attribut_dic
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)
        # Statistiques du joueurs
        k = 5 # nombre de lignes utilisées avant les attributs


        playerimage = PhotoImage(file=self.player_dic['image'])
        name_label = Label(self.attribut_canvas,
                        text=self.player_dic['name'],
                        fg='black',font="Constantia 13 bold",image=playerimage)
        name_label.grid(row=0, column=0, sticky=W,columnspan=1)

        level_label = Label(self.attribut_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font="Constantia 13 bold",image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=0,columnspan=10)

        xp_label = Label(self.attribut_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font='Constantia 13 bold',image=self.img_dic['xpnoir'])
        xp_label.grid(row=0,column=2,columnspan=1,sticky=E)
        Frame(self.attribut_canvas,height=20).grid(row=1)

        txt_point_label = Label(self.attribut_canvas,
                            text='Disponible : ',
                            fg='black',font='Constantia 13 bold',image=self.img_dic['star'])
        txt_point_label.grid(row=1,column=0,columnspan=10)
        self.point_label = Label(self.attribut_canvas,
                            text=str(self.player_dic['attribut_point']),
                            fg='black',font='Constantia 13 bold')
        self.point_label.grid(row=1,column=1,columnspan=2)


        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        if player_dic['attribut_point']>0:
            plus_state='normal'
            minus_state='disabled'
        else:
            plus_state='disabled'
            minus_state='disabled'

        attribut_name_list = list(self.attribut_dic.keys())[:6]
        self.widget_list = []
        imglist=[]
        for i in range(len(attribut_name_list)):

            attribut_name = str(attribut_name_list[i])
            attribut_value = int(self.attribut_dic[attribut_name]['level'])
            color = str(self.attribut_dic[attribut_name]['color'])
            imglist.append( PhotoImage(file=self.attribut_dic[attribut_name]['image']) )

            l1=Label(self.attribut_canvas,
                    text=" "+attribut_name,
                    fg=color,font="Constantia 16 bold",
                    image=imglist[i])
            l1.grid(row=i+k,column=0,padx=20,pady=5,sticky=W)
            b1=Button(self.attribut_canvas,
                    text="+",name=f'1|{i}',
                    state=plus_state,font='Constantia 15 bold',fg='green')
            b1.grid(row=i+k,column=1,padx=2)
            b1.bind('<Button-1>',self.plus)
            b2=Button(self.attribut_canvas,
                    text="-",name=f'2|{i}',
                    state=minus_state,font='Constantia 15 bold',fg='red')
            b2.grid(row=i+k,column=3,padx=2)
            b2.bind('<Button-1>',self.minus)
            l2=Label(self.attribut_canvas,text=attribut_value,fg='black',font='Constantia 16',width=3)
            l2.grid(row=i+k,column=2)
            self.widget_list.append({'attribut_name':l1,'button1':b1,'button2':b2,'attribut_value':l2,'point_spent':0,'button1_state':plus_state,'button2_state':minus_state})


            if type(self.widget)==str:
                ctt.CreateToolTip(l1,self.attribut_dic[attribut_name]['description'])


        if type(self.widget)== str:
            # Séparateur suivi du bouton 'Confirmer'
            Frame(self.attribut_canvas,height=20,width=400).grid(row=i+k+1)
            self.confirmbutton = Button(self.attribut_canvas,text="Confirmer",command=self.confirm)
            self.confirmbutton.grid(row=i+k+2,column=0,columnspan=10)


        self.attribut_window.mainloop()


    # Renvoie en str la liste des attributs, comme ça on peut savoir ce qui a été changé
    def __repr__(self):
        s = str(self.attribut_dic)
        s += "\n"
        s += str(self.player_dic)
        return(s)

    # Ferme la fenêtre de levelup, et donne le dictionnaire des attributs
    def confirm(self):
        import manipulate_stats
        self.player_dic = manipulate_stats.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)


        import manipulate_json as jm

        jm.save_file(self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])

        if self.function is not None:
            self.function()

        self.attribut_window.destroy()

    # +1 à l'attribut correspondant
    def plus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if self.widget_list[i]['button1_state']=='normal':
            # manipulation des dictionnaires pour changer la valeur correspondante
            thisattribut_name = list(self.attribut_dic.keys())[i]
            self.attribut_dic[thisattribut_name]['level'] += 1
            self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name]['level'])
            self.widget_list[i]['attribut_value'].update()

            # On dépense un point, et on vérifie s'il reste encore des points
            self.player_dic['attribut_point'] -= 1
            self.widget_list[i]['point_spent'] += 1
            self.point_label.config(text=str(self.player_dic['attribut_point']))
            self.point_label.update()

            if self.player_dic['attribut_point'] == 0:
                self.disable_all_buttons('plus')

            self.widget_list[i]['button2_state'] = 'normal'
            self.widget_list[i]['button2'].config(state='normal')
            self.widget_list[i]['button2'].update()

            self.widget_list[i]['attribut_value'].config(fg='green')
            self.widget_list[i]['attribut_value'].update()


    # -1 à l'attribut correspondant
    def minus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if self.widget_list[i]['button2_state'] == 'normal':
            # manipulation des dictionnaires pour changer la valeur correspondante
            thisattribut_name = list(self.attribut_dic.keys())[i]
            self.attribut_dic[thisattribut_name]['level'] -= 1
            self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name]['level'])
            self.widget_list[i]['attribut_value'].update()

            # Si tous les boutons "+" ont été précédemment disabled
            if self.player_dic['attribut_point']==0:
                self.enable_all_buttons('plus')


            # On rembourse un point d'attribut, et on vérifie après si on peut encore être remboursé
            self.player_dic['attribut_point'] += 1
            self.widget_list[i]['point_spent'] -= 1
            self.point_label.config(text=str(self.player_dic['attribut_point']))
            self.point_label.update()

            if self.widget_list[i]['point_spent'] == 0:
                self.widget_list[i]['button2_state'] = 'disabled'
                self.widget_list[i]['button2'].config(state='disabled')
                self.widget_list[i]['button2'].update()

                self.widget_list[i]['attribut_value'].config(fg='black')
                self.widget_list[i]['attribut_value'].update()


    def enable_all_buttons(self,type):
        if type=='plus':
            for i in range(len(self.widget_list)):
                self.widget_list[i]['button1_state'] = 'normal'
                self.widget_list[i]['button1'].config(state='normal')
                self.widget_list[i]['button1'].update()


    def disable_all_buttons(self,type):
        if type=='plus':
            for i in range(len(self.widget_list)):
                self.widget_list[i]['button1_state'] = 'disabled'
                self.widget_list[i]['button1'].config(state='disabled')
                self.widget_list[i]['button1'].update()


def Tooltip(player_dic,attribut_dic,toplevel='',widget=''):
    toolTip = AttributWindow(widget=widget)
    def enter(event):
        toolTip.show(player_dic=player_dic,attribut_dic=attribut_dic)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

if __name__=='__main__':
    #player_dic,attribut_dic,spelldic,inventory_dic = dictionnaires.dictionnaires_vierge()
    global w

    import manipulate_json as jm
    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')

    a=0

    if a==0:

        w=AttributWindow(toplevel=False)
        w.show(player_dic,attribut_dic)

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

        Tooltip(player_dic,attribut_dic,widget=l)

        w.mainloop()