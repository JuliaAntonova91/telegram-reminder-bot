import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import requests
import time

TOKEN = "8989800358:AAH4WFQ2Qe0FNckpE84RgcSJ6F06jkkIEXc"
CHAT_ID = 477470467

scope = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("magnetic-port-500910-p8-2218381dec72.json", scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("судове таблиця").sheet1

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": text})

print("Бот запущено...")

while True:
    try:
        rows = sheet.get_all_records()
        today = datetime.now().strftime("%d.%m.%Y")

        for row in rows:
            if str(row.get("дата"))[:10] == today:
                msg = f"🔔 Нагадування!\nСудова справа: {row.get('Номер справи')}\nДія: {row.get('Дія яку треба зробити')}\nЧас: {row.get('дата')}"
                send_message(msg)

        time.sleep(60)

    except Exception as e:
        print("Помилка:", e)
        time.sleep(10)
