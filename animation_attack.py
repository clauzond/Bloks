from tkinter import *
from random import uniform
import tkinter.ttk as ttk
from time import time

class AttackAnimation():


    def __init__(self,canvas,x,y,width,height,difficulty_level,backgroundcolor,backgroundbordercolor,linecolor,linebordercolor,hitboxcolor):
        """

        param :
        :canvas -> le canvas sur lequel on va dessiner l'animation
        :x,y -> coordonné (x,y) du coin NW
        :width,height -> dimensions du background
        :difficulty_level -> entre 1 et 20, gère les difficultés de l'attaque
        :______color -> self-explicit
        """


        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.difficulty_level = difficulty_level
        self.backgroundcolor = backgroundcolor
        self.backgroundbordercolor = backgroundbordercolor
        self.linecolor = linecolor
        self.linebordercolor = linebordercolor
        self.hitboxcolor = hitboxcolor

        self.hitboxtuple = None
        self.player_input = False
        self.linewidth = 30
        self.speed = ((self.difficulty_level)**0.5 )*150

        self.pourcentage_total = 0
        self.looping = False



    # Dessine le background
    def show(self):
        self.draw_background()
        self.draw_hitbox()
        pass

    # On retire TOUS les paramètres qu'on a défini en "self.param = ..."
    def hide(self):
        self.canvas.delete("myline","myhitbox","mybackground")
        self.canvas = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.difficulty_level = None
        self.backgroundcolor = None
        self.backgroundbordercolor = None
        self.linecolor = None
        self.linebordercolor = None
        self.hitboxcolor = None

        self.hitboxtuple = None
        self.player_input = None
        self.linewidth = None
        self.speed = None

        self.pourcentage_total = None
        self.looping = None

    def draw_background(self):

        self.canvas.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,
                                    tags="mybackground",
                                    fill=self.backgroundcolor,
                                    outline=self.backgroundbordercolor,
                                    width=2
                                    )


    # Pour arrêter l'animation, ce sera avec "playerinput" qui définiera une variable stoppant la loop
    def start_animation(self,number_of_times=1,function=lambda *args:None):
        if self.looping:
            return
        self.remove_hitbox()
        self.draw_hitbox()
        self.pourcentage_total = 0
        self.player_input = False
        self.looping = True
        t = time()
        self.loop_for_input(x=self.x,_time=t,i=0,maximum_times=number_of_times,function=function)

    def loop_for_input(self,x,_time,i,maximum_times,function):
        if i>=maximum_times:
            function(self.pourcentage_total,maximum_times)
            self.looping = False

        elif (not self.player_input) and (x <= self.x + self.width - self.linewidth):
            t = time()
            dt = t - _time
            pas = self.speed * dt

            self.remove_lines()
            self.draw_line(x)

            self.canvas.after(1,self.loop_for_input,x+pas,t,i,maximum_times,function)
        else:
            t = time()
            self.pourcentage_total += self.check_collision(line_x = x)

            if i+1 != maximum_times:
                self.player_input = False
                self.remove_hitbox()
                self.draw_hitbox()

            self.canvas.after(1,self.loop_for_input,self.x,t,i+1,maximum_times,function)




    def draw_hitbox(self):
        limit_amplitude = (self.difficulty_level)*15
        hitbox_width = (5 - self.difficulty_level**0.5)*20

        _x =( (self.x+self.width) + (self.x) )/2 # milieu "exact" du background

        r = uniform(_x-limit_amplitude,_x+limit_amplitude)

        if r>=self.x+self.width-hitbox_width/2:
            r = self.x + self.width - hitbox_width/2
        elif r<=self.x + hitbox_width/2:
            r = self.x + hitbox_width/2


        self.canvas.create_rectangle(r-hitbox_width/2,self.y,r+hitbox_width/2,self.y+self.height,
                                    tags="myhitbox",
                                    fill=self.hitboxcolor,
                                    outline=self.backgroundbordercolor,
                                    width=2
                                    )
        self.hitboxtuple = (r-hitbox_width/2 , r+hitbox_width/2)


    def check_collision(self,line_x):
        """
        :line_x -> celui utilisé pour draw la ligne
        """
        if self.hitboxtuple is None:
            return

        x0 = line_x
        x1 = line_x + self.linewidth

        (a0,a1) = self.hitboxtuple

        # En plein dans la hitbox
        if a0<=x0<=a1 and a0<=x1<=a1:
            return(1)

        # La hitbox est entièrement dedans
        elif x0<=a0<=x1 and x0<=a1<=x1:
            return(1)

        # La partie gauche de la ligne (à droite de la hitbox) est dedans
        elif a0<=x0<=a1:
            maximum = min(self.linewidth,a1-a0)
            actuel = a1-x0
            pourcentage = actuel/maximum
            return(pourcentage)

        # La partie droite de la ligne (à gauche de la hitbox) est dedans
        elif a0<=x1<=a1:
            maximum = min(self.linewidth,a1-a0)
            actuel = x1-a0
            pourcentage = actuel/maximum
            return(pourcentage)
        else:
            return(0)







    def draw_line(self,x):
        """
        self.linewidth est définie dans __init__ pour la largeur de la ligne

        :x -> le coin NW de la ligne
        """
        self.canvas.create_rectangle(x,self.y,x+self.linewidth,self.y+self.height,
                                tags="myline",
                                fill=self.linecolor,
                                outline=self.linebordercolor,
                                width=1
                                )

    def remove_lines(self):
        self.canvas.delete("myline")

    def remove_hitbox(self):
        self.canvas.delete("myhitbox")

    def stoptheline(self):
        self.player_input = True




def truc4(event):
    aa.stoptheline()

def truc5(event):
    aa.start_animation(number_of_times=3,function=truc0)

def truc0(pourcentage,nbr):
    print(f"Fini ! Vous avez fait {pourcentage*100:0.0f}/{nbr*100}%")

if __name__ == "__main__":
    global aa

    w = Tk()

    w.title("Un petit test")
    w.resizable(False,False)
    w.iconbitmap("img/icone.ico")

    w.option_add('*Font','Constantia 12')
    w.option_add('*Button.relief','flat')
    w.option_add('*Button.overRelief','ridge')
    w.option_add('*justify','left')
    #self.backgroundcolor='#8BD8BD'
    #self.foregroundcolor='#243665'
    backgroundcolor="#292826"
    foregroundcolor="#F9D342"
    w.option_add('*background',backgroundcolor)
    w.option_add('*foreground',foregroundcolor)
    w.option_add('*compound','left')


    wc = Canvas(w,width=600,height=600)
    wc.pack(fill=BOTH,expand=True,padx=0,pady=0)

    aa = AttackAnimation(canvas=wc,x=20,y=20,width=500,height=200,difficulty_level=10,backgroundcolor="gray",backgroundbordercolor="yellow",linecolor="blue",linebordercolor="yellow",hitboxcolor="red")

    aa.show()


    #wc.bind_all('<a>',truc)
    #wc.bind_all('<Button-1>',truc2)
    #wc.bind_all('<b>',truc3)
    wc.bind_all('<space>',truc4)
    wc.bind_all('<p>',truc5)


    w.mainloop()