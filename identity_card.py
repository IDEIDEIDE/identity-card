#add tkinter basic template
from tkinter import *
import random
root=Tk()
root.title("lol")
root.geometry("400x400")
root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Identity Card")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_grade_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Grade :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Subjects :")

#add label for name
label_name = Label(root, text = "name : Jarronn")

#add label for grade
label_grade = Label(root, text = "grade : A+")
#add label for Subjects
label_subjects = Label(root, text = "Subjects : smart")

#add function
def placestuff():
    label_name.place(relx = 0.5, rely = 0.4, anchor=CENTER)
    label_grade.place(relx = 0.5, rely = 0.5, anchor=CENTER)
    label_subjects.place(relx = 0.5, rely = 0.6, anchor=CENTER)
    

#add button

btn = Button(root,text="school",command=placestuff)
btn.place(relx = 0.5, rely = 0.3, anchor=CENTER)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()

#tkinter basic template end statement
root.mainloop()
