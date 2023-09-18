from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class  Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System Trainer")
        
        title_lbl= Label(self.root,text="!<Train the System>!",font=("times new roman",35,"bold"),bg="black",fg="gold")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        img_top=Image.open(r"Images\facialrecognition.webp")
        img_top= img_top.resize((1535, 325), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1535,height=335)

        #Button
        b1_1 = Button(self.root,text ="*<!TRAIN!>*",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),borderwidth=5,highlightthickness=4,bg="black",fg="cyan")
        b1_1.place(x=1,y=378,width = 1535,height=60)

        img_bottom=Image.open(r"Images\facialrecognition.webp")
        img_bottom= img_bottom.resize((1535, 335), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1535,height=325)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #Gray scale image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split(".")[1].split(".")[0])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #====================Train the classifier and save===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        clf.save("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training the System has been completed!!")        


if __name__=="__main__":
    root=Tk() 
    obj=Train(root)
    root.mainloop() 