import time
from random import seed
from random import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from Pages.LoginPage import LoginPage
from Tests import conftest
from Pages.DashBoardPage import DashBoardPage
from Pages.AdminPage import AdminPage
from Utilities.readproperty import ReadConfig
from Utilities.cutomLogger import LogGen
import time



class Test_AdminPage_Add_Job:
    #baseURL = "https://opensource-demo.orangehrmlive.com/"
    # userName = "Admin"
    # password = "admin123"
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    mylogger = LogGen.loggen()
    jobtitlecreated=False

    @pytest.mark.sanity
    def test_AddJobTitle(self,setup):
        self.mylogger.info("*******test_AddJobTitle********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.mylogger.info("*******Browser started********")
        self.lPage = LoginPage(self.driver)
        self.lPage.setUserName(self.username)
        self.lPage.setPassword(self.password)
        self.lPage.clickLogin()
        self.mylogger.info("*******Login successful********")
        time.sleep(3)
        self.dashPage= DashBoardPage(self.driver)
        self.dashPage.clickAdmin()
        time.sleep(3)
        self.mylogger.info("*******Landed on Admin page********")
        self.AdPage = AdminPage(self.driver)
        self.AdPage.clickJob()
        time.sleep(3)
        self.AdPage.clickJob()
        self.AdPage.clickJobTitle()
        self.AdPage.clickAddJobTitle()
        # seed random number generator
        #seed(1)
        #rndom_number = str(random())
        self.mylogger.info("*******Adding new  Job title********")
        self.AdPage.setJobTitle("Automation Engineer" )
        self.AdPage.setJobDesc(" Selenium python java cucumber junit")
        self.AdPage.choosefile("C:\\Users\\bala_\\Desktop\\MyTesting.txt")
        self.AdPage.setNote("10 years experience required")
        self.AdPage.clickSave()
        ####3Checkin record is added ot not
        self.rows =self.driver.find_elements_by_xpath("//table[@id='resultTable']/tbody/tr")
        self.rowcount=len(self.rows)
        print(self.rowcount)
        if self.rowcount > 0:
            for i in range(1,self.rowcount):
                self.newjobtitle = self.driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr["+str(i)+"]/td[2]")
                if self.newjobtitle.text == "Automation Engineer":
                    self.jobtitlecreated=True
                    self.driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[" + str(i) + "]/td[1]").click()

        main_window_handle = self.driver.current_window_handle
        print(main_window_handle)
        self.AdPage.clickDelete()
        #self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.find_element_by_id("dialogDeleteBtn").click()
        if self.jobtitlecreated:
            assert True
        else:
            self.drier.get_screenshot(".\\Screenshots\\test_AddJobTitle.png")
            assert False

        self.driver.close()


