from tkinter import *
import tkinter.ttk as ttk


class SpellBar():


    def __init__(self,canvas,x,y,length,height,current_value,maximum,color,backgroundcolor,bordercolor,special=""):
        # La longueur maximuale de la barre sera fixe.
        # Il faudra donc tout compter en "relatif"
        self.length = length
        self.maximum = maximum

        self.current_value = current_value
        self.loop = False
        self.canvas = canvas

        self.widget = self.label = None

        self.special = special


        self.color = color
        self.backgroundcolor = backgroundcolor
        self.bordercolor = bordercolor

        self.x = x
        self.y = y

        self.height = height

        #from ttkthemes import ThemedStyle
        #style = ThemedStyle()
        #style.set_theme('plastik')

    def hidetip(self):
        self.widget.place_forget()
        self.label.place_forget()
        self.widget.destroy()
        self.label.destroy()

    def show(self):
        if self.widget:
            return

        style = ttk.Style()
        style.theme_use('clam')
        # troughcolor pour le fond, background pour le devant de la barre, bordercolor pour les bords, lightcolor/darkcolor pour le haut/bas des bords
        style.configure("orange.Horizontal.TProgressbar", background=self.color,bordercolor=self.bordercolor,troughcolor=self.backgroundcolor,lightcolor=self.backgroundcolor,darkcolor=self.backgroundcolor)


        self.widget = ttk.Progressbar(self.canvas,style="orange.Horizontal.TProgressbar",orient=HORIZONTAL,length=self.length,maximum=self.maximum,mode='determinate',value=self.current_value)

        self.widget.place(x=self.x,y=self.y,height=self.height)
        self.label = Label(self.canvas,text=f"{self.current_value:0.0f}%")

        if self.special == "right":
            self.label.place(x=self.x+self.length,y=self.y+25,anchor="ne")
        elif self.special == "middle":
            self.label.place(x=self.x + self.length/2,y=self.y+25,anchor="n")
        else:
            self.label.place(x=self.x,y=self.y+25)



    def func(self,event):
        self.slowprogress(30)


    def slowprogress(self,value):
        # l'intervalle de temps (en ms) sera de 1% de la valeur max par 10 ms
        # donc "valeur max en 1000 ms = 1s"
        intervalle = 1

        pas = 0.001 * self.maximum

        final_value = self.current_value + value


        if not self.loop:
            self.mini_loop(intervalle,pas,final_value)


    def mini_loop(self,intervalle,pas,final_value):
        self.loop = True
        if self.current_value + pas < final_value:
            self.current_value += pas
            self.progress(pas)
            self.label.config(text=f"{self.current_value:0.0f}%")

            self.widget.after(intervalle,self.mini_loop,intervalle,pas,final_value)
            #self.widget.update()

        else:
            self.set(final_value)

            self.current_value = final_value

            self.loop = False


    # Ajoute value à la barre de progression
    def progress(self,value):
        if self.current_value >= self.maximum:
            self.widget['value'] = self.current_value + value
        else:
            self.widget.step(amount=+value)

    # Défini la barre de progression à value
    def set(self,value):
        self.widget['value'] = value
        self.widget.update()




if __name__=="__main__":
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


    wc = Canvas(w,width=500)
    wc.pack(fill=BOTH,expand=True,padx=0,pady=0)

    healthbar = SpellBar(canvas=wc,length=200,height=25,current_value=0,maximum=100,x=10,y=0,color="red",backgroundcolor="white",bordercolor="yellow",special="middle")
    healthbar.show()
    wc.bind_all('<Button-1>',healthbar.func)



    w.mainloop()