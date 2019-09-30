from time import sleep

from values import mnemonics

class Homepage:
    def __init__(self,driver):
        self.driver = driver


    def search_item(self):
        self.driver.instance.find_element_by_css_selector(mnemonics.box).send_keys(mnemonics.item_search)
        self.driver.instance.find_element_by_css_selector(mnemonics.btn_search).click()
        sleep(5)
        self.driver.instance.find_element_by_css_selector(mnemonics.price).click()
        sleep(5)
        self.driver.instance.find_element_by_css_selector(mnemonics.item).click()
        sleep(5)
        self.driver.instance.find_element_by_css_selector(mnemonics.addCart).click()
        sleep(5)
        self.driver.instance.find_element_by_css_selector(mnemonics.proceed).click()
        sleep(5)
        btn_text= self.driver.instance.find_element_by_link_text(mnemonics.createBtn)
        assert btn_text.text == mnemonics.createBtn

