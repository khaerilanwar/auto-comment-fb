import os
import time
from dotenv import load_dotenv
from lib.driver import WebDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

url_login = os.getenv("LINK_LOGIN")
email = os.getenv("EMAIL_FB")
password = os.getenv("PASSWORD_FB")

driver = WebDriverManager()

# Login Facebook
driver.authentication(url_login, email, password)
time.sleep(4)

# Masuk ke halaman feed grup
driver.get("https://web.facebook.com/groups/784838364941674")
time.sleep(3)

# scroll ke bawah
for i in range(4):
    driver.scroll()
    time.sleep(4)

feed_grup = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
feed_posts = feed_grup.find_elements(By.XPATH, './div')

count_post = 0
for post in feed_posts:
    try:
        # mendapatkan tombol komentar
        button_comment = post.find_element(By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]')
        button_comment.click()

        # pindah ke input komentar
        input_comment = driver.switch_to.active_element
        input_comment.send_keys('Jasa pembuatan surat lamaran email dan CV menarik ..')
        input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
        input_comment.send_keys('Harga mulai dari 5.000, pemesanan hanya melalui')
        input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
        input_comment.send_keys('Whatsapp : 0821 3763 3527')
        input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
        input_comment.send_keys('https://api.whatsapp.com/send?phone=6282137633527')
        input_comment.send_keys(Keys.ENTER)

        count_post += 1
        print(f"Berhasil komentar ke {count_post}")

        time.sleep(30)
    except:
        continue

else:
    print(len(feed_posts))
    print(count_post)

time.sleep(8)

driver.quit()