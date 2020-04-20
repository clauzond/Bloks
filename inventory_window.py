from tkinter import *
import classtooltip as ctt
import dictionnaires

class Inventory_Window():


    def __init__(self,toplevel,player_dic,inventory_dic):
        if toplevel:
            self.inventory_window = Toplevel()
        else:
            self.inventory_window = Tk()
        self.inventory_window.title("Inventory")
        self.inventory_window.resizable(False,False)
        self.inventory_window.iconbitmap("img/icone.ico")

        self.inventory_window.option_add('*Font','Constantia 12')
        self.inventory_window.option_add('*Button.activebackground','darkgray')
        self.inventory_window.option_add('*Button.activeforeground','darkgray')
        self.inventory_window.option_add('*Button.relief','groove')
        self.inventory_window.option_add('*Button.overRelief','ridge')
        self.inventory_window.option_add('*justify','left')
        self.inventory_window.option_add('*bg','lightgray')
        self.inventory_window.option_add('*compound','left')


        self.inventory_canvas = Canvas(self.inventory_window)
        self.inventory_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)

        self.player_dic = player_dic
        self.inventory_dic = inventory_dic
        self.baseimg_dic = dictionnaires.dictionnaires_vierge(loadimg=True)


        self.create_owned_itemlist()
        self.current_page = 1
        self.number_of_page = self.func_number_of_page()
        self.playerimg = PhotoImage(file=self.player_dic['image'])

        self.create_imgdic()



        self.generate_page(self.current_page)


        self.inventory_window.deiconify()
        self.inventory_window.mainloop()


    def create_owned_itemlist(self):
        itemlist = self.inventory_dic['itemlist']
        owned_itemlist = []
        for i in range(len(itemlist)):
            if itemlist[i]['owned'] > 0:
                owned_itemlist.append(itemlist[i])

        self.owned_itemlist = owned_itemlist
        self.selected_nbr = 'None'
        self.selected_item = 'None'

    def create_imgdic(self):
        self.imgdic = {}

        for i in range(len(self.owned_itemlist)):
            self.imgdic[self.owned_itemlist[i]['id']] = PhotoImage(file = self.owned_itemlist[i]['image'])


    def confirm(self):
        print(self.player_dic)
        print(self.inventory_dic)
        self.inventory_window.destroy()


    def func_number_of_page(self):
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

        self.inventory_canvas = Canvas(self.inventory_window)
        self.inventory_canvas.pack(fill=BOTH,expand=True,padx=20,pady=20)


        # Statistiques de base du joueur
        name_label = Label(self.inventory_canvas,
                        text=self.player_dic['name'],
                        fg='black',font="Constantia 13 bold",image=self.playerimg)
        name_label.grid(row=0, column=0, columnspan=1)

        money_label = Label(self.inventory_canvas,
                        text=self.player_dic['money'],
                        fg='black',font="Constantia 13 bold",image=self.baseimg_dic['money'])
        money_label.grid(row=0,column=1,columnspan=1)

        self.level_label = Label(self.inventory_canvas,
                        text=str(self.player_dic['level']),
                        fg='black',font="Constantia 13 bold",image=self.baseimg_dic['starnoir'])
        self.level_label.grid(row=0,column=20,columnspan=1)

        self.xp_label = Label(self.inventory_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        fg='black',font='Constantia 13 bold',image=self.baseimg_dic['xpnoir'])
        self.xp_label.grid(row=0,column=21,columnspan=1)


        self.sell_button = Button(self.inventory_canvas,
                            text='Sell',command=self.sell_current_item)
        self.sell_button.grid(row=4,column=20)

        self.equip_button = Button(self.inventory_canvas,
                            text='Equip',command=self.equip_current_item)
        self.equip_button.grid(row=2,column=20)

        self.unequip_button = Button(self.inventory_canvas,
                            text='Unequip',command=self.unequip_current_item)
        self.unequip_button.grid(row=3,column=20)


        self.selected_equipped_item = 'None'
        self.selected_equipped_nbr = 'None'
        k=2
        self.equipped_widget_list = []
        for i in range(len(self.player_dic['equipped_list'])):
            item = self.player_dic['equipped_list'][i]

            # Item non vide
            if len(item)>0:
                number_owned = item['owned']
                img = self.imgdic[item['id']]
                name = item['name']
                description = item['description']
                sellprice = item['sellprice']
                itemlevel = item['itemlevel']
                stats = item['stats']
                if len(stats)==0:
                    x = ""
                else:
                    x = str(stats)+'\n'
                tooltip = f"{x}{description}\nSell price : {sellprice}\nItem level : {itemlevel}"
                itemlabel=Label(self.inventory_canvas,name=f'a|{i}',
                        image=img,relief=GROOVE)
                itemlabel.grid(row=k+i,column=0)
                itemlabel.bind('<Button-1>',self.bind_equipped_label)

                self.equipped_widget_list.append(itemlabel)

                ctt.CreateToolTip(itemlabel,tooltip)

            # Item vide
            else:
                itemlabel=Label(self.inventory_canvas,name=f'a|{i}',
                        image=self.baseimg_dic['nothing'],relief=GROOVE)
                itemlabel.grid(row=k+i,column=0)
                itemlabel.bind('<Button-1>',self.bind_equipped_label)

                self.equipped_widget_list.append(itemlabel)
                ctt.CreateToolTip(itemlabel,'Vide')


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

        self.number_of_page = self.func_number_of_page()
        self.clear_everything()
        self.pagelabel.config(text=f'{self.current_page}/{self.number_of_page}')

        self.current_itemlist = self.owned_itemlist[(number*30):(number*30 +30)]




        self.current_widgetlist = []
        for i in range(len(self.current_itemlist)):
            item = self.current_itemlist[i]
            number_owned = item['owned']
            img = self.imgdic[item['id']]
            name = item['name']
            description = item['description']
            sellprice = item['sellprice']
            itemlevel = item['itemlevel']
            stats = item['stats']
            if len(stats)==0:
                x = ""
            else:
                x = str(stats)+'\n'

            tooltip = f"{x}{description}\nOwned : {number_owned}\nSell price : {sellprice}\nItem level : {itemlevel}"

            ligne,colonne = self.n_to_coord(i)

            itemlabel=Label(self.inventory_canvas,name=f'0|{i}',
                    image=img,relief=GROOVE,text=f"{number_owned}",compound="top")
            itemlabel.grid(row=a+ligne,column=b+colonne)
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

        if i != self.selected_nbr:
            self.current_widgetlist[i].config(relief=SUNKEN)
            self.selected_item = self.current_itemlist[i]
            self.selected_nbr = i
        else:
            self.selected_item = 'None'
            self.selected_nbr = 'None'

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
            self.selected_nbr = 'None'
            self.selected_item = 'None'
        pass



    def next_page(self):
        if self.current_page == self.number_of_page:
            pass
        else:
            self.current_page += 1
            self.generate_page(self.current_page)
            self.selected_item = 'None'
            self.selected_nbr = 'None'
        pass


    def sell_current_item(self):

        if self.selected_nbr=='None' or self.selected_item=='None':
            pass

        else:
            itsnbr = self.selected_nbr
            myprice = self.selected_item['sellprice']
            myid = self.selected_item['id']
            self.player_dic['money'] += myprice

            self.inventory_dic['itemlist'][myid]['owned'] -= 1


            self.create_owned_itemlist()

            self.generate_page(self.current_page)

            # Le bouton n'a pas bougé
            if self.inventory_dic['itemlist'][myid]['owned'] > 0:
                self.groove_all_label()
                self.current_widgetlist[itsnbr].config(relief=SUNKEN)
                self.selected_item = self.current_itemlist[itsnbr]
                self.selected_nbr = itsnbr



    def bind_equipped_label(self,event):
        # event.widget = .!canvas.i|j
        # on veut récupérer j
        i = str(event.widget)
        i = i.split('.')[-1]
        i = i.split('|')[-1]
        i = int(i)

        if i == self.selected_equipped_nbr:
            self.selected_equipped_nbr = 'None'
            self.selected_equipped_item = 'None'
            self.equipped_widget_list[i].config(relief=GROOVE)

        else:
            self.selected_equipped_item = self.player_dic['equipped_list'][i]
            self.selected_equipped_nbr = i

            for j in range(len(self.equipped_widget_list)):
                self.equipped_widget_list[j].config(relief=GROOVE)
            self.equipped_widget_list[i].config(relief=SUNKEN)


    def equip_current_item(self):

        if self.selected_equipped_item == 'None' or self.selected_equipped_nbr =='None' or self.selected_item == 'None' or self.selected_nbr == 'None':
            pass
        elif len(self.selected_equipped_item) == 0:
            oldnbr = self.selected_equipped_nbr
            newid = self.selected_item['id']

            self.player_dic['equipped_list'][oldnbr] = self.inventory_dic['itemlist'][newid]
            self.inventory_dic['itemlist'][newid]['owned'] -= 1
            self.create_owned_itemlist()

            self.generate_page(self.current_page)

            # On applatit tous les boutons, inventaire ou équipement
            self.groove_all_label()
            for j in range(len(self.equipped_widget_list)):
                self.equipped_widget_list[j].config(relief=GROOVE)
            self.equipped_widget_list[oldnbr].config(relief=GROOVE)
            self.selected_equipped_item,self.selected_equipped_nbr = 'None','None'
            self.selected_item,self.selected_nbr = 'None','None'



        else:
            oldnbr = self.selected_equipped_nbr
            oldid = self.selected_equipped_item['id']

            newid = self.selected_item['id']




            self.player_dic['equipped_list'][oldnbr] = self.inventory_dic['itemlist'][newid]

            self.inventory_dic['itemlist'][oldid]['owned'] += 1
            self.inventory_dic['itemlist'][newid]['owned'] -= 1
            self.create_owned_itemlist()

            self.generate_page(self.current_page)

            # On applatit tous les boutons, inventaire ou équipement
            self.groove_all_label()
            for j in range(len(self.equipped_widget_list)):
                self.equipped_widget_list[j].config(relief=GROOVE)
            self.equipped_widget_list[oldnbr].config(relief=GROOVE)
            self.selected_equipped_item,self.selected_equipped_nbr = 'None','None'
            self.selected_item,self.selected_nbr = 'None','None'

    def unequip_current_item(self):

        if self.selected_equipped_item == 'None' or self.selected_equipped_nbr =='None':
            pass
        elif len(self.selected_equipped_item) == 0:
            pass
        else:
            oldnbr = self.selected_equipped_nbr
            oldid = self.selected_equipped_item['id']

            self.player_dic['equipped_list'][oldnbr] = {}
            self.inventory_dic['itemlist'][oldid]['owned'] += 1
            self.create_owned_itemlist()

            self.generate_page(self.current_page)

            # On applatit tous les boutons, inventaire ou équipement
            self.groove_all_label()
            for j in range(len(self.equipped_widget_list)):
                self.equipped_widget_list[j].config(relief=GROOVE)
            self.equipped_widget_list[oldnbr].config(relief=GROOVE)
            self.selected_equipped_item,self.selected_equipped_nbr = 'None','None'
            self.selected_item,self.selected_nbr = 'None','None'

if __name__ == "__main__":
    player_dic,attribut_dic,spell_dic,inventory_dic = dictionnaires.dictionnaires_vierge()

    w = Inventory_Window(toplevel=False,player_dic=player_dic,inventory_dic=inventory_dic)