from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.common import CommonPage


def test_valid_login(page: Page, config):
    login = LoginPage(page)
    com = CommonPage()
    com.navigate_to_url(page, config['base_url'])
    login.login_to_saucelab(config['username'], config['password'])
    login.verify_login_success()


def test_invalid_login(page: Page, config):
    login = LoginPage(page)
    com = CommonPage()
    com.navigate_to_url(page, config['base_url'])
    login.invalid_login_to_saucelab(config['invalid_username'], config['password'])
    login.verify_error_message()
   
    