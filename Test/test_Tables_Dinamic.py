import time
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DinamicTablePage import DinamicTablePage


class TestTablesDinamic(BaseClass):

    def test_TablesDinamic(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectTablesLink()
        time.sleep(1)
        mmp.selectDinamicTablesLink()
        time.sleep(1)
        dtp = DinamicTablePage(driver)
        dtp.showAllElementsFromDinamicTable()
        time.sleep(1)





