from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
from mysql.connector import connect

conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="prj")
print("DATABASE CONNECTION SUCCESSFUL")
mycursor = conn.cursor()

#Class for BOOKING APPOINTMENT   
class Appointment:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.emp_ID=StringVar()
        self.ap_time=StringVar()
        self.ap_date=StringVar()
        self.des=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR SPECIALTY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.emp_ID )
        self.lbldid.grid(row=1,column=1)

            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ap_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=0)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=1)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
        
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)
        
    #FUNCTION TO EXIT APPOINTMENT WINDOW
    def Exit(self):            
        self.master.destroy()
        
    #FUNCTION TO INSERT DATA IN APPOINTMENT FORM   
    def INSERT_AP(self):
        global e1,e2,e4,e5,e6,var
        e1=(self.pat_ID.get())
        e2=(self.emp_ID.get())
        e4=(self.ap_time.get())
        e5=(self.ap_date.get())
        e6=(self.des.get())
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234", 
        database="prj"
        )
        mycursor = conn.cursor()
        sql_check = "SELECT * FROM appointment WHERE PATIENT_ID = %s"
        mycursor.execute(sql_check, (e1,))
        result = mycursor.fetchone()
        if not result:
            mycursor.execute("Insert into appointment SET PATIENT_ID=%s,DOCTOR_SPECIALITY=%s,APPOINTMENT_TIME=%s,APPOINTMENT_DATE=%s,DESCRIPTION=%s",(e1,e2,e5+" "+e4,e5,e6,))


            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")

            conn.commit()
        else:
             
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "APPOINTMENT ALREADY EXISTS")     


    #FUNCTION TO OPEN DELETE APPOINTMENT DISPLAY WINDOW
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH APPOINTMENT DISPLAY WINDOW
    def S_AP_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           

#CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT   
class DEL_AP:
    def __init__(self,master):    
        global de1_ap,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN APPOINTMENT FORM      
    def DELETE_AP(self):        
        global inp_d,de1_ap
        inp_d = str(self.de1_ap.get())
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  # Replace with a secure way to store credentials
        database="prj"
        )
        mycursor = conn.cursor()
        sql_check = "SELECT * FROM appointment WHERE PATIENT_ID= %s"
        mycursor.execute(sql_check, (inp_d,))
        result = mycursor.fetchone()
        if not result:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")     
        else:
            mycursor.execute('DELETE FROM APPOINTMENT where PATIENT_ID=%s',(inp_d ,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
            conn.commit()
        
#CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class SEA_AP:

    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.entry=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_AP)
        self.SearchB.grid(row=0,column=1)
        

    #FUNCTION TO SEARCH DATA IN APPOINTMENT FORM   
    def SEARCH_AP(self):
        global inp_s,entry
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="prj"
        )
        mycursor = conn.cursor()
        inp_s=(self.entry.get())  
        sql_check = "SELECT * FROM appointment WHERE APPOINTMENT_DATE = %s"
        mycursor.execute(sql_check, (inp_s,))
        result = mycursor.fetchall()
        if not result:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","THERE'S NO APPOINTMENT BOOKED")
        else:
            mycursor.execute('SELECT * FROM appointment where APPOINTMENT_DATE=%s',(inp_s,))
            row = mycursor.fetchall()
            print(row)
            for i in row:
                
                self.window = tkinter.Toplevel()
                self.window.title(f"Appointment Details on {inp_s}")
                self.window.geometry("1000x700+0+0")
                self.window.config(bg="cadet blue")
                self.frame = Frame(self.master,bg="cadet blue")
                self.frame.pack()
                self.lbTitle = Label(self.window,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
                self.lbTitle.grid(row =0 ,column = 4,columnspan=2,pady=25)
                self.LoginFrame = Frame(self.window,width=100,height=0,relief="ridge",bg="cadet blue",bd=20)
                self.LoginFrame.grid(row=1,column=4,padx=150)


                self.l1 = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)     

                self.l2 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="APPOINTMENT DATE AND TIME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=3,column=0)
                self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis3.grid(row=3,column=1)

                self.l4 = Label(self.LoginFrame,text="DOCTOR SPECIALTY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=4,column=0)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis4.grid(row=4,column=1)
                        
                self.l5 = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l5.grid(row=5,column=0)
                self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
                self.dis5.grid(row=5,column=1)



            
