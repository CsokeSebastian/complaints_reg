import sqlite3
IS_ADMIN_LOGGED_IN = False


def add_admin():
    """Adds a new Admin
    Accepts two inputs: - Username
                       - Password
    Puts the date in the database."""

    username = input("Enter Username:")
    password = input("Enter Password:")
    connection = sqlite3.connect("user.db")
    cur = connection.cursor()
    table_user = """ CREATE TABLE IF NOT EXISTS
                users(User TEXT, Password TEXT) """         
    cur.execute(table_user)
    cur.execute("SELECT * FROM users")
    user = cur.fetchall()
    
    for row in user:
        if username not in row:
            cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
            connection.commit()
            print(f"{username} added successfully!")
        else:
            return "Username exists."
    
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

    global IS_ADMIN_LOGGED_IN
    if IS_ADMIN_LOGGED_IN:
        return True
    else:
        username = input("Username: \n")
        password = input("Password: \n")
        if log_in(username, password):
            print("You are logged in!")
            return True
        else:
            print("Try again, username/password incorrect!")
            return False


def log_out():
    """Logs out the Admin"""
    
    global IS_ADMIN_LOGGED_IN
    if IS_ADMIN_LOGGED_IN:
        return False
