from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import csv
from time import strftime
from datetime import datetime
import time
import cv2
import os
import numpy as np

class Face_Recognizer2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.last_recognition_time = 0
        self.cooldown_time = 30  # Adjust this value based on your requirements (in seconds)
        

        title_lbl = Label(self.root, text="Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #image to be changed according to aditya
        img_top = Image.open(r"F:\Face Recognition System\Images\bmw-m4-competition-mg-02.jpg")
        img_top = img_top.resize((1530,325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)
                         
        #button
        b1_1= Button(self.root,text ="Face_Recognition",command=self.face_recognize,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=600,y=380,width = 240,height=40)

           #=====================Attendance=====================
    def mark_attendance(self, r, n, d, check_out_time=None):
        now = datetime.now()
        d1 = now.strftime("%d_%m_%Y")
        current_time = now.strftime("%H:%M:%S")
        attendance_file = f"Attendance_{d1}.csv"

        # is_new_file = not os.path.exists(attendance_file)  ---> old code

        # with open(attendance_file, "a", newline="\n") as f:
        #     if is_new_file:
        #         f.write("SSN,Name,Department,CheckInTime,CheckOutTime,Date,Status\n")
        
        #     check_in_time = current_time
        #     if check_out_time:
        #         check_out_time = current_time

        #     f.writelines(f"{r},{n},{d},{check_in_time},{check_out_time},{d1},Present\n")
        
         # Read the existing data from the CSV file if it exists
        attendance_data = []
        if os.path.exists(attendance_file):
            with open(attendance_file, "r") as f:
                reader = csv.reader(f)
                attendance_data = list(reader)

        # if check_out_time:
        #     with open(attendance_file, "a", newline="\n") as f:
        #         f.writelines(f"\n{r},{n},{d},{current_time},{check_out_time},{d1},Present\n")
        # else:
        #     with open(attendance_file, "a", newline="\n") as f:
        #         f.writelines(f"\n{r},{n},{d},{current_time},null,{d1},Present\n")

        # Find the record corresponding to the current employee (based on SSN and date)
        found = False
        for record in attendance_data:
            if len(record) >= 6 and record[0] == r and record[5] == d1:
                found = True
                if check_out_time:
                    # Update the checkout time for the existing record
                    record[4] = check_out_time
                else:
                    # Use the existing login time for the record
                    current_time = record[3]
        
        if not found:
        # Create a new record if it doesn't exist
            new_record = [r, n, d, current_time, check_out_time or "NA", d1, "Present"]
            attendance_data.append(new_record)

        # Write the updated data back to the CSV file
        with open(attendance_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(attendance_data)

        # Split the line to extract the original login time
        # parts = lines[i].strip().split(',')
        # original_check_in_time = parts[3]

        # # Update the line with the checkout time
        # if check_out_time:
        #     lines[i] = f"{r},{n},{d},{original_check_in_time},{check_out_time},{d1},Present\n"
        # else:
        #     lines[i] = f"{r},{n},{d},{original_check_in_time},NA,{d1},Present\n"

        # # Write the updated data back to the CSV file
        # with open(attendance_file, "w", newline="\n") as f:
        #     f.writelines(lines)


    def face_recognize(self):
        cooldown_time = 30  # Adjust this value based on your requirements (in seconds)
        last_recognition_time = 0  
        def draw_boundary(img,classifier,scaleFactor,minimumneighbour,text_color,clf,current_time):
            #current_time=now.strftime("%H:%M:%S")  # Define current_time here
            nonlocal last_recognition_time
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minimumneighbour)
            coord = []
            response = None  # Define response variable here

            for(x,y,w,h) in features:
                current_time = datetime.now().strftime("%H:%M:%S")
                if time.time() - last_recognition_time >= cooldown_time:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                    confidence = int((100*(1-predict/300)))
                    conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("select Name from employee where SSN="+str(id))
                    n = my_cursor.fetchone()
                    #n = str(n) # Incase join function doesen't work use this
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
                    # Ask the user if they want to continue or check out, include the name in the prompt message
                        response = messagebox.askquestion("Check-Out", f" {n},Do you want to check out?", icon='warning')


                    # if response:
                    #     self.mark_attendance(r, n, d,current_time)
                    # # Close the OpenCV window
                    # cv2.destroyAllWindows()

                    if response == "yes":
                        self.mark_attendance(r, n, d, current_time)
                        self.last_recognition_time = time.time()
                        cv2.destroyAllWindows()  # Close the OpenCV window
                        return  # Exit the function
                    
            return coord             
                # if confidence>80:        #old code made some improvements
                #   cv2.putText(img,f"SSN:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #   self.mark_attendance(r,n,d)

            #     else:
            #       text_color = (255, 255, 255)
            #       font = cv2.FONT_HERSHEY_SIMPLEX  # Change the font to Hershey Simplex
            #       font_scale = 0.8
            #       font_thickness = 3
            #       cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            #       cv2.putText(img,f"Unknown",(x,y-5),font, font_scale, text_color, font_thickness)
            #       coord = [x,y,w,h]
            # return coord

        def recognize(img, clf, faceCascade):
            current_time = datetime.now().strftime("%H:%M:%S")  # Define current_time here
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), clf, current_time)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            key = cv2.waitKey(1)
            if key == 13:  # Press Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk() 
    obj=Face_Recognizer2(root)
    root.mainloop() 