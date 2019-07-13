# This will be the actual function app to track combat and skill challenges in DnD
import cantripfunctions as cf
import random
from tkinter import *
from tkinter.ttk import Notebook
# Test area here
window = Tk()
window.title("Cantrip: Making wizarding easier since 20 minutes into the future")

def add_roller(parent):
    # this function will pack the basic roll widget to the frame this is called on
    # intended to be called when a new tab is created

    rollWidget= LabelFrame(parent,text='Roll some dice!')

    entry1 = Entry(rollWidget,width=2,bg='white',)
    entry1.insert(0, '1')
    label2 = Label(rollWidget,text='d')
    entry2 = Entry(rollWidget,width=4,bg='white')
    entry2.insert(0, '20')
    label3 = Label(rollWidget,text='+')
    entry3 = Entry(rollWidget,width=2,bg='white')
    entry3.insert(0, '0')
    label4 = Label(rollWidget,text='   Results: ')
    entry4 = Entry(rollWidget,width=5,bg='SystemButtonFace',bd=3)
    def roll_the_dice(x,y,z):
        total=cf.roll(x,y,z)
        entry4.insert(0,total)

    label1 = Button(rollWidget, text='I want to roll:', command=roll_the_dice(int(entry1.get()),int(entry2.get()),int(entry3.get())))

    rollWidget.pack()

    label1.pack(side='left',fill='y')
    entry1.pack(side='left',fill='y')
    label2.pack(side='left',fill='y')
    entry2.pack(side='left',fill='y')
    label3.pack(side='left',fill='y')
    entry3.pack(side='left',fill='y')
    label4.pack(side='left',fill='y')
    entry4.pack(side='left',fill='y')





#Create the tabs under the window
tab_control=Notebook(window)
#All tabs listed here
skillTab = Frame(tab_control)
addTab = Frame(tab_control,padx=100)

tab_control.add(skillTab,text='Skill Rolls')
tab_control.add(addTab,text='Import a character')
tab_control.pack(expand=1,fill='both')

def click():
    entered_text=nameentry.get()

# Skill tab
add_roller(skillTab)
# Import a character Tab

w = Label(addTab,text='Enter the stats for the creature you want to add:',)
w.grid(row=1,column=0,sticky=W)

nameentry=Entry(addTab,width=20,bg='white')
nameentry.grid(row=1,column=1,sticky=W)

submitname = Button(addTab,text="submit",width=6,command=click)
submitname.grid(row=1,column=2,sticky=W)


window.mainloop()
# Test area end

# app builder functions
