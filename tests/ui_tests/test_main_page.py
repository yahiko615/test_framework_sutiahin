# idk why but create_driver fixture didnt work without that import, and it also said that import didnt used yet
from page_objects.main_page_pack.main_page import MainPage
import pytest
from flaky import flaky
import allure


@allure.feature('Main Page')
@pytest.mark.smoke
@pytest.mark.headless
@flaky(max_runs=10, min_passes=1)
def test_search_input(create_driver):
    text_for_search = 'augmentation evoker'
    driver = create_driver
    spell_page = MainPage(driver).set_search_text(text_for_search).click_search_result()
    assert spell_page.is_h1_label_displayed(), 'Spell page is not shown!'


@allure.feature('Main Page')
@pytest.mark.smoke
@pytest.mark.headless
@flaky(max_runs=10, min_passes=1)
def test_eu_na_switchers(create_driver):
    driver = create_driver
    switcher_eu = MainPage(driver).click_switcher('EU')
    assert switcher_eu == 'active', 'EU switcher must be active after clicking on it!'
    switcher_na = MainPage(driver).click_switcher('NA')
    assert switcher_na == 'active', 'NA switcher must be active after clicking on it!'


@pytest.mark.regression
@flaky(max_runs=10, min_passes=1)
@pytest.mark.headless
def test_news_types(create_driver):
    driver = create_driver
    live_type = MainPage(driver).hover_on_news_types().click_on_live_type_at_news_types()
    assert live_type.check_if_live_tag_is_displayed() is False, 'News with removed tad should disappear!'


@allure.feature('Main Page')
@pytest.mark.smoke
@pytest.mark.headless
@flaky(max_runs=10, min_passes=1)
def test_live_tag_only(create_driver):
    driver = create_driver
    live_tag = MainPage(driver).click_on_live_tag()
    assert live_tag.check_if_not_live_tag_news_is_displayed(), 'When a particular news tag is selected, ' \
                                                               'news from other tags should not be displayed!'


@allure.feature('Main Page')
@pytest.mark.smoke
@pytest.mark.headless
@flaky(max_runs=10, min_passes=1)
def test_settings_wow_today(create_driver):
    driver = create_driver
    news_page = MainPage(
        driver).click_to_check_all_news()
    assert news_page.is_h1_label_displayed(), 'News page is not displayed'
