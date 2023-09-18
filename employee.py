from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ===================Variables=================
        self.var_SSN=StringVar()
        self.var_Name=StringVar()
        self.var_Department=StringVar()
        self.var_Joined_Date=StringVar()
        self.var_Experience=StringVar()
        self.var_Shift=StringVar()
        self.var_Supervisor=StringVar()
        self.var_DOB=StringVar()
        self.var_Address=StringVar()
        self.var_Email=StringVar()
        self.var_Phone_No=StringVar()
        self.var_Gender=StringVar()
        self.var_Dependent=StringVar()

        # Attributes for search functionality
        self.var_Search_by = StringVar()
        self.var_Search_txt = StringVar()
        

#Here add Employee images
# first image 
        img=Image.open(r"F:\Face Recognition System\Images\background0.jpg")
        img= img.resize((500, 130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
#2nd Image
        img1=Image.open(r"F:\Face Recognition System\Images\background1.jpg")
        img1= img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
#3rd Image
        img2=Image.open(r"F:\Face Recognition System\Images\background2.jpg")
        img2= img2.resize((530, 130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

#Backgroung Image
        img3=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img3= img3.resize((1535, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img. place(x=0,y=130,width=1535,height=710)

#title
        title_lbl= Label(bg_img,text="Employee Management System",font=("times new roman",32,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=650)

#left label frame
        Left_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=625)

        img_left=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img_left= img_left.resize((680, 130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=680,height=130)
#Current course
        current_course_frame=LabelFrame(Left_frame,bd=5,bg="white",relief=RIDGE,text="Current Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=745,height=150)
#Department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("  Select Department  ","Marketing","H.R","Project Management","Testing","Finance")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#Experience
        dep_label=Label(current_course_frame,text="Experience level",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=2,padx=50,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Experience,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("  Select level  ","Intern","Trainee","Fresher","Permanent Employee","Senior Employee")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=20,sticky=W)

#Joined date
        dep_label=Label(current_course_frame,text="Joined Date",font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Joined_Date,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("  Select Year  ","2018","2019","2020","2021","2022","2023")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#shift details
        shift_label=Label(current_course_frame,text="Shift Details",font=("times new roman",12,"bold"))
        shift_label.grid(row=1,column=2,padx=50,sticky=W)

        shift_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Shift,font=("times new roman",12,"bold"),state="readonly")
        shift_combo["values"]=("  Select Shift  ","Day","Night")
        shift_combo.current(0)
        shift_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#Employee Information
        employee_Information_frame=LabelFrame(Left_frame,bd=5,bg="white",relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        employee_Information_frame.place(x=5,y=285,width=745,height=310)

#Employee id
        ssn_label=Label(employee_Information_frame,text="Employee id",font=("times new roman",12,"bold"))
        ssn_label.grid(row=0,column=0,padx=10,sticky=W)

        ssn_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_SSN,font=("times new roman",12,"bold"))
        ssn_entry.grid(row=0,column=1,padx=10,sticky=W)

#Employee Name
        EmployeeName_label=Label(employee_Information_frame,text="Employee Name",font=("times new roman",12,"bold"))
        EmployeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        EmployeeName_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Name,font=("times new roman",12,"bold"))
        EmployeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
 
 #Employee Department
        EmployeeDepartment_label=Label(employee_Information_frame,text="Employee Department",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Department,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Employee email
        EmployeeDepartment_label=Label(employee_Information_frame,text="Email address:",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Email,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#Employee phone no
        EmployeeDepartment_label=Label(employee_Information_frame,text="Phone No:",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Phone_No,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#Employee Address
        EmployeeDepartment_label=Label(employee_Information_frame,text="Address",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Address,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#Employee DOB
        EmployeeDepartment_label=Label(employee_Information_frame,text="DOB",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_DOB,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#Employee Supervisor
        EmployeeDepartment_label=Label(employee_Information_frame,text="Supervisor",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Supervisor,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

#Employee Gender
        EmployeeDepartment_label=Label(employee_Information_frame,text="Gender",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=3,column=2,padx=10,sticky=W)

        
        gender_combo=ttk.Combobox(employee_Information_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),state="readonly",width=18)#width is given to change the size of drop down box
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Employee Dependent
        EmployeeDepartment_label=Label(employee_Information_frame,text="Dependent",font=("times new roman",12,"bold"))
        EmployeeDepartment_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        EmployeeDepartment_entry=ttk.Entry(employee_Information_frame,width=20,textvariable=self.var_Dependent,font=("times new roman",12,"bold"))
        EmployeeDepartment_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

#radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(employee_Information_frame,variable=self.var_radio1,text="Take Sample Photos",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(employee_Information_frame,variable=self.var_radio1,text="No Sample Photos",value="No")
        radiobtn2.grid(row=6,column=1)

#Buttons Frame
        btn_frame=Frame(employee_Information_frame,bd=5,relief=RIDGE,bg="white")
        btn_frame.place(x=6,y=204,width=727,height=32)

        savebtn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        savebtn.grid(row=0,column=0)

        updatebtn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatebtn.grid(row=0,column=1)

        deletebtn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        deletebtn.grid(row=0,column=2)

        resetbtn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        resetbtn.grid(row=0,column=3)

        btn_frame1=Frame(employee_Information_frame,bd=5,relief=RIDGE,bg="white")
        btn_frame1.place(x=6,y=244,width=727,height=32)

        takephoto_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takephoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo",width=39,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=1)


#right label frames
        Right_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=790,y=12,width=692,height=625)

        img_right=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img_right= img_right.resize((690, 130), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=690,height=130)

       #=========Search System===========

        search_frame=LabelFrame(Right_frame,bd=5,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=675,height=90)

        #Label
        search_label=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_Search_by,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","SSN","Name","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
       
        search_entry=ttk.Entry(search_frame,textvariable=self.var_Search_txt,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #buttons
        search_btn=Button(search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showall_btn=Button(search_frame,text="Show all",command=self.show_all_data,width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=3)

        #==============table frame============
        table_frame=Frame(Right_frame,bd=5,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=675,height=375)
        
        #===========scroll bars===============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("SSN","Name","Department","Joined Date","Experience","Shift","Supervisor","DOB","Address","Email","Phone No","Gender","Dependent","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


        self.employee_table.heading("SSN",text="SSN")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("Department",text="Department")
        self.employee_table.heading("Joined Date",text="Joined Date")
        self.employee_table.heading("Experience",text="Experience")
        self.employee_table.heading("Shift",text="Shift")
        self.employee_table.heading("Supervisor",text="Supervisor")
        self.employee_table.heading("DOB",text="DOB")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("Email",text="Email")
        self.employee_table.heading("Phone No",text="Phone No")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("Dependent",text="Dependent")
        self.employee_table.heading("photo",text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

        #Setting common width
        self.employee_table.column("SSN",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Department",width=100)
        self.employee_table.column("Joined Date",width=100)
        self.employee_table.column("Experience",width=100)
        self.employee_table.column("Shift",width=100)
        self.employee_table.column("Supervisor",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("Address",width=100)
        self.employee_table.column("Email",width=100)
        self.employee_table.column("Phone No",width=100)
        self.employee_table.column("Gender",width=100)
        self.employee_table.column("Dependent",width=100)
        self.employee_table.column("photo",width=150)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#=================Function declaration==================
    def add_data(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get()=="" or self.var_SSN.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_SSN.get(),
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Department.get(),
                                                                                                        self.var_Joined_Date.get(),
                                                                                                        self.var_Experience.get(),
                                                                                                        self.var_Shift.get(),        
                                                                                                        self.var_Supervisor.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_Address.get(),
                                                                                                        self.var_Email.get(),
                                                                                                        self.var_Phone_No.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_Dependent.get(),
                                                                                                        self.var_radio1.get()
                                                                                        ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Employee details have been added successfully!!",parent = self.root)
             except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
        #==========fetch data===========
        
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select *from employee")
            data=my_cursor.fetchall()
        
            if len(data)!=0:
                self.employee_table.delete(*self.employee_table.get_children())
                for i in data:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        #=======get cursor=================

    def get_cursor(self,event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]
    
        self.var_SSN.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_Department.set(data[2]),
        self.var_Joined_Date.set(data[3]),
        self.var_Experience.set(data[4]),
        self.var_Shift.set(data[5]),
        self.var_Supervisor.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_Address.set(data[8]),
        self.var_Email.set(data[9]),
        self.var_Phone_No.set(data[10]),
        self.var_Gender.set(data[11]),
        self.var_Dependent.set(data[12]),
        self.var_radio1.set(data[13])

        #update function
    def update_data(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get()=="" or self.var_SSN.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update= messagebox.askyesno("Update","Do you want to update this employee's details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                    my_cursor = conn.cursor()
                    #for the below line see timestamp 44:28 to 45:55 query to be changed according to database
                    my_cursor.execute("update employee set Department=%s,Experience=%s,Joined_Date=%s,Shift=%s,Name=%s,DOB=%s,Email=%s,Phone_No=%s,Address=%s,Gender=%s,Supervisor=%s,Dependent=%s,photo=%s where SSN=%s",(
                                                                       self.var_Department.get(),
                                                                       self.var_Experience.get(),
                                                                       self.var_Joined_Date.get(),
                                                                       self.var_Shift.get(),                                                                       
                                                                       self.var_Name.get(),                                                                                                                                                                                                    
                                                                       self.var_DOB.get(),
                                                                       self.var_Email.get(),
                                                                       self.var_Phone_No.get(),
                                                                       self.var_Address.get(),
                                                                       self.var_Gender.get(),
                                                                       self.var_Supervisor.get(),
                                                                       self.var_Dependent.get(),
                                                                       self.var_radio1.get(),
                                                                       self.var_SSN.get()
                                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success!!","Employee Details Successfully updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        #Delete function
    def delete_data(self):
     if self.var_SSN.get=="":
          messagebox.showerror("Error","SSN is required!!",parent=self.root)
     else:
          try:
               delete=messagebox.askyesno("Employee data delete page","Do you want to delete this employee's data",parent=self.root)
               if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from employee where SSN=%s"
                    val=(self.var_SSN.get(),)
                    my_cursor.execute(sql,val)
               else:
                    if not delete:
                         return
                    
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Delete","Sucessfully deleted the employee details!!",parent=self.root)
          except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    
        #Reset function
    def reset_data(self):
         self.var_Department.set("Select Department")
         self.var_Experience.set("Select Experience")
         self.var_Joined_Date.set("Selct Joined_Date")
         self.var_Shift.set("Select Shift")
         self.var_SSN.set("")
         self.var_Name.set("")
         self.var_Gender.set("Male")
         self.var_DOB.set("")
         self.var_Email.set("")
         self.var_Phone_No.set("")
         self.var_Address.set("")
         self.var_Supervisor.set("")
         self.var_radio1.set("")

#=================generate dataset or take photo sample=================
    def generate_dataset(self):
        if self.var_Department.get() == "Select Department" or self.var_Name.get()=="" or self.var_SSN.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
             try:
                  conn=mysql.connector.connect(host="localhost",username="root",password="chlorine15",database="face_recognizer")
                  my_cursor = conn.cursor()
                  my_cursor.execute("select * from employee")
                  my_result = my_cursor.fetchall()
                  id=0
                  ssn = self.var_SSN.get()
                  for x in my_result:
                       id+=1
                 #change query according to dataset
                  my_cursor.execute("update employee set Department=%s,Experience=%s,Joined_Date=%s,Shift=%s,Name=%s,DOB=%s,Email=%s,Phone_No=%s,Address=%s,Gender=%s,Supervisor=%s,Dependent=%s,photo=%s where SSN=%s",(
                                                                       self.var_Department.get(),
                                                                       self.var_Experience.get(),
                                                                       self.var_Joined_Date.get(),
                                                                       self.var_Shift.get(),                                                                       
                                                                       self.var_Name.get(),                                                                                                                                                                                                    
                                                                       self.var_DOB.get(),
                                                                       self.var_Email.get(),
                                                                       self.var_Phone_No.get(),
                                                                       self.var_Address.get(),
                                                                       self.var_Gender.get(),
                                                                       self.var_Supervisor.get(),
                                                                       self.var_Dependent.get(),
                                                                       self.var_radio1.get(),
                                                                       self.var_SSN.get()==id+1
                                                                     ))

                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close()

                  #====================Load Predefined Data on face frontals from Opencv====================

                  
                  face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                  def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
                        for (x, y, w, h) in faces:
                                face_cropped = img[y:y+h, x:x+w]
                                return face_cropped

                # Create a VideoCapture object (0 for default camera)
                  cap = cv2.VideoCapture(0)
                  img_id = 0

                  try:
                       while True:
                            ret, my_frame = cap.read()
                            
                            if face_cropped(my_frame) is not None:
                                 img_id += 1
                                 face = cv2.resize(face_cropped(my_frame), (450, 450))
                                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
                                 # Check if the image is already in grayscale or convert it if necessary
                                 if len(face.shape) == 3 and face.shape[2] == 3:
                                      face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                                 file_name_path = f"Data/user.{ssn}.{img_id}.jpg"  # Updated filename format
                                 
                                 #file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg" # old filename format can remove if needed
                                 cv2.imwrite(file_name_path, face)
                                 cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                 cv2.imshow("Cropped Face", face)
        
                            if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                break

                       cap.release()
                       cv2.destroyAllWindows()
                       messagebox.showinfo("Result", "Dataset Generation Complete!!")

                  except Exception as es:
                #print the error message for debugging                
                       print(f"Due to: {str(es)}")
                       messagebox.showerror("Error", f"Due to: {str(es)}")

             except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def search_data(self):
                if self.var_Search_by.get() == "Select" or self.var_Search_txt.get() == "":
                        messagebox.showerror("Error", "Select a valid search criteria and provide a search value", parent=self.root)
                else:
                     try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="chlorine15", database="face_recognizer")
                        my_cursor = conn.cursor()
            
                        # Define a dictionary to map search criteria to database columns
                        search_columns = {
                                "SSN": "SSN",
                                "Name": "Name",
                                "Phone No": "Phone_No"
                        }
            
                        selected_column = search_columns[self.var_Search_by.get()]
                        search_value = self.var_Search_txt.get()
            
                        my_cursor.execute(f"SELECT * FROM employee WHERE {selected_column} LIKE '%{search_value}%'")
                        data = my_cursor.fetchall()
            
                        if len(data) != 0:
                                self.employee_table.delete(*self.employee_table.get_children())
                                for i in data:
                                        self.employee_table.insert("", END, values=i)
                                conn.commit()
                        else:
                                messagebox.showinfo("Info", "No records found matching the search criteria", parent=self.root)
            
                        conn.close()
                     except Exception as es:
                        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def show_all_data(self):
                self.fetch_data()
            

if __name__=="__main__":
    root=Tk() 
    obj=Employee(root)
    root.mainloop()

