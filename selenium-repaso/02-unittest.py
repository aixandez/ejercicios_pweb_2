"""El mismo test pero usando el framework unittest"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test: abre el navegador
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.driver.get('http://www.python.org')
        self.assertIn('Python', self.driver.title)
        elem = self.driver.find_element(By.NAME, 'q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        self.assertNotIn('No results found.', self.driver.page_source)

    def tearDown(self):
        # Se ejecuta después de cada test: cierra el navegador
        self.driver.close()

if __name__ == '__main__':
    unittest.main(defaultTest='PythonOrgSearch', argv=[''], verbosity=2, exit=False)