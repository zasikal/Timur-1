from db import cur, conn
from insert_from_console import insert_from_console
from update_user import update_user
from delete_user import delete_user
from search_by_pattern import search_by_pattern
from show_paginated import show_paginated
from insert_many import insert_many
from show_all import show_all
from upload_csv import upload_from_csv

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
if __name__ == "__main__":
    main()