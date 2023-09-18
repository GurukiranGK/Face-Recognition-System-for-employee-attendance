from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import tkinter
import os
from employee import Employee
from train import Train
from face_recognizer import Face_Recognizer1
from attendance import Attendance
from developer import Developer
from Checkout import Face_Recognizer2

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
#first image
        img=Image.open(r"Images\background0.jpg")
        img= img.resize((500, 130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#2nd Image
        img1=Image.open(r"Images\background1.jpg")
        img1= img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#3rd Image
        img2=Image.open(r"Images\background2.jpg")
        img2= img2.resize((530, 130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

#Backgroung Image
        img3=Image.open(r"Images\background3.jpg")
        img3= img3.resize((1535, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img. place(x=0,y=130,width=1535,height=710)

#title
        title_lbl= Label(bg_img,text="Face Recognition System",font=("times new roman",34,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=45)

#=====================Time=========================
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

#Employee Details button
        img4=Image.open(r"Images\Emp1.png")
        img4= img4.resize((250, 250), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.employee_details,cursor="hand2")
        b1.place(x=200,y=100,width=240,height=240)

        b1_1 = Button(bg_img,text ="Employee Details",command=self.employee_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width = 240,height=40)

#Employee LogIn button
        img5=Image.open(r"Images\Emp1.png")
        img5= img5.resize((250, 250), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=240,height=240)

        b2_2=Button(bg_img,text="Employee LogIn",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_2.place(x=500,y=300,width=240,height=40)
        
#Employee Log out Details
        img7=Image.open(r"Images\EMP.jpg")
        img7= img7.resize((250, 250), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.checkout_data)
        b3.place(x=800,y=100,width=240,height=240)

        b3_3=Button(bg_img,text="Employee LogOut",cursor="hand2",command=self.checkout_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3_3.place(x=800,y=300,width=240,height=40)

# Employee Log Details
        img6=Image.open(r"Images\Emp1.png")
        img6= img6.resize((250, 250), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b4=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b4.place(x=1100,y=100,width=240,height=240)  

        b4_4=Button(bg_img,text="Employee Log Details",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_4.place(x=1100,y=300,width=240,height=40)

#Train the model
        img8=Image.open(r"Images\Emp1.png")
        img8= img8.resize((250, 250), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=200,y=370,width=240,height=240)

        b5_5=Button(bg_img,text="Train the model",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_5.place(x=200,y=570,width=240,height=40)

#Photos button
        img9=Image.open(r"Images\Emp1.png")
        img9= img9.resize((250, 250), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=370,width=240,height=240)

        b6_6=Button(bg_img,text="Photos and Updates",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6_6.place(x=500,y=570,width=240,height=40)

#Developers button
        img10=Image.open(r"Images\emp3.jpg")
        img10= img10.resize((250, 250), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=370,width=240,height=240)

        b7_7=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_7.place(x=800,y=570,width=240,height=40)

#Exit button
        img11=Image.open(r"Images\EMP.jpg")
        img11= img11.resize((250, 250), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Exits)
        b8.place(x=1100,y=370,width=240,height=240)

        b8_8=Button(bg_img,text="Exit",cursor="hand2",command=self.Exits,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b8_8.place(x=1100,y=570,width=240,height=40)

    def open_img(self):
        os.startfile("Data")

    def Exits(self):
        self.Exits=tkinter.messagebox.askyesno("Face Recognition System","Are you sure you want to exit this application!",parent=self.root)
        if self.Exits>0:
            self.root.destroy()
        else:
            return

#================Function Buttons=================
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognizer1(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def checkout_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognizer2(self.new_window)    

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()