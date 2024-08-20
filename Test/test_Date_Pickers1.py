import time
import sys
import os

import softest

from POM.CalendarsPage import CalendarsPage
from POM.FileUploadPage import FileUploadPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage


class TestDatePickers1(BaseClass):

    def test_DatePickers1(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(1)
        mmp.selectdatePickersLink()
        cp = CalendarsPage(driver)
        cp.selectBaseCalendar()
        time.sleep(2)
        monthYear = cp.getYearAndMonth()
        actualYear = monthYear[-4:]
        expectedYear = '2026'
        expectedMonth = 'Feb'
        expectedDay = "10"
        cp.changeYearAndMonth()
        cp.verifyYearMonthDay(expectedYear, actualYear, expectedMonth, expectedDay)
        assert expectedYear in cp.showSelectedDate()
        assert expectedDay in cp.showSelectedDate()
        time.sleep(2)



