import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class StaticTableLocators:
    tableAllElements = (By.ID, "peopleTable")
    rowTable = (By.CSS_SELECTOR, "#peopleTable > tbody > tr")
    columnTable = (By.CSS_SELECTOR, "#peopleTable > thead > tr > th")
    dinamicTableAllElements = (By.ID, "data-table")


class StaticTablePage:

    def __init__(self, driver):
        self.driver = driver

    def showAllElementsFromTable(self):
        elements = self.driver.find_elements(*StaticTableLocators.tableAllElements)
        for element in elements:
            print(element.text)


    # def showTableWithTheCorrectFormat(self):
    #     rows = self.driver.find_elements(*StaticTableLocators.rowTable)
    #     columns = self.driver.find_elements(*StaticTableLocators.columnTable)
    #     countrows = len(rows)
    #     countcolumn = len(columns)
    #     print("\n" + "#" + "     " + "First" + "      " + "Last" + "     " + "Email")
    #     for r in range(2, countrows + 2):
    #         for c in range(1, countcolumn + 1):
    #             value = self.driver.find_element(By.CSS_SELECTOR, "#peopleTable > tbody > tr:nth-child(" + str(r) + "> td:nth-child(" + str(c) + ")").text
    #             print(value, end="        ")
    #         print()

    def foundAParticularEmailFromTable(self, ema):
        emails = self.driver.find_elements(By.CSS_SELECTOR, "#peopleTable>tbody>tr>td:nth-child(4)")
        aux = "No se ha encontrado el email buscado"
        for email in emails:
            if email.text == ema:
                return "El email buscado encontrado es "+email.text
        return aux



    def showAllElementsFromDinamicTable(self):
        elements = self.driver.find_elements(*StaticTableLocators.dinamicTableAllElements)
        for element in elements:
            print(element.text)
