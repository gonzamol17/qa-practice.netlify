import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RecoverPasswordPageLocators:
    txtEmail = (By.ID, "email")
    btnRecoverPass = (By.XPATH, "//button[@id='recover-password']")
    messageAlert = (By.ID, "message")


class RecoverPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    def fillEmailToRecover(self, email):
        self.driver.find_element(*RecoverPasswordPageLocators.txtEmail).send_keys(email)

    def selectBtnRecover(self):
        self.driver.find_element(*RecoverPasswordPageLocators.btnRecoverPass).click()

    def getSuccessfullyMessageToRecoverPassword(self):
        return self.driver.find_element(*RecoverPasswordPageLocators.messageAlert).text

    def getColorOfMessageToRecoverPassword(self):
        return self.driver.find_element(*RecoverPasswordPageLocators.messageAlert).value_of_css_property('color')

