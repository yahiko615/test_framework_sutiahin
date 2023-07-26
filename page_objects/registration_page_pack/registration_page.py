from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.ui_utilities.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    __h1_label = (By.XPATH, "//h1[@class='heading-size-1']")

    def is_label_displayed(self):
        text_registration = 'Registration - Step 1 of 2'
        element_text = self.get_text(self.__h1_label)
        if text_registration in element_text:
            return True
        else:
            return False
