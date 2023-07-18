from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class PetSpell(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __slider_progress_locator = (By.XPATH, "//div[@class='slider-track-bar-progress']")
    __slider_locator = (By.XPATH, "//div[@class='slider-track-handle']")
    __searched_spell_page_locator = (By.XPATH, "//h1[@class='heading-size-1']")

    def move_slider(self):
        self.move_slider_to(self.__slider_locator, self.__slider_progress_locator, desired_position="50%")
        return self

    def right_dmg_scaling_is_displayed(self):
        return self.get_element_style(self.__slider_locator) == "left: 50%;"

    def right_spell_found(self):
        return self.is_displayed(self.__searched_spell_page_locator) \
            and self.get_text(self.__searched_spell_page_locator) == 'Expunge'

    def right_spell_found_after_column_sorting(self):
        return self.is_displayed(self.__searched_spell_page_locator) \
            and self.get_text(self.__searched_spell_page_locator) == 'Evolving Bite'
