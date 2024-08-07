import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.NewBrowserTabPage import NewBrowserTabPage


class TestNewBrowserTab(BaseClass):

    def test_NewBrowserTab(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectNewTabWindowLink()
        time.sleep(1)
        mmp.selectNewBrowserTabLink()
        time.sleep(1)
        nbt = NewBrowserTabPage(driver)
        assert "Switch to a" in nbt.getTitleNewBrowserTab()
        time.sleep(1)
        parent_handle = nbt.showDataFromCurrentTab()
        time.sleep(1)
        nbt.selectNewTabBtn()
        originalUrl = nbt.managerSecondTab(parent_handle)
        assert "qa-practice.netlify.app/tab" in originalUrl
        time.sleep(1)


