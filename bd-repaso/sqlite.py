import sqlite3

# Crear BD y conexión (si no existe el archivo, lo crea)
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()

# Crear tablas
cur.execute('CREATE TABLE IF NOT EXISTS customers(id, name, address)')
cur.execute('CREATE TABLE IF NOT EXISTS cities(cod, name)')

# Mostrar tablas existentes
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tablas:', res.fetchall())

# Insertar una fila
cur.execute("INSERT INTO customers VALUES (1, 'pablo', 'capilla del señor')")
con.commit()

# Insertar varias filas
cur.execute("""
    INSERT INTO customers VALUES
        (2, 'mariano', 'palermo'),
        (3, 'ana', 'merlo')
""")
con.commit()

# Insertar con marcadores de posición
data = [
    (4, 'luis', 'bariloche'),
    (5, 'maria', 'iguazú'),
    (6, 'alex', 'rosario'),
]
cur.executemany('INSERT INTO customers VALUES(?, ?, ?)', data)
con.commit()

# Seleccionar todos los nombres
res = cur.execute('SELECT name FROM customers')
print('Nombres:', res.fetchall())

# Seleccionar con bucle
print('\nNombre y dirección:')
for row in cur.execute('SELECT name, address FROM customers'):
    print(row)

con.close()