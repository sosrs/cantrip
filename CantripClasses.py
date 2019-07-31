# this contains all the widget classes I created for this application

import cantripfunctions as cf
import random
from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
from CombatTab import *


class Cantrip(Tk):
    # Main application class
    def __init__(self):
        Tk.__init__(self)
        self.characterdict = dict()

        self.title("Cantrip: " + random.choice(cf.TITLESET))
        self.tab_control = ttk.Notebook(self)

        # All tabs listed here
        self.skillTab = SkillTab(self.tab_control)
        self.importChar = ImportTab(self.tab_control, padx=100)
        self.rollTab = ComplexRollsTab(self.tab_control)
        self.combatTab = CombatTab(self.tab_control)

        # Tabs added below
        self.tab_control.add(self.skillTab, text='Skill Rolls')
        self.tab_control.add(self.importChar, text='Import a character')
        self.tab_control.add(self.combatTab, text='Combat Tracker')
        self.tab_control.add(self.rollTab, text='Complex Rolls')
        self.tab_control.pack(expand=1, fill='both')


class SkillTab(Frame):
    # This class will organize the tab for the skill check roller.
    # This includes all of the skill roll widgets, and a dropdown menu that will select the character rolling
    # todo: Implement the character selector
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
    # This self contained widget will list a single skill and allow you to roll checks for it
    def __init__(self, parent, skill: str, modifier: int = 0):
        self.optionfont = font.Font(family='Segoe UI', size=8)
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

        self.mode = StringVar()
        self.mode.set('normal')
        self.nor_radio = Radiobutton(self, variable=self.mode, value='normal', text='Normal', font=self.optionfont)
        self.adv_radio = Radiobutton(self, variable=self.mode, value='advantage', text='Advantage',
                                     font=self.optionfont)
        self.dis_radio = Radiobutton(self, variable=self.mode, value='disadvantage', text='Disadvantage',
                                     font=self.optionfont)
        self.nor_radio.grid(row=0, column=7)
        self.adv_radio.grid(row=0, column=8)
        self.dis_radio.grid(row=0, column=9)

        self.rollbutton = Button(self, text='Roll:', command=self.roll_the_die)
        self.rollbutton.grid(row=0, column=10)

        self.result = Entry(self, width=3, bg='SystemButtonFace', justify=CENTER)
        self.result.grid(row=0, column=11)

    def roll_the_die(self):
        bonus = int(self.bonus.get())
        if self.proficient.get() and self.master.get_proficiency_bonus() != '':
            bonus = bonus + int(self.master.get_proficiency_bonus())
        self.result.delete(0, END)
        self.result.insert(0, cf.roll_die(1, 20, bonus, self.mode.get()))


class ComplexRollsTab(Frame):
    # This widget contains a more advanced roll parser
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


