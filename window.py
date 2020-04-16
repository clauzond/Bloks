# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:32:33 2020

@author: Damien
"""

from tkinter import *


class BloksWindow:
    
    def __init__(self,toplevel=False,title="Bloks",cwidth=300,cheight=300,gwidth=300,gheight=100,wcolor="white",ccolor="black",gcolor="gray"):
        
        if toplevel:
            self.window= Toplevel()
        else:
            self.window = Tk()

        self.window.title(title)
        self.window.resizable(width=False,height=False)
        self.window.maxsize(width=max(cwidth,gwidth), height=cheight+cwidth)
        
        self.gamecanvas = Canvas(self.window, width=cwidth, height=cheight, bg=ccolor)
        self.gamecanvas.pack(side="top",expand=True,fill="both")
        
                         
        self.guicanvas = Canvas(self.window, width=gwidth, height=gheight, bg=gcolor)
        self.guicanvas.pack(side="bottom",expand=True,fill="both",pady=10)
        
        
        #Lab=Label(self.guicanvas,text="aaa",font="Constantia 20",padx=10,pady=10)
        #Lab.pack()
        
        
        self.window.config(bg=wcolor)
        
        self.quit = False
        
        
        #self.window.iconbitmap("test.ico")


    def click(self,event):
        print(event.x,event.y)

    def quit(self,event):
        if not self.quit:
            print("Appuyez à nouveau pour quitter")
            self.quit = True
            
            self.window.after(100,self.dontquit)
        else:
            self.window.destroy()
        print("a")
        
    def dontquit(self):
        self.quit=False
        
        
        
if __name__ == "__main__" :
    w = BloksWindow()
    w.window.bind('<Escape>',w.quit)
    w.window.bind('<Button-1>',w.click)
    
    
    w.window.mainloop()