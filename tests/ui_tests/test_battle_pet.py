from conftest import create_black_claw_page, create_battle_pet_page
from page_objects.battle_pet_pack.battle_pet_abilities_page import BattlePetAbilities
from page_objects.battle_pet_pack.pet_spell_page import PetSpell
import pytest


@pytest.mark.regression
@pytest.mark.headless
def test_class_changing(create_black_claw_page):
    driver = create_black_claw_page
    pet_ability = PetSpell(driver).move_slider()
    assert pet_ability.right_dmg_scaling_is_displayed(), "Dmg of ability don't scales wtih the slider value"


@pytest.mark.regression
@pytest.mark.headless
def test_search_by_spell_name(create_battle_pet_page):
    driver = create_battle_pet_page
    item = 'Expunge'
    pet_ability = BattlePetAbilities(driver).set_search(item).click_search().click_search_result()
    assert pet_ability.right_spell_found(), "Switching to the spell page after a search is not done!"


@pytest.mark.regression
@pytest.mark.headless
def test_remove_filter(create_battle_pet_page):
    driver = create_battle_pet_page
    item = 'Expunge'
    pet_ability = BattlePetAbilities(driver).set_search(
        item).click_search()
    assert pet_ability.is_spell_found(), 'Spell is not found'
    pet_ability.click_remove_filter()
    assert pet_ability.is_default_list_of_results_is_displayed(), "Filter is not removed!"


@pytest.mark.regression
@pytest.mark.headless
def test_column_filtering(create_battle_pet_page):
    driver = create_battle_pet_page
    pet_ability = BattlePetAbilities(driver).click_column_filtering().click_add_column_filter() \
        .click_add_column_filter_healing().set_healing().click_search_result()
    assert pet_ability.right_spell_found_after_column_sorting(), "Column is filtered to the wrong spell"


@pytest.mark.regression
@pytest.mark.headless
def test_column_filtering(create_battle_pet_page):
    driver = create_battle_pet_page
    pet_ability = BattlePetAbilities(driver).click_damage_column_name()
    assert pet_ability.check_of_what_element_on_top() is not None, "Column is filtered to the wrong values"
