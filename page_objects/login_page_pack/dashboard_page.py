from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_label = (By.XPATH, "//a[text()='John Smith']")

    def is_user_label_displayed(self):
        return self.is_displayed(self.__user_label)
