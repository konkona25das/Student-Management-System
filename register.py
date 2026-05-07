from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
#import pymysql 
import sqlite3
import os
class RegisterClass:
    def __init__(self, root):
        self.root= root
        self.root.title("Registration Window")
        self.root.geometry("1300x500+90+190")
        self.root.config(bg= "white")

        #======Bg Image=====
        self.bg= ImageTk.PhotoImage(file="images/bg2.jpg")
        bg= Label(self.root, image= self.bg).place(x= 250, y=0, relwidth=1, relheight=1)

        #======Register Frame======
        frame1= Frame(self.root, bg= "white")
        frame1.place(x= 480, y= 30, width=700, height=500)

        title= Label(frame1, text="REGISTER HERE", font= ("times new roman", 20, "bold"), bg="white", fg= "green").place(x=50, y=20)

        #=================Row1
        f_name= Label(frame1, text= "First Name", font=("times new roman", 15, "bold"), bg= "white", fg= "gray"). place(x=50, y=90)
        self.txt_fname= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_fname.place(x=50, y=120, width= 250)

        l_name= Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=90)
        self.txt_lname= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_lname.place(x=370, y=120, width= 250)

        #======Row2=======

        contact= Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=160)
        self.txt_contact= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_contact.place(x=50, y=190, width= 250)

        email= Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=160)
        self.txt_email= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_email.place(x=370, y=190, width= 250)

        #======Row3========
        question= Label(frame1, text="Security question", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=230)
        self.cmb_quest= ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify= CENTER)
        self.cmb_quest['values']= ("Select", "your first pet name","Your birth place", "Your best friend name")
        self.cmb_quest.place(x=50, y=260, width= 250)
        self.cmb_quest.current(0)

        answer= Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=230)
        self.txt_answer= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_answer.place(x=370, y=260, width= 250)

        password= Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=300)
        self.txt_password= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_password.place(x=50, y=330, width= 250)

        cpassword= Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=300)
        self.txt_cpassword= Entry(frame1, font=("times new roman", 15), bg= "lightgray")
        self.txt_cpassword.place(x=370, y=330, width= 250)

        #========Terms=========
        self.var_chk= IntVar()
        chk=Checkbutton(frame1, text= 'I agree the terms and Conditions',variable=self.var_chk, onvalue=1, offvalue=0, bg= "white", font=("times new roman", 12)). place(x=50, y= 380)
        self.btn= Button(frame1, text= "Register Now",bd=0, cursor="hand2", command= self.register_data, font=("times new roman", 15)).place(x=50,y=420)
        btn_login= Button(frame1, text= "Sign In",command= self.login_window, font= ("times new roman", 20), bd=0, cursor='hand2').place(x=250, y=460)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)

        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and confirm password should be same", parent= self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please agree to the Terms and Conditions", parent= self.root)
        
        else:
            try:
                con= sqlite3.connect(database="rms.db")                
                cur=con.cursor()
                cur.execute("Select * from employee where email=?", (self.txt_email.get(),))
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error", "User already exists")

                else:
                    cur.execute("insert into employee(f_name, l_name, contact, email, question, answer, password) values(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(),
                                 self.txt_password.get()
                                 ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent= self.root)
                    self.clear()
                    self.login_window()
                    
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")


root= Tk()
obj= RegisterClass(root)
root.mainloop()