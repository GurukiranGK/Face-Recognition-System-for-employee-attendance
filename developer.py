from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl= Label(self.root,text="!<Developers>!",font=("times new roman",35,"bold"),bg="black",fg="gold")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        img_top=Image.open(r"F:\Face Recognition System\Images\Dev_bg.jpg")
        img_top= img_top.resize((1535, 800), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1535,height=800)

        Frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=1000,y=0,width=580,height=800)

        #img_top1=Image.open(r"Images\facialrecognition.webp")
        #img_top1= img_top1.resize((200, 200), Image.LANCZOS)
        #self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        #f_lbl=Label(main_frame,image=self.photoimg_top1)
        #f_lbl.place(x=300,y=45,width=200,height=200)

        #Developer information
        dep_label=Label(main_frame,text="You have entered the domain of  The Akatsuki !!",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=5)

        dep_label=Label(main_frame,text="We are the Developers of this system,",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=45)

        dep_label=Label(main_frame,text="We are THE Interns from DLithe,",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=85)
        dep_label=Label(main_frame,text="The AIML Division!",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=125)
        dep_label=Label(main_frame,text="We are the Cognitive CodeWarriors!",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=165)
        dep_label=Label(main_frame,text="Aditya.Y.Kesarkar",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=205)
        dep_label=Label(main_frame,text="Gurukiran B",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=245)
        dep_label=Label(main_frame,text="Harsha M S",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=285)
        dep_label=Label(main_frame,text="Kishan Navali",font=("times new roman",18,"bold"),bg="black",fg="cyan")
        dep_label.place(x=0,y=325)

        img2=Image.open(r"F:\Face Recognition System\Images\Dev_bg.jpg")    #photo should be added by Aditya(jpg)
        img2= img2.resize((500, 300))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=300)





if __name__=="__main__":
    root=Tk() 
    obj=Developer(root)
    root.mainloop()



