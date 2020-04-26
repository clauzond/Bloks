from tkinter import *
import tkinter.ttk as ttk
from math import log

class SpeedBar():


    def __init__(self,canvas,x,y,length,max1,max2,speed1,speed2,color1,color2,backgroundcolor,bordercolor):
        # La longueur maximuale de la barre sera fixe.
        # Il faudra donc tout compter en "relatif"
        self.length = length


        self.max1 = max1
        self.max2 = max2

        self.value1 = 0
        self.value2 = 0

        self.id_speed1 = speed1
        self.id_speed2 = speed2

        self.speed1= self.fonction_lc(speed1)
        self.speed2= self.fonction_lc(speed2)


        self.loop = False
        self.canvas = canvas

        self.bar1 = self.bar2 = None

        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y

        self.backgroundcolor = backgroundcolor
        self.bordercolor = bordercolor

        self.order = None


        #from ttkthemes import ThemedStyle
        #style = ThemedStyle()
        #style.set_theme('plastik')


    # Une fonction qui : croit très lentement, prend des valeurs en R+, strictement positive
    def fonction_lc(self,value):
        new_value = log(10+value)

        return(new_value)


    def hidetip(self):
        self.order = "stop"
        self.bar1.place_forget()
        self.bar2.place_forget()
        self.bar1.destroy()
        self.bar2.destroy()

    def show(self):
        if self.bar1:
            return

        style = ttk.Style()
        style.theme_use('clam')
        # troughcolor pour le fond, background pour le devant de la barre, bordercolor pour les bords, lightcolor/darkcolor pour le haut/bas des bords
        style.configure("TProgressbar", background=self.color1,troughcolor=self.backgroundcolor,bordercolor=self.bordercolor,lightcolor=self.backgroundcolor,darkcolor=self.backgroundcolor)


        self.bar1 = ttk.Progressbar(self.canvas,style="TProgressbar",orient=VERTICAL,length=self.length,maximum=self.max1,mode='determinate',value=self.value1)
        self.bar1.place(x=self.x,y=self.y,height=self.length,width=30)


        style.configure("red.Horizontal.TProgressbar",background=self.color2,troughcolor=self.backgroundcolor,bordercolor=self.bordercolor,lightcolor=self.backgroundcolor,darkcolor=self.backgroundcolor)
        self.bar2 = ttk.Progressbar(self.canvas,style="red.Horizontal.TProgressbar",orient=VERTICAL,length=self.length,maximum=self.max2,mode='determinate',value=self.value2)
        self.bar2.place(x=self.x + 30 ,y=self.y,height=self.length,width=30)




    def start(self,event=''):
        self.lets_go()




    # La barre passe de la current_value à la valeur "valeur", en considérant que on ENLEVE valeur
    def lets_go(self):


        # pour self.max1 = self.max2 = 100 :
        # Théoriquement, comme le plus grand des pas fait 0.1, alors au max on devrait avoir 1s
        # Comme tkinter est plus ou moins lent, on peut compteur 2s
        self.intervalle = 1

        coef = 0.1 / (min(self.max1,self.max2) * max(self.speed1, self.speed2))


        self.pas1 = self.max1 * self.speed1 * coef
        self.pas2 = self.max2 * self.speed2 * coef

        if not self.loop:
            return(self.mini_loop())
        else:
            self.order = "wait"


    def mini_loop(self):
        self.loop = True

        if (self.value1 + self.pas1 < self.max1) and (self.value2 + self.pas2 < self.max2):
            self.value1 += self.pas1
            self.progress1(self.pas1)

            self.value2 += self.pas2
            self.progress2(self.pas2)


            self.canvas.after(self.intervalle,self.mini_loop)

        else:
            # on compare pour savoir qui est premier. S'il y a égalité, c'est le premier qui l'emporte par défault.
            self.loop = False
            if (self.value1 + self.pas1 > self.max1):
                self.value1 = 0
                self.set1(0)

                self.order = 1

            else:
                self.value2 = 0
                self.set2(0)
                self.order = 2





    # Ajoute value à la barre de progression 1
    def progress1(self,value):
        self.bar1.step(amount=value)

    # Enlève value à la barre de progression 2
    def progress2(self,value):
        self.bar2.step(amount=value)


    # Défini la barre de progression à value
    def set1(self,value):
        self.bar1['value'] = value
        self.bar1.update()

    def set2(self,value):
        self.bar2['value'] = value
        self.bar2.update()

    def set_speed1(self,value,*args):
        self.id_speed1 = value
        self.speed1= self.fonction_lc(value)


    def set_speed2(self,value,*args):
        self.id_speed2 = value
        self.speed2= self.fonction_lc(value)


if __name__ == "__main__":
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


    wc = Canvas(w)
    wc.pack(fill=BOTH,expand=True,padx=20,pady=20)

    sb = SpeedBar(wc,x=30,y=30,length=100,max1=100,max2=100,speed1=200.1,speed2=159.3,color1="yellow",color2="orange",bg='black')
    sb.show()

    wc.bind('<Button-1>',sb.start)

    w.mainloop()