import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalisanModel(BaseModel):
    isim:str
    bolum:str
    yas:int

def create_db():
    return sqlite3.connect("sirket.db")


def create_employee_table():
    baglanti = create_db()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            CREATE TABLE IF NOT EXISTS calisanlar(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                bolum TEXT NOT NULL,
                yas INTEGER NOT NULL
            )
        """
    )

    baglanti.commit()
    baglanti.close()
    return {
        "durum": "basarili",
        "mesaj": "calisanlar tablosu basari ile olusturuldu"
    }

def add_employee(isim:str, bolum:str, yas:int):
    baglanti = create_db()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            INSERT INTO calisanlar(isim, bolum, yas)
            VALUES (?, ?, ?)
        """,(isim, bolum, yas)
    )

    baglanti.commit()
    baglanti.close()

    return {
        "durum": "basarili",
        "mesaj": "calisan basari ile eklendi",
        "yeni_calisan":{
            "isim": isim,
            "bolum": bolum,
            "yas": yas
        }
    }

def get_all_employees():
    baglanti = create_db()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            SELECT * FROM calisanlar
        """
    )

    kayitlar = imlec.fetchall()
    baglanti.close()

    sonuc = []
    for kayit in kayitlar:
        sonuc.append(
            {
                "id": kayit[0],
                "isim": kayit[1],
                "bolum": kayit[2],
                "yas": kayit[3]
            }
        )

    return {
        "durum": "basarili",
        "toplam_kayit": len(sonuc),
        "calisanlar": sonuc
    }


@app.post("/calisan-ekle")
def calisan_ekle(veri:CalisanModel):
    add_employee(veri.isim, veri.bolum, veri.yas)

    return {
        "durum": "basarili",
        "mesaj": "calisan basari ile eklendi",
        "eklenen_calisan": {
            "isim": veri.isim,
            "bolum": veri.bolum,
            "yas": veri.yas
        }
    }

@app.get("/calisanlar")
def calisanlari_getir():
    calisanlar = get_all_employees()
    return calisanlar

create_employee_table()
