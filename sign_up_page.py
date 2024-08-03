import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import Button

class LoginGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign Up")
        self.geometry("500x400")
        self.widgets_configuration()
        self.widgets_packing()

    def widgets_configuration(self):

        self.log_in_label = Label(
            self, text="Create New Account", font=("Bradley Hand ITC", 30, "bold"))
        self.frame = Frame(self)

        self.name_label = Label(self.frame, text="Name", font=("Dubai, 16"))
        self.name_entry = Entry(self.frame, width=18, font=("Dubai, 16"))

        self.user_name_label = Label(self.frame, text="User Name", font=("Dubai, 16"))
        self.user_name_entry = Entry(self.frame, width=18, font=("Dubai, 16"))

        self.password_label = Label(self.frame, text="Password", font=("Dubai, 16"))
        self.password_entry = Entry(self.frame, width=18, font=("Dubai, 16"))

        self.mail_label = Label(self.frame, text="Recovery Email", font=("Dubai, 16"))
        self.mail_entry = Entry(self.frame, width=18, font=("Dubai, 16"))

        self.log_in_button = Button(
            self, text="Sign Up", font=("Bradley Hand ITC", 25, "bold"))

    def widgets_packing(self):
        self.log_in_label.pack(pady=15)
        self.frame.pack()

        self.name_label.grid(row = 0 , column = 0 , pady= 10, padx = 10)
        self.name_entry.grid(row = 0, column = 1 , pady= 10, padx = 10)

        self.user_name_label.grid(row = 1, column = 0, pady= 10, padx = 10)
        self.user_name_entry.grid(row = 1 , column = 1, pady= 10, padx = 10)

        self.password_label.grid(row = 2 , column = 0, pady= 10, padx = 10)
        self.password_entry.grid(row = 2, column = 1, pady= 10, padx = 10)

        self.mail_label.grid(row = 3 , column = 0, pady= 10, padx = 10)
        self.mail_entry.grid(row = 3, column = 1, pady= 10, padx = 10)



        self.log_in_button.pack(pady=20)


login = LoginGui()
login.mainloop()
