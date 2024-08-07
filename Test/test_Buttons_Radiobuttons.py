import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.RadioButtonPage import RadioButtonPage


class TestButtonsRadioButtons(BaseClass):

    def test_ButtonsRadioButtons(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectButtonsLink()
        time.sleep(1)
        mmp.selectButtonsRadioButtonsLink()
        time.sleep(1)
        rbp = RadioButtonPage(driver)
        rbp.getAllTitleFromRadioButtons()
        time.sleep(1)
        rbp.selectAllFromRadioButtons()
        time.sleep(1)
        assert rbp.verifyIfIsDeselectedRadioButton() is False
        print("El radio button deshabilitado es: "+rbp.showTitleFromDeselectedRadioButton())
        time.sleep(1)



