import allure
from flaky import flaky
from page_objects.dressing_room_page.dressing_room_page import DressingRoom
import pytest

@allure.feature('Dressing Room Page')
@allure.issue('https://docs.qameta.io/allure/', 'Wrong asertion')
@allure.severity('CRITICAL')
@pytest.mark.smoke
@pytest.mark.headless
@pytest.mark.skip('so long')
@flaky(max_runs=4, min_passes=1)
def test_helm(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    text = 'Sum'
    dressing_room = DressingRoom(driver).click_helm().set_search(text).click_new_helm()
    assert dressing_room.is_new_helm_is_displayed() == 'bla', 'New helm is not displayed'


@allure.feature('Dressing Room Page')
@pytest.mark.regression
@pytest.mark.headless
@flaky(max_runs=4, min_passes=1)
@pytest.mark.skip('so long')
def test_shoulders(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    text = 'ald'
    dressing_room = DressingRoom(driver).click_shoulders().click_replace().set_search(text).click_new_shoulders()
    assert dressing_room.is_new_shoulders_is_displayed(), 'New shoulders is not displayed'

    
    
@allure.feature('Dressing Room Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
def test_save_outfit_when_not_logged_in(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_save_outfit()
    assert dressing_room.is_you_must_be_logged_in_to_save_is_displayed(), 'Error message is not displayed when you' \
                                                                          ' trying to save outfit!'


@allure.feature('Dressing Room Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
def test_toggle_character_ui(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_toggle_ui()
    assert dressing_room.is_ui_is_displayed() is False, "Ui isn't disappear after hiding!"
    dressing_room.click_toggle_ui()
    assert dressing_room.is_ui_is_displayed(), "Ui isn't shown after clicking show button!"


@allure.feature('Dressing Room Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
def test_class_changing(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_character_options().click_change_class().click_class_warlock()
    assert dressing_room.is_class_is_warlock(), "Class isn't changed!"


@allure.feature('Dressing Room Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
def test_pause(create_driver_dressing_room_page):
    driver = create_driver_dressing_room_page
    dressing_room = DressingRoom(driver).click_pause()
    assert dressing_room.is_data_paused(), "Data is not paused"
