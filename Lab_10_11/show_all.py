from db import cur, conn

def show_all():
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)