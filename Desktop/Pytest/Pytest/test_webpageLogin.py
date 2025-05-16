from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

import time

def test_google():
    
    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('https://www.google.com/')
    
    assert driver.title=="Google"
    driver.quit()

def test_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('https://www.facebook.com/')
    
    assert driver.title =="Facebook - log in or sign up"
        
    driver.quit()

def test_amazon():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get('https://www.amazon.com/')
    
    assert driver.title == "Amazon.com. Spend less. Smile more."
    driver.quit()