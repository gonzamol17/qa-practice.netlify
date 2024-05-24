import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegisterFormPageLocators:
    txtFirstName = (By.ID, "firstName")
    txtLastName = (By.ID, "lastName")
    txtPhone = (By.ID, "phone")
    dropdownCountry = (By.ID, "countries_dropdown_menu")
    txtEmail = (By.ID, "emailAddress")
    txtPassword = (By.ID, "password")
    checkBoxAgree = (By.ID, "exampleCheck1")
    successfullyAlert = (By.ID, "message")
    btnRegisterUser = (By.ID, "registerBtn")


class RegisterFormPage:

    def __init__(self, driver):
        self.driver = driver

    def fillAndSendOrder(self, firstName, lastName, phone, country, email, password):
        self.driver.find_element(*RegisterFormPageLocators.txtFirstName).send_keys(firstName)
        self.driver.find_element(*RegisterFormPageLocators.txtLastName).send_keys(lastName)
        self.driver.find_element(*RegisterFormPageLocators.txtPhone).send_keys(phone)
        sel = Select(self.driver.find_element(*RegisterFormPageLocators.dropdownCountry))
        sel.select_by_visible_text(country)
        time.sleep(2)
        self.driver.find_element(*RegisterFormPageLocators.txtEmail).send_keys(email)
        self.driver.find_element(*RegisterFormPageLocators.txtPassword).send_keys(password)
        self.driver.find_element(*RegisterFormPageLocators.checkBoxAgree).click()
        self.driver.find_element(*RegisterFormPageLocators.btnRegisterUser).click()


    def getSuccessfullyRegisterMessage(self):
        return self.driver.find_element(*RegisterFormPageLocators.successfullyAlert).text

