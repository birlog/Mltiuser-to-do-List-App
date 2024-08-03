from tkinter import Button
import tkinter as tk
from tkinter import Frame
from tkinter import Label

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To Do list")
        self.geometry("750x500")
        
        self.widgets_configuration()
        self.widgets_packing()
        
    def widgets_configuration(self):
        self.frame1 = Frame(self, width = 715, height=50)
        self.frame2 = Frame(self, width = 715, height = 415, bg = 'Black')
        self.name_label = Label(self.frame1, text = 'DUI DOO', font=("Bradley Hand ITC", 30, "bold"))
        self.switch_user = Button(self.frame1, text = 'Switch User', font=('arial', 10, "bold"))
        self.log_out = Button(self.frame1, text="Log out", font = ("arial", 10, "bold"))

    def widgets_packing(self):
        self.frame1.pack(pady = 10)
        self.frame2.pack()

        self.name_label.place(x = 10 , y = 0)

        self.switch_user.place(x = 550, y = 10)
        self.log_out.place(x = 650, y = 10)

    def login():
        pass

    def switch_user():
        pass


main = Main()
main.mainloop()