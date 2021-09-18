from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestEvaly(BaseTest):

    # Case 1
    def test_a_sign_in(self):  # TODO 0: Look for the solution of webdriver getting detected.
        print("\n" + str(test_cases(0)))
        login_modal = MainPage(self.driver).click_user_icon()
        login_modal.login()  # doesn't login as server detects selenium webdriver

    # Case 2
    def test_b_speaker(self):
        print("\n" + str(test_cases(1)))
        speaker_page = HomePage(self.driver).click_speaker_link()
        speaker_page.grab_brands()
        self.assertIn('categories/speaker', speaker_page.get_url())

    def test_c_products(self):  # TODO 1: Create excel from list of dictionaries.
        speaker_page = HomePage(self.driver).click_speaker_link()
        speaker_page.grab_products()

    # def test_03_compare_price(self): #TODO 2: Price compare for some products with details page.
    #     pass
    #
    # # Case 3
    # def test_04_career_page(self): #TODO 3: Navigate to career page and assert email domains.
    #     pass
