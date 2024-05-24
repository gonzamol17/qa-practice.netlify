import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainMenuPageLocators:
    shopEcommerceLink = (By.ID, "auth-shop")
    email = (By.ID, "email")
    password = (By.ID, "password")
    btnSubmit = (By.ID, "submitLoginBtn")
    productListLink = (By.ID, "products-list")
    formsLink = (By.XPATH, "//a[contains(text(),'Forms')]")
    formsLoginLink = (By.ID, "login")
    formsRegisterLink = (By.ID, "register")
    formsRecoverLink = (By.ID, "recover-password")


class MainMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def selectShopEcommerceLink(self):
        self.driver.find_element(*MainMenuPageLocators.shopEcommerceLink).click()

    def doLogin(self, email, password):
        self.driver.find_element(*MainMenuPageLocators.email).send_keys(email)
        self.driver.find_element(*MainMenuPageLocators.password).send_keys(password)
        self.driver.find_element(*MainMenuPageLocators.btnSubmit).click()

    def selectProductListLink(self):
        self.driver.find_element(*MainMenuPageLocators.productListLink).click()

    def selectFormsLink(self):
        self.driver.find_element(*MainMenuPageLocators.formsLink).click()

    def selectFormsLoginLink(self):
        self.driver.find_element(*MainMenuPageLocators.formsLoginLink).click()

    def selectFormsRegisterLink(self):
        self.driver.find_element(*MainMenuPageLocators.formsRegisterLink).click()

    def selectFormsRecoverPasswordLink(self):
        self.driver.find_element(*MainMenuPageLocators.formsRecoverLink).click()




