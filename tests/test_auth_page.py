# python -m pytest -v --tb=line tests/test_auth_page.py
from pages.auth_page import AuthPage
from settings import url_base_page

class TestAuthPage():
    def test_TK001_the_authorization_form_is_open(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.the_authorization_form_is_open()

    def test_TK002_location_of_the_logo_and_slogan(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_of_the_logo_and_slogan()

    def test_TK003_location_of_the_tab_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.location_of_the_tab_menu()

    def test_TK004_default_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.default_authentication_type()

    def test_TK005_automatic_change_of_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.automatic_change_of_authentication_type()

    def test_TK006_link_to_the_password_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_password_recovery_form()

    def test_TK007_link_to_the_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_registration_form()

    def test_TK008_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_user_agreement_page()

    def test_TK009_link_fut_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_fut_to_the_user_agreement_page()

    def test_TK010_link_to_social_vk(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_social_vk()

    def test_TK011_authorization_with_blank_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_with_blank_fields()

    def test_TK012_sql_injection_in_a_text_field(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.sql_injection_in_a_text_field()

