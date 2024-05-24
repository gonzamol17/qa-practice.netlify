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


class TestFirstExmaple(BaseClass):

    def test_FirstExample(self):
        log = self.get_Logger()
        log.info("Se llegó a la home page")
        driver = self.driver




