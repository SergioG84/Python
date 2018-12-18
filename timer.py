from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    # get the time remaining until event
    timeLeft = endTime - datetime.datetime.now()
    #remove microseconds
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    # show time left
    txt.set(timeLeft)
    #start countdown after 1000 ms
    root.after(1000,cant_wait)

#use tkinter for showing timer
root = Tk()
root.attributes("-fullscreen", FALSE)
root.configure(background = "black")
root.bind("x", quit)
root.after(1000,cant_wait)
#set time for timer to stop
endTime = datetime.datetime(2020, 5, 18, 0, 0)

fnt = font.Font(family = 'Helvetica', size = 60, weight = 'bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor = CENTER)

root.mainloop()

