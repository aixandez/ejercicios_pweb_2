import requests #para le carrito vacio
import unittest #para pruebas
import time #para time.sleep()
from selenium import webdriver # para abrir chrome
from selenium.webdriver.common.by import By #importa by paara buscar elementos
from selenium.webdriver.support.wait import WebDriverWait #esperas
from selenium.webdriver.support import expected_conditions as EC #importa las condiciones esperadas


class GatitosCartE2E(unittest.TestCase): #clase para pruebas

    def setUp(self):
        requests.delete('http://localhost:5000/cart') #vacia completamente el carrito
        self.driver = webdriver.Chrome() #abre chrome
        self.driver.get('http://localhost:5000') #abre la app
        self.wait = WebDriverWait(self.driver, 10) #espera q ocurra una condicion para continuar, hasta 10 segundos

    
    # test 1: Visualizar productos


    def test_01_visualizar_productos(self):
        self.wait.until( #empieza una espera
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )# espera q exista 1 elemento, y busca product item q es lo q genera cargarProductos en js()
        productos = self.driver.find_elements(By.CLASS_NAME, 'product-item') #busca todos los productos
        self.assertGreater(len(productos), 0) #verifica que haya mas de cero

    
    # test 2: Agregar producto al carrito


    def test_02_agregar_producto_al_carrito(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]') #busca 1° boton Agregar
        btn.click() #le hace click. el xpath busca la ubicacion del elemento

        self.wait.until( #espera cart-item xq despues del click el carrito debe actualizarse
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )
        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item') #cuenta los productos del carrito
        self.assertGreater(len(items), 0) #co9omprueba que exista al menos uno para ver q fue agregado


    # test 3: Mostrar total de la compra (y que no sea cero)


    def test_03_total_mayor_a_cero(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn.click() #primero agrega un producto
        time.sleep(1) #espera 1 segundo para actualizar el total

        total_elem = self.driver.find_element(By.ID, 'total') #busca <div id="total">
        total_valor = float(total_elem.text.replace('Total: $', '')) #obtiene algo asi: 1.50
        self.assertGreater(total_valor, 0) #comprueba q total sea mayor a cero

    
    # test 4: Eliminar producto del carrito
    

    def test_04_eliminar_producto_del_carrito(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn_agregar = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]')
        btn_agregar.click() #agrega un producto

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )
        btn_eliminar = self.wait.until( #espera q aparezca eliminar
            EC.element_to_be_clickable((By.XPATH, '(//button[text()="Eliminar"])[1]')) #tmb chequea q se pueda clickear
        )
        btn_eliminar.click() #le da click a eliminar
        time.sleep(1) #espera q se borre

        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertEqual(len(items), 0) #debe quedar vacío

    
    # test 5: Flujo de compra completo (visualizar elementos, agregar, calcular total)
    
    def test_05_flujo_compra_completo(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        botones = self.driver.find_elements(By.XPATH, '//button[text()="Agregar"]') #busca botones agregar
        botones[0].click() #agrega el 1ero
        time.sleep(0.5)
        botones[1].click() #agrega el 2do
        time.sleep(1)

        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item') #cuenta los productos
        self.assertEqual(len(items), 2) #se fija q haya 2 productos en el carrito q es lo q agregó

        total_elem = self.driver.find_element(By.ID, 'total') #verifica total igual q antes
        total_valor = float(total_elem.text.replace('Total: $', ''))
        self.assertGreater(total_valor, 0)

 
    # test 6: Persistencia de datos (recarga de página)

    def test_06_persistencia_datos(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
        )
        btn = self.driver.find_element(By.XPATH, '(//button[text()="Agregar"])[1]') #agrega un producto
        btn.click()
        time.sleep(1)

        self.driver.refresh() #recarga la pagina
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-item'))
        )

        # el carrito debe seguir teniendo el gatito (persistencia en SQLite)
        items = self.driver.find_elements(By.CLASS_NAME, 'cart-item')
        self.assertGreater(len(items), 0) #verifica que aun haya elementos

    def tearDown(self): #cierra ventana del navegador web
        self.driver.close()


if __name__ == '__main__': #inicio la ejecucion de los tests
    unittest.main(argv=[''], verbosity=2, exit=False)
