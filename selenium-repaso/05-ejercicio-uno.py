"""Testea la duración de la carrera en el sitio de la UNO"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TecUnivTecWebUNO(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_duracion_carrera(self):
        self.driver.get('https://www.uno.edu.ar/oferta-academica/tecnicaturas/tec-univ-en-tecnologias-web.html')
        elem = self.driver.find_element(By.XPATH, "//strong[text()='Duración de la carrera: ']/parent::span")
        actual = elem.text.split(':')[1].strip()
        expected = '2 años y medio.'
        self.assertEqual(actual, expected)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(defaultTest='TecUnivTecWebUNO', argv=[''], verbosity=2, exit=False)