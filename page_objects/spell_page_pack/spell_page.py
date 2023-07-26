from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page_pack.login_page import LoginPage
from utilities.ui_utilities.base_page import BasePage


class SpellPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __h1_label = (By.XPATH, "//h1[@class='heading-size-1' and contains(text(), 'Augmentation Evoker')]")
    __add_to_favorites_locator = (By.XPATH, "//span[@class='fa fav-star fa-star-o']")
    __table_locator = (By.XPATH, "//table[@class='grid']")
    __comment_section_locator = (By.XPATH, '//a[@rel="np" and @href="#comments"]/div[contains(text(), "Comments")]')
    __rows_locator = "tr.first"
    __th_locator = '//*[@id="spelldetails"]/tbody/tr[1]/td[2]/table/tbody/tr[2]/th'
    __td_locator = '//*[@id="spelldetails"]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td'
    __span_locator = 'span.q0'
    __oldest_comment_first_sorting_locator = (By.XPATH, "//a[@href='javascript:'][contains(text(), 'oldest first')]")
    __oldest_comment_locator = '//a[@id="comments:id=180162"]'
    __second_comment_locator = '//a[@id="comments:id=271590"]'
    __highest_rated_comment_locator = (By.XPATH, '//a[@id="comments:id=1398350"]')
    __second_highest_rated_comment_locator = (By.XPATH, '//a[@id="comments:id=4068"]')
    __first_comment_pages_locator = (
        By.XPATH, "//span[b[contains(text(), '1')] and b[contains(text(), '40')] and b[contains(text(), '100')]]")
    __next_comment_page_swap_locator = (
    By.CSS_SELECTOR, '#tab-comments > div.listview-band-top > div.listview-nav > a:nth-child(5)')
    __last_comment_page_swap_locator = (
    By.CSS_SELECTOR, '#tab-comments > div.listview-band-top > div.listview-nav > a:nth-child(6)')
    __second_comment_pages_locator = (
        By.XPATH, "//span[b[contains(text(), '41')] and b[contains(text(), '80')] and b[contains(text(), '100')]]")
    __last_comment_pages_locator = (
        By.XPATH, "//span[b[contains(text(), '81')] and b[contains(text(), '100')] and b[contains(text(), '100')]]")
    __highest_rated_comment_filter_locator = (
        By.XPATH, "// a[text() = 'highest rated']")

    def is_h1_label_displayed(self):
        return self.is_displayed(self.__h1_label)

    def click_add_to_favorites(self):
        self.click(self.__add_to_favorites_locator)
        return LoginPage(self._driver)

    def is_spell_table_values_much(self) -> bool:
        try:
            table = self._wait.until(EC.visibility_of_element_located(self.__table_locator))
            rows = table.find_elements(By.CSS_SELECTOR, self.__rows_locator)

            for row in rows:
                th = row.find_element(By.XPATH, self.__th_locator)
                td = row.find_element(By.XPATH, self.__td_locator)

                text_th = th.text.strip()

                if text_th == 'Duration' and td.find_element(By.CSS_SELECTOR, self.__span_locator).is_displayed():
                    span_text = td.find_element(By.CSS_SELECTOR, self.__span_locator).text.strip()
                    if span_text == 'n/a':
                        return True
                else:
                    return False
        except NoSuchElementException:
            return False

    def click_to_show_comments(self):
        self.click(self.__comment_section_locator)
        return self

    def click_oldest_first(self):
        self.click(self.__oldest_comment_first_sorting_locator)
        return self

    def is_oldest_comment_on_top(self):
        element_1 = self.get_element(By.XPATH, self.__oldest_comment_locator)
        date_1 = datetime.strptime(element_1.text[3:], "%Y/%m/%d")

        element_2 = self.get_element(By.XPATH, self.__second_comment_locator)
        date_2 = datetime.strptime(element_2.text[3:], "%Y/%m/%d")
        if date_1 < date_2:
            return True
        else:
            return False

    def click_to_swap_to_the_page_of_comments(self, comment_page_id):
        if comment_page_id == 2:
            self.click_via_js(self.__next_comment_page_swap_locator)
        elif comment_page_id == 3:
            self.click_via_js(self.__last_comment_page_swap_locator)
        else:
            self.click_via_js(self.__last_comment_page_swap_locator)
        return self

    def comment_page_is_displayed(self, comment_page_id):
        if comment_page_id == 1:
            return self.is_displayed(self.__first_comment_pages_locator)
        elif comment_page_id == 2:
            return self.is_displayed(self.__second_comment_pages_locator)
        else:
            return self.is_displayed(self.__last_comment_pages_locator)

    def click_highest_rated_first(self):
        self.click(self.__highest_rated_comment_filter_locator)
        return self

    def is_highest_comment_on_top(self):
        element_1 = self.get_element_by_locator(self.__highest_rated_comment_locator)
        date_1 = element_1.text

        element_2 = self.get_element_by_locator(self.__second_highest_rated_comment_locator)
        date_2 = element_2.text
        if date_1 > date_2:
            return True
        else:
            return False
