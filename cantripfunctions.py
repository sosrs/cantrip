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
        outputlist = list(map(int,inputstr.split('d')))
        output = roll_die(outputlist[0],outputlist[1])
        print(inputstr,'=',output)
        return output


def master_roll(string:str)-> int:
    # This function will take in a string of any number of XdY or integer components and sum the total
    if string=='':
        return ''
    a=re.split("([-+])",string.replace(' ',''))
    if a[0]=='':
        a.remove('')
    def slave_roll(input:list):
        if len(input) == 0:
            return 0
        elif len(input) == 1 and (input[0]== '+' or input[0]== '-'):
            return 0
        elif len(input) == 1:
            return evaluate_roll(input[0])

        first = input.pop(0)
        if first == '+':
            return evaluate_roll(input.pop(0)) + slave_roll(input)
        if first == '-':
            return -evaluate_roll(input.pop(0))+slave_roll(input)
        else:
            return evaluate_roll(first)+slave_roll(input)
    return(slave_roll(a))


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
class Char:
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

print(re.split("([-+])",'1d4'.replace(' ','')))
print(master_roll('1d4'))
