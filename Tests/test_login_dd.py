import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Tests import conftest
from Utilities.readproperty import ReadConfig
from Utilities.cutomLogger import LogGen
import time
from Utilities import XLUtils


class Test_LoginTest_DDT:
    baseURL=ReadConfig.getURL()
    path=".//TestData/LoginData.xlsx"
    mylogger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.mylogger.info("******test_title_ddt********")
        self.mylogger.info("******Verifying Login DDT Test from Excel file********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.mylogger.info("*******Test test_login browser launched*****")
        self.lPage= LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.passw = XLUtils.readData(self.path,"Sheet1",r,2)
            self.lPage.setUserName(self.user)
            self.lPage.setPassword(self.passw)
            self.mylogger.info("*****Username : "+ self.user +"***********Password : "+self.passw+"***********")
            self.lPage.clickLogin()
            time.sleep(2)
            actual_title = self.driver.title
            if actual_title == "OrangeHRM":
                 self.mylogger.info("********Test test_Login passed********")
                 assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.mylogger.info("******Test test_login failed******")
                assert False
                time.sleep(5)

        self.driver.close()



