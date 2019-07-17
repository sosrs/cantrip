from tkinter import *
import tkinter.ttk as ttk
import re

# These are the custom functions I will use in my cantrip app
skillSet = {'Athletics','Acrobatics','Sleight of Hand','Stealth,','Arcana','History','Investigation','Nature',
            'Religion','Animal Handling','Insight','Medicine','Perception','Survival','Deception','Intimidation',
            'Performance','Persuasion'}
conditionSet = {'Blinded','Charmed','Deafened','Fatigued','Frightened','Grappled','Incapacitated','Invisible',
                'Paralyzed','Petrified','Poisoned','Prone','Restrained','Stunned','Unconscious','Exhaustion'}


def roll_die(num: int, die: int, bonus: int = 0)->int:

    # This function will make a standard XdY + Z roll and return it as an integer
    # Both the number of dice and the number of sides must be positive nonzero integers
    from random import randint
    total = 0
    for i in range(num):
        total += randint(1,die)
    return total + bonus


def evaluate_roll(inputstr:str):
    # This will take in a string of either an integer or a XdY roll and return the result as an integer
    try:
        return int(inputstr)
    except ValueError:
        try:
            outputlist = list(map(int,inputstr.split('d')))
        except ValueError:
            # todo: how to output this error to the window
            print("Is there a typo in your query? We couldn't evaluate this item:",inputstr)
            return 0
        output = roll_die(outputlist[0],outputlist[1])
        # print(inputstr,'=',output)
        return output


def master_roll(string: str):
    # This function will take in a single string expression of any number of XdY or integer components
    # and sum the total
    string = string.replace(' ', '')
    if string == '' or string== '\n':
        return ''
    # strip string of spaces, split the string on - or + but keep those items as entries in the list
    a = re.split("([-+])", string)
    for i in range(len(a)):
        if a[i] == '':
            a.remove('')

    def slave_roll(input: list):
        # this subfunction will take a string list of integers, XdY rolls, and + or - operations, and
        # evaluate the statement
        if len(input) == 0:
            return 0
        elif len(input) == 1 and (input[0] == '+' or input[0] == '-'):
            # hanging operators at the end will be assumed to add 0
            return 0
        elif len(input) == 1:
            # a single roll or integer string will be evaluated and returned. if another item is passed,
            # the evaluate function will throw an error
            return evaluate_roll(input[0])

        first = input.pop(0)
        if first == '+':
            return evaluate_roll(input.pop(0)) + slave_roll(input)
        if first == '-':
            return -evaluate_roll(input.pop(0)) + slave_roll(input)
        else:
            return evaluate_roll(first) + slave_roll(input)

    return (slave_roll(a))


def master_master_roll(string:str)->str:
    # this expression will take any number of dice summing expressions as a string, separated by commas, and return
    # their evaluations in the same order, separated by commas
    string2 = string.replace(' ', '')
    a = string2.split(',')
    for i in range(len(a)):
        a[i] = str(master_roll(a[i]))
    return ','.join(a)


def add_roller(parent):
    # this function will pack the basic roll widget to the frame this is called on
    # intended to be called when a new tab is created
    def roll_the_dice(x, y, z, outputWidget):
        total = roll_die(x, y, z)
        outputWidget.delete(0,END)
        outputWidget.insert(0, total)
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
    label1 = Button(rollWidget, text='I want to roll:', command=lambda:roll_the_dice(int(entry1.get()),int(entry2.get()),int(entry3.get()),entry4))

    rollWidget.pack()

    label1.pack(side='left',fill='y')
    entry1.pack(side='left',fill='y')
    label2.pack(side='left',fill='y')
    entry2.pack(side='left',fill='y')
    label3.pack(side='left',fill='y')
    entry3.pack(side='left',fill='y')
    label4.pack(side='left',fill='y')
    entry4.pack(side='left',fill='y')


def widgetFunc(inputList,outputWidget,func=sum):
    outputWidget.delete(0,END)
    outputWidget.insert(func(inputList))

class SkillWidget(Frame):
    def __init__(self,parent,skill):
        pass
    # This will create a composite widget which will hold


class Character:
    # This will create an instance of a character with their immutable characteristics (skills and stats)
    def __init__(self,name,STR,DEX,CON,INT,WIS,CHA):
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
print(re.split("([-+])",'1d4'.replace(' ','')))
print(master_roll(''))

