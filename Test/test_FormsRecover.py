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
from POM.RecoverPasswordPage import RecoverPasswordPage


class TestFormsRecover(BaseClass):

    def test_FormsRecover(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        mmp.selectFormsLink()
        time.sleep(1)
        mmp.selectFormsRecoverPasswordLink()
        time.sleep(1)
        rpp = RecoverPasswordPage(driver)
        email = "pepito@gmail.com"
        rpp.fillEmailToRecover(email)
        time.sleep(1)
        rpp.selectBtnRecover()
        time.sleep(1)
        assert "An email with the new password has been sent to "+email in rpp.getSuccessfullyMessageToRecoverPassword()
        assert "rgba(114, 28, 36, 1)" == rpp.getColorOfMessageToRecoverPassword()
        time.sleep(1)



