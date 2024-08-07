import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class NewBrowserTabLocators:
    titeOfPage = (By.CSS_SELECTOR, "#content>h2")
    btnSwitchMe = (By.ID, "newTabBtn")
    btnPressMe = (By.ID, "newWindowBtn")


class NewBrowserTabPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitleNewBrowserTab(self):
        return self.driver.find_element(*NewBrowserTabLocators.titeOfPage).text

    def selectNewTabBtn(self):
        self.driver.find_element(*NewBrowserTabLocators.btnSwitchMe).click()

    def showDataFromCurrentTab(self):
        print("La primera url es: " + self.driver.current_url)
        parent_handle = self.driver.current_window_handle
        print("Y el primer handle es: " + parent_handle)
        return parent_handle

    def managerSecondTab(self, parent):
        all_handles = self.driver.window_handles
        canthandles = (len(all_handles))
        self.driver.switch_to.window(self.driver.window_handles[canthandles - 1])
        second_handle = self.driver.current_window_handle
        print("La segunda url es: " + self.driver.current_url)
        print("Y la segunda handle es: " + second_handle)
        self.driver.close()
        self.driver.switch_to.window(parent)
        return self.driver.current_url


    def selectNewWindowBtn(self):
        self.driver.find_element(*NewBrowserTabLocators.btnPressMe).click()

