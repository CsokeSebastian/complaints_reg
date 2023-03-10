from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from text_messages import *
from authentication import *
from table_function import *


def create_icon():
    icon = PhotoImage(file="logo.png")
    icon.iconphoto(True, icon)


def destroy_last_window(window):
    window.destroy()


def del_entry(first, second):
        first.delete(0, 999999)
        second.delete(0, 999999)

#_____________________


def add_admin_window():


    def new_admin():
        admin_name = admin_name_.get()
        admin_password = admin_password_.get()
        add_admin(admin_name, admin_password)
        messagebox.showinfo(title="Success.",message="Your Admin was added successfully!")
        del_entry(admin_name_, admin_password_)


    add_admin_window = Tk()
    add_admin_window.geometry("500x500")
    add_admin_window.title("Add Admin")
    Label(add_admin_window, text="Enter Admin name:").pack()
    admin_name_ = Entry(add_admin_window, width=50)
    admin_name_.pack()
    Label(add_admin_window, text="Enter a password:").pack()
    admin_password_ = Entry(add_admin_window, width=50)
    admin_password_.pack()
    add_button = Button(add_admin_window, text="Add", command=new_admin)
    add_button.pack()
    back_button = Button(add_admin_window, text="Back", command=menu_buttons)
    back_button.pack()
    add_admin_window.mainloop()
    



def view_all_complaints_window():

    view_all_complaints_window = Tk()
    view_all_complaints_window.geometry("500x500")
    view_all_complaints_window.title("All Complaints")
    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM complaints")
    all_complaints = cur.fetchall()
    frm = Frame(view_all_complaints_window)
    frm.pack()
    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5), show="headings", height="15")
    tv.pack()

    tv.heading(1, text="Id")
    tv.heading(2, text="Complaint")
    tv.heading(3, text="Name")
    tv.heading(4, text="Date")
    tv.heading(5, text="Resolved")

    for complaint in all_complaints:
        tv.insert("", "end", values=complaint)
    cur.close()
    connection.close()
    view_all_complaints_window.mainloop()

def view_unresolved_complaints_window():
    pass

def change_status_window():
    pass

def log_out_window():
    pass


#__________________


def menu_buttons():

    menu_buttons = Tk()
    menu_buttons.geometry("500x500")
    menu_buttons.title("Menu")
    Label(menu_buttons, text="What do you want to do?").pack()
    add_admin_button = Button(menu_buttons, text="Add Admin", command=add_admin_window)
    add_admin_button.pack()
    view_all_complaints_button = Button(menu_buttons, text="View All Complaints", command=view_all_complaints_window)
    view_all_complaints_button.pack()
    view_unresolved_complaints_button = Button(menu_buttons, text="View Unresolved Complaints", command=view_unresolved_complaints_window)
    view_unresolved_complaints_button.pack()
    change_status_button = Button(menu_buttons, text="Change Status", command=change_status_window)
    change_status_button.pack()
    log_out_button = Button(menu_buttons, text="Log Out", command=log_out_window)
    log_out_button.pack()
    back_button = Button(menu_buttons, text="Back", command=log_in_window)
    back_button.pack()
    exit_button = Button(menu_buttons, text="Exit", command=exit)
    exit_button.pack()
    menu_buttons.mainloop()
   

#----------------------------------------


def add_complaint_window():


    def add():
        complaint = complaint_.get()
        complainant = complainant_.get()
        add_new_complaint(complaint, complainant)
        messagebox.showinfo(title="Success.",message="Your complaint was added successfully!")
        del_entry(complaint_, complainant_)

    add_complaint_window = Tk()
    add_complaint_window.geometry("500x500")
    add_complaint_window.title("You can now add your complaint.")
    Label(add_complaint_window, text="Enter your complaint: ").pack()
    complaint_ = Entry(add_complaint_window, width=50)
    complaint_.pack()
    Label(add_complaint_window, text="Enter your name: ").pack()
    complainant_ = Entry(add_complaint_window, width=50)
    complainant_.pack()
    add_button = Button(add_complaint_window, text="Add", command=add)
    add_button.pack()
    exit_button = Button(add_complaint_window, text="Exit", command=exit)
    exit_button.pack()
    back_button = Button(add_complaint_window, text="Back", command=last_window)
    back_button.pack()
    add_complaint_window.mainloop()


def log_in_window():

    def verify():
        username = username_.get()
        password = password_.get()
        global IS_ADMIN_LOGGED_IN
        if IS_ADMIN_LOGGED_IN:
            
            return True
        else:
            if log_in(username, password):
                del_entry(username_, password_)
                menu_buttons()
                return True
            else:
                messagebox.showerror(title="Error!", message="Something went wrong!")
                return False
       
    log_in_window = Tk()
    log_in_window.geometry("500x500")
    log_in_window.title("You have to Log In.")
    Label(log_in_window, text="Enter your Username: ").pack()
    username_ = Entry(log_in_window, width=50)
    username_.pack()
    Label(log_in_window, text="Enter password: ").pack()
    password_ = Entry(log_in_window, width=50)
    password_.pack()
    log_in_button = Button(log_in_window, text="Log In", command=verify)
    log_in_button.pack()
    Button(log_in_window, text="Exit", command=exit).pack()
    back_button = Button(log_in_window, text="Back", command=last_window)
    back_button.pack()
    log_in_window.mainloop()


#---------------------------------------


last_window = Tk()
last_window.geometry("500x500")
last_window.title("Complaint Register")
icon = PhotoImage(file="logo.png")
last_window.iconphoto(True, icon)
Label(last_window, text="Welcome to Complaint Register.", font=("Arial", 12)).pack()
Button(last_window, text="Add complaint", command=add_complaint_window).pack()
Button(last_window, text="Log in", command=log_in_window).pack()
Button(last_window, text="Exit", command=exit).pack()
    
last_window.mainloop()    
