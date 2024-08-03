from tkinter import *



window = Tk()
window.geometry("300x300")

def import_login():
    print("line 6 ")
    import log_in_page
    

b = Button(window, text="click login", command=import_login)
b.pack()


window.mainloop()
