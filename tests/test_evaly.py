from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestEvaly(BaseTest):

    # Case 1
    def test_01_sign_in(self):
        print("\n" + str(test_cases(0)))
        login_modal = MainPage(self.driver).click_user_icon()
        login_modal.login() # doesn't login as server detects selenium webdriver

    # Case 2
    def test_02_speaker(self):
        print("\n" + str(test_cases(1)))
        speaker_page = HomePage(self.driver).click_speaker_link()
        speaker_page.grab_brands()
        self.assertIn('categories/speaker', speaker_page.get_url())

    def test_03_products(self):
        speaker_page = HomePage(self.driver).click_speaker_link()
        speaker_page.grab_products()

    # def test_03_compare_price(self):
    #     pass
    #
    # # Case 3
    # def test_04_career_page(self):
    #     pass
