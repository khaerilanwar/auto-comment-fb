import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()

email = os.getenv("EMAIL_FB")
password = os.getenv("PASSWORD_FB")

def authentication(driver):
    url_login = 'https://web.facebook.com/'

    driver.get(url_login)
    driver.wait_until((By.NAME, "email")).send_keys(email)
    driver.wait_until((By.NAME, "pass")).send_keys(password)
    driver.wait_until((By.NAME, "login")).click()