import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="postgres",
    password="Stomap7406+"
)
cur = conn.cursor()








def upload_from_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("CALL insert_or_update_user(%s, %s)", (row[0], row[1]))  # row[0] - имя, row[1] - телефон
    conn.commit()
    print("Файл CSV был успешно загружен в бд")















def insert_from_console():
    name = input("Имя: ")
    phone = input("Телефон: ")

    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Новый контакт был успешно добавлен")







def update_user():
    id_val = int(input("Введите ID контакта для обновления: "))
    name = input("Введите новое имя: ")
    phone = input("Введите новый телефон: ")
    cur.execute("CALL update_user(%s, %s, %s)", (id_val, name, phone))
    conn.commit()
    print(f"Контакт с ID {id_val} был успешно обновлен")






def delete_user():
    id_val = int(input("Введите ID контакта для удаления: "))
    cur.execute("CALL delete_by_id(%s)", (id_val,))
    conn.commit()
    print(f"Контакт с ID {id_val} был успешно удален")




def search_by_pattern():
    pattern = input("Введите шаблон: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)






def show_paginated():
    limit = int(input("Сколько контактов: "))
    offset = int(input("Смещение: "))
    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)



def insert_many():
    names = input("Имена через запятую: ").split(",")
    phones = input("Телефоны через запятую: ").split(",")
    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    print("Новые пользователи были добавлены")
    conn.commit()







def show_all():
    cur.execute("SELECT * FROM PhoneBook ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)







def main():
    while True:
        print("1. Загрузить из CSV файла в бд")
        print("2. Добавить 1 контакт")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Поиск по шаблону")
        print("6. Пагинация")
        print("7. Добавить несколько контактов")
        print("8. Показать все контакты")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1":
            upload_from_csv(input("Путь к CSV: "))
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            search_by_pattern()
        elif choice == "6":
            show_paginated()
        elif choice == "7":
            insert_many()
        elif choice == "8":
            show_all()
        elif choice == "0":
            break
        else:
            print("Неверный ввод, попробуйте снова")

    cur.close()
    conn.close()
if __name__ == '__main__':
    main()
