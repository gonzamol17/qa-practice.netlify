import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class NewWindowLocators:
    titeOfPage = (By.CSS_SELECTOR, "#content>h2")
    btnPressMe = (By.ID, "newWindowBtn")
    columnFirst = (By.CSS_SELECTOR, "#peopleTable tr > th:nth-child(2)")


class NewWindowPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitleNewBrowserTab(self):
        return self.driver.find_element(*NewWindowLocators.titeOfPage).text

    def selectNewWindowBtn(self):
        self.driver.find_element(*NewWindowLocators.btnPressMe).click()
        all_handles = self.driver.window_handles
        canthandles = (len(all_handles))
        self.driver.switch_to.window(self.driver.window_handles[canthandles - 1])

    def getNewTitleFromNewWindow(self):
        return self.driver.find_element(*NewWindowLocators.columnFirst).text

    def verifyTheNewWindowHasBeenClosed(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self.driver.current_url

