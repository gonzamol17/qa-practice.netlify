import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoaderLocators:
    title = (By.XPATH, "//h2[normalize-space()='Tada!']")

class LoaderPage:

    def __init__(self, driver):
        self.driver = driver


    def showTitle(self):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Tada!']")))
        return element.text




