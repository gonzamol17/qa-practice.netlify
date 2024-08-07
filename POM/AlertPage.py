import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AlertPageLocators:
    btnAlert = (By.ID, "alert-btn")
    btnConfirm = (By.ID, "confirm-btn")



class AlertPage:

    def __init__(self, driver):
        self.driver = driver

    def handleAlertPopUp(self):
        self.driver.find_element(*AlertPageLocators.btnAlert).click()
        wait = WebDriverWait(self.driver, timeout=4)
        alert = wait.until(lambda d: d.switch_to.alert)
        text = alert.text
        if text == "Hello! I am an alert box!!":
            print("Se encontró el texto buscado")
            print(text)

        else:
            print("El pop up, no tenía el mensaje esperado")
        alert.accept()

    def handleConfirmPopUp(self):
        self.driver.find_element(*AlertPageLocators.btnConfirm).click()
        wait = WebDriverWait(self.driver, timeout=4)
        alert = wait.until(lambda d: d.switch_to.alert)
        text = alert.text
        if text == "Press a button!\nEither OK or Cancel.":
            print("Se encontró el texto buscado")
            print(text)

        else:
            print("El pop up, no tenía el mensaje esperado")
        alert.dismiss()
        time.sleep(4)





