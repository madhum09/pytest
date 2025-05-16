from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest


# @pytest.fixture(params=['chrome','firfox'],scope='class')
# def init_driver(request):
#     if request.param=="chrome":
#         service=Service(ChromeDriverManager().install())
#         web_driver=webdriver.Chrome(service=service)
#     if request.param=="firfox":
#         service=Service(GeckoDriverManager().install())  
#         web_driver=webdriver.Firefox(service=service)  
#     request.cls.driver=web_driver
#     yield
#     web_driver.close()