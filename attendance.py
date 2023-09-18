from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Login Details")

        #=====================Variables=======================
        #self.var_atten_id=StringVar()
        self.var_atten_SSN=StringVar()
        self.var_atten_Name=StringVar()
        self.var_atten_Department=StringVar()
        self.var_atten_LoginTime=StringVar()
        self.var_atten_LogoutTime=StringVar()
        self.var_atten_Date=StringVar()
        self.var_atten_Attendance=StringVar()


#first image 
        img=Image.open(r"F:\Face Recognition System\Images\background0.jpg")
        img= img.resize((800, 200), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
#2nd Image
        img1=Image.open(r"F:\Face Recognition System\Images\background1.jpg")
        img1= img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

#Backgroung Image
        img3=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img3= img3.resize((1535, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img. place(x=0,y=130,width=1535,height=710)

#title
        title_lbl= Label(bg_img,text="Employee Login Management System",font=("times new roman",32,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1535,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=650)

#left label frame
        Left_frame=LabelFrame(main_frame,bd=8,bg="white",relief=RIDGE,text="Employee Login Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=625)

        img_left=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img_left= img_left.resize((680, 130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=680,height=130)

#Employee login details label frame
        Employee_Detail_frame=LabelFrame(Left_frame,bd=5,bg="white",relief=RIDGE)
        Employee_Detail_frame.place(x=3,y=130,width=740,height=465)

#Labels And Entries
        #Attendance id (SSN)
        attendanceid_label=Label(Employee_Detail_frame,text="SSN",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=20,textvariable=self.var_atten_SSN,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Department
        attendanceid_label=Label(Employee_Detail_frame,text="Department",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=0,column=2,padx=10,pady=8,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=22,textvariable=self.var_atten_Department,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=3,padx=10,pady=8,sticky=W)

        #Name
        attendanceid_label=Label(Employee_Detail_frame,text="Name",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=1,column=0,padx=10,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=20,textvariable=self.var_atten_Name,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=1,column=1,padx=10,pady=8,sticky=W)

        #Date
        attendanceid_label=Label(Employee_Detail_frame,text="Date",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=1,column=2,padx=10,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=20,textvariable=self.var_atten_Date,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=1,column=3,padx=10,pady=8,sticky=W)

        #Login-Time
        attendanceid_label=Label(Employee_Detail_frame,text="LogIn-Time",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=2,column=0,padx=10,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=20,textvariable=self.var_atten_LoginTime,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=2,column=1,padx=10,pady=8,sticky=W)

        #Logout-Time
        attendanceid_label=Label(Employee_Detail_frame,text="LogOut-Time",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=2,column=2,padx=10,sticky=W)

        attendanceid_entry=ttk.Entry(Employee_Detail_frame,width=20,textvariable=self.var_atten_LogoutTime,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=2,column=3,padx=10,pady=8,sticky=W)

        #Attendance Status
        attendanceid_label=Label(Employee_Detail_frame,text="Attendance status",font=("times new roman",12,"bold"))
        attendanceid_label.grid(row=3,column=0,padx=10,sticky=W)

        self.attendance_combo=ttk.Combobox(Employee_Detail_frame,textvariable=self.var_atten_Attendance,font=("times new roman",12,"bold"),state="readonly",width=18)#width is given to change the size of drop down box
        self.attendance_combo["values"]=("Status","Present","Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=3,column=1,padx=10,pady=8,sticky=W)

        #Buttons frame
        btn_frame=Frame(Employee_Detail_frame,bd=5,relief=RIDGE,bg="white")
        btn_frame.place(x=6,y=350,width=727,height=32)

        Importbtn=Button(btn_frame,text="Import csv",width=19,command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Importbtn.grid(row=0,column=0)

        Exportbtn=Button(btn_frame,text="export csv",width=19,command=self.exortCsv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Exportbtn.grid(row=0,column=1)

        Updatebtn=Button(btn_frame,text="Update",width=19,command=self.update_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Updatebtn.grid(row=0,column=2)

        Resetbtn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Resetbtn.grid(row=0,column=3)

        
#right label frames
        Right_frame=LabelFrame(main_frame,bd=8,bg="white",relief=RIDGE,text="Login Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=790,y=12,width=692,height=625)

        img_right=Image.open(r"F:\Face Recognition System\Images\background3.jpg")
        img_right= img_right.resize((690, 130), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=690,height=130)

        #=======================scroll bar table==================
        table_frame=LabelFrame(Right_frame,bd=5,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=3,y=135,width=675,height=450)

        #Label
        #search_label=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="red",fg="white")
        #search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("SSN","Name","Department","CheckIn Time","CheckOut Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("SSN",text="SSN")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("CheckIn Time",text="CheckIn Time")
        self.AttendanceReportTable.heading("CheckOut Time",text="CheckOut Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("SSN",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("CheckIn Time",width=100)
        self.AttendanceReportTable.column("CheckOut Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

#=============================fetch data=============================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #imort csv button
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #export csv button
    def exortCsv(self):
        try:
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to Export",parent=self.root)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export in Process","Your data has been exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content["values"]
        if row and len(row) >= 7:
                self.var_atten_SSN.set(row[0])
                self.var_atten_Name.set(row[1])
                self.var_atten_Department.set(row[2])
                self.var_atten_LoginTime.set(row[3])
                self.var_atten_LogoutTime.set(row[4])
                self.var_atten_Date.set(row[5])
                self.var_atten_Attendance.set(row[6])
        else:
        # Handle the case where the row is empty or doesn't have enough elements
        # You can clear the variables or show a message
                self.var_atten_SSN.set("")
                self.var_atten_Name.set("")
                self.var_atten_Department.set("")
                self.var_atten_LoginTime.set("")
                self.var_atten_LogoutTime.set("")
                self.var_atten_Date.set("")
                self.var_atten_Attendance.set("")

    def reset_data(self):
        self.var_atten_SSN.set("")
        self.var_atten_Name.set("")
        self.var_atten_Department.set("")
        self.var_atten_LoginTime.set("")
        self.var_atten_LogoutTime.set("")
        self.var_atten_Date.set("")
        self.var_atten_Attendance.set("")

    def update_data(self):
        ssn = self.var_atten_SSN.get()
        name = self.var_atten_Name.get()
        department = self.var_atten_Department.get()
        login_time = self.var_atten_LoginTime.get()
        logout_time = self.var_atten_LogoutTime.get()
        date = self.var_atten_Date.get()
        attendance = self.var_atten_Attendance.get()

        if not ssn:
                messagebox.showerror("Error", "Please select a record to update.", parent=self.root)
                return

        try:
            # Check if mydata is empty or not
                if not mydata:
                        messagebox.showerror("Error", "No data imported. Please import a CSV file first.", parent=self.root)
                        return

                updated_data = []

                for row in mydata:
                        if row[0] == ssn:
                                # Update the record with new values
                                row[1] = name
                                row[2] = department
                                row[3] = login_time
                                row[4] = logout_time
                                row[5] = date
                                row[6] = attendance

                        updated_data.append(row)

                # Rewrite the imported CSV file with the updated data
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
                with open(fln, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(updated_data)

                # Refresh the table with the updated data
                mydata.clear()
                with open(fln) as myfile:
                        csvread = csv.reader(myfile, delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata)

                self.reset_data()
                messagebox.showinfo("Success", "Record updated successfully.", parent=self.root)

        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

if __name__=="__main__":
    root=Tk() 
    obj=Attendance(root)
    root.mainloop()        