# This will be the actual function app to track combat and skill challenges in DnD
import cantripfunctions as cf
from CantripClasses import *
import random
from tkinter import *
import tkinter.ttk as ttk


# Test area here
window = Tk()
window.title("Cantrip: Making wizarding easier since 20 minutes into the future")


# Create the tabs under the window
tab_control = ttk.Notebook(window)

# All tabs listed here
skillTab = SkillTab(tab_control)
importChar = Frame(tab_control,padx=100)
rollTab = Frame(tab_control)

tab_control.add(skillTab, text='Skill Rolls')
tab_control.add(importChar, text='Import a character')
tab_control.add(rollTab, text='Complex Rolls')
tab_control.pack(expand=1, fill='both')

# Skill tab
skillList= sorted(cf.SKILLDICT)
skillDict={}
header= Frame(skillTab,bd=1,relief=RIDGE,pady=2,)
nameheader = Label(header, text='Skill', justify=CENTER,width=12,)
nameheader.grid(row=0, column=0)
abilityheader= Label(header,text='Ability',width=4)
abilityheader.grid(row=0, column=1)


header.pack(anchor='w')

for skill in skillList:
    skillDict[skill] = SkillWidget(skillTab,skill)
    skillDict[skill].pack(anchor='w')


# Import a character Tab

def click():
    entered_text=nameentry.get()


w = Label(importChar,text='Enter the stats for the creature you want to add:',)
w.grid(row=1,column=0,sticky=W)

nameentry=Entry(importChar,width=20,bg='white')
nameentry.grid(row=1,column=1,sticky=W)

submitname = Button(importChar,text="submit",width=6,command=click)
submitname.grid(row=1,column=2,sticky=W)

# Complex Rolls tab
def show_roll():
    output = rollentry.get('1.0',END)
    rollout.delete(0, END)
    rollout.insert(0, cf.master_master_roll(output))


rollinstructions = Label(rollTab,text='Enter any number of rolls you want calculated! Separate them by commas. \n'
                                     'This handles addition or subtraction of integers or XdY rolls. '
                                     'No parentheses, or multiplication')
rollentry = Text(rollTab,bg='white', width=20,height=2,wrap=CHAR)
rollButton = Button(rollTab, text='Roll!', command = show_roll)
rollout = Entry(rollTab,bg='SystemButtonFace',bd=3)
rollentry.insert('1.0','1d20 + 1 - 1d6')
rollinstructions.pack()
rollentry.pack()
rollButton.pack()
rollout.pack()






window.mainloop()
# Test area end

# app builder functions
