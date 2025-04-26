from db import cur, conn
import csv

def upload_from_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("CALL insert_or_update_user(%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV файл был успешно загружен")