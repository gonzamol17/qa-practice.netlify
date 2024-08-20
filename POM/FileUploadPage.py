import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FileUploadPageLocators:
    btnSeleccionarArchivo = (By.ID, "file_upload")
    btnSubmit = (By.XPATH, "//button[contains(text(),'Submit')]")
    successfullMsg = (By.ID, "file_upload_response")


class FileUploadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBtnSelectFile(self, location):
        self.driver.find_element(*FileUploadPageLocators.btnSeleccionarArchivo).send_keys(location)
        time.sleep(1)

    def selectBtnSubmit(self):
        self.driver.find_element(*FileUploadPageLocators.btnSubmit).click()

    def showSuccessfullMsgFileUpload(self):
        return self.driver.find_element(*FileUploadPageLocators.successfullMsg).text
