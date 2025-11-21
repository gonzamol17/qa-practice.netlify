import time
import sys
import os
import pytest
import pytest_check as check

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DropDownPage import DropDownPage


class TestDropDownAndSlide(BaseClass):

    def test_DropDownAndSlide(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectDropDownLink()
        time.sleep(1)
        ddp = DropDownPage(driver)
        ddp.selectBtnMultiLevel()
        time.sleep(1)
        ddp.selectMultipleOptions()
        level = "4th level - 2"
        ddp.selectAParticularLevel(level)
        aux = level.replace(" ", "")
        aux = aux[3:10]
        #assert aux in self.driver.current_url
        # Soft assert
        check.is_in(aux, driver.current_url)
        time.sleep(2)






