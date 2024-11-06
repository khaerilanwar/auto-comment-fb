import os
import time
from dotenv import load_dotenv
from lib.driver import WebDriverManager
from selenium.webdriver.common.by import By

load_dotenv()

url_login = os.getenv("LINK_LOGIN")
email = os.getenv("EMAIL_FB")
password = os.getenv("PASSWORD_FB")

driver = WebDriverManager()

# Login Facebook
driver.authentication(url_login, email, password)
time.sleep(4)

# Masuk ke halaman feed grup
driver.get("https://web.facebook.com/groups/feed/")
time.sleep(3)

# scroll ke bawah
for i in range(2):
    driver.scroll()
    time.sleep(4)

feed_grup = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
feed_posts = feed_grup.find_elements(By.XPATH, './div')

for post in feed_posts:
    # text_post = post.find_element(By.CSS_SELECTOR, 'div[data-ad-rendering-role="message"]').text
    # print(text_post)
    print(post.text)
    print("\n", 50 * "-", "\n")

time.sleep(8)

driver.quit()