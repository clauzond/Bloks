from tkinter import *
import classtooltip as ctt
import dictionnaires


class Stats_Window():

    # anystat_dic correspond au dictionnaire stats contenu dans "player_dic" ou dans "monster_dic"
    def __init__(self,toplevel,stat_dic,name,level,image_dir,category=''):
        if toplevel:
            self.stats_window = Toplevel()
        else:
            self.stats_window = Tk()
        self.stats_window.title("Attributs")
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
                        fg='black',font="Constantia 13 bold",image=itsimage)
        name_label.grid(row=0, column=0)

        level_label = Label(self.stats_canvas,
                        text=str(level),
                        fg='black',font="Constantia 13 bold",image=self.img_dic['starnoir'])
        level_label.grid(row=0,column=1)

        if len(category)>0 :
            category_label = Label(self.stats_canvas,
                                text = str(category),
                                fg='black',font="Constantia 13 bold",image=self.img_dic[category])
            category_label.grid(row=0,column=2)

        Frame(self.stats_canvas,height=10).grid(row=1)

        # Ecriture de tous les boutons
        # On ajoute 'name' pour pouvoir les identifier en cliquant dessus
        stat_name_list = list(self.stat_dic.keys())
        stat_value_list = list(self.stat_dic.values())

        import json_manager as jm
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
                    fg=color,font="Constantia 12 bold",
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



        # Séparateur suivi du bouton 'Confirmer'
        Frame(self.stats_canvas,height=10).grid(row=i+k1+1)
        Button(self.stats_canvas,text="Confirmer",command=self.confirm).grid(row=i+k1+2,column=0,columnspan=10)


        self.stats_window.deiconify()
        self.stats_window.mainloop()


    def confirm(self):
        self.stats_window.destroy()



if __name__ == "__main__" :
    player_dic,b,c,d = dictionnaires.dictionnaires_vierge()

    stats = player_dic['stats']['total']
    name = player_dic['name']
    level = player_dic['level']
    img_dir = player_dic['image']

    w = Stats_Window(toplevel=False,stat_dic=stats,name=name,level=level,image_dir=img_dir,category='Elite')