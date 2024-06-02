from customtkinter import *
from tkinter import ttk, messagebox
from BLL.bl_personnel import bl_personnel
from BE.personnel_cls import personnel


class App(CTkFrame):

    def __init__(self, screen=None):
        super().__init__(screen)
        self.master = screen
        self.CreateWidget()

    def CreateWidget(self):
        self.varName = StringVar()
        self.varLastName = StringVar()
        self.varAge = StringVar()
        persian_font = CTkFont(family="Tahoma", size=12)

        CTkLabel(self.master, text="Name:").pack()
        self.txtname = CTkEntry(self.master,
                                textvariable=self.varName,
                                font=persian_font)
        self.txtname.pack()

        CTkLabel(self.master, text="Last Name:").pack()
        self.txtlastname = CTkEntry(self.master,
                                    textvariable=self.varLastName,
                                    font=persian_font)
        self.txtlastname.pack()

        CTkLabel(self.master, text="Age:").pack()
        self.txtage = CTkEntry(self.master,
                               textvariable=self.varAge)
        self.txtage.pack()

        self.btn = CTkButton(self.master, text="Register", command=self.Register)
        self.btn.pack()

        self.tbl = ttk.Treeview(self.master,
                                columns=("c1", "c2", "c3"),
                                show="headings",
                                height=50)
        self.tbl.column("#3", width=50)
        self.tbl.heading("#3", text="نام")
        self.tbl.column("#2", width=50)
        self.tbl.heading("#2", text="نام خانوادگی")
        self.tbl.column("#1", width=50)
        self.tbl.heading("#1", text="سن")
        self.tbl.place(relx=0.35, rely=0.3)

    def Register(self):
        if self.varName.get() == "":
            messagebox.showwarning("", "نام را وارد کنید")
            self.txtname.focus()
        elif self.varLastName.get() == "":
            messagebox.showwarning("", "نام خانوادگی را وارد کنید")
            self.txtlastname.focus()
        elif self.varAge.get() == "" or not (self.varAge.get().isdigit()):
            messagebox.showwarning("", "سن را به درستی وارد کنید")
            self.txtage.focus()
        else:
            object = personnel(self.varName.get(), self.varLastName.get(), self.varAge.get())
            n = bl_personnel()
            result = n.Add(object)
            print(result)
            if result:
                messagebox.showinfo("", "ثبت شد")
            elif result == "2":
                messagebox.showerror("", "کمتر از 18سال ثبت نمیشود")
            else:
                messagebox.showerror("", "مشکل پیش آمده بعدا سعی کن...")
