import smtplib
from lib.utils import get_today
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail:
    def __init__(self, email_address, email_password):
        self.email_address = email_address
        self.email_password = email_password
        self.message = MIMEMultipart()

    def send_mail(self, receiver, data: dict = None, error=None, start_time=None):
        # Membuat pesan email
        self.message['From'] = "BOT LAPORAN"
        self.message['To'] = receiver

        if error:
            self.message['Subject'] = "Error Bot Facebook Promosi"
            # Isi email
            body = f"""
                        Error Bot Facebook Promosi {get_today()}

                        \t-- Error : {error}
                    """
        else:
            self.message['Subject'] = "Laporan Bot Facebook Promosi"
            # Isi email
            body = f"""
                        Laporan Promosi Bot Facebook {get_today()}

                        \t----------------- Data Promosi -----------------
                        \t-- Total melakukan scroll {data['total_scrolls']}
                        \t-- Total element postingan {data['total_posts']}
                        \t-- Total berhasil berkomentar {data['total_comments']}

                        \t-- Terima kasih
                        \t-- Mulai : {start_time if start_time else get_today()}
                        \t-- Selesai : {get_today()}
                    """
        
        self.message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.sendmail(self.email_address, receiver, self.message.as_string())
                print("Email berhasil dikirim")
                
        except Exception as e:
            print(f"Error : {e}")