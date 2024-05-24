import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShippingDetailsPageLocators:
    txtPhone = (By.ID, "phone")
    txtStreet = (By.XPATH, "//input[@name='street']")
    txtCity = (By.XPATH, "//input[@name='city']")
    dropdownCountry = (By.ID, "countries_dropdown_menu")
    btnSubmitOrder = (By.ID, "submitOrderBtn")
    messageConfirmation = (By.ID, "message")


class ShippingDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    def fillAndSendOrder(self, phone, street, city, country):
        self.driver.find_element(*ShippingDetailsPageLocators.txtPhone).send_keys(phone)
        self.driver.find_element(*ShippingDetailsPageLocators.txtStreet).send_keys(street)
        self.driver.find_element(*ShippingDetailsPageLocators.txtCity).send_keys(city)
        sel = Select(self.driver.find_element(*ShippingDetailsPageLocators.dropdownCountry))
        sel.select_by_visible_text(country)
        time.sleep(2)
        self.driver.find_element(*ShippingDetailsPageLocators.btnSubmitOrder).click()

    def getMessageConfirmation(self):
        return self.driver.find_element(*ShippingDetailsPageLocators.messageConfirmation).text








