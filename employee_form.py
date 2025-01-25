from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
from mysql.connector import connect

conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="prj")
print("DATABASE CONNECTION SUCCESSFUL")
mycursor = conn.cursor()

#Class for EMPLOYEE REGISTRATION 
class Employee:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.emp_ID=IntVar()
        self.emp_name=StringVar()
        self.emp_sex=StringVar()
        self.emp_age=IntVar()
        self.emp_type=StringVar()
        self.emp_salary=IntVar()
        self.emp_email=StringVar()
        self.emp_contact=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblempid = Label(self.LoginFrame,text="EMPLOYEE ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempid.grid(row=0,column=0)
        self.lblempid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_ID)
        self.lblempid.grid(row=0,column=1)
        
        self.lblempname = Label(self.LoginFrame,text="EMPLOYEE NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempname.grid(row=1,column=0)
        self.lblempname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_name)
        self.lblempname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_sex)
        self.etype1.grid(row=2,column=1)
        

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="EMPLOYEE DESIGNATION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_salary)
        self.lblCon.grid(row=0,column=3)
        
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=1,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_contact)
        self.lbleid.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_email)
        self.lbleid.grid(row=2,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_EMP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=5)
        
        self.button7 = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SE_SEARCH)
        self.button7.grid(row=3,column=4)

        self.button8 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.UPDATE_PAT)
        self.button8.grid(row=3,column=3)
        
        

   #FUNCTION TO EXIT PATIENT FORM
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM
        
    def INSERT_EMP(self):
        global e1,e2,e3,e4,e5,e6,e8,e9,var
        e1=(self.emp_ID.get())
        e2=(self.emp_name.get())
        e3=(self.emp_sex.get())
        e4=(self.emp_age.get())
        e5=(self.emp_type.get())
        e6=(self.emp_salary.get())
        e8=(self.emp_email.get())
        e9=(self.emp_contact.get())
        cnt=0
        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  # Replace with a secure way to store credentials
        database="prj"
        )
        mycursor = conn.cursor()

            # Check for existing ID (optional, can be done in a separate query)
        sql_check = "SELECT * FROM employee WHERE EMPLOYEE_ID = %s"
        mycursor.execute(sql_check, (e1,))
        result = mycursor.fetchone()

        if not result:  # Insert only if ID doesn't exist
            sql = "INSERT INTO employee (EMPLOYEE_ID, NAME, SEX, AGE, DESIGNATION, SALARY, CONTACT, EMAIL) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
            val = (e1, e2, e3, e4, e5, e6, e9, e8)
            mycursor.execute(sql, val)
            conn.commit()
            print(mycursor.rowcount, "record inserted.")
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")
        conn.close()
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_EMP(self.newWindow)
    def SE_SEARCH(self):
        self.newWindow = Toplevel(self.master)
        self.app = SMenu(self.newWindow)
    def UPDATE_PAT(self):
        global de

        u1 = (self.emp_ID.get())
        u2 = (self.emp_name.get())
        u3 = (self.emp_sex.get())
        u4 = (self.emp_age.get())
        u5 = (self.emp_type.get())
        u6 = (self.emp_salary.get())
        u7 = (self.emp_email.get())
        u8 = (self.emp_contact.get())
      

        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="prj")
        mycursor = conn.cursor()
        de = int(self.emp_ID.get())
        sql_check = "SELECT * FROM employee WHERE EMPLOYEE_ID =%s"
        mycursor.execute(sql_check, (de,))
        p = mycursor.fetchone()
        conn.cursor()
        if p is not None:
            mycursor.execute('UPDATE EMPLOYEE SET NAME=%s,SEX=%s,AGE=%s,DESIGNATION=%s,SALARY=%s,EMAIL=%s,CONTACT=%s where EMPLOYEE_ID=%s', ( u2, u3, u4, u5, u6, u7, u8,u1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_EMP:
    def __init__(self,master):    
        global de1_emp,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_EMP)
        self.DeleteB.grid(row=3,column=1)
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=2)
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_EMP(self):        
        conn=mysql.connector.connect(host="localhost",
            user="root",
            password="1234",
            database="prj"
        )
        mycursor = conn.cursor()
        de = int(self.de1_emp.get())
        sql_check = "SELECT * FROM employee WHERE EMPLOYEE_ID =%s"
        mycursor.execute(sql_check, (de,))
        result = mycursor.fetchone()
        if not result:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        else:
            mycursor.execute("DELETE from employee where EMPLOYEE_ID=%s", (de,))
            conn.commit() 
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
        conn.close()
class SMenu:
    def __init__(self,master):    
        global se1_emp,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.se1_emp=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.se1_emp)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_PAT)
        self.SearchB.grid(row=0,column=1)
        
    def SEARCH_PAT(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="prj")
        mycursor = conn.cursor()
        de = int(self.se1_emp.get())
        sql_check = "SELECT * FROM employee WHERE EMPLOYEE_ID =%s"
        mycursor.execute(sql_check, (de,))
        print (sql_check)
        result = mycursor.fetchone()
        if not result:
            error = tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        else: 
            mycursor.execute('SELECT * FROM EMPLOYEE where EMPLOYEE_ID=%s',(de,))
            row = mycursor.fetchone()
            i = list(row)
            print(i)
            
            self.l1 = Label(self.LoginFrame,text="EMPLOYEE ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l1.grid(row=1,column=0)
            self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
            self.dis1.grid(row=1,column=1)
                        
            self.l2 = Label(self.LoginFrame,text="EMPLOYEE NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
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
                        
            self.l5 = Label(self.LoginFrame,text="DESIGNATION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l5.grid(row=5,column=0)
            self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[4])
            self.dis5.grid(row=5,column=1)
                        
            self.l6 = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l6.grid(row=1,column=2)
            self.dis6  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
            self.dis6.grid(row=1,column=3)
                        
            self.l7 = Label(self.LoginFrame,text=" CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l7.grid(row=2,column=2)
            self.dis7  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[6])
            self.dis7.grid(row=2,column=3)
                        
            self.l8 = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.l8.grid(row=3,column=2)
            self.dis8  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[7])
            self.dis8.grid(row=3,column=3)
        conn.close()
    