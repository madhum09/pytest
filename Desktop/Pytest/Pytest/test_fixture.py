from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#driver=None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    driver.implicitly_wait(10)

    yield driver
    driver.quit()    

def test_URL(init_driver):
    assert driver.current_url=="https://www.google.com/"
    
def test_title(init_driver):
    assert driver.title=="Google"
