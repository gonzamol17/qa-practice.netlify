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


class TestLoginShopEcommerce(BaseClass):

    def test_LoginShopEcommerce(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        mmp.selectShopEcommerceLink()
        email = "admin@admin.com"
        password = "admin123"
        mmp.doLogin(email, password)
        scp = ShoppingCartPage(driver)
        assert scp.verifyBtnCheckoutIsVisible()
        time.sleep(2)
