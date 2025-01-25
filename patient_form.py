from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
from mysql.connector import connect

conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="prj")
print("DATABASE CONNECTION SUCCESSFUL")
mycursor = conn.cursor()
                      
#Class for PATIENT REGISTRATION 
class Patient:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        self.pat_ID=IntVar()
        self.pat_name=StringVar()
        self.pat_AGE=IntVar()
        self.pat_address=StringVar()
        self.pat_sex=StringVar()
        self.pat_BG=StringVar()
        self.pat_contact=IntVar()
        self.pat_email=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "PATIENT REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpatid.grid(row=0,column=1)
        
        self.lblPatname = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPatname.grid(row=1,column=0)
        self.lblPatname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_name)
        self.lblPatname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.lblsex  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_sex)
        self.lblsex.grid(row=2,column=1)

        self.lblDOB = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblDOB.grid(row=3,column=0)
        self.lblDOB  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_AGE)
        self.lblDOB.grid(row=3,column=1)
        
        self.lblbgrp = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblbgrp.grid(row=0,column=2)
        self.lblbgrp  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_BG)
        self.lblbgrp.grid(row=0,column=3)
        
        self.lblCon = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=1,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contact)
        self.lblCon.grid(row=1,column=3)
        

        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_email)
        self.lbleid.grid(row=2,column=3)

        self.lbladd = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbladd.grid(row=3,column=2)
        self.lbladd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_address)
        self.lbladd.grid(row=3,column=3)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_PAT)
        self.button2.grid(row=5,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_PAT)
        self.button3.grid(row=5,column=2)
        
        self.button4 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.D_DISPLAY)
        self.button4.grid(row=5,column=3)
        
        self.button5 = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.S_DISPLAY)
        self.button5.grid(row=5,column=4)
    
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=5,column=5)
            

    #FUNCTION TO INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        global p1,p2,p3,p4,p5,p6,p8,p10,var
        p1=(self.pat_ID.get())
        p2=(self.pat_name.get())
        p3=(self.pat_sex.get())
        p4=(self.pat_AGE.get())
        p5=(self.pat_BG.get())
        p6=(self.pat_contact.get())
        p8=(self.pat_email.get())
        p10=(self.pat_address.get())
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234", 
        database="prj"
        )
        mycursor = conn.cursor()
        sql_check = "SELECT * FROM patient WHERE PATIENT_ID = %s"
        mycursor.execute(sql_check, (p1,))
        result = mycursor.fetchone()
        if not result:
            mycursor.execute('INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(p1,p2,p3,p4,p5,p6,p8,p10,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM","DETAILS INSERTED INTO DATABASE")
            conn.commit()
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT_ID ALREADY EXISTS")
        
    #FUNCTION TO UPDATE DATA IN PATIENT FORM

    def UPDATE_PAT(self):
        global de
        u1 = (self.pat_ID.get())
        u2 = (self.pat_name.get())
        u3 = (self.pat_sex.get())
        u4 = (self.pat_AGE.get())
        u5 = (self.pat_BG.get())
        u6 = (self.pat_contact.get())
        u7 = (self.pat_email.get())
        u8 = (self.pat_address.get())
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="prj"
        )
        mycursor = conn.cursor()
        de = int(self.pat_ID.get())
        sql_check = "SELECT * FROM PATIENT WHERE PATIENT_ID =%s"
        mycursor.execute(sql_check, (de,))
        p = mycursor.fetchone()
        conn.cursor()
        if p is not None:
            mycursor.execute('UPDATE PATIENT SET NAME=%s,SEX=%s,AGE=%s,BLOOD_GROUP=%s,CONTACT_NUMBER=%s,EMAIL=%s,ADDRESS=%s where PATIENT_ID=%s', ( u2, u3, u4, u5, u6, u7, u8,u1))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")
            
    #FUNCTION TO EXIT PATIENT REGISTRATION WINDOW
    def Exit(self):            
        self.master.destroy()

    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH PATIENT DISPLAY WINDOW
    def S_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SMenu(self.newWindow)

#CLASS FOR DISPLAY MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self,master):    
        global inp_d,entry1,DeleteB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.del_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "DELETE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.del_pid)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_PAT)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN PATIENT FORM
    def DELETE_PAT(self):        
        global inp_d,del_pid
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="prj"
        )
        mycursor = conn.cursor()
        inp_d = (self.del_pid.get())
        sql_check = "SELECT * FROM PATIENT WHERE PATIENT_ID =%s"
        mycursor.execute(sql_check, (inp_d,))
        result = mycursor.fetchone()
        if not result:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
        else:
            mycursor.execute('DELETE FROM PATIENT where PATIENT_ID=%s',(inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS DELETED FROM DATABASE")
            conn.commit()

#CLASS FOR SEARCH MENU FOR SEARCH PATIENT
class SMenu:
    def __init__(self,master):    
        global inp_s,s_pid,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.s_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.s_pid)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_PAT)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def SEARCH_PAT(self):
        global inp_s,s_pid
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="prj"
        )
        mycursor = conn.cursor()
        inp_s=(self.s_pid.get())  
        sql_check = "SELECT * FROM patient WHERE PATIENT_ID =%s"
        mycursor.execute(sql_check, (inp_s,))
        print (sql_check)
        result = mycursor.fetchone()
        if not result:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT DATA DOESN'T EXIST")
        else: 
            mycursor.execute('SELECT * FROM PATIENT where PATIENT_ID=%s',(inp_s,))
            row = mycursor.fetchone()
            i = list(row)
            print(i)
            self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
            self.dis1.grid(row=1,column=1)
            
            self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l2.grid(row=2,column=0)
            self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
            self.dis2.grid(row=2,column=1)

            self.l3 = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l3.grid(row=3,column=0)
            self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
            self.dis3.grid(row=3,column=1)

            self.l4 = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l4.grid(row=4,column=0)
            self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
            self.dis4.grid(row=4,column=1)
            
            self.l5 = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l5.grid(row=5,column=0)
            self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[4])
            self.dis5.grid(row=5,column=1)
            
            self.l6 = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l6.grid(row=1,column=2)
            self.dis6  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
            self.dis6.grid(row=1,column=3)
            
            self.l8 = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l8.grid(row=3,column=2)
            self.dis8  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[6])
            self.dis8.grid(row=3,column=3)

            self.l10 = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l10.grid(row=5,column=2)
            self.dis10 = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[7])
            self.dis10.grid(row=5,column=3)
    

