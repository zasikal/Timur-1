from db import cur, conn

def search_by_pattern():
    pattern = input("Введите шаблон: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)