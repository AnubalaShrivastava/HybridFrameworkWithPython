from selenium.webdriver.chrome import webdriver

class LoginPage:
    txt_username_id ="txtUsername"
    txt_password_id ="txtPassword"
    btn_login_id = "btnLogin"

    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_id(self.btn_login_id).click()

