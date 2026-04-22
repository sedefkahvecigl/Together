# 🚀 UniCircle: 100x Detaylandırılmış Ürün Geliştirme ve Büyüme Planı

Bu döküman, fikrin doğrulanmasından ilk 1000 kullanıcıya ulaşılmasına kadar olan 16 haftalık mikro adımları kapsar.

---

## 📅 FAZ 1: Ürün Stratejisi ve Tasarım (1. - 4. Hafta)
**Hedef:** Hipotezleri doğrula ve görsel dili oluştur.

### 1. Hafta: Pazar Validasyonu ve Persona Derinleşmesi
- [ ] **Saha Görüşmeleri:** Beşiktaş ve Kadıköy'deki 3. nesil kahvecilerde 30 öğrenciyle yüz yüze mülakat.
- [ ] **Problem Doğrulama:** "Arkadaş bulamamak mı sorun, yoksa güvenli arkadaş bulamamak mı?" sorusuna yanıt bul.
- [ ] **Araç Seti:** Typeform (Anket), Notion (Notlar).

### 2. Hafta: Marka Kimliği ve Tone of Voice
- [ ] **Görsel Kimlik:** Gen-Z estetiğine uygun renk paleti (Canlı neonlar veya modern pastel).
- [ ] **Mesajlaşma Dili:** Uygulama bildirimlerinin tonunu belirle (Eğlenceli, samimi, merak uyandırıcı).
- [ ] **Logo & Asset Hazırlığı:** Figma üzerinde ikon seti ve logo varyasyonları.

### 3. Hafta: UX/UI Tasarımı (High-Fidelity)
- [ ] **User Flow:** Kayıt -> .edu doğrulaması -> Haritada gezinti -> Etkinlik oluşturma -> Chat akışını çiz.
- [ ] **Figma Prototip:** Tıklanabilir prototip ile kullanıcı testleri yap.
- [ ] **Tasarım Sistemi:** Butonlar, input alanları ve kart tasarımları için bileşen kütüphanesi oluştur.

### 4. Hafta: Yasal Altyapı ve Teknik Hazırlık
- [ ] **KVKK/GDPR:** Konum verisi ve kullanıcı gizliliği için yasal metinleri hazırla.
- [ ] **Developer Hesapları:** Apple App Store ve Google Play Console hesaplarını aç.
- [ ] **Altyapı Seçimi:** Firebase vs Supabase karşılaştırmasını yap ve seçimi netleştir.

---

## 🛠️ FAZ 2: Teknik Geliştirme (MVP Build) (5. - 10. Hafta)
**Hedef:** En az özellik (Must-haves) ile çalışan ürünü kodla.

### 5-6. Hafta: Kimlik ve Profil Yönetimi
- [ ] **Auth Sistemi:** .edu.tr e-posta doğrulaması ve şifresiz giriş (OTP).
- [ ] **Profil Geliştirme:** Instagram API entegrasyonu ile fotoğrafların çekilmesi.
- [ ] **Veritabanı Şeması:** Kullanıcı, Etkinlik, Katılım ve Yorum tablolarının kurulması.

### 7-8. Hafta: Harita ve Etkinlik Motoru
- [ ] **Harita Entegrasyonu:** Mapbox veya Google Maps SDK kurulumu.
- [ ] **Etkinlik Oluşturma:** Kategori seçimi, konum işaretleme ve kişi sınırı mantığı.
- [ ] **Filtreleme:** Harita üzerinde kategoriye ve zamana göre filtreleme kodlanması.

### 9-10. Hafta: Sosyal Katman ve Güvenlik
- [ ] **Real-time Chat:** Firebase Cloud Messaging ile anlık mesajlaşma ve bildirimler.
- [ ] **QR Doğrulama:** Buluşma anı için QR oluşturucu ve tarayıcı entegrasyonu.
- [ ] **Puanlama Sistemi:** Etkinlik bittikten sonra tetiklenen değerlendirme ekranı.

---

## 🧪 FAZ 3: Kapalı Beta ve Optimizasyon (11. - 13. Hafta)
**Hedef:** Hataları ayıkla ve kullanıcı tutma (retention) oranını ölç.

### 11. Hafta: Alpha Testleri (Internal)
- [ ] **Bug Hunting:** 10 kişilik bir ekiple tüm senaryoları test et (İnternet kopması, yanlış konum vb.).
- [ ] **Performans:** Harita üzerindeki yükleme hızını optimize et.

### 12. Hafta: Kapalı Beta (100 Kullanıcı)
- [ ] **Davetiye Sistemi:** Belirlenen 3 üniversiteden 100 öğrenciyi test uçuşuna al.
- [ ] **Analitik:** Mixpanel veya Amplitude ile kullanıcıların en çok hangi ekranda vakit geçirdiğini izle.

### 13. Hafta: Feedback Döngüsü
- [ ] **Pivot Kararı:** Kullanıcılar "Chat"i mi yoksa "Harita"yı mı daha çok sevdi? Veriye göre küçük değişiklikler yap.
- [ ] **İçerik Denetimi:** İlk "Shadowban" ve raporlama araçlarını admin paneline ekle.

---

## 🚀 FAZ 4: Lansman ve Büyüme (14. - 16. Hafta)
**Hedef:** Kritik kitleye (Liquidity) ulaş.

### 14. Hafta: Kampüs Elçileri (The Nodes)
- [ ] **Influencer Seçimi:** 10 "mikro-influencer" öğrenciyle anlaş (İTÜ, Boğaziçi, YTÜ).
- [ ] **Görev Dağılımı:** Her elçinin haftalık 3 kaliteli etkinlik açmasını sağla.

### 15. Hafta: Mekan İş Birlikleri
- [ ] **Pilot Bölge Anlaşmaları:** Beşiktaş'taki 5 kahveciyle "UniCircle Noktası" anlaşması yap (İndirimler).
- [ ] **Seed Etkinlikler:** Mekan sponsorlu "ilk kahve bizden" etkinlikleri düzenle.

### 16. Hafta: Viral Döngü ve Public Launch
- [ ] **TikTok/Reels:** "Arkadaşım ekti ama ben UniCircle ile harika bir sergiye gittim" temalı videolar.
- [ ] **Referral:** Arkadaşını getirene özel rozet veya etkinlik öne çıkarma hakkı tanımla.

---

## 📈 MVP SONRASI: Başarı Metrikleri (KPIs)
- **Kritik Metrik:** Haftalık Aktif Kullanıcı (WAU) artışı.
- **Güvenlik Metriği:** Kullanıcı başına düşen ortalama güven puanı (>4.2 olmalı).
- **Likitide:** Haritayı açan bir kullanıcının 1km içinde en az 2 etkinlik bulma oranı.

---
*Hazırlayan: Profesyonel Ürün Geliştirici Mentorunuz*
