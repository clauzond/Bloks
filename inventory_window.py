from tkinter import *
import classtooltip as ctt
import dictionnaires

class Inventory_Window():


    def __init__(self,toplevel,player_dic,inventory_dic):
        if toplevel:
            self.level_window = Toplevel()
        else:
            self.level_window = Tk()
        self.level_window.title("Inventory")
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


        self.inventory_canvas = Canvas(self.level_window)
        self.inventory_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.player_dic = player_dic
        self.inventory_dic = inventory_dic
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)

        itemlist = self.inventory_dic['itemlist']

        owned_itemlist = []
        for i in range(len(itemlist)):
            if itemlist[i]['owned'] > 0:
                owned_itemlist.append(itemlist[i])

        self.owned_itemlist = owned_itemlist
        self.selected_label = 'None'
        self.selected_item = 'None'
        self.current_page = 1
        self.number_of_page = self.number_of_page()



        self.generate_page(self.current_page)


        self.level_window.deiconify()
        self.level_window.mainloop()


    def confirm(self):
        print(self.player_dic)
        print(self.inventory_dic)
        self.level_window.destroy()


    def number_of_page(self):
        # On veut avoir 3 lignes de 10 items, et on affichera seulement les items possédés
        # Il y a donc 1 page par tranche de 30 items

        n = len(self.owned_itemlist)
        if n%30 == 0:
            number_of_page = n//30
        else:
            number_of_page = n//30 + 1
        return(number_of_page)

    def clear_everything(self):
        self.inventory_canvas.destroy()

        self.inventory_canvas = Canvas(self.level_window)
        self.inventory_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)


        # Statistiques de base du joueur
        name_label = Label(self.inventory_canvas,
                        text=self.player_dic['name'],
                        fg='black',font="Constantia 13 bold",image=self.img_dic['player'])
        name_label.grid(row=0, column=0, columnspan=1)

        money_label = Label(self.inventory_canvas,
                        text=self.player_dic['money'],
                        fg='black',font="Constantia 13 bold",image=self.img_dic['money'])
        money_label.grid(row=0,column=1,columnspan=1)

        self.level_label = Label(self.inventory_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font="Constantia 13 bold",image=self.img_dic['starnoir'])
        self.level_label.grid(row=0,column=20,columnspan=1)

        self.xp_label = Label(self.inventory_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font='Constantia 13 bold',image=self.img_dic['xpnoir'])
        self.xp_label.grid(row=0,column=21,columnspan=1)

        # Séparateur suivi du bouton 'Confirmer'
        k = 10 # tout en bas
        Frame(self.inventory_canvas,height=10,width=400).grid(row=k,columnspan=100)
        Button(self.inventory_canvas,text="Confirmer",command=self.confirm).grid(row=k+1,column=0,columnspan=1)
        Button(self.inventory_canvas,text="Previous",command=self.previous_page).grid(row=k+1,column=19,padx=10)
        self.pagelabel = Label(self.inventory_canvas,text=f'{self.current_page}/{self.number_of_page}')
        self.pagelabel.grid(row=k+1,column=20,columnspan=1)
        Button(self.inventory_canvas,text="Next",command=self.next_page).grid(row=k+1,column=21,padx=10)


    def generate_page(self,number):
        number -= 1 # pour indexer correctement
        a = 1 # pour indiquer la ligne de départ
        b = 2 # pour indiquer la colonne de départ

        self.clear_everything()
        self.pagelabel.config(text=f'{self.current_page}/{self.number_of_page}')

        self.current_itemlist = self.owned_itemlist[(number*30):(number*30 +30)]




        self.current_widgetlist = []
        for i in range(len(self.current_itemlist)):
            item = self.current_itemlist[i]
            number_owned = item['owned']
            img = self.img_dic[item['image']]
            name = item['name']
            description = item['description']
            sellprice = item['sellprice']
            itemlevel = item['itemlevel']

            tooltip = f"{description}\nOwned : {number_owned}\nSell price : {sellprice}\nItem level : {itemlevel}"

            ligne,colonne = self.n_to_coord(i)

            itemlabel=Label(self.inventory_canvas,name=f'0|{i}',
                    image=img,relief=GROOVE,text=f"{number_owned}",compound="top")
            itemlabel.grid(row=a+ligne,column=b+colonne,padx=0,pady=2)
            itemlabel.bind('<Button-1>',self.bind_label)

            self.current_widgetlist.append(itemlabel)

            ctt.CreateToolTip(itemlabel,tooltip)

    def bind_label(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j
        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        self.groove_all_label()
        self.current_widgetlist[i].config(relief=SUNKEN)
        self.selected_label = self.current_widgetlist[i]
        self.selected_item = self.current_itemlist[i]

    def groove_all_label(self):
        for label in self.current_widgetlist:
            label.config(relief=GROOVE)
            label.update()

    def n_to_coord(self,n):
        # transforme un nombre 11 (commence à 0) en coordonnées, on a donc 11 -> (ligne 2,colonne 3)
        ligne = n//10 + 1
        colonne = n - (n//10)*10 + 1
        return(ligne,colonne)

    def previous_page(self):
        if self.current_page == 1:
            pass
        else:
            self.current_page -= 1
            self.generate_page(self.current_page)
            self.selected_label = 'None'
            self.selected_item = 'None'
        pass



    def next_page(self):
        if self.current_page == self.number_of_page:
            pass
        else:
            self.current_page += 1
            self.generate_page(self.current_page)
            self.selected_label = 'None'
            self.selected_item = 'None'
        pass


if __name__ == "__main__":
    player_dic,attribut_dic,spell_dic,inventory_dic = dictionnaires.dictionnaires_vierge()

    w = Inventory_Window(toplevel=False,player_dic=player_dic,inventory_dic=inventory_dic)