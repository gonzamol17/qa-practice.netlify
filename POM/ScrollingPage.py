import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ScrollingLocators:
    titleScrollingPage = (By.CSS_SELECTOR, "#content>h2")
    endTitleScrolling = (By.ID, "the-end")



class ScrollingPage:

    def __init__(self, driver):
        self.driver = driver

    def showFirstTitleScrollingPage(self):
        return self.driver.find_element(*ScrollingLocators.titleScrollingPage).text

    def doScrollingDownEfect(self):
        lastTitle = self.driver.find_element(*ScrollingLocators.endTitleScrolling)
        ActionChains(self.driver).scroll_to_element(lastTitle).perform()

    def doScrollingUpEfect(self):
        firstTitle = self.driver.find_element(*ScrollingLocators.titleScrollingPage)
        ActionChains(self.driver).scroll_to_element(firstTitle).perform()

    def showLastTitleScrollingPage(self):
        return self.driver.find_element(*ScrollingLocators.endTitleScrolling).text
