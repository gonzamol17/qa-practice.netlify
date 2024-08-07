import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.ScrollingPage import ScrollingPage


class TestBtnActionScrolling(BaseClass):

    def test_BtnActionScrolling(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectBtnActionLink()
        time.sleep(1)
        mmp.selectScrollingLink()
        time.sleep(2)
        slp = ScrollingPage(driver)
        slp.doScrollingDownEfect()
        print(slp.showLastTitleScrollingPage())
        time.sleep(1)
        slp.doScrollingUpEfect()
        time.sleep(1)
        print(slp.showFirstTitleScrollingPage())
        time.sleep(1)






