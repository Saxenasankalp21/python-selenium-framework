#Author#SankalpSaxena
from base.base_driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.common.by import By


class BenzingaLoginPage(BaseDriver):
    global utilities
    ut = Utils()
    def __init__(self, driver):
        super().__init__(driver) # This keyword allows to use base driver class methods in test files
        self.driver = driver

    #LOCATORS#####
    EMAIL_INPUT = "email"
    PASSWORD_INPUT =  "current-password"
    LOGIN_BUTTON = "/html/body/div[1]/div/div/div/div/div/div/div[3]/form/div[3]/button"
    BENZINGA_LINK_FROM_ACCESS_PAGE = "a.sc-hhTLmD"

    #locatos
    def get_email_input(self):
        return self.wait_element_to_be_clickable(By.ID, self.EMAIL_INPUT)

    def get_password_input(self):
        return self.driver.find_element(By.ID, self.PASSWORD_INPUT)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def get_benzinga_access_your_subscription_link(self):
        return self.wait_visibility_of_element_located(By.CSS_SELECTOR, self.BENZINGA_LINK_FROM_ACCESS_PAGE)

    def verify_email_field(self):
        self.get_email_input().click()
        self.get_email_input().send_keys("sankalpsaxena@benzinga.com")

    def verify_password_field(self):
        self.get_password_input().send_keys("Wisdom21#")

    def verify_login_button(self):
        self.get_login_button().click()

    def verify_access_your_link(self):
        self.get_benzinga_access_your_subscription_link().click()

    def benzinga_login(self):
        self.verify_email_field()
        self.verify_password_field()
        self.verify_login_button()
        self.verify_access_your_link()




    # wait.until(EC.element_to_be_clickable((By.ID, "email"))).click()
    # driver.find_element(By.ID, "email").send_keys("sankalpsaxena@benzinga.com")
    # driver.find_element(By.ID, "current-password").send_keys("Wisdom21#")
    # # click on login button
    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[3]/form/div[3]/button").click()
    # # click on benzinga.com link
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.sc-hhTLmD"))).click()