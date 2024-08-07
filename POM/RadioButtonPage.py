import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RadioButtonPageLocators:
    radioButtons = (By.XPATH, "//label[@class='form-check-label']")
    radioButtonsDisabled = (By.ID, "radio-button4")
    titleRadioButtonDisabled = (By.XPATH, "//label[@class='form-check-label disabled']")


class RadioButtonPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllTitleFromRadioButtons(self):
        radios = self.driver.find_elements(*RadioButtonPageLocators.radioButtons)
        for radio in radios:
            print(radio.text)

    def selectAllFromRadioButtons(self):
        radios = self.driver.find_elements(*RadioButtonPageLocators.radioButtons)
        for radio in radios:
            time.sleep(1)
            radio.click()

    def verifyIfIsDeselectedRadioButton(self):
        return self.driver.find_element(*RadioButtonPageLocators.radioButtonsDisabled).is_enabled()

    def showTitleFromDeselectedRadioButton(self):
        return self.driver.find_element(*RadioButtonPageLocators.titleRadioButtonDisabled).text






