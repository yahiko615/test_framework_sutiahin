# idk why but create_driver fixture didnt work without that import, and it also said that import didnt used yet
from page_objects.login_page_pack.login_page import LoginPage
from page_objects.registration_page_pack.forgot_password_page import ForgotPasswordPage
from utilities.config_reader import ReadConfig
import pytest


@pytest.mark.smoke
@pytest.mark.headless
def test_login_without_checked_captcha(create_driver_login_page, env):
    user_name, password = env.email, env.password
    driver = create_driver_login_page
    login_page = LoginPage(driver).set_email(user_name).set_password(password).click_login()
    assert login_page.is_error_captha_text_displayed(), 'Error text is not displayed'


@pytest.mark.smoke
@pytest.mark.headless
def test_lend_to_reg_page(create_driver_login_page):
    driver = create_driver_login_page
    login_page = LoginPage(driver).click_new_account()
    assert login_page.is_label_displayed(), 'Registration page label text is not shown'


@pytest.mark.smoke
@pytest.mark.headless
def test_lend_resend_page(create_driver_login_page):
    driver = create_driver_login_page
    login_page = LoginPage(driver).click_resend()
    assert login_page.is_label_displayed(), 'Resend page label text is not shown'


@pytest.mark.smoke
@pytest.mark.headless
def test_lend_forgot_pass_page(create_driver_login_page):
    driver = create_driver_login_page
    login_page = LoginPage(driver).click_forgot_password()
    assert login_page.is_label_displayed(), 'Forgot password page label text is not shown'
    user_name = ReadConfig.get_user_creds()
    login_page = ForgotPasswordPage(driver).set_forgot_pass_email(user_name)
    assert login_page.is_error_captha_text_displayed(), 'Error text is not displayed'
