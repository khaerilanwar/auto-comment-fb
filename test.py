import os
from dotenv import load_dotenv
from lib.mail import Mail

load_dotenv()

email = os.getenv("EMAIL_ADDR")
password = os.getenv("EMAIL_PASS")

data = {
    'total_scrolls': 8,
    'total_posts': 50,
    'total_comments': 35
}

receiver = 'infografisbrebes@gmail.com'

mail_server = Mail(email, password)

mail_server.send_mail(receiver, data)