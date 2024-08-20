import time
import sys
import os

from selenium.webdriver.support.wait import WebDriverWait

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.LoaderPage import LoaderPage


class TestLoader(BaseClass):

    def test_Loader(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 650)")
        time.sleep(1)
        mmp.selectloaderLink()
        lp = LoaderPage(driver)
        assert lp.showTitle() == "Tada!"
        time.sleep(2)



