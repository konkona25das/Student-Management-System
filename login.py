from tkinter import*
from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk, messagebox
from datetime import*
from math import*
import sqlite3
import os

class LoginClass:
    def __init__(self, root):
        self.root= root
        self.root.title("Login Window")
        self.root.geometry("1300x500+90+190")
        self.root.config(bg= "darkblue")
                   
        #=======Frames==========
        login_frame= Frame(self.root, bg= "white")
        login_frame.place(x=250, y=50, width=850, height=600)
        title= Label(login_frame, text='LOGIN HERE', font=("times new roman",30, "bold"), bg= "white", fg= "#08A3D2").place(x=250, y=50)
        
        email= Label(login_frame, text='EMAIL ADDRESS', font=("times new roman",15, "bold"), bg= "white", fg= "gray").place(x=250, y=150)
        self.txt_email= Entry(login_frame, font=("times new roman",15), bg= "lightgray")
        self.txt_email.place(x=250, y=180, width= 350, height=35)

        pass_= Label(login_frame, text='PASSWRORD', font=("times new roman",15, "bold"), bg= "white", fg= "gray").place(x=250, y=250)
        self.txt_pass_= Entry(login_frame, font=("times new roman",15), bg= "lightgray")
        self.txt_pass_.place(x=250, y=280, width= 280, height=35)

        btn_reg= Button(login_frame, text= "Register New Account",cursor="hand2", font=("times new roman", 20), bg= "white", bd= 2, fg= "#B00857", command= self.register_window).place(x=150, y=360 )
        btn_forget= Button(login_frame,cursor="hand2", text= "Forgot password", font=("times new roman", 20), bg= "white", bd= 2, fg= "#B00857", command= self.forget_pass_window).place(x=450, y=360)

        btn_login= Button(login_frame, text= "LOGIN", font=("times new roman", 20, "bold"), fg= "white",bg= "#B00857", cursor="hand2", command= self.login).place(x=250, y=450, width= 150, height=40)

    def forget_pass_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter correct email")
        else: 
            try:
                con= sqlite3.connect(database="rms.db")                
                cur=con.cursor()
                cur.execute("Select * from employee where email=?", (self.txt_email.get(),))
                row=cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "please enter valid email")
                else:
                    con.close()
                    self.root2= Toplevel()
                    self.root2.geometry("400x450+500+200")
                    self.root2.title("Forget password")
                    self.root2.config(bg= "white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t= Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold")).place(x=50, y=50)

    #========Forget password======
                    question= Label(self.root2, text="Security question", font=("times new roman",15)).place(x=50, y=100)
                    self.cmb_ques=ttk.Combobox(self.root2, font=("times new roman", 13), state= 'readonly')
                    self.cmb_ques['values']=("Select",  "your first pet name","Your birth place", "Your best friend name")
                    self.cmb_ques.place(x=50, y=130, width=250)
                    self.cmb_ques.current(0)

                    answer= Label(self.root2, text="answer", font=('times new roman', 15, 'bold')).place(x=50, y=170)
                    self.txt_answer= Entry(self.root2, font=("times new roman", 15), bg= 'lightgray')
                    self.txt_answer.place(x=50, y=200, width=250)

                    new_password= Label(self.root2, text="New Password", font=('times new roman')).place(x=50, y=260)
                    self.txt_new_pass= Entry(self.root2, font=('times new roman', 15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)
        
        else:
            con= sqlite3.connect(database="rms.db")                
            cur=con.cursor()
            cur.execute("Select * from employee where email=? and password=?", (self.txt_email.get(),self.txt_pass_.get(),))
            row=cur.fetchone()
            if row== None:
                messagebox.showerror("Error", "Invalid Username and Password", parent= self.root)

            else:
                messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}", parent= self.root)
                self.root.destroy()
                os.system("python dashboard.py")

            con.close()

    def reset(self):
        self.cmb_ques.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass_.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        if self.cmb_ques.get()=="Select":
            messagebox.showerror("Error", "All fields are required", parent= self.root)
        elif self.txt_answer.get()=="":
            messagebox.showerror("Error", "Please enter the answer")
        else:
            try:
                con= sqlite3.connect(database="rms.db")                
                cur=con.cursor()
                cur.execute("Select * from employee where email=?", (self.txt_email.get(),))
                row=cur.fetchone()
                if row== None:
                    messagebox.showerror("Error", "Please enter correct security question", parent= self.root)
                
                else:
                    cur.execute("update employee set password= ? where email=?",(self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

root= Tk()
obj= LoginClass(root)
root.mainloop()