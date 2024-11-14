from datetime import datetime, timedelta, timezone

def get_today():
    # utc_now = datetime.utcnow()
    # tz = timezone(timedelta(hours=7))
    # actual_time = utc_now.astimezone(tz)
    actual_time = datetime.now()

    hari_dalam_minggu = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan_dalam_tahun = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

    hari = hari_dalam_minggu[actual_time.weekday()]
    bulan = bulan_dalam_tahun[actual_time.month - 1]
    today_translate = f"{hari}, {actual_time.day} {bulan}, {actual_time.year} Pukul {actual_time.hour}:{actual_time.minute}"

    return today_translate