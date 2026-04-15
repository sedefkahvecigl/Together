# 🚀 MVP Kapsam Dökümanı: UniCircle (Geçici İsim)

**Sürüm:** 1.0  
**Durum:** Taslak / Geliştirme Öncesi  
**Hedef Kitle:** 18-25 Yaş, İstanbul’daki Üniversite Öğrencileri

---

## 1. Ürün Vizyonu ve Problem Tanımı
İnsanlar, sosyal çevrelerinin programı uymadığı için aktivitelerini (kahve, sergi, spor vb.) ertelemek zorunda kalıyor. **UniCircle**, bu "yalnızlık" ve "erteleme" sorununu, güvenli ve üniversite odaklı bir toplulukla çözerek sosyal keşfi demokratikleştirir.

---

## 2. Değer Önerisi (Value Proposition)
"Arkadaşların meşgul mü? Sorun değil. Seninle aynı ilgi alanına sahip, doğrulanmış üniversitelilerle bugün güvenle sosyalleş."

---

## 3. Temel Persona: "Üniversiteli Can" (20, İstanbul)
- **Motivasyon:** Yeni mekanlar keşfetmek, kampüs dışı çevre edinmek.
- **Engeller:** Güvenlik kaygısı, bütçe kısıtı, planların iptal olması.

---

## 4. MVP Özellik Seti (Must-Have)

### A. Güvenlik ve Doğrulama (The Fortress)
1. **.edu.tr Doğrulaması:** Kayıt sırasında öğrenci e-postası zorunluluğu.
2. **Instagram Entegrasyonu:** Sosyal kanıt için son 6 fotoğrafın profilde gösterimi.
3. **Sadece Kadınlara Özel Modu:** Kadın kullanıcılar için görünürlük kısıtlama seçeneği.

### B. Aktivite Motoru (The Engine)
4. **Niş Etkinlik Formu:** Konum (mekan API), zaman, kişi sınırı ve kategori (Koşu, Kahve, Müze vb.).
5. **Harita Görünümü:** Kullanıcının 5-10km çevresindeki aktif pinlerin gösterilmesi.
6. **Onay Mekanizması:** Etkinlik sahibinin profilleri inceleyip katılımcıları tek tek onaylaması.

### C. Sosyal Etkileşim ve Güven (The Loop)
7. **Geçici Grup Sohbeti:** Sadece onaylı katılımcıların girdiği, etkinlikten 24 saat sonra silinen chat.
8. **QR Check-in Sistemi:** Fiziksel buluşmada tarafların birbirine kod okutması.
9. **Güven Puanı & Yorum:** Sadece buluşma sonrası aktifleşen puanlama sistemi.

---

## 5. Günlük Tutundurma (Daily Retention) Stratejisi
*Kullanıcıyı her gün uygulamaya sokacak "Hook" mekanizmaları:*

- **Günün Sorusu (Daily Ice-Breaker):** Her sabah saat 10:00'da yayınlanan sosyal bir soru (örn: "Sizce İstanbul'un en iyi kütüphanesi hangisi?"). Cevap verenler o günkü etkinliklerde "Öne Çıkan Profil" olur.
- **Daily FOMO Feed:** "Şu an kampüsünde 5 farklı grup buluşuyor" bildirimi.
- **Flash Etkinlikler (Anlık Buluşma):** 2 saat içinde geçerliliğini yitiren, "Kütüphanede kahve molası verecek?" tarzı hızlı pinler.

---

## 6. Teknik Gereksinimler & Teknoloji Yığını
- **Mobil:** Flutter veya React Native (Cross-platform maliyet avantajı).
- **Backend:** Firebase (Real-time DB ve Auth hızı için).
- **Harita:** Google Maps SDK / Mapbox.
- **Altyapı:** Konum bazlı (Geofencing) anlık bildirimler.

---

## 7. Başarı Metrikleri (KPIs)
- **Retention (D1):** %40 (İlk günden sonraki gün geri dönme).
- **Match Rate:** Oluşturulan etkinliklerin %60'ının en az 1 onaylı katılımcı bulması.
- **Safety Metric:** Raporlama oranının toplam kullanıcı sayısına oranla <%0.5 olması.

---

## 8. Faz 1: Pilot Bölge Planı
Uygulama tüm İstanbul yerine sadece **Beşiktaş - Kadıköy - Şişli** üçgeninde (Üniversite yoğunluğunun en yüksek olduğu yerler) 500 beta kullanıcısıyla başlatılacaktır.
