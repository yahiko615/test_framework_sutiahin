import json
import os

import pytest
from selenium.webdriver.chrome.options import Options

from utilities.config_object import ConfigObject
from utilities.driver_factory import create_driver_factory

_screenshot_path = r"C:\Users\Admin\Downloads"


# def pytest_addoption(parser):
#     parser.addoption('--env', action='store', help='Specify env name', required=True)


@pytest.fixture(scope="session", autouse=True)
def env(request):
    # env_name = request.config.getoption('--env')
    config_file = "configurations/env_1.json"
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
    with open(config_path) as file:
        file_data = file.read()
    json_data = json.loads(file_data)
    return ConfigObject(**json_data)


@pytest.fixture
def create_driver(request, env):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.app_url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_spell_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.spell_page)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_spell_page_with_comments(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.spell_page_with_comments)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_login_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.login_page)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_driver_dressing_room_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.dressing_room_page)
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

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.black_claw_page)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_battle_pet_page(request):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    driver = create_driver_factory(env.browser_id, options=driver_options)
    driver.get(env.battle_pet_page)
    driver.maximize_window()
    yield driver
    driver.quit()
