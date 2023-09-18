from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import time
import cv2
import os
import numpy as np

class Face_Recognizer1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Recognization",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #image to be changed according to aditya
        img_top = Image.open(r"F:\Face Recognition System\Images\bmw-m4-competition-mg-02.jpg")
        img_top = img_top.resize((1530,325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
                         
        #button
        b1_1= Button(self.root,text ="face_recognition",command=self.face_recognize,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=600,y=380,width = 240,height=40)

           #=====================Attendance=====================
    def mark_attendance(self,r,n,d):
          #  with open("Attendance.csv","r+",newline="\n") as f:  this all old code
          #     myDataList=f.readlines()
          #     name_list=[]
          #     for line in myDataList:
          #          entry=line.split((","))
          #          name_list.append(entry[0])
        now=datetime.now()
        d1=now.strftime("%d_%m_%Y")                 #dtString=now.strftime("%H:%M:%S") these 2 lines are old code lines for taking attendance any time
        current_time=now.strftime("%H:%M:%S")        #f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")                  
    #time frame for attendance      
        start_time="00:00:00"      # Start of the attendance time frame                                     
        end_time="24:00:00"        # End of the attendance time frame
        attendance_file=f"Attendance_{d1}.csv"

        if start_time <= current_time <= end_time:
            #attendance_file = f"Attendance_{d1}.csv"
            if not os.path.exists(attendance_file):
                                                    #with open("Attendance.csv","r+",newline="\n") as f:    #old line of code for using the file for storing attendance
                                                    #myDataList=f.readlines()
                                                    #name_list=[]
                with open(attendance_file, "w", newline="\n") as f:               #if is_new_file:
                    f.write("SSN,Name,Department,LogIn Time,LogOut Time,Date,Status\n")  # Write header if it's a new file
            with open(attendance_file, "r", newline="\n") as f:
                myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((r not in name_list) and (n not in name_list) and (d not in name_list)):
                dtString = now.strftime("%H:%M:%S")
                with open(attendance_file, "a", newline="\n") as f:
                    f.writelines(f"\n{r},{n},{d},{dtString},NA,{d1},Present")

    def face_recognize(self):
          
          def draw_boundary(img,classifier,scaleFactor,minimumneighbour,text_color,clf):
              gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
              features = classifier.detectMultiScale(gray_image,scaleFactor,minimumneighbour)
              coord = []

              for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from employee where SSN="+str(id))
                n = my_cursor.fetchone()
                #n = str(n)
                #print # Incase join function doesen't work use this
                n="+".join(n)

                my_cursor.execute("select Department from employee where SSN="+str(id))
                d = my_cursor.fetchone()
                #d = str(d) # Incase join function doesen't work use this
                d="+".join(d)

                my_cursor = conn.cursor()
                my_cursor.execute("select SSN from employee where SSN="+str(id))
                r = my_cursor.fetchone()
                #r = str(r) # Incase join function doesen't work use this
                r="+".join(r)
            
                if confidence > 80:
                    text_color = (255, 255, 255)
                    # Define font parameters
                    font = cv2.FONT_HERSHEY_SIMPLEX  # Change the font to Hershey Simplex
                    font_scale = 0.8
                    font_thickness = 3

                    cv2.putText(img, f"SSN: {r}", (x, y - 75), font, font_scale, text_color, font_thickness)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), font, font_scale, text_color, font_thickness)
                    cv2.putText(img, f"Department: {d}", (x, y - 30), font, font_scale, text_color, font_thickness)
                    self.mark_attendance(r, n, d)

                # if confidence>80:        #old code made some improvements
                #   cv2.putText(img,f"SSN:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   self.mark_attendance(r,n,d)

                else:
                  text_color = (255, 255, 255)
                  font = cv2.FONT_HERSHEY_SIMPLEX  # Change the font to Hershey Simplex
                  font_scale = 0.8
                  font_thickness = 3
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                  cv2.putText(img,f"Unknown",(x,y-5),font, font_scale, text_color, font_thickness)
                  coord = [x,y,w,h]
              return coord

          def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),clf)
            return img
          faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
          clf= cv2.face.LBPHFaceRecognizer_create()
          clf.read("classifier.xml")
          video_cap = cv2.VideoCapture(0)

          while True:
             ret,img = video_cap.read()
             img = recognize(img,clf,faceCascade)
             cv2.imshow("Welcome to face Recognition",img)

             if cv2.waitKey(1) == 13:
                break
          video_cap.release()
          cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk() 
    obj=Face_Recognizer1(root)
    root.mainloop() 