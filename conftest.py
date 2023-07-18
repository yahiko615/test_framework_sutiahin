import os

import pytest

from utilities.config_reader import ReadConfig
from utilities.driver_factory import create_driver_factory
from selenium.webdriver.chrome.options import Options

_screenshot_path = r"C:\Users\Admin\Downloads"


@pytest.fixture
def create_driver(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_base_url())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_spell_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_spell_page_url())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_spell_page_with_comments(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_spell_page_with_comments())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_login_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_login_page())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_dressing_room_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_dressing_room_page())
    driver.maximize_window()
    yield driver
    for file_name in os.listdir(_screenshot_path):
        if file_name.__contains__("Wowhead Dressing Room"):
            file_path = os.path.join(_screenshot_path, file_name)
            os.remove(file_path)
    driver.quit()


@pytest.fixture
def create_black_claw_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_black_claw_page())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_battle_pet_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(ReadConfig.get_browser_id(), options=driver_options)
    driver.get(ReadConfig.get_app_battle_pet_page())
    driver.maximize_window()
    yield driver
    driver.quit()
