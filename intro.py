from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Create the GUI elements
        self.create_gui()

    def create_gui(self):
        # Create the main title label
        title_lbl = Label(self.root, text="!<Developers>!", font=("times new roman", 35, "bold"), bg="black", fg="gold")
        title_lbl.place(x=0, y=0, width=1535, height=45)

        # Load and display the background image
        img_top = Image.open(r"F:\Face Recognition System\Images\Dev_bg.jpg")
        img_top = img_top.resize((1535, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1535, height=800)

        # Create the main frame on the background image
        main_frame = Frame(f_lbl, bd=2, bg="black")
        main_frame.place(x=1000, y=0, width=580, height=800)

        # Developer information labels
        dev_info = [
            "You have entered the domain of !!",
            "We are the Developers of this system,",
            "We are THE Interns from DLithe,",
            "The AIML Division!",
            "Aditya.Y.Kesarkar",
            "Gurukiran B",
            "Harsha M S",
            "Kishan Navali"
        ]

        y_position = 5

        # Create labels for developer information
        for info in dev_info:
            dep_label = Label(main_frame, text=info, font=("times new roman", 18, "bold"), bg="black", fg="cyan")
            dep_label.place(x=0, y=y_position)
            y_position += 40

        # Load and display an image on the main window
        img2 = Image.open(r"F:\Face Recognition System\Images\Dev_bg.jpg")
        img2 = img2.resize((500, 300), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=0, y=210, width=500, height=300)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
