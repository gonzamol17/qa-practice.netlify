import time
import sys
import os

import softest

from POM.FileUploadPage import FileUploadPage
from Utils.BaseClass import BaseClass

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM.MainMenuPage import MainMenuPage
from POM.DropDownPage import DropDownPage


class TestFileUpload(BaseClass):

    def test_FileUpload(self):
        log = self.get_Logger()
        log.info("Se está por loguear en la página")
        driver = self.driver
        mmp = MainMenuPage(driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        mmp.selectFileUploadLink()
        fup = FileUploadPage(driver)
        location = "C:\\Users\\User\\PycharmProjects\\QaPracticeNetlif\\Screenshots\\MacroSolucionesLogo.png"
        fup.selectBtnSelectFile(location)
        time.sleep(1)
        fup.selectBtnSubmit()
        time.sleep(1)
        assert "You have successfully uploaded" in fup.showSuccessfullMsgFileUpload()
        time.sleep(2)






