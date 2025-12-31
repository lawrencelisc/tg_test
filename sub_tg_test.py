# quick_test.py
import requests
import socket

# 強制 IPv4
old_getaddrinfo = socket.getaddrinfo
socket.getaddrinfo = lambda *args, **kwargs: [
    res for res in old_getaddrinfo(*args, **kwargs)
    if res[0] == socket.AF_INET
]

# 測試
TOKEN = "8022395376:AAGC6r3pNGq1PBodeMZ3leYxhqgGaKr51rs"
response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe", timeout=5)
print(f"✅ Success! Status: {response.status_code}")
print(response.json())