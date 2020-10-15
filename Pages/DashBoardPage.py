from selenium import webdriver
class DashBoardPage:
    menu_Admin_id="menu_admin_viewAdminModule"
    menu_PIM_id = "menu_pim_viewPimModule"
    menu_Leave_id = "menu_leave_viewLeaveModule"
    menu_Time_id = "menu_time_viewTimeModule"
    menu_Recuirtment_id = "menu_recruitment_viewRecruitmentModule"
    menu_MyInfo_id = "menu_pim_viewMyDetails"
    menu_Performance_id = "menu__Performance"
    menu_DashBoard_id = "menu_dashboard_index"
    menu_Directory_id = "menu_directory_viewDirectory"
    menu_Maintance_id = "menu_maintenance_purgeEmployee"
    menu_Buzz_id = "menu_buzz_viewBuzz"
    btn_Marketplace_id = "MP_link"
    btn_Subscribe_id = "Subscriber_link"
    menu_Help_xpath = "//a[@class='help-icon-div']/span[contains(@class,'fa-lg fa-layers fa-fw')]"
    menu_Notification_xpath = "//div[@class='notification']/span[@id='notification']"
    link_User_id = "welcome"
    list_About_id = "aboutDisplayLink"
    list_Logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver


    def clickAdmin(self):
        self.driver.find_element_by_id(self.menu_Admin_id).click()
    def clickPIM(self):
        self.driver.find_element_by_id(self.menu_PIM_id).click()
    def clickLeave(self):
        self.driver.find_element_by_id(self.menu_Leave_id).click()
    def clickTime(self):
        self.driver.find_element_by_id(self.menu_Time_id ).click()
    def clickRecuirtment(self):
        self.driver.find_element_by_id(self.menu_Recuirtment_id).click()
    def clickMyInfo(self):
        self.driver.find_element_by_id(self.menu_MyInfo_id).click()
    def clickLogOut(self):
        self.driver.find_element_by_link_text(self.list_Logout_linktext).click()
