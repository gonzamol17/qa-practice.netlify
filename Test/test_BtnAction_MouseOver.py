import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.MouseOverPage import MouseOverPage


class TestBtnActionMouseOver(BaseClass):

    def test_BtnActionMouseOver(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectBtnActionLink()
        time.sleep(1)
        mmp.selectMouseOverLink()
        time.sleep(1)
        mop = MouseOverPage(driver)
        mop.doHoverOverTheBtn()
        time.sleep(2)
        assert "I am shown when someone" in mop.showHideMessage()
        time.sleep(2)






