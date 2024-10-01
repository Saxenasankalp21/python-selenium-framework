#Author#SankalpSaxena
import pytest
import softest
from pages.PageObjectName import BenzingaComHomepagePage
from pages.Benzinga_Qoutes_Page import BenzingaQuotePage
from ddt import ddt, file_data

#This is the main test case file which has business test language testcases the code is abstracted
@pytest.mark.usefixtures("setup")
@ddt()
class TestClassName(softest.TestCase): #Add your actual class name like landing page or login test cases like that

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.object = className(self.driver)


    #@pytest.mark.skip("later")
    @file_data("../testData/tickerData.json")
    @pytest.mark.order(1)
    def test_case_name(self, tickername):
        self.object.methodName()




