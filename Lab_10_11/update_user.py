from db import cur, conn

def update_user():
    id_val = int(input("Введите ID контакта для обновления: "))
    name = input("Введите новое имя: ")
    phone = input("Введите новый телефон: ")
    cur.execute("CALL update_user(%s, %s, %s)", (id_val, name, phone))
    conn.commit()
    print(f"Контакт с ID {id_val} был успешно обновлен")