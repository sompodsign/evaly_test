from pages.base_page import BasePage
from utils.locators import *
from pages.speaker_page import SpeakerPage


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = Locators
        super(HomePage, self).__init__(driver)  # Python2 version

    def close_popup_modal(self):
        try:
            self.find_element(*self.locator.POPUP).click()
        except:
            print('popup was not there')

    def click_speaker_link(self):
        self.close_popup_modal()
        self.wait_element(*self.locator.SPEAKER_LINK)
        self.find_element(*self.locator.SPEAKER_LINK).click()
        return SpeakerPage(self.driver)


