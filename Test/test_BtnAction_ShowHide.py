import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.ShowHidePage import ShowHidePage


class TestBtnActionShowHide(BaseClass):

    def test_BtnActionShowHide(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectBtnActionLink()
        time.sleep(1)
        mmp.selectShowHideLink()
        time.sleep(2)
        shp = ShowHidePage(driver)
        assert shp.msgeIsPresent() is True
        shp.selectShowHideBtn()
        assert shp.msgeIsPresent() is False
        time.sleep(1)
        shp.selectShowHideBtn()
        assert shp.msgeIsPresent() is True







