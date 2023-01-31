import sqlite3


def add_user():

    username = input("Enter your username:")
    password = input("Enter your password:")
    connection = sqlite3.connect("user.db")
    cur = connection.cursor()
    table_user = """ CREATE TABLE IF NOT EXISTS
                users(User TEXT, Password TEXT) """         
    cur.execute(table_user)
    cur.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
    connection.commit()
    cur.close()
    connection.close()


def log_in(username, password):


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


def must_log_in(IS_USER_LOGGED_IN):


    if IS_USER_LOGGED_IN:
        return True
    else:
        username = input("username: \n")
        password = input("password:  \n")
        if log_in(username, password):
            print("User has logged in!")
            return True
        else:
            print("Try again, username/password incorrect!")
            return False


def log_out(IS_USER_LOGGED_IN):

    if IS_USER_LOGGED_IN:
        return False
