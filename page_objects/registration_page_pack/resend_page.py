from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class ResendPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __h1_label = (By.XPATH, "//h1[@class='heading-size-1']")

    def is_label_displayed(self):
        text_resend = 'Re-Send Verification Email'
        element_text = self.get_text(self.__h1_label)
        if text_resend in element_text:
            return True
        else:
            return False
