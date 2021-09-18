from selenium.webdriver.common.by import By


class Locators(object):
    POPUP = (By.XPATH, '//body/reach-portal[1]/div[1]/div[1]/div[1]/section[1]/div[1]/button[1]/*[1]')
    USER_ICON = (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]")
    USERNAME = (By.XPATH, '//*[@id="custom-popover"]/div/div/div/form/div[1]/label/input')
    PASSWORD = (By.XPATH, "//input[@placeholder='*********']")
    LOGIN = (By.XPATH, "//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]")
    SPEAKER_LINK = (By.XPATH, "//div[@class='ProductCarousel___StyledDiv-sc-1lnkzzh-2 cWpFqW flex-1"
                              " hidden mr-4 bg-white shadow xl:block']//li[9]//a[1]")
    CATEGORY = (By.XPATH, "//body/div[@id='__next']/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/a")
    PRODUCT = (By.XPATH, "//div[@class='layouts___StyledDiv-sc-6pqol9-0 iJmXUL']//a")
    DETAIL_PRICE = (By.XPATH, "//body/div[@id='__next']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/h2[1]")
    ACCORDION = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div")
    AVATAR = (By.XPATH, "//img[@alt='Avatar']")
    FULL_NAME = (By.XPATH, "//body/div[@id='__next']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/h3[1]")
