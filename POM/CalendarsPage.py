import this
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CalendarsPageLocators:
    baseCalendar = (By.ID, "calendar")
    monthYearIcon = (By.CSS_SELECTOR, "table[class=' table-condensed'] th[class='datepicker-switch']")
    nextYear = (By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='next']")
    previousYear = (By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='prev']")
    updatedYear = (By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='datepicker-switch']")
    titleSingleCanlendar = (By.CSS_SELECTOR, ".input-group.date")
    rangeCalendar = (By.ID, "range-date-calendar")
    backDateRange = (By.CSS_SELECTOR, "th.prev.available")
    nextDateRange = (By.CSS_SELECTOR, "th.next.available")
    leftCalendarDate = (By.CSS_SELECTOR, "div[class ='drp-calendar left'] th[class ='month']")
    rightCalendarDate = (By.CSS_SELECTOR, "div[class ='drp-calendar right'] th[class ='month']")
    btnApply = (By.XPATH, "//button[normalize-space()='Apply']")
    dataSelectedFromTo = (By.CSS_SELECTOR, "span.drp-selected")



class CalendarsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBaseCalendar(self):
        self.driver.find_element(*CalendarsPageLocators.baseCalendar).click()

    def getYearAndMonth(self):
        return self.driver.find_element(*CalendarsPageLocators.monthYearIcon).text

    def changeYearAndMonth(self):
        self.driver.find_element(*CalendarsPageLocators.monthYearIcon).click()

    def fastForwardYear(self):
        self.driver.find_element(*CalendarsPageLocators.nextYear).click()

    def delayYear(self):
        self.driver.find_element(*CalendarsPageLocators.previousYear).click()

    def updatedYear(self):
        return self.driver.find_element(*CalendarsPageLocators.updatedYear).text

    def selectMonth(self, month):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='"+str(month)+"']").click()

    def selectDay(self, day):
        self.driver.find_element(By.XPATH, "//td[@class='day'][normalize-space()='"+str(day)+"']").click()

    def closeSingleCalendar(self):
        self.driver.find_element(*CalendarsPageLocators.titleSingleCanlendar).click()

    def showSelectedDate(self):
        return self.driver.find_element(*CalendarsPageLocators.baseCalendar).get_attribute('value')

    def verifyYearMonthDay(self, expectedYear, actualYear, expectedMonth, expectedDay):
        if expectedYear < actualYear:
            #print("el año que se busca seleccionar es inferior al año corriente y por lo tanto hay que Descender")
            while expectedYear < actualYear:
                self.updatedYear()
                self.delayYear()
                time.sleep(1)
                actualYear = self.updatedYear()
        elif expectedYear > actualYear:
            while expectedYear > actualYear:
                 #print("el año que se busca seleccionar es mayor al año corriente y por lo tanto hay que Ascender")
                 #print(self.updatedYear())
                 self.fastForwardYear()
                 time.sleep(1)
                 actualYear = self.updatedYear()
        else:
            print("El año buscado es igual al corriente no hacer nada")
        print("Este es el último año que ha quedado seleccionado")
        print(actualYear)
        self.selectMonth(expectedMonth)
        self.selectDay(expectedDay)
        print(self.showSelectedDate())

    def selectRangeCalendar(self):
        self.driver.find_element(*CalendarsPageLocators.rangeCalendar).click()

    def showRangeDateSelected(self):
        return self.driver.find_element(*CalendarsPageLocators.rangeCalendar).get_attribute('value')

    def selectNextDateRangeCalendar(self):
        self.driver.find_element(*CalendarsPageLocators.nextDateRange).click()

    def selectBackDateRangeCalendar(self):
        self.driver.find_element(*CalendarsPageLocators.backDateRange).click()

    def showFromDateRangeCalendar(self):
        return self.driver.find_element(*CalendarsPageLocators.leftCalendarDate).text

    def showToDateRangeCalendar(self):
        return self.driver.find_element(*CalendarsPageLocators.rightCalendarDate).text

    def selectApplyFilterBtn(self):
        self.driver.find_element(*CalendarsPageLocators.btnApply).click()

    def getDataSelectedFromAndTo(self):
        return self.driver.find_element(*CalendarsPageLocators.dataSelectedFromTo).text

    def verifyFromMonthAndYear(self, actualYear, expectedYear, fullydate, expectedDay):
        fulldate = self.showFromDateRangeCalendar()
        if expectedYear >= actualYear:
            # while expectedYear >= actualYear:
            #     actualYear = self.showFromDateRangeCalendar()[-4:]
            #     actualUpdatedYear = self.showFromDateRangeCalendar()[-4:]
            #     actualUpdatedMonth = self.showFromDateRangeCalendar()[0:3]
            #     fulldate = self.showFromDateRangeCalendar()
            #     print(actualUpdatedYear)
            #     print(fulldate)
            #     print(actualUpdatedMonth)
            #     self.selectNextDateRangeCalendar()
            while fulldate != fullydate:
                self.selectNextDateRangeCalendar()
                fulldate = self.showFromDateRangeCalendar()
                #print(fulldate)
            days = self.driver.find_elements(By.XPATH, "//body[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr/td[not(contains(@class, 'weekend off ends available')) and not(contains(@class, 'off ends available'))]")
            for day in days:
                if day.text == expectedDay:

                    self.driver.find_element(By.XPATH, "//div[@class='drp-calendar left'] // div[@ class ='calendar-table'] // td[@ class ='available' or @ class = 'active start-date available' or @ class = 'available in-range' or @ class = 'weekend available in-range' or @ class ='active end-date in-range available' or @ class ='in-range available' or @ class ='weekend in-range available' or @class='weekend available' or @class='weekend active start-date available'][normalize-space()='" + str(expectedDay) + "']").click()
                    #self.driver.find_element(By.XPATH, "(//td[contains(text(),'13')])[1]").click()
                    #self.driver.find_element(By.XPATH, "//div[@class='drp-calendar right'] // div[@ class ='calendar-table'] // td[@ class ='available' or @ class = 'active start-date available' or @ class = 'available in-range' or @ class = 'weekend available in-range' or @ class ='active end-date in-range available' or @ class ='in-range available' or @ class ='weekend in-range available' or @class='weekend available' or @class='weekend active start-date available'][normalize-space()='21']").click()
                    #time.sleep(2)
                    break
        elif expectedYear < actualYear:
            #print("ver este escenario")
            while fulldate != fullydate:
                self.selectBackDateRangeCalendar()
                fulldate = self.showFromDateRangeCalendar()
                print(fulldate)
            days = self.driver.find_elements(By.XPATH, "//body[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr/td[not(contains(@class, 'weekend off ends available')) and not(contains(@class, 'off ends available'))]")
            for day in days:
                if day.text == expectedDay:
                    self.driver.find_element(By.XPATH, "//div[@class='drp-calendar left'] // div[@ class ='calendar-table'] // td[@ class ='available' or @ class = 'active start-date available' or @ class = 'available in-range' or @ class = 'weekend available in-range' or @ class ='active end-date in-range available' or @ class ='in-range available' or @ class ='weekend in-range available' or @class='weekend available' or @class='weekend active start-date available'][normalize-space()='" + str(expectedDay) + "']").click()
                    time.sleep(2)
                    break



    def verifyToMonthAndYear(self, actualToYear, expectedToYear, fullydateTo, expectedDayTo):
        fulldate = self.showToDateRangeCalendar()
        if expectedToYear >= actualToYear:
            while fulldate != fullydateTo:
                self.selectNextDateRangeCalendar()
                fulldate = self.showToDateRangeCalendar()
            days = self.driver.find_elements(By.XPATH,
                                            "//body[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr/td[not(contains(@class, 'weekend off ends available')) and not(contains(@class, 'off ends available'))]")
            for day in days:
                if day.text == expectedDayTo:
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='drp-calendar right'] // div[@ class ='calendar-table'] // td[@ class ='available' or @ class = 'active start-date available' or @ class = 'available in-range' or @ class = 'weekend available in-range' or @ class ='active end-date in-range available' or @ class ='in-range available' or @ class ='weekend in-range available' or @class='weekend available' or @class='weekend active start-date available'][normalize-space()='" + str(
                                                 expectedDayTo) + "']").click()
                    time.sleep(2)
                    data = self.getDataSelectedFromAndTo()
                    self.selectApplyFilterBtn()
                    return data
        elif expectedToYear < actualToYear:
            # print("ver este escenario")
            while fulldate != fullydateTo:
                self.selectBackDateRangeCalendar()
                fulldate = self.showToDateRangeCalendar()
                print(fulldate)
            days = self.driver.find_elements(By.XPATH,
                                             "//body[1]/div[2]/div[3]/div[1]/table[1]/tbody[1]/tr/td[not(contains(@class, 'weekend off ends available')) and not(contains(@class, 'off ends available'))]")
            for day in days:
                if day.text == expectedDayTo:
                    self.driver.find_element(By.XPATH,
                                             "//div[@class='drp-calendar right'] // div[@ class ='calendar-table'] // td[@ class ='available' or @ class = 'active start-date available' or @ class = 'available in-range' or @ class = 'weekend available in-range' or @ class ='active end-date in-range available' or @ class ='in-range available' or @ class ='weekend in-range available' or @class='weekend available' or @class='weekend active start-date available'][normalize-space()='" + str(
                                                 expectedDayTo) + "']").click()
                    data = self.getDataSelectedFromAndTo()
                    self.selectApplyFilterBtn()
                    return data




