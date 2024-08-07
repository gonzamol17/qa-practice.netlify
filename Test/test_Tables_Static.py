import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.StaticTablePage import StaticTablePage


class TestTablesStatic(BaseClass):

    def test_TablesStatic(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectTablesLink()
        time.sleep(1)
        mmp.selectStaticTablesLink()
        time.sleep(1)
        stp = StaticTablePage(driver)
        stp.showAllElementsFromTable()
        time.sleep(2)
        email = "bobby_23@gmail.com"
        msg = stp.foundAParticularEmailFromTable(email)
        print(msg)
        time.sleep(1)




