from db import cur, conn

def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Новый контакт был успешно добавлен")