from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


import pytest

@pytest.fixture()
def setup(browser):
    if browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Selenium\\geckodriver.exe")
        #driver = webdriver.Firefox()
    # elif browser=='IE':
    #     driver = webdriver.Ie()


    else :
        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
     return request.config.getoption("--browser")

