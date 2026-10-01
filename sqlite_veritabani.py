import sqlite3

baglanti = sqlite3.connect("mesajlar.db")

#sql komutlari icin cursor nesnesi
imlec = baglanti.cursor()

imlec.execute(
    """
    CREATE TABLE IF NOT EXISTS mesajlar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kullanici_mesajlari TEXT NOT NULL,
        bot_cevabi TEXT NOT NULL
    )
"""
)

imlec.execute(
    """
        INSERT INTO mesajlar (kullanici_mesajlari, bot_cevabi)
        VALUES(?, ?)
    """,(
        "Merhaba Nasilsin?", 
        "Merhaba ben ornek bir chatbot cevabiyim."
        )
)

#yapilan degisiklikleri dbye kaydet
baglanti.commit()
