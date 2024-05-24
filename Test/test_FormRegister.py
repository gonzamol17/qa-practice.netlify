import time
import pytest
import unittest
import sys
import os

from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from POM.MainMenuPage import MainMenuPage
from POM.RegisterFormPage import RegisterFormPage


class TestFormsRegister(BaseClass):

    def test_FormsRegister(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        mmp.selectFormsLink()
        time.sleep(1)
        mmp.selectFormsRegisterLink()
        time.sleep(1)
        rfp = RegisterFormPage(driver)
        firstName = "Pedro"
        lastName = "Alfonso"
        phone = "35126541"
        country = "Austria"
        email = "pedro10@gmail.com"
        password = "Pudo103"
        rfp.fillAndSendOrder(firstName, lastName, phone, country, email, password)
        time.sleep(1)
        assert rfp.getSuccessfullyRegisterMessage() == "The account has been successfully created!"
        time.sleep(1)

