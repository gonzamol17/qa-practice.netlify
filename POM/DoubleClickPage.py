import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DoubleClickPageLocators:
    titleDoubleClick = (By.CSS_SELECTOR, "#content>h2")
    btnDoubleClick = (By.ID, "double-click-btn")
    lblResulMessage = (By.ID, "double-click-result")


class DoubleClickPage:

    def __init__(self, driver):
        self.driver = driver

    def showTitleFromDoubleClickPage(self):
        return self.driver.find_element(*DoubleClickPageLocators.titleDoubleClick).text

    def selectDoubleClickBtn(self):
        btn = self.driver.find_element(*DoubleClickPageLocators.btnDoubleClick)
        ActionChains(self.driver).double_click(btn).perform()

    def showSuccessfullMessage(self):
        return self.driver.find_element(*DoubleClickPageLocators.lblResulMessage).text

