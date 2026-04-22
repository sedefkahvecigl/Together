# Event Map Mobile App

Flutter ile yazılmış mobil uygulama. Harita üzerinde etkinlikleri göster, QR kod tara ve sohbet et.

## Teknoloji Stack

- **Framework**: Flutter
- **Dil**: Dart
- **Backend**: Firebase
- **Harita**: Google Maps
- **Sohbet**: Firebase Realtime Database

## Kurulum

### Önkoşullar

- Flutter SDK 3.0+ yüklü
- Android Studio veya Xcode
- Firebase projesi oluşturulmuş

### Adımlar

```bash
cd frontend
flutter pub get
```

## Geliştirme

```bash
flutter run
```

## Build

### iOS

```bash
flutter build ios
```

### Android

```bash
flutter build apk
```

## Dosya Yapısı

```
frontend/
├── lib/
│   ├── main.dart                # Entry point
│   ├── screens/                 # UI Ekranları
│   │   ├── home_screen.dart
│   │   ├── map_screen.dart
│   │   ├── chat_screen.dart
│   │   └── qr_screen.dart
│   ├── widgets/                 # Yeniden kullanılabilir Widget'lar
│   ├── services/                # Firebase ve API servisleri
│   ├── models/                  # Veri modelleri
│   └── providers/               # State management (Riverpod)
├── assets/                      # Görseller ve fontlar
├── android/                     # Android spesifik dosyalar
├── ios/                         # iOS spesifik dosyalar
├── pubspec.yaml                 # Bağımlılıklar
└── pubspec.lock
```

## Özellikler

- **Harita**: Google Maps ile etkinlik konumlarını göster
- **QR Tarayıcı**: QR kod okuyarak etkinliklere katıl
- **Sohbet**: Gerçek zamanlı sohbet
- **Kullanıcı Profili**: Profil yönetimi

## Konfigürasyon

Firebase bağlantısı için `lib/services/firebase_service.dart` dosyasını düzenle.

## Testler

```bash
flutter test
```

## Troubleshooting

### iOS Build Hatası

```bash
cd ios
pod install
cd ..
flutter clean
flutter run
```

### Android Build Hatası

```bash
./gradlew clean
flutter clean
flutter pub get
flutter run
```
