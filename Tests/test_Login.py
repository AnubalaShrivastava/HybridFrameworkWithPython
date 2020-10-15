import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Tests import conftest
from Utilities.readproperty import ReadConfig
from Utilities.cutomLogger import LogGen
import time


class Test_LoginTest:
    baseURL=ReadConfig.getURL()
    userName=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    mylogger = LogGen.loggen()


    @pytest.mark.regression
    def test_title(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.mylogger.info("Browser Launched")
        actual_title= self.driver.title
        print(actual_title)
        if actual_title=="OrangeHRM":
            assert True
            self.mylogger.info("Test test_title passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_title.png")
            assert False
            self.mylogger.info("Test test_title failed")
        time.sleep(5)
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.mylogger.info("Test test_login browser launched")
        self.lPage= LoginPage(self.driver)
        self.lPage.setUserName(self.userName)
        self.lPage.setPassword(self.password)
        self.lPage.clickLogin()
        actual_title = self.driver.title
        print(actual_title)
        if actual_title == "OrangeHRM":
            assert True
            self.mylogger.info("Test test_Login passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False
            self.mylogger.info("Test test_login failed")
        time.sleep(5)
        self.driver.close()



