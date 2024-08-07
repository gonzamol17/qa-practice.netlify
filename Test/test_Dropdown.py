import time
import sys
import os

import softest

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DropDownPage import DropDownPage


class TestDropDown(BaseClass, softest.TestCase):

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
        country = "Uruguayy"
        countriesList = ddp.getCountriesListFromDropdown()
        ddp.selectCountryFromSimpleDropdown(countriesList, country)
        self.assertIn(country, countriesList)
        time.sleep(1)






