# 🚀 SQLite & FastAPI CRUD Projesi

Bu proje, Python'da yerel **SQLite** veritabanı yönetimi ile modern, hızlı ve yüksek performanslı **FastAPI** web çatısının entegrasyonunu gösteren örnek bir RESTful API ve CRUD (Create, Read, Update, Delete) uygulama koleksiyonudur.

Proje içerisinde hem doğrudan SQLite fonksiyonları ile veri yönetimi, hem FastAPI üzerinden HTTP endpoint'leri, hem de `requests` kütüphanesi ile istemci (client) tarafı tüketimi yer almaktadır.

---

## 📂 Proje Yapısı

```text
sqlite_db_fastapi/
│
├── company_example.py      # Şirket / Çalışan yönetimi için FastAPI & SQLite uygulaması (sirket.db)
├── fastapi_crud.py         # Chatbot mesaj kayıtları için RESTful FastAPI servisi (mesajlar.db)
├── crud.py                 # Konsol üzerinden çalışan modüler SQLite CRUD fonksiyonları
├── sqlite_veritabani.py    # Temel SQLite bağlantısı ve tablo oluşturma giriş örneği
├── client.py               # FastAPI servislerini test eden örnek Python istemcisi
│
├── mesajlar.db             # Mesaj verilerinin saklandığı SQLite veritabanı
├── sirket.db               # Çalışan verilerinin saklandığı SQLite veritabanı
└── readme.md               # Proje dokümantasyonu
```

---

## 🛠️ Teknolojiler ve Gereksinimler

- **Python 3.8+**
- **FastAPI**: Modern, asenkron destekli REST API çatısı
- **Uvicorn**: Yüksek performanslı ASGI sunucusu
- **Pydantic**: Veri doğrulama ve modelleme
- **SQLite3**: Python ile dahili gelen ilişkisel veritabanı
- **Requests**: HTTP istekleri gönderen istemci kütüphanesi

### Kurulum

Gerekli paketleri sanal ortamınıza yüklemek için:

```bash
pip install fastapi uvicorn requests pydantic
```

---

## 🚀 Uygulamaları Çalıştırma

### 1. Şirket & Çalışan Yönetimi API'si (`company_example.py`)

Çalışan ekleme ve listeleme işlemlerini yöneten FastAPI servisini başlatmak için:

```bash
uvicorn company_example:app --reload
```

- **Swagger UI (İnteraktif Dokümantasyon):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Endpoint'ler:
| Metot | Endpoint | Açıklama |
|---|---|---|
| `POST` | `/calisan-ekle` | Yeni çalışan kaydı oluşturur |
| `GET` | `/calisanlar` | Kayıtlı tüm çalışanları listeler |

**Örnek POST Gövdesi (`/calisan-ekle`):**
```json
{
  "isim": "Ahmet Yılmaz",
  "bolum": "Yazılım",
  "yas": 28
}
```

---

### 2. Mesaj Yönetimi API'si (`fastapi_crud.py`)

Kullanıcı ve bot mesajlaşma kayıtlarını saklayan, güncelleyen ve listeleyen FastAPI servisini başlatmak için:

```bash
uvicorn fastapi_crud:app --reload
```

#### Endpoint'ler:
| Metot | Endpoint | Açıklama |
|---|---|---|
| `POST` | `/mesaj-ekle` | Kullanıcı mesajı ve bot cevabını kaydeder |
| `GET` | `/mesajlar` | Tüm mesajlaşma geçmişini listeler |
| `PATCH` | `/mesaji-guncelle/{kayit_id}` | Belirtilen ID'ye sahip mesaj kaydını günceller |

**Örnek POST Gövdesi (`/mesaj-ekle`):**
```json
{
  "kullanici_mesaji": "Merhaba, nasıl yardımcı olabilirsin?",
  "bot_cevabi": "Size çeşitli konularda destek sağlayabilirim."
}
```

---

### 3. İstemci Testi (`client.py`)

`fastapi_crud:app` sunucusu çalışırken ayrı bir terminalde istemci betiğini çalıştırarak endpoint'lere otomatik istek gönderebilirsiniz:

```bash
python client.py
```

Bu script:
1. `POST /mesaj-ekle` ile yeni mesaj gönderir.
2. `GET /mesajlar` ile tüm mesajları çeker ve konsola yazdırır.

---

### 4. Saf SQLite CRUD Betiği (`crud.py`)

FastAPI olmadan, konsol üzerinden doğrudan SQLite veritabanı işlemlerini (Create, Read, Update, Delete) test etmek için:

```bash
python crud.py
```

---

## 🗄️ Veritabanı Şemaları

### `calisanlar` Tablosu (`sirket.db`)

| Sütun | Tip | Kısıtlamalar |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| `isim` | TEXT | NOT NULL |
| `bolum` | TEXT | NOT NULL |
| `yas` | INTEGER | NOT NULL |

### `mesajlar` Tablosu (`mesajlar.db`)

| Sütun | Tip | Kısıtlamalar |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| `kullanici_mesajlari` | TEXT | NOT NULL |
| `bot_cevabi` | TEXT | NOT NULL |

---

## 📌 İpuçları & Güvenlik

- SQL sorgularında parametre bağlama (`?` yer tutucuları) kullanılarak **SQL Injection** açıkları önlenmiştir.
- FastAPI modelleri için **Pydantic** kullanılarak tip kontrolü ve otomatik validasyon sağlanmıştır.
- Her işlem sonrasında veritabanı bağlantısı `close()` fonksiyonu ile kapatılarak bağlantı sızıntıları engellenmiştir.