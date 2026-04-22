# Event Map Analytics & Automation Scripts

Python tabanlı analiz ve otomasyon scriptleri.

## Teknoloji Stack

- **Runtime**: Python 3.8+
- **Database**: Cloud Firestore
- **Framework**: Flask (API servisleri için)

## Kurulum

### Önkoşullar

- Python 3.8+
- pip

### Adımlar

```bash
cd scripts
pip install -r requirements.txt
```

## Ortam Değişkenleri

`.env` dosyası oluştur:

```
FIREBASE_KEY_PATH=path/to/firebase-key.json
FLASK_ENV=development
FLASK_DEBUG=True
```

## Scriptler

### main.py - Ana Analytics Script

```bash
python main.py
```

**İşlevleri:**
- Kullanıcı verilerini doğrula
- Etkinlik istatistiklerini al
- Genel rapor oluştur
- Veri kalitesini kontrol et

### generate_report.py

```bash
python generate_report.py
```

**İşlevleri:**
- Günlük rapor oluştur
- CSV/JSON formatında dışa aktar
- Analiz sonuçlarını görselle

## Flask API

```bash
python app.py
```

**Endpoints:**

- `GET /api/stats` - İstatistikleri al
- `GET /api/report` - Rapor oluştur
- `POST /api/validate` - Veri doğrula
- `GET /api/export` - Veri dışa aktar

## Kullanım Örnekleri

### Python kodu ile kullanım

```python
from main import EventMapAnalytics

analytics = EventMapAnalytics()
report = analytics.generate_report()
print(report)
```

### Command line

```bash
python main.py
```

## Dosya Yapısı

```
scripts/
├── main.py                  # Ana analytics script
├── generate_report.py       # Rapor oluşturma
├── app.py                   # Flask API
├── utils/
│   ├── firebase_utils.py
│   ├── data_validation.py
│   └── helpers.py
├── requirements.txt         # Python bağımlılıkları
├── .env.example            # Ortam değişkenleri örneği
└── README.md
```

## Scheduling (Otomatik Çalıştırma)

### Linux/Mac (cron)

```bash
0 2 * * * cd /path/to/scripts && python main.py >> logs/cron.log 2>&1
```

### Windows (Task Scheduler)

Bir batch dosyası oluştur ve Task Scheduler'a ekle.

## Troubleshooting

### Firebase bağlantı hatası

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/firebase-key.json"
python main.py
```

### ModuleNotFoundError

```bash
pip install -r requirements.txt --upgrade
```

## Logging

Log dosyaları `logs/` dizininde tutulur.

```bash
tail -f logs/app.log
```
