import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.CheckboxesPage import CheckboxesPage


class TestButtonsCheckboxes(BaseClass):

    def test_ButtonsCheckboxes(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectButtonsLink()
        time.sleep(1)
        mmp.selectButtonsCheckboxesLink()
        time.sleep(1)
        cbp = CheckboxesPage(driver)
        cbp.selectAllCheckboxes()
        time.sleep(1)
        check = cbp.verifyIfCheckboxIsSelected()
        for che in check:
            assert che.is_selected() is True
        time.sleep(1)
        cbp.selectResetButton()
        time.sleep(1)
        for che in check:
            assert che.is_selected() is False
        time.sleep(1)
        cbp.showAllTitles()
        time.sleep(1)


