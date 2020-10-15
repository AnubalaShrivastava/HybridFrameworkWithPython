import pytest

from Pages.LoginPage import LoginPage
from Tests import conftest
from Pages.DashBoardPage import DashBoardPage
from Pages.AdminPage import AdminPage
from Utilities.readproperty import ReadConfig
from Utilities.cutomLogger import LogGen
import time

class Test_AdminPage_Search_User:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    mylogger = LogGen.loggen()

    @pytest.mark.regression
    def test_Search_User(self,setup):
        self.mylogger.info("*******Searching for Existing User**********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lPage = LoginPage(self.driver)
        self.lPage.setUserName(self.username)
        self.lPage.setPassword(self.password)
        self.lPage.clickLogin()
        self.mylogger.info("*******Login is successfull**********")
        time.sleep(2)
        #Clicking on menu Admin
        self.dashPage = DashBoardPage(self.driver)
        self.dashPage.clickAdmin()
        time.sleep(2)
        self.mylogger.info("*******Menu Admin click is successfull**********")

        # AdminPage Avtivities
        self.mylogger.info("*******Entered In Admin Page**********")
        self.AdPage = AdminPage(self.driver)
        self.AdPage.clickUserManagement()
        self.AdPage.clickUsers()
        #searching with no username
        self.mylogger.info("*******Entering search info**********")
        self.AdPage.setUserName("")
        self.AdPage.setUserRoleByIndex(1)
        self.AdPage.setEmpName("John Smith")
        self.AdPage.setstatusByIndex(1)
        self.AdPage.clickSearch()
        self.mylogger.info("*******Clicked search**********")

        #Checking search result
        self.rows = self.AdPage.getrows()
        self.rowcount = len(self.rows)
        if self.rowcount > 0:
            assert True
            self.mylogger.info("*******User Exist :Test Pass**********")
        else:
            assert False
            self.mylogger.info("*******User  not Exist :Test Fail**********")
        self.mylogger.info("*******Exiting test_Search_User**********")
        self.driver.close()


