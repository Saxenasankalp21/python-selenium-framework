#Author#SankalpSaxena
import pytest
import softest
from pages.Benzinga_Home_Page import BenzingaComHomepagePage
from pages.Benzinga_Qoutes_Page import BenzingaQuotePage
from ddt import ddt, file_data

#This is the main test case file which has business test language testcases the code is abstracted
@pytest.mark.usefixtures("setup")
@ddt()
class TestBzHomePage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bzHomePage = BenzingaComHomepagePage(self.driver)
        self.bzQuotePage = BenzingaQuotePage(self.driver)

    @pytest.mark.order(2)
    def test_BZ_landing(self):
        self.bzHomePage.verify_landing()

    #@pytest.mark.skip("later")
    @pytest.mark.order(3)
    def test_BZ_Menu_List1_Header(self):
        self.bzHomePage.verify_header_menu_list1()

    #@pytest.mark.skip("later")
    @pytest.mark.order(4)
    def test_BZ_Menu_List2_Header(self):
        self.bzHomePage.verify_header_menu_list2()

    #@pytest.mark.skip("later")
    @file_data("../testData/tickerData.json")
    @pytest.mark.order(5)
    def test_Ticker_Search(self, tickername):
        self.bzHomePage.verify_ticker_search_input(tickername)
        self.bzQuotePage.verify_quote_page_url()

    #@pytest.mark.skip("later")
    @pytest.mark.order(1)
    def test_BZ_Footer(self):
        self.bzHomePage.verify_bz_footer_logo()




