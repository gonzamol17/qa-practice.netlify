import time
import pytest
import unittest
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.MainMenuPage import MainMenuPage
from POM.ShoppingCartPage import ShoppingCartPage


class TestAddProductAndRemoveIt(BaseClass):

    def test_AddProductAndRemoveIt(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        mmp.selectProductListLink()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        scp = ShoppingCartPage(driver)
        product = "Nokia 105"
        scp.searchProduct(product)
        print("The total numbers of products founded was: "+str(scp.getTotalOfProducts()))
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, -300)")
        assert product in scp.getTitleOfSelectedProduct()
        print("The total price of the selected product is: "+scp.getTotalPriceOfSelectedProduct())
        time.sleep(1)
        scp.selectRemoveProduct()
        time.sleep(2)




