import time
import sys
import os
from POM.MainMenuPage import MainMenuPage
from POM.AlertPage import AlertPage
from Utils.BaseClass import BaseClass
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


class TestAlertExample(BaseClass):

      def test_AlertExample(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        mmp.selectAlertsLink()
        ap = AlertPage(driver)
        ap.handleAlertPopUp()
        time.sleep(2)
        ap.handleConfirmPopUp()
        time.sleep(2)




