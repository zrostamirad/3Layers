import PL.reg_form
from customtkinter import *
from BE.dbcontext import dbcontext

if __name__ == "__main__":
    #این چبه؟
    db = dbcontext()
    screen = CTk()
    screen.geometry("400x700+650+0")
    set_appearance_mode("dark")
    PageMe = PL.reg_form.App(screen)
    screen.mainloop()
