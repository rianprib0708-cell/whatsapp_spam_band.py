import time
import random
import requests
from bs4 import BeautifulSoup

# Nomor target (contoh: +6281234567890)
target_number = input("Masukkan nomor WhatsApp target: ")

# Proxy untuk menghindari deteksi (contoh IP dari Dark Web)
proxies = [
    "http://10.10.1.1:8080",
    "http://10.10.1.2:8080",
    "http://10.10.1.3:8080"
]

# Jumlah pesan & interval (lebih cepat, semakin berbahaya)
num_messages = 1000
interval = 0.5  # detik

# Membuat bot spam menggunakan WhatsApp Web API
def whatsapp_spam(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    
    for _ in range(num_messages):
        # Konten spam acak
        spam_content = random.choice([
            "MASUK KE FIREWALL! 🚫🔥",
            "PING PONG PING PONG PING 🩸💻",
            "WIFI CRACKED! 💥☠️",
            "ANTI-AV ATTACK IN PROGRESS! 😈💣"
        ])
        
        # URL untuk mengirim pesan (dengan proxy)
        url = f"https://api.whatsapp.com/send?phone={target}&text={spam_content}"
        response = requests.get(url, headers=headers, proxies=random.choice(proxies))
        
        # Cek respons
        if response.status_code == 200:
            print(f"[+] Pesan ke {target} berhasil dikirim: {spam_content}")
        else:
            print(f"[-] Gagal mengirim pesan ke {target}: {response.status_code}")
        
        # Delay antar pesan (dapat disesuaikan untuk lebih berbahaya)
        time.sleep(interval)

# Jalankan script
whatsapp_spam(target_number)
