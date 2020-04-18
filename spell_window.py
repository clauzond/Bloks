from tkinter import *
import classtooltip as ctt
import dictionnaires

class SpellWindow():

    def __init__(self,toplevel,player_dic,spell_dic,spellbind_dic):

        if toplevel:
            self.level_window = Toplevel()
        else:
            self.level_window = Tk()
        self.level_window.title("Spells")
        self.level_window.resizable(False,False)
        self.level_window.iconbitmap("img/icone.ico")

        self.level_window.option_add('*Font','Constantia 12')
        self.level_window.option_add('*Button.activebackground','darkgray')
        self.level_window.option_add('*Button.activeforeground','darkgray')
        self.level_window.option_add('*Button.relief','groove')
        self.level_window.option_add('*Button.overRelief','ridge')
        self.level_window.option_add('*justify','left')
        self.level_window.option_add('*bg','lightgray')
        self.level_window.option_add('*compound','left')


        self.level_canvas = Canvas(self.level_window)
        self.level_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.player_dic = player_dic
        self.spell_dic = spell_dic
        self.color_dic = dictionnaires.dictionnaires_vierge(loadcolor=True)
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)
        self.tooltips_dic = dictionnaires.dictionnaires_vierge(loadspelltip=True)
        self.spellname_dic = dictionnaires.dictionnaires_vierge(loadspellname=True)
        self.spellbind_dic = spellbind_dic

        self.bind_state = (-1,'off')
        self.level_window.bind_all('<Key>',self.listen)
        self.liste_num = ['&','é','"',"'","(","-","è","_","ç","à"]

        self.next_label_bind = 0

        # Statistiques du joueurs
        k = 5 # nombre de lignes utilisées avant les spells

        name_label = Label(self.level_canvas,
                        text=self.player_dic['name'],
                        fg='black',font="Constantia 13 bold",image=self.img_dic['player'])
        name_label.grid(row=0, column=0, sticky=W,columnspan=10)

        level_label = Label(self.level_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font="Constantia 13 bold",image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=0,columnspan=10)

        xp_label = Label(self.level_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font='Constantia 13 bold',image=self.img_dic['xpnoir'])
        xp_label.grid(row=0,column=0,columnspan=100,sticky=E)
        Frame(self.level_canvas,height=20).grid(row=1)

        txt_point_label = Label(self.level_canvas,
                            text='Disponible : ',
                            fg='black',font='Constantia 13 bold',image=self.img_dic['star'])
        txt_point_label.grid(row=1,column=0,columnspan=10)
        self.point_label = Label(self.level_canvas,
                            text=str(self.player_dic['spell_point']),
                            fg='black',font='Constantia 13 bold')
        self.point_label.grid(row=1,column=1,columnspan=10,sticky=W)


        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        if player_dic['spell_point']>0:
            plus_state='normal'
            minus_state='disabled'
        else:
            plus_state='disabled'
            minus_state='disabled'

        spell_bind_list = list(self.spellbind_dic.values())
        spell_name_list = list(self.spellname_dic.values())
        spell_number_list = list(self.spellname_dic.keys())
        spell_value_list = list(self.spell_dic.values())
        color_value_list = list(self.color_dic.values())
        self.widget_list = []
        for i in range(len(spell_name_list)):
            spell_number = spell_number_list[i]
            spell_name = spell_name_list[i]
            spell_value = spell_value_list[i]
            spell_bind = spell_bind_list[i]

            l1=Label(self.level_canvas,name=f'0|{i}',
                    text=" "+spell_name,
                    fg=self.color_dic[spell_number],font="Constantia 12",
                    image=self.img_dic[spell_number])
            l1.grid(row=i+k,column=0,padx=20,pady=1,sticky=W)
            l1.bind('<Button-1>',self.bind_label)

            b1=Button(self.level_canvas,
                    text="+",name=f'1|{i}',
                    state=plus_state,font='Constantia 16 bold',fg='green')
            b1.grid(row=i+k,column=1,padx=2)
            b1.bind('<Button-1>',self.plus)
            b2=Button(self.level_canvas,
                    text="-",name=f'2|{i}',
                    state=minus_state,font='Constantia 16 bold',fg='red')
            b2.grid(row=i+k,column=3,padx=2)
            b2.bind('<Button-1>',self.minus)
            l2=Label(self.level_canvas,text=spell_value,fg='black',font='Constantia 16',width=3)
            l2.grid(row=i+k,column=2)

            b3=Button(self.level_canvas,
                    text=f'< {spell_bind} >',name=f'3|{i}',
                    font='Constantia 12 bold',fg='black')
            b3.grid(row=i+k,column=4,padx=10)
            b3.bind('<Button-1>',self.bind_button)

            self.widget_list.append({'spell_name':l1,'button1':b1,'button2':b2,'button3':b3,'spell_value':l2,'point_spent':0,'button1_state':plus_state,'button2_state':minus_state})

            ctt.CreateToolTip(l1,self.tooltips_dic[spell_number])



        # Séparateur suivi du bouton 'Confirmer'
        Frame(self.level_canvas,height=10,width=400).grid(row=i+k+1)
        Button(self.level_canvas,text="Confirmer",command=self.confirm).grid(row=i+k+2,column=0,columnspan=10)


        self.underline_activebind()

        self.level_window.deiconify()
        self.level_window.mainloop()

    # Renvoie en str la liste des spells, comme ça on peut savoir ce qui a été changé
    def __repr__(self):
        s = str(self.player_dic)
        s += "\n"
        s += str(self.spell_dic)
        s += '\n'
        s += str(self.spellbind_dic)
        return(s)

    # Ferme la fenêtre de levelup, et donne le dictionnaire des spells
    def confirm(self):
        print(self.player_dic)
        print(self.spell_dic)
        print(self.spellbind_dic)
        self.level_window.destroy()

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
            thisspell_number = list(self.spell_dic.keys())[i]
            self.spell_dic[thisspell_number] += 1
            self.widget_list[i]['spell_value'].config(text=self.spell_dic[thisspell_number])
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
            thisspell_number = list(self.spell_dic.keys())[i]
            self.spell_dic[thisspell_number] -= 1
            self.widget_list[i]['spell_value'].config(text=self.spell_dic[thisspell_number])
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
        self.level_window.after(3000,self.stop_waiting_for_bind,i)


    def try_bind_to(self,char,i):
        self.bind_state=(i,'off')

        self.widget_list[i]['button3'].config(text=f'< {char} >')
        self.widget_list[i]['button3'].update()

        self.spellbind_dic[f'spell{i+1}'] = str(char)


    def stop_waiting_for_bind(self,i):
        if self.bind_state==(i,'on'):
            spell_bind_list = list(self.spellbind_dic.values())
            spell_bind = spell_bind_list[i]
            self.widget_list[i]['button3'].config(text=f'< {spell_bind} >')
            self.widget_list[i]['button3'].update()
            self.bind_state=(-1,'off')



    def bind_label(self,event):
        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        spell_id = f'spell{i+1}'

        if spell_id not in self.spellbind_dic['active']:
            if self.next_label_bind==0:
                self.spellbind_dic['active'][0] = spell_id
                self.next_label_bind += 1
            elif self.next_label_bind==1:
                self.spellbind_dic['active'][1] = spell_id
                self.next_label_bind += 1
            elif self.next_label_bind==2:
                self.spellbind_dic['active'][2] = spell_id
                self.next_label_bind = 0


            self.underline_activebind()



    def underline_activebind(self):
        num0 = int(self.spellbind_dic['active'][0].split('spell')[1]) - 1
        num1 = int(self.spellbind_dic['active'][1].split('spell')[1]) - 1
        num2 = int(self.spellbind_dic['active'][2].split('spell')[1]) - 1

        for i in range(len(self.widget_list)):
            if i not in [num0,num1,num2]:
                self.widget_list[i]['spell_name'].config(font='Constantia 12')
            else:
                self.widget_list[i]['spell_name'].config(font='Constantia 12 bold underline')
            self.widget_list[i]['spell_name'].update()



if __name__=='__main__':
    player_dic,attribut_dic,spell_dic,spellbind_dic = dictionnaires.dictionnaires_vierge()

    player_dic['spell_point']=20
    spell_dic['spell1']=2
    spell_dic['spell5']=13


    w=SpellWindow(toplevel=False,player_dic=player_dic,spell_dic=spell_dic,spellbind_dic=spellbind_dic)