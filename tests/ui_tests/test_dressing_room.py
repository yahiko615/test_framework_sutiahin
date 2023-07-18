from conftest import create_driver_dressing_room_page
from page_objects.dressing_room_page.dressing_room_page import DressingRoom
from page_objects.login_page_pack.login_page import LoginPage
import pytest


@pytest.mark.smoke
@pytest.mark.headless
def test_helm(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    text = 'Sum'
    dressing_room = DressingRoom(driver).click_helm().set_search(text).click_new_helm()
    assert dressing_room.is_new_helm_is_displayed(), 'New helm is not displayed'


@pytest.mark.regression
@pytest.mark.headless
def test_shoulders(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    text = 'ald'
    dressing_room = DressingRoom(driver).click_shoulders().click_replace().set_search(text).click_new_shoulders()
    assert dressing_room.is_new_shoulders_is_displayed(), 'New shoulders is not displayed'


@pytest.mark.smoke
@pytest.mark.headless
def test_screenshot_downloading(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_screenshot_download()
    assert dressing_room.check_if_screen_is_downloaded(), 'Screenshot is not downloaded!'


@pytest.mark.regression
@pytest.mark.headless
def test_save_outfit_when_not_logged_in(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_save_outfit()
    assert dressing_room.is_you_must_be_logged_in_to_save_is_displayed(), 'Error message is not displayed when you' \
                                                                          ' trying to save outfit!'


@pytest.mark.regression
@pytest.mark.headless
def test_toggle_character_ui(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_toggle_ui()
    assert dressing_room.is_ui_is_displayed() is False, "Ui isn't disappear after hiding!"
    dressing_room.click_toggle_ui()
    assert dressing_room.is_ui_is_displayed(), "Ui isn't shown after clicking show button!"


@pytest.mark.regression
@pytest.mark.headless
def test_class_changing(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_character_options().click_change_class().click_class_warlock()
    assert dressing_room.is_class_is_warlock(), "Class isn't changed!"


@pytest.mark.regression
@pytest.mark.headless
def test_pause(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_pause()
    assert dressing_room.is_data_paused(), "Data is not paused"