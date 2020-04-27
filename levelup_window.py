from tkinter import *
import classtooltip as ctt
import dictionnaires

class Levelup_Window():

    def __init__(self,toplevel,player_dic,attribut_dic,function=lambda :None,rel_x=0,rel_y=0):

        self.function = function

        if toplevel:
            self.level_window = Toplevel()
            self.level_window.wm_overrideredirect(1)
            self.level_window.wm_geometry('+%d+%d' % (rel_x,rel_y))
            self.level_window.focus_force()
        else:
            self.level_window = Tk()
        self.level_window.title("Pas assez d'expérience...")
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
        self.attribut_dic = attribut_dic
        self.img_dic = dictionnaires.dictionnaires_vierge(loadimg=True)
        self.newlevel = 0
        self.newattributpoint = 0
        self.newspellpoint = 0

        playerimg = PhotoImage(file=self.player_dic['image'])
        name_label = Label(self.level_canvas,
                        text=self.player_dic['name'],
                        font="Constantia 13 bold",image=playerimg)
        name_label.grid(row=0, column=0, sticky=W,columnspan=10)

        self.level_label = Label(self.level_canvas,
                        text=str(self.player_dic['level']),
                        font="Constantia 13 bold",image=self.img_dic['starnoir'])
        self.level_label.grid(row=0,column=0,columnspan=10)

        self.xp_label = Label(self.level_canvas,
                        text=str(self.player_dic['current_xp'])+'/'+str(self.player_dic['max_xp']),
                        font='Constantia 13 bold',image=self.img_dic['xpnoir'])
        self.xp_label.grid(row=0,column=0,columnspan=100,sticky=E)


        Frame(self.level_canvas,height=20).grid(row=1)


        if int(self.player_dic['attribut_point'])>1:
            s='s'
        else:
            s=''
        txt=f"Attribut point{s} : {str(self.player_dic['attribut_point'])}"
        self.txt_point_label1 = Label(self.level_canvas,
                            text=txt,
                            font='Constantia 13 bold',image=self.img_dic['star'])
        self.txt_point_label1.grid(row=1,column=0,columnspan=10)

        if int(self.player_dic['spell_point'])>1:
            s='s'
        else:
            s=''
        txt=f"Spell point{s} : {str(self.player_dic['spell_point'])}"
        self.txt_point_label2 = Label(self.level_canvas,
                            text=txt,
                            font='Constantia 13 bold',image=self.img_dic['star'])
        self.txt_point_label2.grid(row=2,column=0,columnspan=10)

        # Séparateur
        Frame(self.level_canvas,height=10,width=400).grid(row=3)


        self.txt_levelup1 = Label(self.level_canvas,
                                text=f'',
                                font='Constantia 13 bold')
        self.txt_levelup1.grid(row=4,column=0,columnspan=10)
        self.txt_levelup2 = Label(self.level_canvas,
                                text=f"Vous n'avez pas assez d'expérience pour level up...",
                                font='Constantia 13 bold')
        self.txt_levelup2.grid(row=5,column=0,columnspan=10)
        self.txt_levelup3 = Label(self.level_canvas,
                                text=f'',
                                font='Constantia 13 bold')
        self.txt_levelup3.grid(row=6,column=0,columnspan=10)

        # Séparateur
        Frame(self.level_canvas,height=20,width=400).grid(row=7)
        self.confirmbutton = Button(self.level_canvas,text="Confirmer",command=self.confirm)
        self.confirmbutton.grid(row=10,column=0,columnspan=10)


        self.checkforlevelup()



        self.level_window.deiconify()
        self.level_window.mainloop()

    def confirm(self):
        import manipulate_stats

        self.player_dic = manipulate_stats.calculate_playerstats(attribut_dic=self.attribut_dic,player_dic = self.player_dic)

        import manipulate_json as jm

        jm.save_file(self.player_dic,filename='player_dic',player_name=self.player_dic['name'])
        jm.save_file(self.attribut_dic,filename='attribut_dic',player_name=self.player_dic['name'])

        if self.function is not None:
            self.function()

        self.level_window.destroy()

    def checkforlevelup(self):

        if int(self.player_dic['current_xp'])>=int(self.player_dic['max_xp']):

            #dic = dictionnaires.dictionnaires_vierge(loadlevelupdics=True)
            mxlist = self.player_dic['max_xp_growth']
            apglist = self.player_dic['attribut_point_growth']
            spglist = self.player_dic['spell_point_growth']
            #apdic = dic['attribut_gain']

            # get new level
            self.player_dic['total_xp'] += int(self.player_dic['current_xp'])
            self.player_dic['current_xp'] -= int(self.player_dic['max_xp'])
            self.player_dic['level'] += 1
            self.player_dic['max_xp'] = int(mxlist[int(self.player_dic['level'])])
            self.newlevel += 1

            # get new attribut point
            gain = int(apglist[int(self.player_dic['level'])])
            self.player_dic['attribut_point'] += gain
            self.newattributpoint += gain

            # get new spell point
            gain = int(spglist[int(self.player_dic['level'])])
            self.player_dic['spell_point'] += gain
            self.newspellpoint += gain

            # add attribut points according to levelup gain
            attribut_name_list = list(self.attribut_dic.keys())
            for i in range(len(attribut_name_list)):
                this_attribut = str(attribut_name_list[i])
                this_gain = int( self.attribut_dic[this_attribut]['growth'][ self.player_dic['level'] ] )

                self.attribut_dic[this_attribut]['level'] += this_gain
                self.player_dic['stats'][this_attribut] += this_gain


            # check for another level up
            self.checkforlevelup()

        else:
            # afficher la majorité des informations une fois que la phase de levelup est terminée
            self.function()

            if int(self.player_dic['attribut_point'])>1:
                s='s'
            else:
                s=''
            txt=f"Attribut point{s} : {str(self.player_dic['attribut_point'])}"
            self.txt_point_label1.config(text=txt)
            self.txt_point_label1.update()


            if int(self.player_dic['spell_point'])>1:
                s='s'
            else:
                s=''
            txt=f"Spell point{s} : {str(self.player_dic['spell_point'])}"
            self.txt_point_label2.config(text=txt)
            self.txt_point_label2.update()

            if self.newlevel>0:
                txt=f"{self.player_dic['level']} (+{self.newlevel})"
            else:
                txt=f"{self.player_dic['level']}"
            self.level_label.config(text=txt)
            self.level_label.update()

            self.xp_label.config(text=f"{self.player_dic['current_xp']}/{self.player_dic['max_xp']}")


            if self.newlevel>0:
                self.level_window.title("Level up !")
                n = self.newlevel
                n2 = self.newattributpoint
                n3 = self.newspellpoint
                if self.newlevel>1:
                    x='x'
                else:
                    x=''
                txt1=f"Bravo ! Vous êtes monté de {n} niveau{x}"
                if self.newspellpoint>1:
                    s='s'
                else:
                    s=''
                txt2=f"Vous avez gagné {n2} points d'attributs et {n3} point{s} de spell"
                txt3=f"Vous avez aussi gagné des attributs bonus, allez voir !"
                self.txt_levelup1.config(text=txt1)
                self.txt_levelup1.update()
                self.txt_levelup2.config(text=txt2)
                self.txt_levelup2.update()
                self.txt_levelup3.config(text=txt3)
                self.txt_levelup3.update()

if __name__=='__main__':
    #player_dic,attribut_dic,spell_dic,inventory_dic = dictionnaires.dictionnaires_vierge()

    import manipulate_json as jm
    player_dic = jm.load_file('player_dic','Blue Dragon')
    attribut_dic =jm.load_file('attribut_dic','Blue Dragon')
    spell_dic = jm.load_file('spell_dic','Blue Dragon')
    inventory_dic = jm.load_file('inventory_dic','Blue Dragon')


    w = Levelup_Window(toplevel=False,player_dic=player_dic,attribut_dic=attribut_dic)


