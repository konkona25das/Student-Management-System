from tkinter import*
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
class reportClass:
    def __init__(self, root):
        self.root= root
        self.root.title("Student Result Management System")
        self.root.geometry("1300x500+90+190")
        self.root.config(bg= "white")
        self.root.focus_force()
        #====title====
        title= Label(self.root, text= "View student results", font=("goudy old style",20, "bold"), bg= "orange",fg="#262626").place(x=10, y=15,width=1275, height= 65)

    #=======Search=====
        self.var_search= StringVar()
        self.var_id=""
        lbl_search= Label(self.root, text= "Search by roll number", font=("goudy old style", 20, "bold"),bg="white").place(x= 250, y=100)
        txt_search= Entry(self.root, textvariable= self.var_search, font=("goudy old style", 20, "bold"),bg="lightyellow").place(x= 520, y=100, width= 150)
        btn_search= Button(self.root, text="Search", font=("goudy old style", 20, "bold"), bg= "#03a9f4", fg= "white", cursor="hand2", command= self.search).place(x=680,y= 100, width= 100, height=35)
        btn_clear= Button(self.root, text="Clear", font=("goudy old style", 20, "bold"), bg= "gray", fg= "white", cursor="hand2", commaand= self.clear).place(x=800,y= 100, width= 100, height=28)
 
        #======Labels=====
        lbl_roll= Label(self.root, text= "Roll Number", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 150, y=230, width=150, height= 50)
        lbl_name=Label(self.root, text= "Name", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 300, y=230, width= 150, height=50)
        lbl_course= Label(self.root, text= "Course", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 450, y=230, width= 150, height= 50)
        lbl_marks_ob= Label(self.root, text= "Marks obtained", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 600, y=230, width= 150, height= 50)
        lbl_full= Label(self.root, text= "Total Marks", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 750, y=230, width= 150, height= 50)
        lbl_per= Label(self.root, text= "Percentage", font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE).place(x= 900, y=230, width= 150, height= 50)

        self.roll= Label(self.root,font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.roll.place(x= 150, y=280, width=150, height= 50)
        self.name=Label(self.root, font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.name.place(x= 300, y=280, width= 150, height=50)
        self.course= Label(self.root, font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.course.place(x= 450, y=280, width= 150, height= 50)
        self.marks_ob= Label(self.root, font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.marks.place(x= 600, y=280, width= 150, height= 50)
        self.full= Label(self.root, font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.full.place(x= 750, y=280, width= 150, height= 50)
        self.per= Label(self.root, font=("goudy old style", 20, "bold"),bg="white", bd=2, relief= GROOVE)
        self.per.place(x= 900, y=280, width= 150, height= 50)

        #========Delete Button =========
        btn_delete= Button(self.root, text="Delete", font=("goudy old style", 20, "bold"), bg= "red", fg= "white", cursor="hand2", command= self.delete).place(x=500,y= 350, width= 100, height=35)
        #=================================
    def search(self):
        con= sqlite3.connect(database="rms.db")
        cur= con.cursor()
        try:
                if self.var.search.get()=="":
                     messagebox.showerror("Error", "Roll No. should be required", parent= self.root)
                else:
                    cur.execute(f"select * from result where roll=?", (self.var_search.get(),))
                    row=cur.fetchone()
                    
                    if row!= None:
                        self.var_id= row[0]
                        self.roll.config(text=row[0])
                        self.name.config(text=row[1])
                        self.course.config(text=row[2])
                        self.marks.config(text=row[3])
                        self.full.config(text=row[4])
                        self.per.config(text=row[5])
                    else:
                        messagebox.showerror("Error", "No record found")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
         self.var_id=""
         self.roll.config(text="")
         self.name.config(text="")
         self.course.config(text="")
         self.marks.config(text="")
         self.full.config(text="")
         self.per.config(text="")

    def delete(self):
        con= sqlite3.connect(database="rms.db")
        cur= con.cursor()
        try:
            if self.var_id== "":
                messagebox.showerror("Error","Search Student result first",parent= self.root)
            else:
                cur.execute("select * from result where rid=?", (self.var_id.get(),))
                row=cur.fetchone()
                if row== None:
                    messagebox.showerror("Error","Invalid Student Result",parent= self.root)
                else:
                    op= messagebox.askyesno("Confirm", "Do you really want to delete?", parent= self.root)
                    if op== True:
                        cur.execute("delete from result where rid=?,"(self.var.id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result deleted successfully", parent= self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
         

if __name__=="__main__":
    root= Tk()
    obj= reportClass(root)
    root.mainloop()