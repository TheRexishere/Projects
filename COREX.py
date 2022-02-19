from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


t=Tk()
t.title('COREX Portal')
t.geometry('600x300')
t.resizable(0,0)
t.configure(bg='cyan')

data=[]

def Datast():
    global data
    con=sqlite3.connect('DATA.db')
    cn=con.cursor()
    cn.execute("CREATE TABLE if not exists COREXDATA(Aadhar Number int,Name text,Vaccine Status text)") 
    cn.execute("SELECT * FROM COREXDATA")
    data=cn.fetchall()
    con.commit() 
    

def COREX():
    global data
    rt=Tk()
    rt.title('COREX Portal')
    rt.geometry('600x400')
    rt.resizable(0,0)
    
    rt.configure(bg='cyan')
    
    def Submitdat():
        y=(enad.get(),ennam.get(),envac.get())
        data.append(y)
        
        con=sqlite3.connect('DATA.db')
        cn=con.cursor()
        
        cn.execute('Delete From COREXDATA')
        for i in data:
            cn.execute('Insert into COREXDATA values(?,?,?)',i)
        messagebox.showinfo('Information','Data saved!!!')
        enad.delete(0,'end')
        ennam.delete(0,'end')
        envac.delete(0,'end')
        con.commit()
        

    Label(rt,text="PATIENT'S DETAILS",bg='cyan',font=("Arial Rounded MT Bold",35)).place(x=65,y=20)

    Label(rt,text="Aadhar Card Number",bg='cyan',font=("Arial Rounded MT Bold",15)).place(x=5,y=120)

    Label(rt,text="Name",bg='cyan',font=("Arial Rounded MT Bold",15)).place(x=5,y=180)

    Label(rt,text="Vaccine Status",bg='cyan',font=("Arial Rounded MT Bold",15)).place(x=5,y=240)

    enad=Entry(rt,width=22,font=("Arial Rounded MT Bold",14))
    enad.place(x=300,y=120)

    ennam=Entry(rt,width=22,font=("Arial Rounded MT Bold",14))
    ennam.place(x=300,y=180)

    envac=Entry(rt,width=22,font=("Arial Rounded MT Bold",14))
    envac.place(x=300,y=240)

    but= Button(rt,text='Submit',bg='cyan',relief='groove',font=("Arial Rounded MT Bold",14),command=Submitdat)
    but.place(x=475,y=325)

    rt.mainloop()
    
def Submitdat():
    con=sqlite3.connect('DATA.db')
    cn=con.cursor()
    
    cn.execute('Delete From COREXDATA')
    for i in data:
        cn.execute('Insert into COREXDATA values(?,?,?)',i)
        
    con.commit()
    
    
def Deletedat():
    global data
    data=[]
    con=sqlite3.connect('DATA.db')
    cn=con.cursor()
    
    cn.execute('Delete From COREXDATA')
    
    messagebox.showinfo("Information",'All Data Deleted!!!')
    con.commit()
    
    
def Showdat():
    Datast()
    rk=Tk()
    rk.title("COREX DATA")
    rk.geometry("650x350")
    rk.configure(bg='cyan')
    
    ttk.Style().configure('Treeview', background='cyan', fieldbackground='cyan')
    
    Label(rk,text="DATA",bg='cyan',font=("Arial Rounded MT Bold ",35,'underline')).place(x=250,y=5)

    tre=ttk.Treeview(rk,column=("c1","c2","c3"),show='headings')
    tre.heading("#1",text='Aadhar Card Number')
    tre.heading("#2",text='Name')
    tre.heading("#3",text='Vaccine Status')
    tre.place(x=25,y=75)


    for i in range(0,len(data)):
        tre.insert("",'end',values=(data[i][0],data[i][1],data[i][2]))
    
        
    rk.mainloop()    

def Display(c):
    a=name.get()
    b=pwd.get()
    if a=='Shivam Pandey':
        if b=='12345':
            if c==1:
                t.destroy()
                COREX()
            elif c==2:
                Showdat()
            else:
                Deletedat()
            
        else:
            messagebox.showinfo('Information','ACCESS DENIED!!!')
            name.delete(0,'end')
            pwd.delete(0,'end')
            #rk.destroy()
            
    else:
        messagebox.showinfo('Information','ACCESS DENIED!!!')
        name.delete(0,'end')
        pwd.delete(0,'end')
        #rk.destroy()
        
        
l= Label(t,text='Welcome to COREX Portal',bg='cyan',font=("Arial Rounded MT Bold",20))
l.place(x=135,y=30)

Name = Label(t,text = "Enter Username:",bg='cyan',font=("Arial Rounded MT Bold",15))
Name.place(x=5,y=100)

name = Entry(t,width=25,bg='floral white',font=("Arial Rounded MT Bold",15))
name.place(x=250,y=100)

pwd = Label(t,text = "Enter Password:",bg='cyan',font=("Arial Rounded MT Bold",15))
pwd.place(x=5,y=130)

pwd = Entry(t,width=25,bg='floral white',font=("Arial Rounded MT Bold",15),show='*')
pwd.place(x=250,y=130)

sm=Button(t,text='Enter',width=5,height=1,relief='groove',bg='cyan',font=("Arial Rounded MT Bold",17),command=lambda:Display(1))
sm.place(x=450,y=200)

sd=Button(t,text='Show Data',width=10,height=1,relief='groove',bg='cyan',font=("Arial Rounded MT Bold",17),command=lambda:Display(2))
sd.place(x=250,y=200)

dd=Button(t,text='Delete Data',width=10,height=1,relief='groove',bg='cyan',font=("Arial Rounded MT Bold",17),command=lambda:Display(3))
dd.place(x=50,y=200)

t.mainloop()
