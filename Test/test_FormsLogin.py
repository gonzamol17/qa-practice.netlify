import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.ShoppingCartPage import ShoppingCartPage


class TestFormsLogin(BaseClass):

    def test_FormsLogin(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        mmp.selectFormsLink()
        time.sleep(1)
        mmp.selectFormsLoginLink()
        time.sleep(1)
        email = "admin@admin.com"
        password = "admin123"
        mmp.doLogin(email, password)
        scp = ShoppingCartPage(driver)
        assert scp.verifyBtnCheckoutIsVisible()
        time.sleep(1)
