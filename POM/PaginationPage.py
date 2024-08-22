import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class PaginationLocators:
    elementsPagination = (By.CSS_SELECTOR, ".page-item.page-item a")
    resultLabel = (By.ID, "pageResult")


class PaginationPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllElementsFromPagination(self):
        itemsPag = self.driver.find_elements(*PaginationLocators.elementsPagination)
        resultsPagination = []
        for item in itemsPag:
            if item.text != "Previous":
                item.click()
                resultsPagination.append(self.driver.find_element(*PaginationLocators.resultLabel).text)
        return resultsPagination













