from tkinter import *
import tkinter as tk

a=str()

rt=Tk()

rt.title("CALCULATOR")

rt.geometry("345x350")
rt.resizable(0,0)

rt.configure(bg='blue')

strg= StringVar()

entry= Entry(rt,width='18',font=('Arial black',20),bd=10,textvariable=strg,fg='blue',bg='light grey',relief='sunken')
entry.place(x=7,y=20)

def enterData(b):
    global a
    a=a+b
    strg.set(a)    
    
def Equlto():
    global a
    try:
        a=eval(a)
        a = str(a)
    except:
        a = ""
    strg.set(a)
    
def clear():
    global a
    entry.delete(0,'end')
    a=''
    

but1= Button(rt,text="1",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('1'),relief='groove')
but1.place(x=5,y=100)

but2= Button(rt,text="2",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('2'),relief='groove')
but2.place(x=5,y=160)

but3= Button(rt,text="3",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('3'),relief='groove')
but3.place(x=5,y=220)

but0= Button(rt,text="0",fg='black',width='14',height='2',bd=7,bg='red',command=lambda:enterData('0'),relief='groove')
but0.place(x=5,y=280)

#Next Column

but4= Button(rt,text="4",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('4'),relief='groove')
but4.place(x=68,y=100)

but5= Button(rt,text="5",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('5'),relief='groove')
but5.place(x=68,y=160)

but6= Button(rt,text="6",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('6'),relief='groove')
but6.place(x=68,y=220)

#Next Column

but7= Button(rt,text="7",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('7'),relief='groove')
but7.place(x=131,y=100)

but8= Button(rt,text="8",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('8'),relief='groove')
but8.place(x=131,y=160)

but9= Button(rt,text="9",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('9'),relief='groove')
but9.place(x=131,y=220)

butDOT= Button(rt,text=".",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('.'),relief='groove')
butDOT.place(x=131,y=280)

#Next Column

butADD= Button(rt,text="+",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('+'),relief='groove')
butADD.place(x=194,y=100)

butSUB= Button(rt,text="-",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('-'),relief='groove')
butSUB.place(x=194,y=160)

butMUL= Button(rt,text="*",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('*'),relief='groove')
butMUL.place(x=194,y=220)

butDIV= Button(rt,text="/",fg='black',width='5',height='2',bd=7,bg='red',command=lambda:enterData('/'),relief='groove')
butDIV.place(x=194,y=280)

#Next Column

butAC= Button(rt,text="AC",fg='black',width='5',height='2',bd=7,bg='red',command=clear,relief='groove')
butAC.place(x=257,y=100)

butEQ= Button(rt,text="=",fg='black',width='5',height='9',bd=7,bg='red',command=Equlto,relief='groove')
butEQ.place(x=257,y=160)

rt.mainloop()