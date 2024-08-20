import time
import sys
import os

import softest

from POM.CalendarsPage import CalendarsPage
from POM.FileUploadPage import FileUploadPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage


class TestRangeDatePicker(BaseClass):

    def test_RangeDatePicker(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(1)
        mmp.selectdatePickersLink()
        cp = CalendarsPage(driver)
        cp.selectRangeCalendar()
        actualMonthYear = cp.showFromDateRangeCalendar()
        actualYear = actualMonthYear[-4:]
        expectedYear = '2021'
        fullydate = 'Mar 2021'
        expectedDay = '11'
        actualToMonthYear = cp.showToDateRangeCalendar()
        actualToYear = actualMonthYear[-4:]
        expectedToYear = '2021'
        fullydateTo = 'Jul 2021'
        expectedDayTo = '28'
        cp.verifyFromMonthAndYear(actualYear, expectedYear, fullydate, expectedDay)
        time.sleep(3)
        data = cp.verifyToMonthAndYear(actualToYear, expectedToYear, fullydateTo, expectedDayTo)
        assert data == cp.showRangeDateSelected()
        print("El rango de fecha seleccionado fue: ")
        print(cp.showRangeDateSelected())
        time.sleep(3)



