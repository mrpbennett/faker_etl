import psycopg2

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="192.168.5.81",
    port="5432",
)
