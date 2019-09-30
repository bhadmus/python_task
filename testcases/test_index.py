import unittest
from webdriver import Driver
from values import mnemonics
from pageobjects.homepage import Homepage

class PythonCy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(mnemonics.home)

    def test_search_product_check_out(self):
        search = Homepage(self.driver)
        search.search_item()

    def tearDown(self):
        self.driver.instance.quit()

if __name__=='__main__':
    unittest.main()