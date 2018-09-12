from tkinter import *
import tkinter as tk
import math
class Paint():


    def __init__(self):

        self.window=Tk()
        sizex=600
        sizey=500
        self.color="red"
        variable=StringVar(self.window)
        color_variable=StringVar(self.window)

        num_list=[]

        for i in range(100):
            if (i%5==0):
                num_list.append(i)
        self.color_label = Label(self.window, text='color size', relief=RIDGE, width=10).grid(row=0, column=2)

        color_list = ["white","green","red","blue","yellow","purple","brown","turquoise", "pink", "black"]
        color_menu = OptionMenu(self.window,color_variable, *color_list, command=self.color_choice).grid(row=0,column=3)
        color_variable.set(color_list[2])

        pen_menu=OptionMenu(self.window,variable,*num_list,command=self.pen_size).grid(row=0,column=1)
        variable.set(num_list[5])
        self.default_pen_size=5
        label=Label(self.window,text='Pen Size', relief=RIDGE,width=10).grid(row=0,column=0)

        self.canvas = Canvas(self.window, width=sizex, height=sizey, bg = "white")
        self.canvas.grid(row=1)

        self.img = PhotoImage(width=sizex, height=sizey-25)
        self.canvas.create_image((sizex/2, (sizey-25)/2), image=self.img, state="normal")
        self.canvas.bind("<Button-1>", self.color_in)
        self.canvas.bind("<B1-Motion>", self.color_in)

    def color_in(self, event):
        radius_sqrt=math.sqrt(self.default_pen_size)
        circle=self.canvas.create_oval(event.x - radius_sqrt, event.y - radius_sqrt, event.x + radius_sqrt,
        event.y + radius_sqrt, fill=self.color,outline="")

    def pen_size(self, selection):
        self.default_pen_size=int(selection)

    def color_choice(self, selection):
        self.color=selection

if __name__=='__main__':
    paint=Paint()
    paint.window.mainloop()