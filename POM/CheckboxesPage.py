import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckboxesPageLocators:
    checkboxes = (By.XPATH, "//input[@type='checkbox']")
    btnReset = (By.XPATH, "//button[contains(text(),'Reset')]")
    titlesOfCheckboxes = (By.XPATH, "//label[@class='form-check-label']")


class CheckboxesPage:

    def __init__(self, driver):
        self.driver = driver

    def selectAllCheckboxes(self):
        checkboxes = self.driver.find_elements(*CheckboxesPageLocators.checkboxes)
        for checkbox in checkboxes:
            checkbox.click()

    def verifyIfCheckboxIsSelected(self):
        checkboxes = self.driver.find_elements(*CheckboxesPageLocators.checkboxes)
        return checkboxes

    def selectResetButton(self):
        self.driver.find_element(*CheckboxesPageLocators.btnReset).click()

    def showAllTitles(self):
        titles = self.driver.find_elements(*CheckboxesPageLocators.titlesOfCheckboxes)
        for checkbox in titles:
            print(checkbox.text)






