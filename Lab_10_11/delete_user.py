from db import cur, conn

def delete_user():
    id_val = int(input("Введите ID контакта для удаления: "))
    cur.execute("CALL delete_by_id(%s)", (id_val,))
    conn.commit()
    print(f"Контакт с ID {id_val} был успешно удален")