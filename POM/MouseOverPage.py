import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MouseOverLocators:
    btnHoverOver = (By.ID, "button-hover-over")
    msgHoverHide = (By.CSS_SELECTOR, "#content>div.hide")

class MouseOverPage:

    def __init__(self, driver):
        self.driver = driver

    def doHoverOverTheBtn(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*MouseOverLocators.btnHoverOver)).perform()

    def showHideMessage(self):
        return self.driver.find_element(*MouseOverLocators.msgHoverHide).text



