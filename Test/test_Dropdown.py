import time
import sys
import os
import pytest
import pytest_check as check

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DropDownPage import DropDownPage


class TestDropDown(BaseClass):

    def test_DropDown(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectDropDownLink()
        time.sleep(1)
        ddp = DropDownPage(driver)
        country = "Uruguay"
        countriesList = ddp.getCountriesListFromDropdown()
        ddp.selectCountryFromSimpleDropdown(countriesList, country)
        #self.assertIn(country, countriesList)
        check.is_in(country, countriesList)
        time.sleep(1)







