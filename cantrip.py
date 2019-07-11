# This will be the actual function app to track combat and skill challenges in DnD
import cantripfunctions as cf
import random
from tkinter import *
from tkinter.ttk import Notebook
# Test area here
window = Tk()
window.title("Cantrip: Making wizarding easier since 20 minutes in the future")
tab_control=Notebook(window)

tab1=Frame(tab_control)
tab_control.add(tab1,text='First')
tab_control.grid(row=0,column=3)

def click():
    entered_text=nameentry.get()

w = Label(window,text='Enter the stats for the creature you want to add:',bg='black',fg='white',)
w.grid(row=0,column=0,sticky=W)

nameentry=Entry(window,width=20,bg='white')
nameentry.grid(row=0,column=1,sticky=W)

submitname = Button(window,text="submit",width=6,command=click)
submitname.grid(row=0,column=2,sticky=W)


window.mainloop()


# Test area end