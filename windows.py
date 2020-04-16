from tkinter import *

class levelup():

    def __init__(self,toplevel,attribut_dic,color_dic,player_name="Empty",player_exp={'level':'0','current':0,'max':0}):

        if toplevel:
            self.level_window = Toplevel()
        else:
            self.level_window = Tk()
        self.level_window.title("Paramètres")
        self.level_window.resizable(False, False)

        self.level_window.option_add('*Font','Constantia 12')
        self.level_window.option_add('*activebackground','white')
        self.level_window.option_add('*activeforeground','blue')
        self.level_window.option_add('*overrelif','groove')
        self.level_window.option_add('*justify','left')
        self.level_window.option_add('*bg','lightgray')


        self.level_canvas = Canvas(self.level_window)
        self.level_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.attribut_dic = attribut_dic
        self.color_dic = color_dic


        # Statistiques du joueurs

        Label(self.level_canvas,text=player_name,fg='black').grid(row=0,column=0,columnspan=10,sticky=W)
        txt = 'lv'+str(player_exp['level'])+" "+str(player_exp['current']) + '/' + str(player_exp['max'])
        Label(self.level_canvas,text=txt,fg='black',font="Constantia 13").grid(row=0,column=1,columnspan=10,sticky=E)

        Frame(self.level_canvas,height=20).grid(row=1)

        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        attribut_name_list = list(self.attribut_dic.keys())
        attribut_value_list = list(self.attribut_dic.values())
        color_value_list = list(self.color_dic.values())
        self.widget_list = []
        for i in range(len(attribut_name_list)):
            l1=Label(self.level_canvas,text=attribut_name_list[i],fg=color_value_list[i])
            l1.grid(row=i+2,column=0,padx=20,pady=10,sticky=W)
            b1=Button(self.level_canvas,text="+",name=f'1|{i}')
            b1.grid(row=i+2,column=1,padx=2)
            b1.bind('<Button-1>',self.plus)
            b2=Button(self.level_canvas,text="-",name=f'2|{i}')
            b2.grid(row=i+2,column=3,padx=2)
            b2.bind('<Button-1>',self.minus)
            l2=Label(self.level_canvas,text=attribut_value_list[i],width=3)
            l2.grid(row=i+2,column=2)
            self.widget_list.append({'attribut_name':l1,'button1':b1,'button2':b2,'attribut_value':l2})



        # Séparateur suivi du bouton 'Confirmer'
        Frame(self.level_canvas,height=20).grid(row=i+3)
        Button(self.level_canvas,text="Confirmer",command=self.confirm).grid(row=i+4,column=0,columnspan=10)


        self.level_window.mainloop()


    # Ferme la fenêtre de levelup, et donne le dictionnaire des attributs
    def confirm(self):
        print(attribut_dic)
        self.level_window.destroy()

    # +1 à l'attribut correspondant
    def plus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        # manipulation des dictionnaires pour changer la valeur correspondante
        thisattribut_name = list(self.attribut_dic.keys())[i]
        self.attribut_dic[thisattribut_name] += 1
        self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name])
        self.widget_list[i]['attribut_value'].update()


    # -1 à l'attribut correspondant
    def minus(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j

        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        # manipulation des dictionnaires pour changer la valeur correspondante
        thisattribut_name = list(self.attribut_dic.keys())[i]
        self.attribut_dic[thisattribut_name] -= 1
        self.widget_list[i]['attribut_value'].config(text=self.attribut_dic[thisattribut_name])
        self.widget_list[i]['attribut_value'].update()

if __name__=='__main__':
    attribut_dic = {'HP':120,'Mana':30,'Force':10,'Agilité':69,'Intelligence':42}
    color_dic = {'HP':'red','Mana':'blue','Force':'saddle brown','Agilité':'green','Intelligence':'red3'}
    player_name = "Blue Dragon"
    player_exp = {'level':2,'current':42,'max':100}

    w=levelup(False,attribut_dic,color_dic,player_name,player_exp)