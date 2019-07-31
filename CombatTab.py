import cantripfunctions as cf
import random
from tkinter import *
import tkinter.ttk as ttk
from tkinter import font

class EffectTracker(LabelFrame):
    # This class will be the container for all effects that need to be tracked during combat (e.g. spell buffs)
    def __init__(self,*args,**kwargs):
        LabelFrame.__init__(self, text='Combat Effects Tracker',labelanchor='n', *args, **kwargs)
        self.effectslist= []

        self.newEffect = LabelFrame(self,bd=2,text='New Effect')
        self.newEffect.pack(expand=True,fill=X,anchor='n')

        Label(self.newEffect,text='Source: ').grid(row=0,column=0)
        Label(self.newEffect,text='Effect: ').grid(row=1,column=0)
        self.sourceEntry= Entry(self.newEffect,bg='white',)
        self.effectEntry= Text(self.newEffect,bg='white',height=3,width=20)
        self.sourceEntry.grid(row=0,column=1)
        self.effectEntry.grid(row=1,column=1)

        self.createEffect= Button(self.newEffect,text='Create Effect')
        self.createEffect.grid(row=3,column=0,columnspan=2)



class Effect(Frame):
    # This is a single effect object, which will be created and tracked by the Effect tracker
    def __init__(self,name,roundupdate=0,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)

class Scrollable(Frame):
    def __init__(self,root):
        Frame.__init__(self, root)
        self.canvas = Canvas(root,borderwidth=0,background='#ffffff')
        self.frame = Frame(self.canvas,background='#ffffff')
        self.vsb = Scrollbar(root,orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side='right',fill='y')
        self.canvas.pack(side='left',fill='both',expand=True)
        self.canvas.create_window((4,4),window=self.frame,anchor='nw',tags='self.frame')

        self.frame.bind('<Configure>',self.onFrameConfigure)

        self.populate()

    def populate(self):
        pass
        '''for row in range(100):
            cf.RollerWidget(self.frame).pack()
            Label(self.frame, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t = "this is the second column for row %s" % row
            Label(self.frame, text=t).grid(row=row, column=1)'''

    def onFrameConfigure(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))