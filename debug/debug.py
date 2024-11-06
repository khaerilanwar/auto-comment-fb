import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.auth import authentication

load_dotenv()

driver = webdriver.Chrome()
driver.implicitly_wait(10)

authentication()

driver.quit()