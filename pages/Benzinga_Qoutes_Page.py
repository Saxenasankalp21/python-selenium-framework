#Author#SankalpSaxena
from base.base_driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.common.by import By


class BenzingaQuotePage(BaseDriver):
    ut = Utils()
    log = ut.custom_logger()
    def __init__(self, driver):
        super().__init__(driver) # This keyword allows to use base driver class methods in test files
        self.driver = driver

    #locators
    TICKER_NAME = "div[class*='quote-exchange-information'] span[class*='border border-bzblue']"



    def get_ticker_name(self):
        self.wait_url_contains("https://www.benzinga.com/quote")
        return self.wait_presence_of_element_located(By.CSS_SELECTOR, self.TICKER_NAME)


    def verify_quote_page_url(self):
        ticker_name  = self.get_ticker_name().text
        self.log.info(f"Landing to Quote URL of {ticker_name}")