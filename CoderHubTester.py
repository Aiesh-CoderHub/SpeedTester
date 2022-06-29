from pydoc import cli
from tkinter import font
from click import Command, command
import speedtest_cli
from tkinter import *


def speedCheck():
    scp = speedtest_cli.Speedtest()
    scp.get_servers()
    down = str(round(scp.download()/(10**6), 3)) + "Mbps"
    up = str(round(scp.upload()/(10**6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("SpeedTester from Coder's Hub")
sp.geometry("300x450")
sp.config(bg="black")
lab = Label(sp, text=" SpeedTest By Coder's Hub",
            font=("Ubuntu"), bg="black", fg="White")
lab.place(x=24, y=28,)

lab = Label(sp, text="Downloading Speed: ",
            font=("Ubuntu"), bg="black", fg="White")
lab.place(x=28.5, y=100,)

lab_down = Label(sp, text="00",
                 font=("Ubuntu"), bg="black", fg="White")
lab_down.place(x=192, y=100,)

lab = Label(sp, text=" Uploading Speed: ",
            font=("Ubuntu"), bg="black", fg="White")
lab.place(x=24.5, y=135,)

lab_up = Label(sp, text="00",
               font=("Ubuntu"), bg="black", fg="White")
lab_up.place(x=170, y=135,)

button = Button(sp, text="Check Speed", font=(
    "Ubuntu"), fg="black", command=speedCheck,)
button.place(x=70, y=265,)

sp.mainloop()
