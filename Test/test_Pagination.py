import time
import sys
import os

from selenium.webdriver.support.wait import WebDriverWait

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.PaginationPage import PaginationPage


class TestPagination(BaseClass):

    def test_Pagination(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 650)")
        time.sleep(1)
        mmp.selectPaginationLink()
        pp = PaginationPage(driver)
        actualLblPaginationItems = pp.getAllElementsFromPagination()
        expectedLblPaginationItems = ['You clicked page no. 1', 'You clicked page no. 2', 'You clicked page no. 3', 'You clicked the "Next" button']
        assert actualLblPaginationItems == expectedLblPaginationItems
        time.sleep(2)



