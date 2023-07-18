import os

from selenium.webdriver.common.by import By

from utilities.ui_utilities.base_page import BasePage


class DressingRoom(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.file_name = None

    __helm_locator = (By.XPATH, "//div[@data-character-slot='1']")
    __picker_search_locator = (By.CSS_SELECTOR, "input.picker-search[type='text']")
    __search_result_helm_locator = (
        By.XPATH, "//img[@src='https://wow.zamimg.com/modelviewer/live/webthumbs/item/246/133366.webp']")
    __search_result_shoulders_locator = (
        By.XPATH, "//img[@src='https://wow.zamimg.com/modelviewer/live/webthumbs/item/100/41572.webp']")
    __new_helm_locator = (By.CSS_SELECTOR, "#dressing-room-paperdoll > div.paperdoll-left > div:nth-child(1) > a")
    __new_shoulders_locator = (By.CSS_SELECTOR, "#dressing-room-paperdoll > div.paperdoll-left > div:nth-child(3) > a")
    __shoulders_locator = (By.CSS_SELECTOR, "a[href='https://www.wowhead.com/item=117327/oathsworn-pauldrons']")
    __replace_locator = (By.XPATH, "//span[text()='Replace...']")
    __screenshot_button_locator = (By.CSS_SELECTOR, "#dr-screenshot")
    __save_outfit_button_locator = (By.CSS_SELECTOR, "#dr-save")
    __toggle_ui_button_locator = (By.CSS_SELECTOR, "#dr-toggle-ui")
    __downloads_dir = r"C:\Users\Admin\Downloads"
    __you_must_be_log_in_to_save_locator = (
        By.XPATH, "//*[contains(text(), 'You must be logged in to use this feature')]")
    __canvas_locator = (By.XPATH, '//div[@class="dressing-room-character"]')
    __gear_locator = (By.XPATH, '//a[@data-category="gear" and @href="javascript:" and @data-active="true"]')
    __character_options_locator = (By.XPATH, '//a[@data-category="character" and @href="javascript:"]')
    __class_changer_locator = (By.XPATH, "//div[@class='dressing-room-character-controls-category-option' "
                                         "and @data-character-customization-type='class']//a[@class='imitation-select' "
                                         "and text()]")
    __class_warlock = (By.XPATH, "//a[@class='c9 tinyicon']")
    __pause_button = (By.XPATH, "//button[@class='btn btn-site fa fa-pause']")

    def find_screenshot(self):
        for self.file_name in os.listdir(self.__downloads_dir):
            if self.file_name.endswith("Wowhead Dressing Room"):
                return self.file_name
        return None

    def check_if_screen_is_downloaded(self):
        self.find_screenshot()
        if self.file_name:
            return True
        else:
            return False

    def click_helm(self):
        self.click(self.__helm_locator)
        return self

    def click_shoulders(self):
        self.click(self.__shoulders_locator)
        return self

    def click_replace(self):
        self.click_via_js(self.__replace_locator)
        return self

    def set_search(self, text):
        self.send_keys(self.__picker_search_locator, text)
        return self

    def hover_on(self):
        self.move_cursor_to_element(self.__replace_locator)
        return self

    def click_new_helm(self):
        self.click(self.__search_result_helm_locator)
        return self

    def click_new_shoulders(self):
        self.click(self.__search_result_shoulders_locator)
        return self

    def is_new_helm_is_displayed(self):
        return self.is_displayed(self.__new_helm_locator)

    def is_new_shoulders_is_displayed(self):
        return self.is_displayed(self.__new_shoulders_locator)

    def click_screenshot_download(self):
        self.click(self.__screenshot_button_locator)
        return self

    def click_save_outfit(self):
        self.click(self.__save_outfit_button_locator)
        return self

    def is_you_must_be_logged_in_to_save_is_displayed(self):
        return self.is_displayed(self.__you_must_be_log_in_to_save_locator)

    def click_toggle_ui(self):
        self.click(self.__toggle_ui_button_locator)
        return self

    def is_ui_is_displayed(self):
        if self.get_element_data_hide_ui(self.__canvas_locator) == 'false' and self.is_displayed(self.__gear_locator):
            return True
        else:
            return False

    def click_character_options(self):
        self.click(self.__character_options_locator)
        return self

    def click_change_class(self):
        self.click(self.__class_changer_locator)
        return self

    def click_class_warlock(self):
        self.click_via_js(self.__class_warlock)
        return self

    def is_class_is_warlock(self):
        return self.get_element_data_class(self.__canvas_locator) == '9'

    def click_pause(self):
        self.click(self.__pause_button)
        return self

    def is_data_paused(self):
        return self.get_element_data_paused(self.__pause_button) == 'true'
