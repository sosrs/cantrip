# this contains all the widget classes I created for this application

import cantripfunctions as cf
import random
from tkinter import *
import tkinter.ttk as ttk

class SkillTab(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
        cf.add_roller(self)


class RollerWidget(LabelFrame):
    def __init__(self,parent):
        LabelFrame.__init__(self,parent,text='Roll a die!')
        self.label1 = Button(self, text='I want to roll:', command=self.roll_the_die)
        self.entry1 = Entry(self,width=2,bg='white')
        self.entry1.insert(0, '1')
        self.label2 = Label(self, text='d')
        self.entry2 = Entry(self, width=4, bg='white')
        self.entry2.insert(0, '20')
        self.label3 = Label(self, text='+')
        self.entry3 = Entry(self, width=2, bg='white')
        self.entry3.insert(0, '0')
        self.label4 = Label(self, text='   Results: ')
        self.entry4 = Entry(self, width=5, bg='SystemButtonFace', bd=3)

    def roll_the_die(self):
        total = cf.roll_die(int(self.entry1.get()), int(self.entry2.get()), int(self.entry3.get()))
        self.entry4.delete(0, END)
        self.entry4.insert(0, total)

    def pack(self,*args,**kwargs):
        self.label1.pack(side='left', fill='y',padx=5)
        self.entry1.pack(side='left', fill='y')
        self.label2.pack(side='left', fill='y')
        self.entry2.pack(side='left', fill='y')
        self.label3.pack(side='left', fill='y')
        self.entry3.pack(side='left', fill='y')
        self.label4.pack(side='left', fill='y')
        self.entry4.pack(side='left', fill='y')
        super().pack(*args,**kwargs)


class SkillWidget(Frame):
    def __init__(self, parent, skill: str,modifier:int = 0):
        Frame.__init__(self, parent,bd=1,relief=RIDGE,pady=2,)
        self.name = Label(self, text=skill, justify=CENTER,width=12)
        self.name.grid(row=0, column=0)
        self.ability= Label(self,text=cf.SKILLDICT[skill],width=4)
        self.ability.grid(row=0, column=1)
        self.abilitybonus=Label(self,text='Modifier: ')
        self.abilitybonus.grid(row=0,column=2)
        self.bonus = Entry(self,width=3,bg='white',justify=CENTER)
        self.bonus.insert(0,modifier)
        self.bonus.grid(row=0,column=3)
        Label(self,text='Proficient?:').grid(row=0,column=4)
        self.proficient = False
        # todo:currently all checkbuttons are linked tot he same variable and are checked all at once
        self.prof = Checkbutton(self,text='Proficient?',variable=self.proficient,onvalue=True,offvalue=False)
        self.prof.grid(row=0,column=5)


    # This will create a composite widget which will hold


class Character:
    # This will create an instance of a character with their immutable characteristics (skills and stats)
    def __init__(self, name, STR, DEX, CON, INT, WIS, CHA):
        self.name = name
        self.status = []
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.skillProf = set()
        self.condition = set()

#class CharCombat:
    # This will take in a Character, and create a representation of them for combat (tracking mutable characteristics
    # like current HP and status effects)