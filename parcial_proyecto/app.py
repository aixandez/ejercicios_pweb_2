from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# -----------------------------
# Datos en memoria
# -----------------------------
products = [
    {"id": 1, "name": "Gato Siamés", "price": 1.50},
    {"id": 2, "name": "Gato Persa", "price": 2.50},
    {"id": 3, "name": "Gato Siberiano", "price": 3.00},
    {"id": 4, "name": "Gato Esfinge", "price": 2.00},
    {"id": 5, "name": "Gato Fold escocés", "price": 3.50},
    {"id": 6, "name": "Gato Himalayo", "price": 4.00}
]

cart = []

# -----------------------------
# GET -> listar productos
# -----------------------------
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
    return jsonify(products), 200


# -----------------------------
# GET -> ver carrito
# -----------------------------
@app.route('/cart', methods=['GET'])
def get_cart():
    """
    Ver el contenido del carrito
    ---
    responses:
      200:
        description: Lista de productos en el carrito
    """
    return jsonify(cart), 200


# -----------------------------
# GET -> total  (debe ir ANTES que /cart/<int:product_id>)
# -----------------------------
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
    total = sum(p['price'] for p in cart)
    return jsonify({"total": total}), 200


# -----------------------------
# POST -> agregar producto
# -----------------------------
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

    for p in products:
        if p['id'] == product_id:
            cart.append(p)
            return jsonify(cart), 201

    return jsonify({"error": "Producto no encontrado"}), 404


# -----------------------------
# DELETE -> eliminar producto
# -----------------------------
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
    for p in cart:
        if p['id'] == product_id:
            cart.remove(p)
            return jsonify(cart), 200

    return jsonify({"error": "Producto no encontrado en el carrito"}), 404


# -----------------------------
# RUN
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
