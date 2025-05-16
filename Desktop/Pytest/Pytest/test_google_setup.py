from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#driver=None

def setup_module(module):
    global driver
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    driver.implicitly_wait(10)

def teardown_module(module):
    driver.quit()    

def test_URL():
    assert driver.current_url=="https://www.google.com/"
    
def test_title():
    assert driver.title=="Google"
