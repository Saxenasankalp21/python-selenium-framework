import inspect
import logging
from datetime import datetime
import softest

class Utils(softest.TestCase):
    def custom_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('/Users/sankalpsmac/Documents/Benzinga/BenzingaDotCom/reports/BenzingaComLogFile.log', mode="w")
        formatter = logging.Formatter('%(asctime)s:  %(levelname)s : %(name)s : %(message)s')
        logger.addHandler(filehandler)
        filehandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger

    def assert_text_in_title(self, actualText, locator):
        getText = locator.text

        self.soft_assert(self.assertEqual, actualText, getText)
        if actualText == getText:
            print("Test Passed")
        else:
            print("Test Failed")
        self.assert_all()

    def assert_actual_expected_List(self, expectedList, list_items, actualList ):
        for list in list_items:
            actualList.append(list.text)
        print(actualList)
        self.soft_assert(self.assertEqual, expectedList, actualList)
        if expectedList == actualList:
            print("Test Passed")
        else:
            print("Test Failed")
        self.assert_all()


    def save_screenshot_locator(self, locator, name):
        dt = datetime.now()
        locator.screenshot(f"../screenshots/logo_Banners_Screenshot/{name}{dt}.png")


