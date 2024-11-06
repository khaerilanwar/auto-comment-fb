driver.get("https://web.facebook.com/profile.php?id=100011345357474")

# scroll kebawah
driver.scroll()
time.sleep(5)

post = driver.find_element(By.XPATH, '//*[@id="mount_0_0_eM"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[2]')

# click input komentar
input_komentar = post.find_element(By.XPATH, './/div[@aria-placeholder="Tulis komentar..."]')
input_komentar.click()
input_komentar.send_keys("Halo, ini adalah komentar dari bot")
time.sleep(3)

# Mendapatkan input file dan mengirimkan gambar
post.find_element(By.XPATH, './/input[@type="file"]').send_keys('/image/gojo.jpg')
time.sleep(3)

# Mengirimkan komentar
post.find_element(By.CSS_SELECTOR, 'div[aria-label="Komentari"][role="button"]').click()