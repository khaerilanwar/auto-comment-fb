import locale
from datetime import datetime

def get_today():
    locale.setlocale(locale.LC_TIME, 'ind')
    today = datetime.today()
    today_translate = today.strftime("%A, %d %B %Y Pukul %H:%M")

    return today_translate