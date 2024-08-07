import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IframeLocators:
    mainTitle = (By.XPATH, "//h2[contains(text(),'Iframe Example')]")
    firstIframe = (By.ID, "iframe-checkboxes")
    secondTitle = (By.XPATH, "//h1[contains(text(),'Hello, this is an Iframe!')]")
    btnLearnMore = (By.ID, "learn-more")
    txtLearnMore = (By.ID, "show-text")




class IframePage:

    def __init__(self, driver):
        self.driver = driver

    def showMeMainTitle(self):
        return self.driver.find_element(*IframeLocators.mainTitle).text

    def showMeIdIframe(self):
        return self.driver.find_element(*IframeLocators.firstIframe)

    def showMeSecondTitle(self):
        return self.driver.find_element(*IframeLocators.secondTitle).text

    def selectBtnLearnMore(self):
        return self.driver.find_element(*IframeLocators.btnLearnMore).click()

    def showMeTextFromLearnBtn(self):
        return self.driver.find_element(*IframeLocators.txtLearnMore)
