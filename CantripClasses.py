# this contains all the widget classes I created for this application

import cantripfunctions as cf
import random
from tkinter import *
import tkinter.ttk as ttk


class SkillTab(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        cf.add_roller(self)
        self.skillDict = {}
        self.header = Frame(self, bd=1, relief=RIDGE, pady=2, )
        self.nameheader = Label(self.header, text='Skill', justify=CENTER, width=14)
        self.nameheader.grid(row=0, column=0)

        ttk.Separator(self.header, orient=VERTICAL).grid(column=1, row=0, sticky='ns')

        self.abilityheader = Label(self.header, text='Ability', width=4)
        self.abilityheader.grid(row=0, column=2)

        ttk.Separator(self.header, orient=VERTICAL).grid(column=3, row=0, sticky='ns')

        self.modheader = Label(self.header, text='Ability\nModifier', )
        self.modheader.grid(row=0, column=4, )

        ttk.Separator(self.header, orient=VERTICAL).grid(column=5, row=0, sticky='ns')

        self.profheader = Frame(self.header)
        self.proflabel = Label(self.profheader, text='Proficiency bonus')
        self.proflabel.pack()
        self.profentry = Entry(self.profheader, width=3, bg='white', justify=CENTER)
        self.profentry.insert(0, '0')
        self.profentry.pack()
        self.profheader.grid(row=0, column=6)

        self.header.pack(anchor='w')
        for skill in sorted(cf.SKILLDICT):
            self.skillDict[skill] = SkillWidget(self, skill)
            self.skillDict[skill].pack(anchor='w')

    def get_proficiency_bonus(self):
        return self.profentry.get()


class SkillWidget(Frame):
    def __init__(self, parent, skill: str, modifier: int = 0):
        Frame.__init__(self, parent, bd=1, relief=RIDGE, pady=2, )
        self.name = Label(self, text=skill, justify=CENTER, width=14)
        self.name.grid(row=0, column=0)

        ttk.Separator(self, orient=VERTICAL).grid(column=1, row=0, sticky='ns')

        self.ability = Label(self, text=cf.SKILLDICT[skill], width=4)
        self.ability.grid(row=0, column=2)

        ttk.Separator(self, orient=VERTICAL).grid(column=3, row=0, sticky='ns')

        self.bonus = Entry(self, width=3, bg='white', justify=CENTER)
        self.bonus.insert(0, modifier)
        self.bonus.grid(row=0, column=4, )
        self.grid_columnconfigure(2, )

        ttk.Separator(self, orient=VERTICAL).grid(column=5, row=0, sticky='ns')

        # Label(self,text='Proficient?:').grid(row=0,column=4)
        self.proficient = BooleanVar()
        self.prof = Checkbutton(self, text='Proficient?', variable=self.proficient, justify=CENTER)
        self.prof.grid(row=0, column=6)

        self.rollbutton = Button(self, text='Roll:', command=self.roll_the_die)
        self.rollbutton.grid(row=0, column=7)

        self.result = Entry(self, width=3, bg='SystemButtonFace', justify=CENTER)
        self.result.grid(row=0, column=8)

    def roll_the_die(self):
        bonus = int(self.bonus.get())
        if self.proficient.get() and self.master.get_proficiency_bonus() != '':
            bonus = bonus + int(self.master.get_proficiency_bonus())
        self.result.delete(0, END)
        self.result.insert(0, cf.roll_die(1, 20, bonus))

    # This will create a composite widget which will hold


class RollerWidget(LabelFrame):
    def __init__(self, parent):
        LabelFrame.__init__(self, parent, text='Roll a die!')
        self.mode = StringVar()
        self.mode.set('normal')

        self.label1 = Button(self, text='I want to roll:', command=self.roll_the_die)

        self.entry1 = Entry(self, width=2, bg='white')
        self.entry1.insert(0, '1')
        self.label2 = Label(self, text='d')
        self.entry2 = Entry(self, width=4, bg='white')
        self.entry2.insert(0, '20')
        self.label3 = Label(self, text='+')
        self.entry3 = Entry(self, width=4, bg='white')
        self.entry3.insert(0, '0')

        self.nor_radio = Radiobutton(self, variable=self.mode, value='normal', text='Normal')
        self.adv_radio = Radiobutton(self, variable=self.mode, value='advantage', text='Advantage')
        self.dis_radio = Radiobutton(self, variable=self.mode, value='disadvantage', text='Disadvantage')

        self.label4 = Label(self, text='   Results: ')
        self.entry4 = Entry(self, width=5, bg='SystemButtonFace', bd=3)

    def roll_the_die(self):
        total = cf.roll_die(int(self.entry1.get()), int(self.entry2.get()), int(self.entry3.get()), self.mode.get())
        self.entry4.delete(0, END)
        self.entry4.insert(0, total)

    def pack(self, *args, **kwargs):
        # Possible functionality: add an additional argument that will pack all of the widgets vertically instead of
        # horizontally
        self.label1.pack(side='left', fill='y', padx=5)
        self.entry1.pack(side='left', fill='y')
        self.label2.pack(side='left', fill='y')
        self.entry2.pack(side='left', fill='y')
        self.label3.pack(side='left', fill='y')
        self.entry3.pack(side='left', fill='y')

        self.nor_radio.pack(side='left', fill='y')
        self.adv_radio.pack(side='left', fill='y')
        self.dis_radio.pack(side='left', fill='y')

        self.label4.pack(side='left', fill='y')
        self.entry4.pack(side='left', fill='y')
        super().pack(*args, **kwargs)


class ComplexRollsTab(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.rollinstructions = Label(self,
                                      text='Enter any number of rolls you want calculated! Separate them by commas. \n'
                                           'This handles addition or subtraction of integers or XdY rolls. '
                                           'No parentheses or multiplication')
        self.rollentry = Text(self, bg='white', width=20, height=2, wrap=CHAR)
        self.rollButton = Button(self, text='Roll!', command=self.show_roll)
        self.rollout = Entry(self, bg='SystemButtonFace', bd=3)
        self.rollentry.insert('1.0', '1d20 - 1 - 1d4, 1d6 + 3')
        self.rollinstructions.pack()
        self.rollentry.pack()
        self.rollButton.pack()
        self.rollout.pack()

    def show_roll(self):
        # This method will take any number of dice summing expressions as a string, separated by commas, and return
        # their evaluations in the same order, separated by commas by running the master_roll function on it
        output = self.rollentry.get('1.0', END)
        self.rollout.delete(0, END)
        string2 = output.replace(' ', '')
        a = string2.split(',')
        for i in range(len(a)):
            a[i] = str(cf.master_roll(a[i]))
        self.rollout.insert(0, ','.join(a))


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

# class CharCombat:
# This will take in a Character, and create a representation of them for combat (tracking mutable characteristics
# like current HP and status effects)
