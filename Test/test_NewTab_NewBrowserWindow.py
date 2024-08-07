import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.NewWindowPage import NewWindowPage


class TestNewBrowserWindow(BaseClass):

    def test_NewBrowserWindow(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectNewTabWindowLink()
        time.sleep(1)
        mmp.selectNewBrowserWindowsLink()
        time.sleep(1)
        nbt = NewWindowPage(driver)
        assert "new Browser Window" in nbt.getTitleNewBrowserTab()
        time.sleep(1)
        nbt.selectNewWindowBtn()
        time.sleep(1)
        assert "First" == nbt.getNewTitleFromNewWindow()
        assert "https://qa-practice.netlify.app/window" == nbt.verifyTheNewWindowHasBeenClosed()
        time.sleep(1)


