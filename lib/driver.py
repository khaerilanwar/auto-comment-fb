import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverManager(webdriver.Chrome):
    def __init__(self, options=None):
        if not options:
            options = Options()
            options.add_argument("--disable-gpu")
        super().__init__(options=options)

    def wait_until(self, locator, timeout=10):
        return WebDriverWait(self, timeout).until(EC.presence_of_element_located(locator))
    
    def test_class(self):
        print("Test class")

    def authentication(self, url, email, password):
        self.get(url)
        self.wait_until((By.NAME, "email")).send_keys(email)
        self.wait_until((By.NAME, "pass")).send_keys(password)
        self.wait_until((By.NAME, "login")).click()

    def scroll(self, duration=5):
        end_time = time.time() + duration
        body = self.find_element(By.TAG_NAME, 'body')
        while time.time() < end_time:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
