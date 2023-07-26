from selenium.webdriver.common.by import By

from page_objects.registration_page_pack.forgot_password_page import ForgotPasswordPage
from page_objects.registration_page_pack.registration_page import RegistrationPage
from page_objects.registration_page_pack.resend_page import ResendPage
from utilities.ui_utilities.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.XPATH, "//input[@name='username']")
    __user_password_input = (By.XPATH, "//input[@name='password']")
    __login_button = (By.XPATH, "//input[@type='submit']")
    __captcha_checkbox_is_not_checked_text_locator = (
        By.XPATH, "//div[@id='inputbox-error' and contains(@class, 'error-container')]")
    __login_screen_text_locator = (
        By.XPATH, "//h1[@class='heading-size-1' and text()='Log in to your Wowhead Account']")
    __create_new_account_a_locator = (By.XPATH, "//a[@href='/account=signup' and text()='Create one now!']")
    __resend_a_locator = (By.XPATH, "//a[contains(text(), 'Re-Send Verification Email')]")
    __forgot_password_a_locator = (By.XPATH, "//a[contains(text(), 'Reset Password')]")

    def set_email(self, email_value):
        self.send_keys(self.__email_input, email_value)
        return self

    def set_password(self, password_value):
        self.send_keys(self.__user_password_input, password_value)
        return self

    def click_captcha(self):
        """
        Dunno how to play with captcha yet

        """
        pass

    def click_login(self):
        self.click(self.__login_button)
        return self

    def is_login_screen_text_displayed(self):
        element_text = self.get_text(self.__login_screen_text_locator)
        if element_text == 'Log in to your Wowhead Account':
            return self.is_displayed(self.__login_screen_text_locator)
        else:
            return False

    def is_error_captha_text_displayed(self):
        return self.is_displayed(self.__captcha_checkbox_is_not_checked_text_locator)

    def click_new_account(self):
        self.click(self.__create_new_account_a_locator)
        return RegistrationPage(self._driver)

    def click_resend(self):
        self.click(self.__resend_a_locator)
        return ResendPage(self._driver)

    def click_forgot_password(self):
        self.click(self.__forgot_password_a_locator)
        return ForgotPasswordPage(self._driver)
