from db import cur, conn

def insert_many():
    names = input("Имена через запятую: ").split(",")
    phones = input("Телефоны через запятую: ").split(",")

    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    print("Новые пользователи были успешно добавлены")
    conn.commit()