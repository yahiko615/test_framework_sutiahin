from selenium.webdriver.common.by import By

from page_objects.battle_pet_pack.pet_spell_page import PetSpell
from utilities.ui_utilities.base_page import BasePage


class BattlePetAbilities(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __input_search_locator = (By.XPATH, "//input[@id='filter-facet-name']")
    __search_button_locator = (By.XPATH, "//button[@type='submit']")
    __search_result_locator = (By.XPATH, "//a[@class='listview-cleartext']")
    __remove_filter_locator = (By.XPATH, "//button[@type='button']")
    __abilities_list_page_locator = (
        By.XPATH, "//span[b[contains(text(), '1')] and b[contains(text(), '100')] and b[contains(text(), '833')]]")
    __column_filter_locator = \
        (By.XPATH, "//a[@class='listview-option-button listview-option-button-filters fa fa-filter']")
    __add_column_filter_locator = (By.XPATH, "//a[@class='fa fa-plus']")
    __healing_filter_locator = (By.XPATH, "//div[@class='menu-item'][contains(a/span/text(), 'Healing')]")
    __healing_column_filter_input_locator = (By.CSS_SELECTOR, ".listview-filters-columns-filter-text")
    __name_column_name_locator = (By.XPATH, "//th[@colspan='2']")
    __name_column_first_item_locator = (
    By.XPATH, "//a[contains(@class, 'listview-cleartext') and text() = '[DNT] INSTADEAD']")
    __name_column_second_item_locator = (
    By.XPATH, "//a[contains(@class, 'listview-cleartext') and text() = '[DNT] TRAP HELP']")

    def set_search(self, search_value):
        self.send_keys(self.__input_search_locator, search_value)
        return self

    def click_search(self):
        self.click_via_js(self.__search_button_locator)
        return self

    def click_search_result(self):
        self.click(self.__search_result_locator)
        return PetSpell(self._driver)

    def is_spell_found(self):
        return self.is_displayed(self.__search_result_locator)

    def click_remove_filter(self):
        return self.click(self.__remove_filter_locator)

    def is_default_list_of_results_is_displayed(self):
        return self.is_displayed(self.__abilities_list_page_locator)

    def click_column_filtering(self):
        self.click(self.__column_filter_locator)
        return self

    def click_add_column_filter(self):
        self.click(self.__add_column_filter_locator)
        return self

    def click_add_column_filter_healing(self):
        self.click(self.__healing_filter_locator)
        return self

    def set_healing(self):
        # I don't know how it's possible, but there is a <div> inside this input.
        # I managed to shove the value inside only through javascript, and after that
        # I couldn't figure out why sorting doesn't happen for another 30 minutes. =)
        self.this_input_makes_me_mad(self.__healing_column_filter_input_locator)
        self.press_enter()
        return self

    def click_damage_column_name(self):
        self.click(self.__name_column_name_locator)
        return self

    def check_of_what_element_on_top(self):
        element_1 = self.get_element_by_locator(self.__name_column_first_item_locator)
        element_2 = self.get_element_by_locator(self.__name_column_second_item_locator)

        elements = [element_1, element_2]

        if len(elements) >= 2:
            index_1 = elements.index(element_1)
            index_2 = elements.index(element_2)

            if index_1 < index_2:
                return True
            else:
                return False
