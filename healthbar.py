from tkinter import *
import tkinter.ttk as ttk



class HealthBar():


    def __init__(self,canvas,x,y,length,maximum,color):
        # La longueur maximuale de la barre sera fixe.
        # Il faudra donc tout compter en "relatif"
        self.length = length
        self.maximum = maximum

        self.current_value = maximum
        self.loop = False
        self.canvas = canvas

        self.widget = self.label = None

        self.color = color
        self.x = x
        self.y = y

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
        style.configure("TProgressbar", background=self.color,bordercolor="black",troughcolor="white")


        self.widget = ttk.Progressbar(self.canvas,style="TProgressbar",orient=HORIZONTAL,length=self.length,maximum=self.maximum,mode='determinate',value=self.current_value)
        self.widget.place(x=self.x,y=self.y,height=25)

        self.label = Label(self.canvas,text=f"{self.current_value:0.1f}/{self.maximum:0.1f}")
        self.label.place(x=self.x,y=self.y+25)



    def func(self,event):
        self.take_hit(900.333)


    # La barre passe de la current_value à la valeur "valeur", en considérant que on ENLEVE valeur
    def take_hit(self,hitdamage):

        # l'intervalle de temps (en ms) sera de 1% de la valeur max par 10 ms
        # donc "valeur max en 1000 ms = 1s"
        intervalle = 1

        pas = 0.001 * self.maximum

        final_value = self.current_value - hitdamage

        if not self.loop:
            self.mini_loop(intervalle,pas,final_value)


    def mini_loop(self,intervalle,pas,final_value):
        self.loop = True
        if self.current_value - pas > final_value:
            self.current_value -= pas
            self.progress(pas)
            self.label.config(text=f"{self.current_value:0.1f}/{self.maximum:0.1f}")

            self.widget.after(intervalle,self.mini_loop,intervalle,pas,final_value)
            #self.widget.update()

        else:
            self.set(final_value)

            self.current_value = final_value

            self.loop = False


    # Enlève value à la barre de progression
    def progress(self,value):
        self.widget.step(amount=-value)

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

    healthbar = HealthBar(canvas=wc,length=100,maximum=10000,x=10,y=0,color="red")
    healthbar.show()
    healthbar.widget.bind('<Button-1>',healthbar.func)



    w.mainloop()