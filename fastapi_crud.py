import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MesajModel(BaseModel):
    kullanici_mesaji:str
    bot_cevabi:str

def create_db_connection():
    return sqlite3.connect("mesajlar.db")


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


create_table()

@app.post("/mesaj-ekle")
def mesaj_ekle_endpoint(veri:MesajModel):
    add_message(veri.kullanici_mesaji, veri.bot_cevabi)
    return{
        "durum":"basarili",
        "mesaj":"kayit dbye basari ile eklendi",
        "eklenen_veri":{
            "kullanici_mesaji": veri.kullanici_mesaji,
            "bot_mesaji": veri.bot_cevabi
        }
    }

@app.get("/mesajlar")
def mesajlari_listele():
    kayitlar = get_all_messages()

    sonuc = []
    for kayit in kayitlar:
        sonuc.append(
            {
                "id":kayit[0],
                "kullanici_mesaji": kayit[1],
                "bot_cevabi": kayit[2]
            }
        )
    return {
        "durum":"basarili",
        "toplam_kayit": len(sonuc),
        "mesajlar": sonuc
    }

@app.patch("/mesaji-guncelle/{kayit_id}")
def mesaji_guncelle(kayit_id:int, veri:MesajModel):
    baglanti = create_db_connection()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            UPDATE mesajlar
            SET kullanici_mesajlari = ?, bot_cevabi = ?
            WHERE id = ?
        """,
        (veri.kullanici_mesaji, veri.bot_cevabi, kayit_id)
    )

    baglanti.commit()
    baglanti.close()

    return {
        "durum":"basarili",
        "mesaj":"kayit dbde basarili guncellendi",
        "guncellenen_kayit": {
            "id": kayit_id,
            "kullanici_mesaji": veri.kullanici_mesaji,
            "bot_cevabi": veri.bot_cevabi
        }
    }

    