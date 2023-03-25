import sqlite3
import pwinput

is_admin_logged_in = False


def add_admin():
    """Adds a new Admin
    Accepts two inputs: - Username
                       - Password
    Puts the date in the database."""

    username = input("Enter Username: ")
    password = pwinput.pwinput(prompt="Enter Password: ", mask="*")
    connection = sqlite3.connect("user.db")
    cur = connection.cursor()
    table_user = """ CREATE TABLE IF NOT EXISTS
                users(User TEXT, Password TEXT) """         
    cur.execute(table_user)
    cur.execute("SELECT * FROM users")
    user = cur.fetchall()
    user_name = False

    for row in user:
        if username in row:
            user_name = True

    if user_name == True:
        print("Username already exists. Please select a different Username!")
    else:
        cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        connection.commit()
        print(f"{username} added successfully!")
        
    cur.close()
    connection.close()
    

def log_in(username, password):
    """Checks if the Username and Password exist in database and
    logs in the Admin.
    Accepts two inputs: - Username
                       - Password"""

    connection = sqlite3.connect("user.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM users")
    user = cur.fetchall()
    connection.commit()
    for row in user:
        if username and password in row:
            return True
    cur.close()
    connection.close()


def must_log_in():
    """Asks for username and password and return True  
    if found or False if not"""

    global is_admin_logged_in
    if is_admin_logged_in:
        return True
    else:
        username = input("Username: \n")
        password = pwinput.pwinput(prompt="Password: \n", mask="*" )
        if log_in(username, password):
            return True
        else:
            print("Try again, username/password incorrect!")
            return False


def log_out():
    """Logs out the Admin"""
    
    global is_admin_logged_in
    if is_admin_logged_in:
        return False
