from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(scope='class')
def init_driver(request):
    service=Service(ChromeDriverManager().install())
    ch_driver=webdriver.Chrome(service=service)
    request.cls.driver=ch_driver
    yield
    ch_driver.close()


@pytest.mark.usefixtures("init_driver")
class Base_chrome_Test:
    pass

class Test_Google_Chrome(Base_chrome_Test):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=="Google"
        