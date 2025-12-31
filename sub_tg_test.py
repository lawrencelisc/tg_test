# 獨立測試腳本
import requests

TOKEN = "8022395376:AAGC6r3pNGq1PBodeMZ3leYxhqgGaKr51rs"
CHAT_ID = "8394621040"

# 測試 1: 檢查 Bot 是否正常
response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe", timeout=5)
print(f"Bot Status: {response.status_code}")
print(f"Bot Info: {response.json()}")

# 測試 2: 發送簡單訊息
response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={'chat_id': CHAT_ID, 'text': 'Test message'},
    timeout=5
)
print(f"Send Status: {response.status_code}")
print(f"Response: {response.json()}")