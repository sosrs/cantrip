from tkinter import *
from CantripClasses import *
import tkinter.ttk as ttk
import re

# These are the custom functions and constants I will use in my cantrip app
TITLESET = ['Making wizarding easier since the spellplague.', 'Ray of frost IS a respectable spell!',
            "No, I don't think that's how \"Friends\" works.",
            'I would like to use Prestidigitation to Charm the king with hypnosis.']

SKILLSET = {'Athletics', 'Acrobatics', 'Sleight of Hand', 'Stealth', 'Arcana', 'History', 'Investigation', 'Nature',
            'Religion', 'Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival', 'Deception', 'Intimidation',
            'Performance', 'Persuasion'}

SKILLDICT = {'Athletics': 'Str', 'Acrobatics': 'Dex', 'Sleight of Hand': 'Dex', 'Stealth': 'Dex', 'Arcana': 'Int',
             'History': 'Int', 'Investigation': 'Int', 'Nature': 'Int', 'Religion': 'Int', 'Animal Handling': 'Wis',
             'Insight': 'Wis', 'Medicine': 'Wis', 'Perception': 'Wis', 'Survival': 'Wis', 'Deception': 'Cha',
             'Intimidation': 'Cha', 'Performance': 'Cha', 'Persuasion': 'Cha'}

CONDITIONSET = {'Blinded', 'Charmed', 'Deafened', 'Fatigued', 'Frightened', 'Grappled', 'Incapacitated', 'Invisible',
                'Paralyzed', 'Petrified', 'Poisoned', 'Prone', 'Restrained', 'Stunned', 'Unconscious', 'Exhaustion'}


def roll_die(num: int, die: int, bonus: int = 0, adv: str = 'none') -> int:
    # This function will make a standard XdY + Z roll and return it as an integer
    # Both the number of dice and the number of sides must be positive nonzero integers
    # The fourth argument notes if someone has advantage or disadvantage, and will calculate the roll appropriately.
    # Under this function, any die roll can have "advantage", not just d20 rolls.
    from random import randint
    total = 0
    for i in range(num):
        total += randint(1, die)
    total = total + bonus
    # print(num, 'd', die, '+', bonus, '=', total)
    if adv in ['advantage', 'a', 'adv', 'Advantage', 'A']:
        total = max(total, roll_die(num, die, bonus, 'n'))
    elif adv in ['disadvantage', 'd', 'disadv', 'dis', 'Disadvantage', 'D']:
        total = min(total, roll_die(num, die, bonus, 'n'))
    return total


def evaluate_roll(inputstr: str) -> int:
    # This will take in a string of either an integer or a XdY roll and return the result as an integer
    try:
        return int(inputstr)
    except ValueError:
        try:
            outputlist = list(map(int, inputstr.split('d')))
        except ValueError:
            # todo: how to output this error to the window
            print("Is there a typo in your query? We couldn't evaluate this item:", inputstr)
            return 0
        output = roll_die(outputlist[0], outputlist[1])
        # print(inputstr,'=',output)
        return output


def master_roll(string: str) -> str:
    # This function will take in a single string expression of any number of XdY or integer components
    # and sum the total
    string = string.replace(' ', '')
    if string == '' or string == '\n':
        return ''
    # strip string of spaces, split the string on - or + but keep those items as entries in the list
    a = re.split("([-+])", string)
    for i in range(len(a)):
        if a[i] == '':
            a.remove('')

    def slave_roll(input: list) -> int:
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

    return str(slave_roll(a))


def add_roller(parent, method='pack'):
    # this function will pack the basic roll widget to the frame this is called on
    # intended to be called when a new tab is created
    if method == 'pack':
        RollerWidget(parent).pack(fill='x')
    elif method == 'grid':
        RollerWidget(parent).grid(row=0, column=0)
