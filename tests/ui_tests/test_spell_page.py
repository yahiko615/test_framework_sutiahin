# idk why but create_driver fixture didnt work without that import, and it also said that import didnt used yet
from page_objects.spell_page_pack.spell_page import SpellPage
import pytest
import allure
from flaky import flaky


@allure.feature('Spell Page')
@pytest.mark.smoke
@pytest.mark.headless
@flaky(max_runs=4, min_passes=1)
@pytest.mark.skip('so long')
def test_search_input(create_driver_spell_page):
    driver = create_driver_spell_page
    spell_page = SpellPage(driver).click_add_to_favorites()
    assert spell_page.is_login_screen_text_displayed(), 'Login page is not shown!'


@allure.feature('Spell Page')
@pytest.mark.smoke
@pytest.mark.headless
@pytest.mark.skip('so long')
@flaky(max_runs=4, min_passes=1)
def test_spell_params(create_driver_spell_page):
    driver = create_driver_spell_page
    spell_page = SpellPage(driver)
    assert spell_page.is_spell_table_values_much(), 'Values of the table is not matching or table is missing!'


@allure.feature('Spell Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
@flaky(max_runs=4, min_passes=1)
def test_comment_section_oldest_first_sorting(create_driver_spell_page):
    driver = create_driver_spell_page
    oldest_comment = SpellPage(driver).click_to_show_comments().click_oldest_first()
    assert oldest_comment.is_oldest_comment_on_top(), 'Oldest comment should be on to after' \
                                                            ' clicking on sorting!'


@allure.feature('Spell Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
@flaky(max_runs=4, min_passes=1)
def test_comments_pagination(create_driver_spell_page_with_comments):
    driver = create_driver_spell_page_with_comments
    comments_page = SpellPage(driver).click_to_show_comments()
    assert comments_page.comment_page_is_displayed(1), "Comments isn't shown"
    SpellPage(driver).click_to_swap_to_the_page_of_comments(2)
    assert comments_page.comment_page_is_displayed(2), 'Next page is not shown!'
    SpellPage(driver).click_to_swap_to_the_page_of_comments(3)
    assert comments_page.comment_page_is_displayed(3), 'Last page is not shown!'


@allure.feature('Spell Page')
@pytest.mark.regression
@pytest.mark.headless
@pytest.mark.skip('so long')
@flaky(max_runs=4, min_passes=1)
def test_comment_section_highest_rated_first_sorting(create_driver_spell_page_with_comments):
    driver = create_driver_spell_page_with_comments
    highest_comment = SpellPage(driver).click_to_show_comments().click_highest_rated_first()
    assert highest_comment.is_highest_comment_on_top(), 'Highest comment should be on to ' \
                                                              'after clicking on sorting!'
