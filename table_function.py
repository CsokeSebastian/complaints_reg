import sqlite3
from datetime import datetime


def add_new_complaint():

    complaint = input("Enter your complaint:\n")
    complainant = input("Enter your name:\n")
    current_datetime = datetime.now()
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

    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM complaints")
    all_complaints = cur.fetchall()
    for complaint in all_complaints:
        print(complaint)
    cur.close()
    connection.close()


def delete_complaint():

    id_number = int(input())
    connection = sqlite3.connect("complaints.db")
    cur = connection.cursor()
    complaint_delete = ("DELETE FROM complaints WHERE id=?")
    cur.execute(complaint_delete, (id_number,))
    connection.commit()
    cur.close()
    connection.close()
    print(f"Your complaint with id number: {id_number} was deleted successfully!")


def mark_as_resolved():

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


def unresolved_complaints():

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
