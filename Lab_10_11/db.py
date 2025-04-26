import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="postgres",
    password="Stomap7406+"
)

cur = conn.cursor()