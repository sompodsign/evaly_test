from utils.locators import *
from pages.base_page import BasePage
from utils.users import user
from pages.home_page import HomePage


class LoginModal(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super(LoginModal, self).__init__(driver)  # Python2 version

    def enter_username(self, username):
        self.find_element(*self.locator.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN).click()

    def click_profile_icon(self):
        self.find_element(*self.locator.PROFILE_ICON).click()

    def login(self):
        print(user)
        self.enter_username(user['username'])
        self.enter_password(user['password'])
        self.click_login_button()
        self.wait_element(*self.locator.PROFILE_ICON)
        self.click_profile_icon()

        return HomePage(self.driver)
