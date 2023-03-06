from tkinter import *
from text_messages import *
from authentication import *
from table_function import *
import os


def create_icon():
    icon = PhotoImage(file="logo.png")
    icon.iconphoto(True, icon)



def destroy_last_window(last_window):
    last_window.destroy()

#----------------------------------------


def add_complaint_window():

    def add():
        complaint = complaint_.get()
        complainant = complainant_.get()
        add_new_complaint(complaint, complainant)
        

    add_complaint_window = Tk()
    add_complaint_window.geometry("500x500")
    complaint_ = Entry(add_complaint_window)
    complaint_.pack()
    complainant_ = Entry(add_complaint_window)
    complainant_.pack()
    Label(add_complaint_window, text="Enter your complaint:", font=("Arial", 12)).pack()
    add_entry = Button(add_complaint_window, text="Add", command=add)
    add_entry.pack()
    Button(add_complaint_window, text="Exit", command=exit).pack()


def log_in_window():
    log_in_window = Tk()
    destroy_last_window(create_must_log_in_window)
    log_in_window.geometry("500x500")

#---------------------------------------

def create_add_new_complaint_window():
    create_add_new_complaint_window = Tk()
    destroy_last_window(last_window)
    
    create_add_new_complaint_window.geometry("500x500")
    create_add_new_complaint_window.title("You can now add your complaint.")
    Label(create_add_new_complaint_window, text="Here you can add a new complaint:", font=("Arial", 12)).pack()
    Button(create_add_new_complaint_window, text="Add complaint", command=add_complaint_window).pack()
    Button(create_add_new_complaint_window, text="Exit", command=exit).pack()


def create_must_log_in_window():
    create_must_log_in_window = Tk()
    destroy_last_window(last_window)
    
    create_must_log_in_window.geometry("500x500")
    create_must_log_in_window.title("Log in.")
    # create_icon()
    Label(create_must_log_in_window, text="You are not logged in! You have to Log in!", font=("Arial", 12)).pack()
    Button(create_must_log_in_window, text="Log in", command=log_in_window).pack()
    Button(create_must_log_in_window, text="Exit", command=exit).pack()


last_window = Tk()
last_window.geometry("500x500")
last_window.title("Complaint Register")
icon = PhotoImage(file="logo.png")
last_window.iconphoto(True, icon)
Label(last_window, text="Welcome to Complaint Register.", font=("Arial", 12)).pack()
Button(last_window, text="Add complaint", command=create_add_new_complaint_window).pack()
Button(last_window, text="Log in", command=create_must_log_in_window).pack()
Button(last_window, text="Exit", command=exit).pack()
    
last_window.mainloop()    
