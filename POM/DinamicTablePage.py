import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DinamicTableLocators:
    tableAllElements = (By.ID, "peopleTable")
    rowTable = (By.CSS_SELECTOR, "#data-tbody > tr")
    columnTable = (By.CSS_SELECTOR, "#data-tbody>tr:nth-child(1)>td")


class DinamicTablePage:

    def __init__(self, driver):
        self.driver = driver


    def showAllElementsFromDinamicTable(self):
        rows = self.driver.find_elements(*DinamicTableLocators.rowTable)
        columns = self.driver.find_elements(*DinamicTableLocators.columnTable)
        countrows = len(rows)
        countcolumn = len(columns)
        print("numero de filas"+str(countrows))
        print("numero de columnas"+str(countcolumn))
        print("\n" +"First Name" + "    " + "Last Name" + "     " + "Age" + "        " + "Email" + "                      " + "City" + "            " + "Country")
        for r in range(1, countrows + 1):
            for c in range(2, countcolumn + 1):
                value = self.driver.find_element(By.CSS_SELECTOR, "#data-tbody > tr:nth-child(" + str(r) +")>td:nth-child(" +str(c) +")").text
                print(value, end="        ")
            print()
