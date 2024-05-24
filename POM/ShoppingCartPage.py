import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShoppingCartPageLocators:
    btnCheckout = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
    listTitleOfProducts = (By.CSS_SELECTOR, "span.shop-item-title")
    lblTitleSelectProduct = (By.CSS_SELECTOR, "span.cart-item-title")
    lblTotalPriceOfSelectedProduct = (By.CSS_SELECTOR, "span.cart-total-price")
    btnRemove = (By.XPATH, "//button[contains(text(),'REMOVE')]")



class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

    def verifyBtnCheckoutIsVisible(self):
        return self.driver.find_element(*ShoppingCartPageLocators.btnCheckout).is_displayed()

    def selectBtnCheckout(self):
        self.driver.find_element(*ShoppingCartPageLocators.btnCheckout).click()

    def searchProduct(self, value):
        products = self.driver.find_elements(*ShoppingCartPageLocators.listTitleOfProducts)
        n = 1
        for product in products:
            if value in product.text:
                self.driver.find_element(By.CSS_SELECTOR, "#prooood div:nth-child("+str(n)+")>div>button").click()
                print("The product selected was "+product.text)
                break
            n = n+1

    def getTotalOfProducts(self):
        products = len(self.driver.find_elements(*ShoppingCartPageLocators.listTitleOfProducts))
        return products

    def getTitleOfSelectedProduct(self):
        return self.driver.find_element(*ShoppingCartPageLocators.lblTitleSelectProduct).text

    def getTotalPriceOfSelectedProduct(self):
        return self.driver.find_element(*ShoppingCartPageLocators.lblTotalPriceOfSelectedProduct).text

    def selectRemoveProduct(self):
        self.driver.find_element(*ShoppingCartPageLocators.btnRemove).click()



    



