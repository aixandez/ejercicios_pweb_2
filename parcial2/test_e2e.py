import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GatitosCartE2E(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')
        self.wait = WebDriverWait(self.driver, 10)

    # -------------------------
    # Test 1: Visualizar productos
    # -------------------------
    def test_01_visualizar_productos(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        productos = self.driver.find_elements(By.CLASS_NAME, 'product-item')
        self.assertGreater(len(productos), 0)

    # -------------------------
    # Test 2: Agregar producto al carrito
    # -------------------------
    def test_02_agregar_producto_al_carrito(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn.click()

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )
        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertGreater(len(items), 0)

    # -------------------------
    # Test 3: Mostrar total de la compra
    # -------------------------
    def test_03_total_mayor_a_cero(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn.click()
        time.sleep(1)

        total_elem = self.driver.find_element(By.ID, 'total')
        total_valor = float(total_elem.text.replace('Total: $', ''))
        self.assertGreater(total_valor, 0)

    # -------------------------
    # Test 4: Eliminar producto del carrito
    # -------------------------
    def test_04_eliminar_producto_del_carrito(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn_agregar = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn_agregar.click()

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )
        btn_eliminar = self.driver.find_element(By.XPATH, '(//button[text()="Eliminar"])[1]')
        btn_eliminar.click()
        time.sleep(1)

        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertEqual(len(items), 0)

    # -------------------------
    # Test 5: Flujo de compra completo
    # -------------------------
    def test_05_flujo_compra_completo(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        botones = self.driver.find_elements(By.XPATH, '//button[text()="Agregar"]')
        botones[0].click()
        time.sleep(0.5)
        botones[1].click()
        time.sleep(1)

        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertEqual(len(items), 2)

        total_elem = self.driver.find_element(By.ID, 'total')
        total_valor = float(total_elem.text.replace('Total: $', ''))
        self.assertGreater(total_valor, 0)

    # -------------------------
    # Test 6: Persistencia de datos (recarga de página)
    # -------------------------
    def test_06_persistencia_datos(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn.click()
        time.sleep(1)

        # Recargar la página
        self.driver.refresh()
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )

        # El carrito debe seguir teniendo el gatito (persistencia en SQLite)
        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertGreater(len(items), 0)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
