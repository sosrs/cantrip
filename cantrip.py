# This will be the actual function app to track combat and skill challenges in DnD
import cantripfunctions as cf
from CantripClasses import *
import random
from tkinter import *
import tkinter.ttk as ttk

# todo: once the structure of the app is finalized, I should put that into its own class
# Test area here
window = Tk()
window.title("Cantrip: " + random.choice(cf.TITLESET))

# Create the tabs under the window
tab_control = ttk.Notebook(window)

# All tabs listed here
skillTab = SkillTab(tab_control)
importChar = Frame(tab_control, padx=100)
rollTab = ComplexRollsTab(tab_control)

tab_control.add(skillTab, text='Skill Rolls')
tab_control.add(importChar, text='Import a character')
tab_control.add(rollTab, text='Complex Rolls')
tab_control.pack(expand=1, fill='both')


# Import a character Tab

def click():
    entered_text = nameentry.get()


w = Label(importChar, text='Enter the stats for the creature you want to add:', )
w.grid(row=1, column=0, sticky=W)

nameentry = Entry(importChar, width=20, bg='white')
nameentry.grid(row=1, column=1, sticky=W)

submitname = Button(importChar, text="submit", width=6, command=click)
submitname.grid(row=1, column=2, sticky=W)

window.mainloop()
# Test area end
