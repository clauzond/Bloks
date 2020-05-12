from tkinter import *
import tkinter.ttk as ttk

class AttackAnimation():


    def __init__(self,canvas,x,y,backgroundcolor,linecolor,linebordercolor,hitboxcolor):
        pass

    # On retire TOUS les paramètres qu'on a défini en "self.param = ..."
    def hide(self):
        pass

    def draw_background(self):
        pass

    # Pour arrêter l'animation, ce sera avec "playerinput" qui définiera une variable stoppant la loop
    def start_animation(self,number_of_times=1,function=lambda:None):
        pass

    # Défini, pour le background,
    def set_hitbox_limits(self,difficulty_level):
        pass

    def aux_draw_line(self,x):
        pass

    def aux_remove_line(self):
        pass

    def playerinput(self):
        pass




def truc():
    pass

if __name__ == "__main__":
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

    wc.bind('<a>',truc)

    w.mainloop()