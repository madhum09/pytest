from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=['chrome','firfox'],scope='class')
def init_driver(request):
    if request.param=="chrome":
        service=Service(ChromeDriverManager().install())
        web_driver=webdriver.Chrome(service=service)
    if request.param=="firfox":
        service=Service(GeckoDriverManager().install())  
        web_driver=webdriver.Firefox(service=service)  
    request.cls.driver=web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class Base_chrome_Test:
    pass

class Test_Google_Chrome(Base_chrome_Test):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=="Google"
        