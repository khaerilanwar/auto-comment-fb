import os
import time
from lib.utils import get_today
from lib.mail import Mail
from colorama import Fore, Back, Style, init
from dotenv import load_dotenv
from lib.driver import WebDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
init(autoreset=True)

# Kredensial akun facebook bot
url_login = os.getenv("LINK_LOGIN")
email_fb = os.getenv("EMAIL_FB")
password_fb = os.getenv("PASSWORD_FB")

# Kredensial akun email laporan bot
email = os.getenv("EMAIL_ADDR")
password = os.getenv("EMAIL_PASS")
receiver = os.getenv("RECEIVER")

start_time = get_today()

mail_server = Mail(email, password)
driver = WebDriverManager()

# Login Facebook
driver.authentication(url_login, email_fb, password_fb)
time.sleep(4)


total_posts = 0
total_comments = 0
total_scrolls = 0

try:
    links_target = [
        "https://web.facebook.com/groups/784838364941674",
        "https://web.facebook.com/groups/feed/"
    ]

    for link in links_target:
        # Masuk ke halaman feed grup
        driver.get(link)
        time.sleep(3)

        # scroll ke bawah
        for i in range(8):

            # scroll ke bawah
            driver.scroll(3)
            print(Fore.BLUE + f"- Scroll ke {i+1}")

            # increment total scroll
            total_scrolls += 1
            time.sleep(5)

            feed_grup = driver.find_element(By.CSS_SELECTOR, 'div[role="feed"]')
            feed_posts = feed_grup.find_elements(By.XPATH, './div')

            count_comment = 0
            for post in feed_posts:
                try:
                    # mendapatkan tombol komentar
                    button_comment = post.find_element(By.CSS_SELECTOR, 'div[aria-label="Beri komentar"][role="button"]')
                    button_comment.click()

                    # pindah ke input komentar
                    input_comment = driver.switch_to.active_element
                    input_comment.send_keys('Jasa pembuatan lamaran email PDF dan CV menarik ..')
                    input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
                    input_comment.send_keys('Harga mulai dari 15.000, pemesanan hanya melalui')
                    input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
                    input_comment.send_keys('Whatsapp : 0821 3763 3527')
                    input_comment.send_keys(Keys.SHIFT, Keys.ENTER)
                    input_comment.send_keys('https://api.whatsapp.com/send?phone=6282137633527')
                    input_comment.send_keys(Keys.ENTER)

                    count_comment += 1
                    print(Fore.GREEN + f"-- Berhasil komentar ke {count_comment}")

                    time.sleep(3*60)
                except:
                    continue

            else:
                count_post = len(feed_posts)
                print(Fore.RED + f"--- Total Post = {count_post}" + "\t" + Fore.GREEN + f"--- Total Komentar {count_comment}")

                # increment total post, comment
                total_posts += count_post
                total_comments += count_comment
                time.sleep(10)
    
    else:
        data_msg = {
            'total_scrolls': total_scrolls,
            'total_posts': total_posts,
            'total_comments': total_comments
        }

        mail_server.send_mail(receiver=receiver, data=data_msg, start_time=start_time)

except Exception as e:
    mail_server.send_mail(receiver=receiver, error=e, start_time=start_time)
    print(Fore.RED + f"Error : {e}")

time.sleep(8)

driver.quit()