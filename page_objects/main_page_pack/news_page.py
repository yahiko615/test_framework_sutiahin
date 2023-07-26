from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class NewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __h1_label = (By.XPATH, "//h1[@class='heading-size-1' and text()='News']")

    def is_h1_label_displayed(self):
        element_text = self.get_text(self.__h1_label)
        if element_text == 'News':
            return self.is_displayed(self.__h1_label)
        else:
            return False
