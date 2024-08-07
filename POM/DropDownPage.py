import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownLocators:
    simpleDropDown = (By.ID, "dropdown-menu")
    listCountries = (By.CSS_SELECTOR, "#dropdown-menu >option")
    btnMultiLevel = (By.ID, "multi-level-dropdown-btn")
    hoverMeOption = (By.XPATH, "//a[normalize-space()='Hover me for more options']")
    evenMoreOption = (By.XPATH, "//a[normalize-space()='Even More..']")
    anotherLevelOption = (By.XPATH, "//a[normalize-space() = 'another level']")




class DropDownPage:

    def __init__(self, driver):
        self.driver = driver

    def getCountriesListFromDropdown(self):
        paises = self.driver.find_elements(*DropDownLocators.listCountries)
        countriesList = []
        for pais in paises:
            countriesList.append(pais.text)
        print("la cantidad de paises en la lista es: "+str(len(paises)))
        return countriesList

    def selectCountryFromSimpleDropdown(self, countries, expected):
        sdd = Select(self.driver.find_element(*DropDownLocators.simpleDropDown))
        b = 0
        for country in countries:
            if country == expected:
                 sdd.select_by_visible_text(expected)
                 print(country)
                 b = 1
                 break
        if b == 1:
            print("Se encontró el pais dentro del dropdown")
        else:
            print("No se encontró el pais dentro del dropdown")

    def selectBtnMultiLevel(self):
        self.driver.find_element(*DropDownLocators.btnMultiLevel).click()

    def selectMultipleOptions(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*DropDownLocators.hoverMeOption)).pause(1).\
            move_to_element(self.driver.find_element(*DropDownLocators.evenMoreOption)).pause(1).\
            move_to_element(self.driver.find_element(*DropDownLocators.anotherLevelOption)).perform()

    def selectAParticularLevel(self, level):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='"+level+"']").click()



