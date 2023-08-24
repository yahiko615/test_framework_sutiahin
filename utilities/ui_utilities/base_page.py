import time

from selenium.common import ElementNotVisibleException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 40)

    def __wait_until_element_visible(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_invisible(self, locator: tuple):
        return self._wait.until(EC.invisibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def send_keys(self, locator, value, is_clear=True):
        element = self.__wait_until_element_visible(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def is_displayed(self, locator):
        user_label_element = self.__wait_until_element_visible(locator)
        return user_label_element.is_displayed()

    def is_not_displayed(self, locator):
        user_label_element = self.__wait_until_element_invisible(locator)
        return user_label_element.is_displayed()

    def get_text(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element.text

    def get_placeholder(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element.placeholder

    def get_element(self, by, value):
        element = self.__wait_until_element_visible((by, value))
        return element

    def get_element_by_locator(self, locator):
        element = self.__wait_until_element_visible(locator)
        return element

    def get_element_data_state(self, locator):
        element = self.__wait_until_element_visible(locator)
        data_state = element.get_attribute("data-state")
        return data_state

    def get_element_data_hide_ui(self, locator):
        element = self.__wait_until_element_visible(locator)
        data_hide_ui = element.get_attribute("data-hide-ui")
        return data_hide_ui

    def get_element_data_class(self, locator):
        element = self.__wait_until_element_visible(locator)
        data_class = element.get_attribute("data-class")
        return data_class

    def get_element_data_paused(self, locator):
        element = self.__wait_until_element_visible(locator)
        data_paused = element.get_attribute("data-paused")
        return data_paused

    def get_element_style(self, locator):
        element = self.__wait_until_element_visible(locator)
        style = element.get_attribute("style")
        return style

    def click_via_js(self, locator):
        element = self.__wait_until_element_clickable(locator)
        self._driver.execute_script('arguments[0].click()', element)

    def move_cursor_to_element(self, locator):
        element = self.__wait_until_element_visible(locator)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def scroll_to_element(self, locator):
        retries = 15
        while retries:
            try:
                element = self.__wait_until_element_visible(locator)
                return element
            except ElementNotVisibleException:
                self._driver.execute_script('window.scrollTo(0, 100)')
                retries -= 1

    def check_if_others_tags_is_displayed(self, locator):
        try:
            elements = self._wait.until(EC.presence_of_all_elements_located(locator))
            return len(elements) == 0
        except TimeoutException:
            return True

    def move_slider_to(self, locator_left, locator_width, desired_position):
        element = self.__wait_until_element_visible(locator_left)
        element2 = self.__wait_until_element_visible(locator_width)
        self._driver.execute_script("arguments[0].style.left = arguments[1]", element, desired_position)
        self._driver.execute_script("arguments[0].style.width = arguments[1]", element2, desired_position)

    def this_input_makes_me_mad(self, locator):
        self._driver.execute_script("""
    var inputElement = document.querySelector('.listview-filters-columns-filter-text');
    var newValue = '4999';
    inputElement.value = newValue;
    var event = new KeyboardEvent('keydown', {key: 'Enter'});
    document.dispatchEvent(event);
    """)
        element = self.__wait_until_element_visible(locator)
        element.send_keys(Keys.ENTER)
        time.sleep(3)

    def press_enter(self):
        self._driver.execute_script("""
    var event = new KeyboardEvent('keydown', {key: 'Enter'});
    document.dispatchEvent(event);
    """)
