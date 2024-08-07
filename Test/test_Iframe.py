import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.IframePage import IframePage


class TestIframe(BaseClass):

    def test_Iframe(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 250)")
        time.sleep(1)
        mmp.selectIframeLink()
        ifp = IframePage(driver)
        print(ifp.showMeMainTitle())
        self.driver.execute_script("window.scrollTo(0, 200)")
        driver.switch_to.frame(ifp.showMeIdIframe())
        print(ifp.showMeSecondTitle())
        driver.switch_to.default_content()
        print(ifp.showMeMainTitle())
        driver.switch_to.frame(ifp.showMeIdIframe())
        time.sleep(2)
        assert ifp.showMeTextFromLearnBtn().is_displayed() is False
        ifp.selectBtnLearnMore()
        time.sleep(2)
        assert ifp.showMeTextFromLearnBtn().is_displayed() is True
        assert "This text appears when you click the" in ifp.showMeTextFromLearnBtn().text
        time.sleep(2)



