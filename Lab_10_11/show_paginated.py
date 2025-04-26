from db import cur, conn

def show_paginated():
    limit = int(input("Сколько записей: "))
    offset = int(input("Смещение: "))
    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)