class ImportTab(Frame):
    # this tab will allow you to add a character or monster to the database, which can then be selected in the skill
    # roller or further loaded into the combat tracker
    # todo: remaining stats to allow entering: AC, initiative, general notes
    # todo: create the save as new function
    # todo: allow loading of an existing character to edit, and overwrite function
    # todo: create the import from text option
    # todo: create the export from text option
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        cf.add_roller(self)
        Label(self, text='Import a character or monster! Fill out the form!', font=(15)).pack()

        self.form = Frame(self)  # this is the parent frame that will contain the entire character form
        self.form.pack()

        # A character needs a name
        # todo: create a button that will auto populate this with "monster1" or some such
        self.namelabel = Label(self.form, text='Name:')
        self.name = Entry(self.form, bg='white', width=40)
        self.namelabel.grid(row=0, column=0)
        self.name.grid(row=0, column=1)

        # Set up the block that will take in the ability modifiers for each stat
        self.statblock = LabelFrame(self.form, text='Ability Modifiers')  # Parent frame for the statblock
        self.statblock.grid(row=1, column=0, sticky='n')

        self.stats = {}  # dictionary of all the entries for each stat; this is what will be referenced to retrieve them
        self.statsframe = {}  # dictionary of all the frames that has the variable and the label

        statcount = 0
        for stat in ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']:
            self.statsframe[stat] = Frame(self.statblock)
            self.statsframe[stat].grid(row=statcount, column=0)
            Label(self.statsframe[stat], text=stat, width=4).grid(row=0, column=0)
            self.stats[stat] = Entry(self.statsframe[stat], bg='white', width=5)
            self.stats[stat].insert(0, '0')
            self.stats[stat].grid(row=0, column=1)
            statcount += 1

        # Set up the skills so you can select what each character is proficient in
        self.skillblock = LabelFrame(self.form, text='Proficient Skills')  # Container Frame
        self.skillblock.grid(row=1, column=1)
        Label(self.skillblock, text='Proficiency Bonus: ').grid(row=0, column=0)

        self.skillvars = {}  # The boolean variable dictionary for each skill
        self.skills = {}  # the actual Checkbutton widget for each skill

        self.profbonus = Entry(self.skillblock, bg='white', width=5)  # the bonus this character earns with proficiency
        self.profbonus.insert(0, '0')
        self.profbonus.grid(row=0, column=1)

        statcount = 0
        for skill in sorted(cf.SKILLDICT):
            self.skillvars[skill] = BooleanVar()
            self.skills[skill] = Checkbutton(self.skillblock, text=skill, variable=self.skillvars[skill])
            self.skills[skill].grid(row=(statcount % 9) + 1, column=statcount // 9, sticky='w')
            statcount += 1
        del statcount

        # save buttons
        self.final_buttons = Frame(self)
        self.final_buttons.pack()

        # todo: Load old character option here?
        self.save_new = Button(self.final_buttons, text='Save New Character', command=self.save_as_new)
        self.save_old = Button(self.final_buttons, text='Save Selected Character', command=self.save_as_existing)
        self.delete_char = Button(self.final_buttons, text='Delete Selected Character', command=self.del_selected)
        self.reset_fields = Button(self.final_buttons, text='Reset Fields', command=self.reset_to_default)
        self.save_new.pack(side='left')
        self.save_old.pack(side='left')
        self.delete_char.pack(side='left')
        self.reset_fields.pack(side='left')

    def save_as_new(self):
        pass

    def save_as_existing(self):
        pass

    def del_selected(self):
        pass

    def reset_to_default(self):
        self.name.delete(0, END)
        self.profbonus.delete(0, END)
        self.profbonus.insert(0, '0')
        for stat in self.stats:
            self.stats[stat].delete(0, END)
            self.stats[stat].insert(0, '0')
        for skill in self.skillvars:
            self.skillvars[skill].set(0)

    def import_file(self):
        pass

    def export_file(self):
        pass


class CombatTab(Frame):
    # this is the combat tracker tab
    # todo: create the entire tab...
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        cf.add_roller(self)

        self.effects = EffectTracker(self,width=200)
        self.effects.pack(side='right',fill=Y,expand=True)

        self.test=LabelFrame(self,text='Initiative',width=300)
        self.test.pack(side='top',fill=Y,expand=True)
        #self.test2=Scrollable(self.effects)



class RollerWidget(LabelFrame):
    # This self contained widget adds a basic dice roller to a widget
    def __init__(self, parent):
        self.optionfont = font.Font(family='Segoe UI', size=8)
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

        self.nor_radio = Radiobutton(self, variable=self.mode, value='normal', text='Normal', font=self.optionfont)
        self.adv_radio = Radiobutton(self, variable=self.mode, value='advantage', text='Advantage',
                                     font=self.optionfont)
        self.dis_radio = Radiobutton(self, variable=self.mode, value='disadvantage', text='Disadvantage',
                                     font=self.optionfont)

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


class Character:
    # This will create an instance of a character with their immutable characteristics (skills and stats)
    # todo: create the functions to edit and/or reference the stats
    def __init__(self, name, Str=0, Dex=0, Con=0, Int=0, Wis=0, Cha=0, prof=set(), profbonus=0):
        self.name = name
        self.status = []
        self.Str = Str
        self.Dex = Dex
        self.Con = Con
        self.Int = Int
        self.Wis = Wis
        self.Cha = Cha
        self.skillProf = prof.intersection(cf.SKILLSET)


class CharCombat:
    # This will take in a Character, and create a representation of them for combat (tracking mutable characteristics
    # like current HP and status effects)
    def __init__(self, character):
        self.condition = set()

