from flask import Flask, request, jsonify, send_from_directory
from flasgger import Swagger
import sqlite3

app = Flask(__name__)
swagger = Swagger(app)

DB_PATH = 'gatitos.db' #guarda el nombre de la bdd


# Base de datos con SQLite


def get_db(): #funcion para conectarse a sqlite
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row #cada fila puede leerse x nombre
    return con #devuelve la conexion

def init_db(): #cuandi arranca la app crea tablas y carga productos
    con = get_db()
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # si la tabla está vacía inserta los productos
    cur.execute('SELECT COUNT(*) FROM products')
    if cur.fetchone()[0] == 0: #si no hay productos los inserta
        productos = [
            (1, 'Gato Siamés', 1.50),
            (2, 'Gato Persa', 2.50),
            (3, 'Gato Siberiano', 3.00),
            (4, 'Gato Esfinge', 2.00),
            (5, 'Gato Fold escocés', 3.50),
            (6, 'Gato Himalayo', 4.00)
        ]
        cur.executemany('INSERT INTO products VALUES (?, ?, ?)', productos)
    con.commit() #guarda y cierra
    con.close()

init_db() #se ejecuta cuando incia flask


# Frontend


@app.route('/')
def index():
    return send_from_directory('static', 'index.html') #cdo el usuario entra a localhost devuelve el index.html
  #separado en otra carpeta solo para dividir el front del back


# endpoints


# GET para listar los productos disponibles


@app.route('/products', methods=['GET'])
def get_products():
    """
    Listar todos los productos disponibles
    ---
    responses:
      200:
        description: Lista de productos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              price:
                type: number
    """
    con = get_db() #abre la conexión sqlite
    cur = con.cursor() #crea el cursor o sea el objeto que hace las consultas sql
    cur.execute('SELECT * FROM products') #trae todos los productos
    products = [dict(row) for row in cur.fetchall()] #convierto las filas sqlite a diccionarios
    con.close()
    return jsonify(products), 200 #devuelve json


# GET para ver el carrito


@app.route('/cart', methods=['GET'])
def get_cart():
    """
    Ver el contenido del carrito
    ---
    responses:
      200:
        description: Lista de productos en el carrito
    """
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM cart') #obtiene los productos agregados
    cart = [dict(row) for row in cur.fetchall()] #convierto las filas sqlite a diccionarios
    con.close()
    return jsonify(cart), 200 #devuelve json


# GET para ver el total de la compra

@app.route('/cart/total', methods=['GET'])
def get_total():
    """
    Calcular el total del carrito
    ---
    responses:
      200:
        description: Total de la compra
        schema:
          type: object
          properties:
            total:
              type: number
    """
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT SUM(price) FROM cart') #suma los precios
    result = cur.fetchone()[0] #extrae 1er valor de la tuppla o sea el total
    con.close()
    total = result if result else 0 #si el carrito esta vacio va a dar cero
    return jsonify({"total": total}), 200 #devuelve total


# POST para agregar un producto

@app.route('/cart', methods=['POST'])
def add_to_cart():
    """
    Agregar un producto al carrito
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - id
          properties:
            id:
              type: integer
              description: ID del producto a agregar
    responses:
      201:
        description: Producto agregado exitosamente
      404:
        description: Producto no encontrado
    """
    data = request.json #lee json enviado
    product_id = data.get('id') #obtiene el id

    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM products WHERE id = ?', (product_id,)) #busca producto
    product = cur.fetchone() #obtiene el resultado

    if not product:
        con.close()
        return jsonify({"error": "Producto no encontrado"}), 404
    # si no existe devuelve 404, si existe lo agerga al carrito

    cur.execute('INSERT INTO cart (product_id, name, price) VALUES (?, ?, ?)',
                (product['id'], product['name'], product['price']))
    con.commit()

    cur.execute('SELECT * FROM cart') #vuelve a leer carrito para devolverlo actualizado
    cart = [dict(row) for row in cur.fetchall()] #fetchall trae todas las filas y dictrow las conviert en diccionario de py
    con.close() #cierro la conexión
    return jsonify(cart), 201 #devuelve el carrito


# DELETE para eliminar un producto del carrito


@app.route('/cart/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Eliminar un producto del carrito
    ---
    parameters:
      - in: path
        name: product_id
        type: integer
        required: true
        description: ID del producto a eliminar
    responses:
      200:
        description: Producto eliminado exitosamente
      404:
        description: Producto no encontrado en el carrito
    """
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT id FROM cart WHERE product_id = ?', (product_id,)) #busca en el carrito
    item = cur.fetchone()

    if not item: #si no lo encuentra da error
        con.close()
        return jsonify({"error": "Producto no encontrado en el carrito"}), 404

    cur.execute('DELETE FROM cart WHERE id = ?', (item['id'],)) #borra del carrito por id
    con.commit()

    cur.execute('SELECT * FROM cart') #lee de nuevo para devolver el carrito actualizado
    cart = [dict(row) for row in cur.fetchall()] #convierte a lista los restantes
    con.close()
    return jsonify(cart), 200


# DELETE para vaciar el carrito (usado solo en los tests)


@app.route('/cart', methods=['DELETE'])
def clear_cart():
    """
    Vaciar el carrito completo
    ---
    responses:
      200:
        description: Carrito vaciado exitosamente
    """
    con = get_db()
    cur = con.cursor()
    cur.execute('DELETE FROM cart') #borra todas las filas
    con.commit()
    con.close()
    return jsonify([]), 200


# RUN: inicia el servidor flask en http://localhost:5000
if __name__ == '__main__':
    app.run(debug=True)
