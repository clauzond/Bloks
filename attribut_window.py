from tkinter import *
import classtooltip as ctt
import dictionnaires

class AttributWindow():

    def __init__(self,toplevel,player_dic,attribut_dic):

        if toplevel:
            self.level_window = Toplevel()
        else:
            self.level_window = Tk()
        self.level_window.title("Attributs")
        self.level_window.resizable(False, False)
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
        self.attribut_dic = attribut_dic
        self.color_dic = dictionnaires.dictionnaires_vierge(loadcolor=True)
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)
        self.tooltips_dic = dictionnaires.dictionnaires_vierge(loadattributtip=True)
        # Statistiques du joueurs
        k = 5 # nombre de lignes utilisées avant les attributs

        name_label = Label(self.level_canvas,
                        text=self.player_dic['name'],
                        fg='black',font="Constantia 13 bold",image=self.img_dic['player'])
        name_label.grid(row=0, column=0, sticky=W,columnspan=1)

        level_label = Label(self.level_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font="Constantia 13 bold",image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=0,columnspan=10)

        xp_label = Label(self.level_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font='Constantia 13 bold',image=self.img_dic['xpnoir'])
        xp_label.grid(row=0,column=2,columnspan=1,sticky=E)
        Frame(self.level_canvas,height=20).grid(row=1)

        txt_point_label = Label(self.level_canvas,
                            text='Disponible : ',
                            fg='black',font='Constantia 13 bold',image=self.img_dic['star'])
        txt_point_label.grid(row=1,column=0,columnspan=10)
        self.point_label = Label(self.level_canvas,
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

        attribut_name_list = list(self.attribut_dic.keys())
        attribut_value_list = list(self.attribut_dic.values())
        color_value_list = list(self.color_dic.values())
        self.widget_list = []
        for i in range(len(attribut_name_list)):
            attribut_name = attribut_name_list[i]
            attribut_value = attribut_value_list[i]

            l1=Label(self.level_canvas,
                    text=" "+attribut_name,
                    fg=self.color_dic[attribut_name],font="Constantia 16 bold",
                    image=self.img_dic[attribut_name])
            l1.grid(row=i+k,column=0,padx=20,pady=5,sticky=W)
            b1=Button(self.level_canvas,
                    text="+",name=f'1|{i}',
                    state=plus_state,font='Constantia 15 bold',fg='green')
            b1.grid(row=i+k,column=1,padx=2)
            b1.bind('<Button-1>',self.plus)
            b2=Button(self.level_canvas,
                    text="-",name=f'2|{i}',
                    state=minus_state,font='Constantia 15 bold',fg='red')
            b2.grid(row=i+k,column=3,padx=2)
            b2.bind('<Button-1>',self.minus)
            l2=Label(self.level_canvas,text=attribut_value,fg='black',font='Constantia 16',width=3)
            l2.grid(row=i+k,column=2)
            self.widget_list.append({'attribut_name':l1,'button1':b1,'button2':b2,'attribut_value':l2,'point_spent':0,'button1_state':plus_state,'button2_state':minus_state})

            ctt.CreateToolTip(l1,self.tooltips_dic[attribut_name])



        # Séparateur suivi du bouton 'Confirmer'
        Frame(self.level_canvas,height=20).grid(row=i+k+1)
        Button(self.level_canvas,text="Confirmer",command=self.confirm).grid(row=i+k+2,column=0,columnspan=10)

        self.level_window.deiconify()
        self.level_window.mainloop()

    # Renvoie en str la liste des attributs, comme ça on peut savoir ce qui a été changé
    def __repr__(self):
        s = str(self.attribut_dic)
        s += "\n"
        s += str(self.player_dic)
        return(s)

    # Ferme la fenêtre de levelup, et donne le dictionnaire des attributs
    def confirm(self):
        print(self.player_dic)
        print(self.attribut_dic)
        self.level_window.destroy()

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
            self.attribut_dic[thisattribut_name] += 1
            self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name])
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
            self.attribut_dic[thisattribut_name] -= 1
            self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name])
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


if __name__=='__main__':
    player_dic,attribut_dic,spelldic,spellbind_dic = dictionnaires.dictionnaires_vierge()

    attribut_dic['HP'] = 15
    attribut_dic['Agilité'] = 2
    player_dic['attribut_point'] = 20


    w=AttributWindow(toplevel=False,player_dic=player_dic,attribut_dic=attribut_dic)