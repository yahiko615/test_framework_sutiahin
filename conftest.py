import json
from contextlib import suppress
import os
from pathlib import Path
import allure
import inspect
import pytest
from selenium.webdriver.chrome.options import Options

from api_collections.booking_api import BookingAPI
from api_collections.data_classes.booking_data import Booking
from utilities.driver_factory import create_driver_factory

_screenshot_path = Path.home().joinpath("Downloads")


def auto_step(cls):
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if not name.startswith('_'):
            setattr(cls, name, allure.step(method))
    return cls


@pytest.fixture(scope="session", autouse=True)
def env():
    config_file = "configurations/env_1.json"
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
    with open(config_path) as file:
        file_data = file.read()
    json_data = json.loads(file_data)
    return json_data


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def create_driver_for_page(request, env, page_url):
    driver_options = Options()
    is_headless = request.node.get_closest_marker("headless")
    if is_headless:
        driver_options.add_argument("--headless")

    env = dict(env)
    driver = create_driver_factory(env["browser_id"], options=driver_options)
    driver.get(page_url)
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture
def create_driver(request, env):
    yield from create_driver_for_page(request, env, env["app_url"])


@pytest.fixture
def create_driver_spell_page(request, env):
    yield from create_driver_for_page(request, env, env["spell_page"])


@pytest.fixture
def create_driver_spell_page_with_comments(request, env):
    yield from create_driver_for_page(request, env, env["spell_page_with_comments"])


@pytest.fixture
def create_driver_login_page(request, env):
    yield from create_driver_for_page(request, env, env["login_page"])


@pytest.fixture
def create_driver_dressing_room_page(request, env):
    yield from create_driver_for_page(request, env, env["dressing_room_page"])
    for file_name in os.listdir(_screenshot_path):
        if file_name.__contains__("Wowhead Dressing Room"):
            file_path = os.path.join(_screenshot_path, file_name)
            os.remove(file_path)


@pytest.fixture
def create_black_claw_page(request, env):
    yield from create_driver_for_page(request, env, env["black_claw_page"])


@pytest.fixture
def create_battle_pet_page(request, env):
    yield from create_driver_for_page(request, env, env["battle_pet_page"])


@pytest.fixture
def create_mock_booking(env):
    mock_data = BookingAPI(env).get_booking_by_id(52)
    response = json.loads(mock_data.text)
    booking = Booking(**response)
    return booking


@pytest.fixture
def create_mock_booking_with_id(env):
    mock_data = BookingAPI(env).create_booking(Booking())
    book_body = mock_data.json()['booking']
    booking = Booking(**book_body)
    booking.update_data(**{'bookingid': mock_data.json()['bookingid']})
    return booking
