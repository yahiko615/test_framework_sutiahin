from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class ResendPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __page = 'resend'
    __h1_label = (By.XPATH, "//h1[@class='heading-size-1']")

    def is_label_displayed(self):
        return self.is_text_present(self.__page, self.__h1_label)
