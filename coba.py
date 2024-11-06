import time
from lib import driver, auth
from selenium.webdriver.common.by import By

driver = driver.WebDriverManager()

# Autentikasi Facebook
auth.authentication(driver)
time.sleep(3) # Tunggu 3 detik

#  Percobaan komentar
# driver.get_url("https://web.facebook.com/profile.php?id=100011345357474")
# time.sleep(2)

# Mendapatkan 1 postingan
# post = driver.find_element(By.XPATH, '//*[@id="mount_0_0_eM"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]')

# click input komentar
# input_komentar = post.find_element(By.XPATH, './/div[@aria-placeholder="Tulis komentar..."]')
# input_komentar.click()
# input_komentar.send_keys("Halo, ini adalah komentar dari bot")
# time.sleep(2)

# Mendapatkan input file dan mengirimkan gambar
# post.find_element(By.XPATH, './/input[@type="file"]').send_keys('/image/gojo.jpg')
# time.sleep(2)

# Mengirimkan komentar
# post.find_element(By.CSS_SELECTOR, 'div[aria-label="Komentari"][role="button"]').click()

time.sleep(7)

driver.quit_driver()