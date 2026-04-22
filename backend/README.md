# Event Map Backend

Firebase Functions tabanlı backend servisi. TypeScript ile yazılmıştır.

## Teknoloji Stack

- **Runtime**: Firebase Functions
- **Dil**: TypeScript
- **Database**: Cloud Firestore
- **Authentication**: Firebase Auth

## Kurulum

```bash
cd backend
npm install
```

## Geliştirme

```bash
npm run build
npm start
```

## Deploy

```bash
npm run deploy
```

## Dosya Yapısı

```
backend/
├── src/
│   ├── index.ts          # Ana entry point
│   ├── functions/        # Firebase fonksiyonları
│   ├── services/         # İş mantığı servisleri
│   ├── models/          # Veri modelleri
│   └── utils/           # Yardımcı fonksiyonlar
├── lib/                 # Compiled JS
├── package.json
├── tsconfig.json
└── .env.example         # Ortam değişkenleri örneği
```

## Fonksiyonlar

### API Endpoints

- `POST /api/users` - Kullanıcı oluştur
- `GET /api/users/:id` - Kullanıcı bilgisi al
- `POST /api/events` - Etkinlik pinini ekle
- `GET /api/events` - Etkinlikleri listele
- `POST /api/messages` - Mesaj gönder
- `GET /api/messages` - Mesajları al

## Ortam Değişkenleri

`.env` dosyası oluştur:

```
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_client_email
```

## Testler

```bash
npm test
```

## Logging

```bash
npm run logs
```
