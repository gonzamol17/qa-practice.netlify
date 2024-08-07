import time
import sys
import os
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.ShippingDetailsPage import ShippingDetailsPage


class TestProccedCheckout(BaseClass):

    def test_Procced_Checkout(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        mmp.selectShopEcommerceLink()
        email = "admin@admin.com"
        password = "admin123"
        mmp.doLogin(email, password)
        scp = ShoppingCartPage(driver)
        scp.selectBtnCheckout()
        sdp = ShippingDetailsPage(driver)
        phone = "3521162"
        street = "Los Ravioles"
        city = "Córdoba"
        country = "Egypt"
        sdp.fillAndSendOrder(phone, street, city, country)
        time.sleep(1)
        #print(sdp.getMessageConfirmation())
        assert "Congrats! Your order of" in sdp.getMessageConfirmation()
        time.sleep(2)
