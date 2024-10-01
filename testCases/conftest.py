import os
import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Utils

driver = None

@pytest.fixture(scope="session", autouse=True)
def setup(request, browser):
    utilities = Utils()
    log = utilities.custom_logger()
    global driver

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        #Chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--private-window")
        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "safari":
        driver = webdriver.Safari()



    driver.maximize_window()
    log.info("Browser open and maximized")

    try:
        driver.get("https://www.benzinga.com/login?action=login&next=https%3A%2F%2Fwww.benzinga.com%2F&utm_source=homepage")
        driver.implicitly_wait(40)
        wait = WebDriverWait(driver, 40)
        wait.until(EC.presence_of_element_located((By.ID, "email"))).click()
        username = driver.find_element(By.ID, "email").send_keys("sankalpsaxena@benzinga.com")
        log.info(f"Username entered : {username}")
        driver.find_element(By.ID, "current-password").send_keys("Wisdom21#")
        log.info("password entered")

        # click on login button
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[3]/form/div[3]/button").click()
        log.info("login button clicked")

        # click on benzinga.com link
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.sc-hhTLmD"))).click()
        curl = driver.current_url
        log.info(f"Landed to url: {curl} ")
        assert curl == "https://www.benzinga.com/"
        log.info("url is correct")
    except Exception as e:
        log.error(f"Exception is : {e} Login or Landing to Benzinga platform has been failed please check!!")
        driver.quit()


    # request.cls.driver = driver  #to use when scope is class in fixture
    # request.cls.wait = wait # to use when scope is class in fixture
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)


    yield
   #driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.benzinga.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "Benzinga.Com"