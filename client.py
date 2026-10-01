import requests

BASE_URL="http://127.0.0.1:8000"

gonderilecek_veri = {
    "kullanici_mesaji":"merhaba ben client",
    "bot_mesaji":"merhaba client ben de chatbot"
}

#post
post_response = requests.post(f"{BASE_URL}/mesaj-ekle", json = gonderilecek_veri)
print(f"post response: {post_response.json()}")

#get
get_response = requests.get(f"{BASE_URL}/mesajlar")
print(f"get response: {get_response.json()}")