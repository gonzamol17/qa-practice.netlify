import time
import sys
import os

from POM.CalendarsPage import CalendarsPage
from POM.FileUploadPage import FileUploadPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DropDownPage import DropDownPage


class TestDatePickers(BaseClass):

    def test_DatePickers(self):
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
        expectedYear = '2020'
        expectedMonth = 'Nov'
        expectedDay = "24"
        cp.changeYearAndMonth()
        if expectedYear < actualYear:
            print("el año que se busca seleccionar es inferior al año corriente y por lo tanto hay que Descender")
            #cp.changeYearAndMonth()
            while expectedYear < actualYear:
                print(cp.updatedYear())
                #cp.changeYearAndMonth()
                cp.delayYear()
                time.sleep(1)
                actualYear = cp.updatedYear()
                #cp.delayYear()

        elif expectedYear > actualYear:
            while expectedYear > actualYear:
                print("el año que se busca seleccionar es mayor al año corriente y por lo tanto hay que Ascender")
                print(cp.updatedYear())
                cp.fastForwardYear()
                time.sleep(1)
                actualYear = cp.updatedYear()
        else:
            print("El año buscado es igual al corriente no hacer nada")

        print("Este es el último año que ha quedado seleccionado")
        print(actualYear)
        cp.selectMonth(expectedMonth)
        cp.selectDay(expectedDay)
        print(cp.showSelectedDate())
        assert expectedYear in cp.showSelectedDate()
        assert expectedDay in cp.showSelectedDate()
        time.sleep(4)



