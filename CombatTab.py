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
        self.roundupdate = BooleanVar()

        self.newEffect = LabelFrame(self,bd=2,text='New Effect')
        self.sourceEntry= Entry(self.newEffect,bg='white',)
        self.effectEntry= Text(self.newEffect,bg='white',height=3,width=40)
        self.container=Frame(self.newEffect)
        self.createEffect= Button(self.container,text='Create Effect',command= self.save_effect)
        self.roundupdatebutton= Checkbutton(self.container,text='Increment every round',variable=self.roundupdate)

        self.newEffect.grid(row=0,column=0,sticky='we')#,expand=True,fill=X,side='top',anchor='n')
        Label(self.newEffect,text='Name: ').grid(row=0,column=0)
        Label(self.newEffect,text='Effect: ').grid(row=1,column=0)
        self.sourceEntry.grid(row=0,column=1,sticky='we')
        self.effectEntry.grid(row=1,column=1,sticky='we')
        self.createEffect.pack(side='left')
        self.roundupdatebutton.pack(side='left')
        self.container.grid(row=3,column=0,columnspan=2)

        self.scrollframe=Frame(self,relief=GROOVE,bd=4)
        self.scrollframe.grid(row=1,column=0,sticky=E+W+N+S)#,anchor='n',side='top')
        self.grid_rowconfigure(1,weight=1)
        self.scrolls= Scrollable(self.scrollframe)

    def save_effect(self):
        #todo: finish this

        self.effectslist.append(Effect(self,self.sourceEntry.get(),self.effectEntry.get('1.0', END),
                                       self.roundupdate.get()))


class Effect(LabelFrame):
    # This is a single effect object, which will be created and tracked by the Effect tracker
    def __init__(self,name, effect, roundupdate=0,*args,**kwargs):
        #todo: finish this
        Frame.__init__(self, text= name,*args,**kwargs)
        self.roundupdate= roundupdate
        self.effect=effect


class Scrollable(Frame):
    def __init__(self,root):
        self.canvas = Canvas(root,borderwidth=0,background='white')
        Frame.__init__(self, self.canvas,background='#ffffff',bd=2)
        #self.frame = Frame(self.canvas,background='#ffffff')
        self.vsb = Scrollbar(root,orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side='right',fill='y')
        self.canvas.pack(side='left',fill='both',expand=True)
        self.canvas.create_window((4,4),window=self,anchor='nw',tags='self.frame')

        self.bind('<Configure>',self.onFrameConfigure)

        # pack or grid widgets to self.frame
        self.populate()

    def populate(self):

        for row in range(3):
            # filler while i create the proper effect widget
            cf.RollerWidget(self).pack()
            '''Label(self, text="%s" % row, width=3, borderwidth="1",
                     relief="solid").grid(row=row, column=0)
            t = "this is the second column for row %s" % row
            Label(self, text=t).grid(row=row, column=1)'''

    def onFrameConfigure(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))