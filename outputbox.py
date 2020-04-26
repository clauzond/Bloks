from tkinter import *
import tkinter.scrolledtext as scrolledtext

class OutputBox():

    def __init__(self,canvas,x,y,height,width,special=''):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.widget = None
        self.width = width
        self.height = height
        self.special=special

    def hidetip(self,*args):
        self.widget.place_forget()
        self.widget.destroy()

    def show(self):
        if self.widget:
            return


        self.widget = scrolledtext.ScrolledText(self.canvas,width=self.width,height=self.height,wrap='word',undo=True)

        if self.special=='':
            self.widget.place(x=self.x,y=self.y,width=self.width,height=self.height)
        elif self.special=='pack':
            self.widget.pack(side=TOP)
        elif self.special=="grid":
            self.widget.grid(row=0,column=1)
        self.widget.config(state=DISABLED)

        self.i = 1

    def add_text(self,text):
        text = "\n" + text
        self.widget.config(state=NORMAL)
        self.widget.insert(END,text)
        self.widget.see(END)
        self.widget.config(state=DISABLED)

        self.widget.update()


    def ajouter(self,event):
        self.i = self.i * 2
        self.add_text(f"{self.i}éé\n")
        self.widget.see(END)


if __name__ == '__main__':
    main_window = Tk()

    main_window.option_add('*background','gray')
    main_window.option_add('*foreground','white')

    c = Canvas(main_window,width=300,height=300)
    c.pack()

    textbox = OutputBox(canvas=c,x=50,y=50,height=1000,width=1000)
    textbox.show()
    textbox.widget.bind('<a>',textbox.ajouter)
    textbox.widget.bind('<b>',textbox.hidetip)

    main_window.mainloop()
