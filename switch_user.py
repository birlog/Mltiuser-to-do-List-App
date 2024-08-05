from tkinter import Button
import tkinter as tk
from tkinter import Frame
from tkinter import Label

class SwitchUser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Switch User Page")
        self.geometry("350x500")
        
        self.widgets_configuration()
        self.widgets_packing()
        
    def widgets_configuration(self):
        self.frame1 = Frame(self, bg= 'black' , width = 330, height=410)
        self.name_label = Label(self, text = 'Switch User', font=("Bradley Hand ITC", 30, "bold"))

    def widgets_packing(self):
        self.name_label.pack(padx=10, pady=10)
        self.frame1.pack()

    def switch(self):
        pass


main = SwitchUser()
main.mainloop()