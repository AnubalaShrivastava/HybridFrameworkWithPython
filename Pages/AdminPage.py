from selenium import webdriver
from selenium.webdriver.support.select import Select


class AdminPage:
    menu_usermanagement_id="menu_admin_UserManagement"
    menu_users_id="menu_admin_viewSystemUsers"
    list_job_id="menu_admin_Job"
    list_jobtitle_id="menu_admin_viewJobTitleList"
    btn_add_id="btnAdd"
    txt_jobtitle_id="jobTitle_jobTitle"
    txtarea_jobdesc_id="jobTitle_jobDescription"
    btn_choosefile_id="jobTitle_jobSpec"
    txtarea_note_id="jobTitle_note"
    btn_save_id="btnSave"
    rows_jobtable_xpath ="//table[@id='resultTable']/tbody/tr"
    cols_jobtable_xpath="//table[@id='resultTable']/tbody/tr/td"
    btn_delete_id ="btnDelete"
    txt_username_id ="searchSystemUser_userName"
    dd_userrole_xpath = "//*[@id='searchSystemUser_userType']"
    txt_empName_id="searchSystemUser_employeeName_empName"
    dd_status_id = "searchSystemUser_status"
    btn_search_id ="searchBtn"
    # rows_result_xpath="//Table[@id='resultTable']/tbody/tr"
    # colss_result_xpath = "//Table[@id='resultTable']/tbody/tr/td"
    
    def __init__(self,driver):
        self.driver=driver

    def clickUserManagement(self):
        self.driver.find_element_by_id(self.menu_usermanagement_id).click()

    def clickUsers(self):
        self.driver.find_element_by_id(self.menu_users_id).click()

    def clickJob(self):
        self.driver.find_element_by_id(self.list_job_id).click()

    def clickJobTitle(self):
        self.driver.find_element_by_id(self.list_jobtitle_id).click()

    def clickAddJobTitle(self):
        self.driver.find_element_by_id(self.btn_add_id).click()

    def setJobTitle(self,jobtitle):
        self.driver.find_element_by_id(self.txt_jobtitle_id).send_keys(jobtitle)

    def choosefile(self,filenamewithpath):
        self.driver.find_element_by_id(self.btn_choosefile_id).send_keys(filenamewithpath)

    def setJobDesc(self,jobdescription):
        self.driver.find_element_by_id(self.txtarea_jobdesc_id).send_keys(jobdescription)

    def setNote(self,note):
        self.driver.find_element_by_id(self.txtarea_note_id).send_keys(note)

    def clickSave(self):
        self.driver.find_element_by_id(self.btn_save_id).click()

    def getrows(self):
         return self.driver.find_elements_by_xpath(self.rows_jobtable_xpath)

    def clickDelete(self):
        self.driver.find_element_by_id(self.btn_delete_id ).click()

    def setUserName(self,username):
        self.driver.find_element_by_id( self.txt_username_id).send_keys(username)

    def setUserRoleByIndex(self, index):
        self.dd_UseRole = Select(self.driver.find_element_by_xpath(self.dd_userrole_xpath))
        self.dd_UseRole.select_by_index(index)

    def setEmpName(self,name):
        self.driver.find_element_by_id( self.txt_empName_id).send_keys(name)

    def setstatusByIndex(self, index):
        self.dd_Status = Select(self.driver.find_element_by_id(self.dd_status_id ))
        self.dd_Status.select_by_index(index)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btn_search_id).click()







