import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShowHideLocators:
    txtVisible = (By.ID, "hiddenText")
    showHideBtn = (By.ID, "showHideBtn")


class ShowHidePage:

    def __init__(self, driver):
        self.driver = driver

    def selectShowHideBtn(self):
        self.driver.find_element(*ShowHideLocators.showHideBtn).click()

    def msgeIsPresent(self):
        return self.driver.find_element(*ShowHideLocators.txtVisible).is_displayed()

    def msgeIsNotPresent(self):
        return self.driver.find_element(*ShowHideLocators.txtVisible).is_displayed()

