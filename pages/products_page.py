from pages.base_page import BasePage
from utils.locators import Locators


class ProductsPage(BasePage):
    def __init__(self, driver):
        self.locator = Locators
        super(ProductsPage, self).__init__(driver)  # Python2 version

    def close_popup_modal(self):
        try:
            self.find_element(*self.locator.POPUP).click()
        except:
            print('popup was not there')

    def grab_products(self):
        self.base_url = 'https://evaly.com.bd/categories/speaker-2f615cf9a'
        self.close_popup_modal()
        brands = self.find_elements(*self.locator.CATEGORY)
        brand_links = [brand.get_attribute['href'] for brand in brands]
        print(brand_links)
