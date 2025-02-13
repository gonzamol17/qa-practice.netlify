import time
import sys
import os

from Utils.BaseClass import BaseClass

#sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DoubleClickPage import DoubleClickPage


class TestBtnActionDoubleClick(BaseClass):

    def test_BtnActionDoubleClick(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectBtnActionLink()
        time.sleep(1)
        mmp.selectBtnActionDoubleClickLink()
        time.sleep(1)
        dcp = DoubleClickPage(driver)
        assert dcp.showTitleFromDoubleClickPage() == "Double Click on Button Example"
        time.sleep(1)
        dcp.selectDoubleClickBtn()
        time.sleep(1)
        assert dcp.showSuccessfullMessage() == "Congrats, you double clicked!"
        time.sleep(2)




