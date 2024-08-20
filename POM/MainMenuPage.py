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
    buttonsLink = (By.XPATH, "//a[contains(text(),'Buttons')]")
    buttonsCheckboxesLink = (By.ID, "checkboxes")
    buttonsRadioButtonLink = (By.ID, "radio-buttons")
    newTabWindowsLink = (By.XPATH, "//a[contains(text(),'New Tab / Window')]")
    newBrowserTabLink = (By.ID, "browser-tab")
    newBrowserWindowLink = (By.ID, "browser-window")
    btnActionLink = (By.ID, "actions")
    doubleClickLink = (By.ID, "double-click")
    scrollingLink = (By.ID, "scrolling")
    mouseOverLink = (By.ID, "mouse-hover")
    showHideLink = (By.ID, "show-hide-elements")
    tablesLink = (By.XPATH, "//a[contains(text(),'Tables')]")
    staticTablesLink = (By.XPATH, "//a[contains(text(),'Static Table')]")
    dinamicTablesLink = (By.XPATH, "//a[contains(text(),'Dynamic Table')]")
    dropDownLink = (By.XPATH, "//a[contains(text(),'Dropdown')]")
    iFrameLink = (By.XPATH, "//a[contains(text(),'Iframes')]")
    alertsLink = (By.XPATH, "//a[contains(text(),'Alerts')]")
    fileUploadLink = (By.XPATH, "//a[contains(text(),'File Upload')]")
    datePickersLink = (By.XPATH, "//a[contains(text(),'Date Pickers')]")
    loaderLink = (By.XPATH, "//a[contains(text(),'Loader')]")





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

    def selectButtonsLink(self):
        self.driver.find_element(*MainMenuPageLocators.buttonsLink).click()

    def selectButtonsCheckboxesLink(self):
        self.driver.find_element(*MainMenuPageLocators.buttonsCheckboxesLink).click()

    def selectButtonsRadioButtonsLink(self):
        self.driver.find_element(*MainMenuPageLocators.buttonsRadioButtonLink).click()

    def selectNewTabWindowLink(self):
        self.driver.find_element(*MainMenuPageLocators.newTabWindowsLink).click()

    def selectNewBrowserTabLink(self):
        self.driver.find_element(*MainMenuPageLocators.newBrowserTabLink).click()

    def selectNewBrowserWindowsLink(self):
        self.driver.find_element(*MainMenuPageLocators.newBrowserWindowLink).click()

    def selectBtnActionLink(self):
        self.driver.find_element(*MainMenuPageLocators.btnActionLink).click()

    def selectBtnActionDoubleClickLink(self):
        self.driver.find_element(*MainMenuPageLocators.doubleClickLink).click()

    def selectScrollingLink(self):
        self.driver.find_element(*MainMenuPageLocators.scrollingLink).click()
    def selectMouseOverLink(self):
        self.driver.find_element(*MainMenuPageLocators.mouseOverLink).click()
    def selectShowHideLink(self):
        self.driver.find_element(*MainMenuPageLocators.showHideLink).click()
    def selectTablesLink(self):
        self.driver.find_element(*MainMenuPageLocators.tablesLink).click()
    def selectStaticTablesLink(self):
        self.driver.find_element(*MainMenuPageLocators.staticTablesLink).click()
    def selectDinamicTablesLink(self):
        self.driver.find_element(*MainMenuPageLocators.dinamicTablesLink).click()
    def selectDropDownLink(self):
        self.driver.find_element(*MainMenuPageLocators.dropDownLink).click()
    def selectIframeLink(self):
        self.driver.find_element(*MainMenuPageLocators.iFrameLink).click()

    def selectAlertsLink(self):
        self.driver.find_element(*MainMenuPageLocators.alertsLink).click()

    def selectFileUploadLink(self):
        self.driver.find_element(*MainMenuPageLocators.fileUploadLink).click()

    def selectdatePickersLink(self):
        self.driver.find_element(*MainMenuPageLocators.datePickersLink).click()

    def selectloaderLink(self):
        self.driver.find_element(*MainMenuPageLocators.loaderLink).click()

