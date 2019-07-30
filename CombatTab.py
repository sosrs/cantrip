import cantripfunctions as cf
import random
from tkinter import *
import tkinter.ttk as ttk
from tkinter import font

class EffectTracker(LabelFrame):
    # This class will be the container for all effects that need to be tracked during combat (e.g. spell buffs)
    def __init__(self,*args,**kwargs):
        LabelFrame.__init__(self, text='Combat Effects Tracker', *args, **kwargs)
        self.effectslist= []

        self.newEffect = Frame(self,relief=GROOVE,bd=2)
        self.newEffect.pack(fill='x')
        Label(self.newEffect,text='New Effect').grid(row=0,column=0)



class Effect(Frame):
    # This is a single effect object, which will be created and tracked by the Effect tracker
    def __init__(self,name,roundupdate=0,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)
