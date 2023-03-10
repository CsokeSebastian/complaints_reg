import sqlite3
from datetime import datetime


def add_new_complaint():
    """Adds a new complaint to database.
    Accepts two inputs: - complaint
                        - complainant.
    Adds the date and time.
    Adds status."""

    complaint = input("Enter your complaint:\n")
    complainant = input("Enter your name:\n")
    current_datetime = datetime.now().strftime("%Y-%m-%d, %H:%M")
    resolved = "In progress."
    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    table_complaints = (""" CREATE TABLE IF NOT EXISTS Complaints(
                    Id INTEGER PRIMARY KEY NOT NULL,
                    Complaint TEXT,
                    Name of the Complainant TEXT, 
                    Date TIMESTAMP,
                    Resolved TEXT);""")
    cur.execute(table_complaints)
    cur.execute("INSERT INTO complaints VALUES (?, ?, ?, ?, ?)",
                (None, complaint, complainant, current_datetime, resolved))
    connection.commit()
    connection.close()


def view_all_complaints():
    """Shows all the complaints"""

    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM complaints")
    all_complaints = cur.fetchall()
    for complaint in all_complaints:
        print(complaint)
    cur.close()
    connection.close()
   

def mark_as_resolved():
    """Marks a complaint as Resolved after a specified Id number
    Accept one input: - id_number.
    Updates the status of a complaint."""
    
    try:
        id_number = int(input())
        updated_status_complaint = "Resolved!"
        connection = sqlite3.connect("complaints.db")
        cur = connection.cursor()
        resolved_status ="""UPDATE Complaints
                                            SET Resolved = ?
                                            WHERE id = ?"""
        cur.execute(resolved_status, (updated_status_complaint, id_number))
        connection.commit()
        cur.close()
        connection.close()
        print(f"Your complaint with Id number {id_number} was marked as resolved!")
    except ValueError:
        print("Enter a existing Id number!")

def unresolved_complaints():
    """Shows you the unresolved complaints"""

    resolved = "In progress."
    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    not_yet_resolved_complaints = ("""SELECT * FROM Complaints WHERE Resolved = ?""")
    cur.execute(not_yet_resolved_complaints, (resolved,))
    connection.commit()
    for row in cur:
        if resolved:
            print(row)
    cur.close()
    connection.close()
