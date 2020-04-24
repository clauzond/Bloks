from tkinter import *
import classtooltip as ctt
import dictionnaires

class SpellWindow():

    def __init__(self,toplevel="",widget=""):
        self.toplevel = toplevel
        self.widget = widget
        self.spell_window = None

    def hidetip(self):
        tw = self.spell_window
        c = self.spell_canvas
        self.spell_canvas = None
        self.spell_window = None
        if tw:
            c.destroy()
            tw.destroy()

    def show(self,player_dic,spell_dic):
        if self.spell_window:
            return


        if type(self.widget)==str:
            if self.toplevel:
                self.spell_window = Toplevel()
                self.spell_window.wm_overrideredirect(1)
                self.spell_window.focus_force()
            else:
                self.spell_window = Tk()


            self.bold_font13 = "Constantia 13 bold"
            self.bold_font16 = "Constantia 16 bold"
            self.classic_font16 = "Constantia 16"

            self.underline_font12 = "Constantia 12 bold underline"
            self.bold_font12 = "Constantia 12 bold"
            self.classic_font12 = "Constantia 12"

        else:
            x, y, cx, cy = self.widget.bbox("insert")
            x = x + self.widget.winfo_rootx() + 12
            y = y + cy + self.widget.winfo_rooty() + 40
            self.spell_window = Toplevel(self.widget)

            self.spell_window.wm_overrideredirect(1)
            self.spell_window.wm_geometry("+%d+%d" % (x, y))

            self.bold_font13 = "Constantia 8 bold"
            self.bold_font16 = "Constantia 9 bold"
            self.classic_font16 = "Constantia 9"

            self.underline_font12 = "Constantia 8 bold underline"
            self.bold_font12 = "Constantia 6 bold"
            self.classic_font12 = "Constantia 6"


        self.spell_window.title("Spells")
        self.spell_window.resizable(False,False)
        self.spell_window.iconbitmap("img/icone.ico")

        self.spell_window.option_add('*font','Constantia 12')
        self.spell_window.option_add('*Button.activebackground','darkgray')
        self.spell_window.option_add('*Button.activeforeground','darkgray')
        self.spell_window.option_add('*Button.relief','groove')
        self.spell_window.option_add('*Button.overRelief','ridge')
        self.spell_window.option_add('*justify','left')
        self.spell_window.option_add('*bg','lightgray')
        self.spell_window.option_add('*compound','left')


        self.spell_canvas = Canvas(self.spell_window)
        self.spell_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.player_dic = player_dic
        self.spell_dic = spell_dic
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)

        self.bind_state = (-1,'off')
        self.spell_window.bind_all('<Key>',self.listen)
        self.liste_num = ['&','é','"',"'","(","-","è","_","ç","à"]

        self.next_label_bind = 0

        # Statistiques du joueurs
        k = 5 # nombre de lignes utilisées avant les spells

        playerimg = PhotoImage(file=self.player_dic['image'])
        name_label = Label(self.spell_canvas,
                        text=self.player_dic['name'],
                        fg='black',font=self.bold_font13,image=playerimg)
        name_label.grid(row=0, column=0, sticky=W,columnspan=10)

        level_label = Label(self.spell_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font=self.bold_font13,image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=0,columnspan=10)

        xp_label = Label(self.spell_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font=self.bold_font13,image=self.img_dic['xpnoir'])
        xp_label.grid(row=0,column=0,columnspan=100,sticky=E)
        Frame(self.spell_canvas,height=20).grid(row=1)

        txt_point_label = Label(self.spell_canvas,
                            text='Disponible : ',
                            fg='black',font=self.bold_font13,image=self.img_dic['star'])
        if type(self.widget)==str:
            txt_point_label.grid(row=1,column=0,columnspan=10)
        else:
            txt_point_label.grid(row=1,column=0)


        self.point_label = Label(self.spell_canvas,
                            text=str(self.player_dic['spell_point']),
                            fg='black',font=self.bold_font13)
        self.point_label.grid(row=1,column=1,columnspan=10,sticky=W)
        if type(self.widget)==str:
            self.point_label.grid(row=1,column=1,columnspan=10,sticky=W)
        else:
            self.point_label.grid(row=1,column=1)

        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        if player_dic['spell_point']>0:
            plus_state='normal'
            minus_state='disabled'
        else:
            plus_state='disabled'
            minus_state='disabled'

        self.widget_list = []

        total_number_of_spells = self.spell_dic['total_number_of_spells']
        imglist=[]
        for i in range(total_number_of_spells):
            spell_number = f'spell{i+1}'
            spell_name = str( self.spell_dic[f'spell{i+1}']['name'] )
            spell_value = int( self.spell_dic[f'spell{i+1}']['level'] )
            spell_bind = str( self.spell_dic[f'spell{i+1}']['bind'] )
            color = str( self.spell_dic[f'spell{i+1}']['color'])

            if type(self.widget)==str:
                imglist.append( PhotoImage(file=self.spell_dic[f'spell{i+1}']['image']) )
            else:
                imglist.append( self.img_dic['vide'])

            l1=Label(self.spell_canvas,name=f'0|{i}',
                    text=" "+spell_name,
                    fg=color,font=self.classic_font12,
                    image=imglist[i])
            l1.grid(row=i+k,column=0,padx=20,pady=1,sticky=W)
            l1.bind('<Button-1>',self.bind_label)

            b1=Button(self.spell_canvas,
                    text="+",name=f'1|{i}',
                    state=plus_state,font=self.bold_font16,fg='green')
            b1.grid(row=i+k,column=1,padx=2)
            b1.bind('<Button-1>',self.plus)
            b2=Button(self.spell_canvas,
                    text="-",name=f'2|{i}',
                    state=minus_state,font=self.bold_font16,fg='red')
            b2.grid(row=i+k,column=3,padx=2)
            b2.bind('<Button-1>',self.minus)
            l2=Label(self.spell_canvas,text=spell_value,fg='black',font=self.classic_font16,width=3)
            l2.grid(row=i+k,column=2)

            b3=Button(self.spell_canvas,
                    text=f'< {spell_bind} >',name=f'3|{i}',
                    font=self.bold_font12,fg='black')
            b3.grid(row=i+k,column=4,padx=10)
            b3.bind('<Button-1>',self.bind_button)

            self.widget_list.append({'spell_name':l1,'button1':b1,'button2':b2,'button3':b3,'spell_value':l2,'point_spent':0,'button1_state':plus_state,'button2_state':minus_state})

            if type(self.widget)==str:
                ctt.CreateToolTip(l1,self.spell_dic[spell_number]['description'])



        if type(self.widget)==str:
            # Séparateur suivi du bouton 'Confirmer'
            Frame(self.spell_canvas,height=10,width=400).grid(row=i+k+1)
            Button(self.spell_canvas,text="Confirmer",command=self.confirm).grid(row=i+k+2,column=0,columnspan=10)


        self.underline_activebind()

        try:
            self.spell_window.mainloop()
        except:
            pass

    # Renvoie en str la liste des spells, comme ça on peut savoir ce qui a été changé
    def __repr__(self):
        s = str(self.player_dic)
        s += "\n"
        s += str(self.spell_dic)
        return(s)

    # Ferme la fenêtre de levelup, et donne le dictionnaire des spells
    def confirm(self):
        import manipulate_json as jm

        jm.save_file(self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(self.spell_dic,filename='spell_dic',player_name=self.player_dic['name'])


        self.spell_window.destroy()

    # +1 au spell correspondant
    def plus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if self.widget_list[i]['button1_state']=='normal':
            # manipulation des dictionnaires pour changer la valeur correspondante
            thisspell_number = f'spell{i+1}'
            self.spell_dic[thisspell_number]['level'] += 1
            self.widget_list[i]['spell_value'].config(text=self.spell_dic[thisspell_number]['level'])
            self.widget_list[i]['spell_value'].update()

            # On dépense un point, et on vérifie s'il reste encore des points
            self.player_dic['spell_point'] -= 1
            self.widget_list[i]['point_spent'] += 1
            self.point_label.config(text=str(self.player_dic['spell_point']))
            self.point_label.update()

            if self.player_dic['spell_point'] == 0:
                self.disable_all_buttons('plus')

            self.widget_list[i]['button2_state'] = 'normal'
            self.widget_list[i]['button2'].config(state='normal')
            self.widget_list[i]['button2'].update()

            self.widget_list[i]['spell_value'].config(fg='green')
            self.widget_list[i]['spell_value'].update()


    # -1 au spell correspondant
    def minus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if self.widget_list[i]['button2_state'] == 'normal':
            # manipulation des dictionnaires pour changer la valeur correspondante
            thisspell_number = f'spell{i+1}'
            self.spell_dic[thisspell_number]['level'] -= 1
            self.widget_list[i]['spell_value'].config(text=self.spell_dic[thisspell_number]['level'])
            self.widget_list[i]['spell_value'].update()

            # Si tous les boutons "+" ont été précédemment disabled
            if self.player_dic['spell_point']==0:
                self.enable_all_buttons('plus')


            # On rembourse un point de spell, et on vérifie après si on peut encore être remboursé
            self.player_dic['spell_point'] += 1
            self.widget_list[i]['point_spent'] -= 1
            self.point_label.config(text=str(self.player_dic['spell_point']))
            self.point_label.update()

            if self.widget_list[i]['point_spent'] == 0:
                self.widget_list[i]['button2_state'] = 'disabled'
                self.widget_list[i]['button2'].config(state='disabled')
                self.widget_list[i]['button2'].update()

                self.widget_list[i]['spell_value'].config(fg='black')
                self.widget_list[i]['spell_value'].update()


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


    def bind_button(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j+1 pour pouvoir manipuler spellj (index commence à 1)

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if self.bind_state[1]=='off':
            self.waiting_for_bind(i)

        # listen pour un bind automatiquement via le bind_all avec la fonction 'listen'



    def listen(self,event):
        if self.bind_state[1]=='on':
            if event.char.isalnum() or ( event.char in self.liste_num ) :
                self.try_bind_to(str(event.char),self.last_bind_widget)





    def waiting_for_bind(self,i):
        self.bind_state=(i,'on')
        self.last_bind_widget = i
        self.widget_list[i]['button3'].config(text='< ... >')
        self.widget_list[i]['button3'].update()
        self.spell_window.after(3000,self.stop_waiting_for_bind,i)


    def try_bind_to(self,char,i):
        self.bind_state=(i,'off')

        self.widget_list[i]['button3'].config(text=f'< {char} >')
        self.widget_list[i]['button3'].update()

        self.spell_dic[f'spell{i+1}']['bind'] = str(char)


    def stop_waiting_for_bind(self,i):
        if self.bind_state==(i,'on'):
            spell_bind = self.spell_dic[f'spell{i+1}']['bind']
            self.widget_list[i]['button3'].config(text=f'< {spell_bind} >')
            self.widget_list[i]['button3'].update()
            self.bind_state=(-1,'off')



    def bind_label(self,event):
        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        spell_id = f'spell{i+1}'

        self.spell_dic['active'] = spell_id
        self.player_dic['active_spell'] = self.spell_dic[spell_id]
        self.underline_activebind()



    def underline_activebind(self):
        try:
            if len(self.spell_dic['active']) > 0 :
                num = int(self.spell_dic['active'].split('spell')[1]) - 1

                for i in range(len(self.widget_list)):
                    if i != num:
                        self.widget_list[i]['spell_name'].config(font=self.classic_font12)
                    else:
                        self.widget_list[i]['spell_name'].config(font=self.underline_font12)
                    self.widget_list[i]['spell_name'].update()
        except:
            pass

def Tooltip(player_dic,spell_dic,toplevel='',widget=''):
    toolTip = SpellWindow(widget=widget)
    def enter(event):
        toolTip.show(player_dic=player_dic,spell_dic=spell_dic)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

if __name__=='__main__':
    player_dic,attribut_dic,spell_dic,inventory_dic = dictionnaires.dictionnaires_vierge()

    import manipulate_json as jm
    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')


    a=0

    if a==0:

        w=SpellWindow(toplevel=True)
        w.show(player_dic=player_dic,spell_dic=spell_dic)

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

        Tooltip(player_dic,spell_dic,widget=l)

        w.mainloop()

