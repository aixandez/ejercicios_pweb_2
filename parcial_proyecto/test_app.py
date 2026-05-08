import unittest
from app import app, cart

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        cart.clear()  # limpiar el carrito antes de cada test

    # -----------------------------
    # Tests de productos
    # -----------------------------
    def test_get_products(self):
        res = self.client.get('/products')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    # -----------------------------
    # Tests del carrito
    # -----------------------------
    def test_get_cart_vacio(self):
        res = self.client.get('/cart')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [])

    def test_add_to_cart(self):
        res = self.client.post('/cart', json={"id": 1})
        self.assertEqual(res.status_code, 201)
        data = res.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 1)

    def test_add_producto_inexistente(self):
        res = self.client.post('/cart', json={"id": 99})
        self.assertEqual(res.status_code, 404)

    def test_delete_product(self):
        self.client.post('/cart', json={"id": 1})
        res = self.client.delete('/cart/1')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), [])

    def test_delete_producto_no_en_carrito(self):
        res = self.client.delete('/cart/1')
        self.assertEqual(res.status_code, 404)

    # -----------------------------
    # Tests del total
    # -----------------------------
    def test_total_carrito_vacio(self):
        res = self.client.get('/cart/total')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['total'], 0)

    def test_total_con_productos(self):
        self.client.post('/cart', json={"id": 1})  # precio 1.50
        self.client.post('/cart', json={"id": 2})  # precio 2.50
        res = self.client.get('/cart/total')
        self.assertEqual(res.status_code, 200)
        self.assertAlmostEqual(res.get_json()['total'], 4.00)


if __name__ == '__main__':
    unittest.main()
