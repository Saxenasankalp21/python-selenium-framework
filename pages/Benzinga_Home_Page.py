#Author#SankalpSaxena
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class BenzingaComHomepagePage(BaseDriver):
    ut = Utils()
    log = ut.custom_logger()
    def __init__(self, driver):
        super().__init__(driver) # This keyword allows to use base driver class methods in test files
        self.driver = driver


    # locators########
    #login
    GO_TO_BENZINGA_PRO_TITLE = "//body/div/div/div/div/div/div/ul/li/a[@aria-label]"
    MY_ACCOUNT_TITLE = "//span[@class='my-account-text']"
    BENZINGA_LOGO_HEADER = "//div[@id='navigation-header']/div[2]/div/div/div/a/span"
    BENZINGA_LIST1_HEADER = "//body/div/div/div/div/div/div/ul/li/a/div"
    BENZINGA_LIST2_HEADER = "//div/div/div/div/ul/li/div/a"
    TICKER_SEARCH = ".search-input"
    TICKER_SEARCH_RESULTS = "//div[@class='search-results-section']/div/a/div/div/div[@class='list-item-title']"
    BENZINGA_LOGO_FOOTER = "//div[@class='footer-top-section']/div[1]/div[1]/span"


    #Get locators method#####
    def get_benzinga_pro_title(self):
        return self.driver.find_element(By.XPATH, self.GO_TO_BENZINGA_PRO_TITLE)

    def get_my_account_title(self):
        return self.wait_presence_of_element_located(By.XPATH, self.MY_ACCOUNT_TITLE)

    def get_bz_header_logo(self):
        return self.driver.find_element(By.XPATH, self.BENZINGA_LOGO_HEADER)
    
    def get_header_items_lists1(self):
        return self.driver.find_elements(By.XPATH, self.BENZINGA_LIST1_HEADER)

    def get_header_items_lists2(self):
        return self.driver.find_elements(By.XPATH, self.BENZINGA_LIST2_HEADER)

    def get_ticker_search_input(self):
        return self.wait_presence_of_element_located(By.CSS_SELECTOR, self.TICKER_SEARCH)

    def get_ticker_search_lists(self):
        return self.wait_presence_of_all_elements_located(By.XPATH, self.TICKER_SEARCH_RESULTS)

    def get_bz_footer_logo(self):
        return self.driver.find_element(By.XPATH, self.BENZINGA_LOGO_HEADER)

    #Operations on loctors######
    def verify_login_myaccount(self):
        self.wait_url_contains("https://www.benzinga.com/")
        self.log.info("landed to URl https://www.benzinga.com/")
        self.ut.assert_text_in_title("My Account", self.get_my_account_title())
        self.log.info("My account title has been verified")


    def verify_bz_header_logo(self):
        self.get_bz_header_logo().is_displayed()
        self.log.info("Benzinga header logo is displayed")
        #utilities.save_screenshot_locator(self.getBzHeaderLogo(), "BenzingaLogoHeader")

    def verify_landing(self):
        self.verify_login_myaccount()
        self.verify_bz_header_logo()


    def verify_header_menu_list1(self):
        headerMenu1 = ['DATA & APIS', 'EVENTS', 'MARKETFY', 'PREMARKET', 'BOOST', 'ADVERTISE']
        actual_list = []
        list_items = self.get_header_items_lists1()
        #self.log.info(actual_list)
        self.ut.assert_actual_expected_List(headerMenu1, list_items, actual_list)
        self.log.info("header menu list1 is correct")

    def verify_header_menu_list2(self):
        headerMenu2 = ['Our Services', 'News', 'Markets', 'Options', 'Ratings', 'Ideas', 'Money', 'Crypto', 'Cannabis', 'Jobs']
        actual_list = []
        #self.log.info(actual_list)
        list_items = self.get_header_items_lists2()
        self.ut.assert_actual_expected_List(headerMenu2, list_items, actual_list)
        self.log.info("header menu list2 is correct")

    def verify_ticker_search_input(self, tickersymbol):
        self.get_ticker_search_input().click()
        self.get_ticker_search_input().send_keys(tickersymbol)
        self.log.info("Ticker name added to input field")
        tickers_list_element = self.get_ticker_search_lists()
        for ticker in tickers_list_element:
            if tickersymbol in ticker.text:
                time.sleep(1)
                ticker.click()
                self.log.info("Ticker has been clicked")
                break


    def verify_bz_footer_logo(self):
        self.page_scroll(direction="down", scroll_amount=1000)
        self.page_scroll(direction="up", scroll_amount=1000)
        self.log.info("Scrolled to the bottom the page")
        ("Benzinga logo displayed: ", self.get_bz_footer_logo().is_displayed())
        self.log.info("Benzinga footer logo is displayed")
        #utilities.save_screenshot_locator(self.getFooterLogo(), "BenzingaLogoFooter")

