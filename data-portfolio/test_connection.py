import psycopg2

# conexión
conn = psycopg2.connect(
    dbname="testdb",
    user="miguel",
    password="1234",
    host="localhost",
    port="5432"
)

# cursor
cur = conn.cursor()

# query simple
cur.execute("SELECT version();")

# resultado
result = cur.fetchone()
print(result)

# cerrar
cur.close()
conn.close()
