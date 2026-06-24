from flask import Flask, request, jsonify, send_from_directory
from flasgger import Swagger
import sqlite3

app = Flask(__name__)
swagger = Swagger(app)

DB_PATH = 'gatitos.db'

# -------------------------
# Base de datos con SQLite
# -------------------------

def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
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
    # Insertar productos si la tabla está vacía
    cur.execute('SELECT COUNT(*) FROM products')
    if cur.fetchone()[0] == 0:
        productos = [
            (1, 'Gato Siamés', 1.50),
            (2, 'Gato Persa', 2.50),
            (3, 'Gato Siberiano', 3.00),
            (4, 'Gato Esfinge', 2.00),
            (5, 'Gato Fold escocés', 3.50),
            (6, 'Gato Himalayo', 4.00)
        ]
        cur.executemany('INSERT INTO products VALUES (?, ?, ?)', productos)
    con.commit()
    con.close()

init_db()

# -------------------------
# Frontend
# -------------------------

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# -------------------------
# GET para listar los productos
# -------------------------

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
    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM products')
    products = [dict(row) for row in cur.fetchall()]
    con.close()
    return jsonify(products), 200

# -------------------------
# GET para ver el carrito
# -------------------------

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
    cur.execute('SELECT * FROM cart')
    cart = [dict(row) for row in cur.fetchall()]
    con.close()
    return jsonify(cart), 200

# -------------------------
# GET para ver el total
# -------------------------

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
    cur.execute('SELECT SUM(price) FROM cart')
    result = cur.fetchone()[0]
    con.close()
    total = result if result else 0
    return jsonify({"total": total}), 200

# -------------------------
# POST para agregar un producto
# -------------------------

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
    data = request.json
    product_id = data.get('id')

    con = get_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cur.fetchone()

    if not product:
        con.close()
        return jsonify({"error": "Producto no encontrado"}), 404

    cur.execute('INSERT INTO cart (product_id, name, price) VALUES (?, ?, ?)',
                (product['id'], product['name'], product['price']))
    con.commit()

    cur.execute('SELECT * FROM cart')
    cart = [dict(row) for row in cur.fetchall()]
    con.close()
    return jsonify(cart), 201

# -------------------------
# DELETE para eliminar un producto del carrito
# -------------------------

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
    cur.execute('SELECT id FROM cart WHERE product_id = ?', (product_id,))
    item = cur.fetchone()

    if not item:
        con.close()
        return jsonify({"error": "Producto no encontrado en el carrito"}), 404

    cur.execute('DELETE FROM cart WHERE id = ?', (item['id'],))
    con.commit()

    cur.execute('SELECT * FROM cart')
    cart = [dict(row) for row in cur.fetchall()]
    con.close()
    return jsonify(cart), 200

# RUN
if __name__ == '__main__':
    app.run(debug=True)
