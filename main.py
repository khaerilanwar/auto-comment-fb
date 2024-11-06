from dotenv import load_dotenv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

load_dotenv()

# kredensial login fb
email = os.getenv("EMAIL_FB")
password = os.getenv("PASSWORD_FB")

# url login fb
url_login = 'https://web.facebook.com/'
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Mengakses url login fb
driver.get(url_login)

# Mengisi form login fb
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "pass").send_keys(password)
driver.find_element(By.NAME, "login").click()

# Mengakses url feed grup

# Ambil tinggi halaman awal
last_height = driver.execute_script("return document.body.scrollHeight")

# Menentukan waktu scroll dalam detik
scroll_duration = 30 # 10 detik
end_time = time.time() + scroll_duration

while True:
    # scroll ke bawah halaman
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Ambil tinggi halaman setelah di scroll
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Cek apakah sudah mencapai akhir halaman
    if new_height == last_height:
        print("Akhir halaman feed grup")
        break

    # Update tinggi halaman untuk perulangan berikutnya
    last_height = new_height

    # Jika memang masih belum ada ujungnya, maka gunakan durasi waktu
    if time.time() > end_time:
        print("Waktu scroll habis")
        break

# Ambil semua postingan di feed grup
feed_grup = driver.find_element(By.XPATH, "//div[@role='feed']")
post_grup = feed_grup.find_elements(By.XPATH, './div')


    
# Jika sudah komen semua postingan di feed grup
# Lanjut ke grup utama yang rame
grup_utama = "https://web.facebook.com/groups/784838364941674"


# 1. Cari wrapper postingan feed grup dengan role="feed"
# 2. Mendapatkan tiap-tiap postingan dengan 

time.sleep(5)
driver.quit()