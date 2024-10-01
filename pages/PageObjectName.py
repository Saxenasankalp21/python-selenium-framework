#Author#SankalpSaxena
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class PageNameClass(BaseDriver):
    ut = Utils()
    log = ut.custom_logger()
    def __init__(self, driver):
        super().__init__(driver) # This keyword allows to use base driver class methods in test files
        self.driver = driver


    # locators########
    #login
    LOCATORNAME= "xpath, id, css etc here"


    #Get locators method#####
    def get_locator(self):
        return self.driver.find_element(By.XPATH, self.LOCATORNAME)


    #Operations on loctors######
    def operationName(self):
        self.get_locator().click()
