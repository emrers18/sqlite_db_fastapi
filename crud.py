from sqlite_veritabani import imlec
import sqlite3

#dbye baglanma func
def create_db_connection():
    return sqlite3.connect("mesajlar.db")

#tablo olusturma func
def create_table():
    baglanti = create_db_connection()
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

    baglanti.commit()
    baglanti.close()


#yeni kayit ekleme 
def add_message(kullanici_mesaji: str, bot_cevabi: str):
    baglanti = create_db_connection()
    imlec = baglanti.cursor()

    imlec.execute(
        """
        INSERT INTO mesajlar (kullanici_mesajlari, bot_cevabi)
        VALUES (?, ?)
        """,
        (kullanici_mesaji, bot_cevabi)
    )

    baglanti.commit()
    baglanti.close()   

def get_all_messages():
    baglanti = create_db_connection()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            SELECT * FROM mesajlar
        """
    )

    kayitlar = imlec.fetchall()
    baglanti.close()
    return kayitlar

def update_message(kayit_id, yeni_mesaj, yeni_bot_cevabi):
    baglanti = create_db_connection()
    imlec = baglanti.cursor()

    imlec.execute(
        """
        UPDATE mesajlar
        SET kullanici_mesajlari = ?, bot_cevabi = ?
        WHERE id = ?

        """, (yeni_mesaj, yeni_bot_cevabi, kayit_id)
    )

    baglanti.commit()
    baglanti.close()

def delete_message(kayit_id):
    baglanti = create_db_connection()
    imlec = baglanti.cursor()

    imlec.execute(
        """
        DELETE FROM mesajlar
        WHERE id = ?

        """, (kayit_id)
    )

    baglanti.commit()
    baglanti.close()



create_table()

add_message("Selam ben ", "Merhaba ben de !")

update_message(5, "Merhaba ben Ali", "Merhaba ben de yeni chat Ali!")  

delete_message(1)

for kayit in get_all_messages():
    print(kayit)  
