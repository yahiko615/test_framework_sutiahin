from selenium.webdriver.common.by import By

from page_objects.main_page_pack.news_page import NewsPage
from page_objects.spell_page_pack.spell_page import SpellPage
from utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __input_search = (By.XPATH, "//input[@type='text' and @name='q']")
    __search_result_locator = (By.XPATH, "//span[@class='exact-match' and text()='Augmentation']")
    __eu_switcher_locator = (By.XPATH, "//a[@class='switcher-choice' and text()='EU']")
    __na_switcher_locator = (By.XPATH, "//a[@class='switcher-choice' and text()='NA']")
    __news_types_locator = (By.XPATH, "//span[@class='fa fa-chevron-down']")
    __news_live_type_sub_menu_locator = (By.XPATH, "//a[contains(@class, 'news-type-color-1') and span[text() = 'Live']]")
    __news_live_tag_locator = (
        By.XPATH, "//a[@class='news-list-card-type fa fa-thumb-tack' and normalize-space()='Live']")
    __not_live_news_tag_locator = (
        By.XPATH, "//a[@class='news-list-card-type fa fa-thumb-tack' and normalize-space()!='Live']")
    __settings_wow_today_switcher_locator = (By.XPATH, "//section[@id='tiw-switcher-settings']")
    __tiw_config_section_locator = (By.XPATH, "//section[@class='tiw-group-wrapper' and @data-tiw-section='group-mythicaffix']")
    __name_of_settings_section_locator = (By.XPATH, '//*[@id="US-group-mythicaffix"]/section[3]/a')
    __check_all_news_locator = (By.XPATH, "//a[text()='Recent News']")

    def set_search_text(self, text):
        self.send_keys(self.__input_search, text)
        return self

    def click_search_result(self):
        self.click(self.__search_result_locator)
        return SpellPage(self._driver)

    def click_switcher(self, switcher_text):
        data_state = 'inactive'
        if switcher_text == 'EU':
            self.click(self.__eu_switcher_locator)
            data_state = self.get_element_data_state(self.__eu_switcher_locator)
        elif switcher_text == 'NA':
            self.click(self.__na_switcher_locator)
            data_state = self.get_element_data_state(self.__na_switcher_locator)
        else:
            return data_state
        return data_state

    def hover_on_news_types(self):
        self.move_cursor_to_element(self.__news_types_locator)
        return self

    def click_on_live_type_at_news_types(self):
        self.move_cursor_to_element(self.__news_live_type_sub_menu_locator)
        self.click(self.__news_live_type_sub_menu_locator)
        return self

    def click_on_live_tag(self):
        self.click(self.__news_live_tag_locator)
        return self

    def check_if_live_tag_is_displayed(self):
        return self.is_not_displayed(self.__news_live_tag_locator)

    def check_if_not_live_tag_news_is_displayed(self):
        return self.check_if_others_tags_is_displayed(self.__not_live_news_tag_locator)

    def click_on_settings_wow_today(self):
        self.move_cursor_to_element(self.__settings_wow_today_switcher_locator)
        self.click(self.__settings_wow_today_switcher_locator)
        return self

    def click_on_settings_mythic_plus_section(self):
        self.move_cursor_to_element(self.__tiw_config_section_locator)
        self.click(self.__tiw_config_section_locator)
        return self

    def is_mythic_plus_section_is_displayed(self):
        return self.is_not_displayed(self.__name_of_settings_section_locator)

    def click_to_check_all_news(self):
        self.click(self.__check_all_news_locator)
        return NewsPage(self._driver)
