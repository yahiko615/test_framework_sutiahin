from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.ui_utilities.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    __h1_label = (By.XPATH, "//h1[@class='heading-size-1']")
    __email_input = (By.XPATH, "//input[@type='text' and @name='email']")
    __captcha_checkbox_is_not_checked_text_locator = (
        By.XPATH, "//div[@id='inputbox-error' and contains(@class, 'error-container')]")

    def is_label_displayed(self):
        text_forgot_password = 'Password Reset: Step 1 of 2'
        element_text = self.get_text(self.__h1_label)
        if text_forgot_password in element_text:
            return True
        else:
            return False

    def set_forgot_pass_email(self, email_value):
        self.send_keys(self.__email_input, email_value)
        return self

    def is_error_captha_text_displayed(self):
        return self.is_displayed(self.__captcha_checkbox_is_not_checked_text_locator)
