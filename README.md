```markdown
# 🎵 Noski - TikTok User Info Tool

**Developer:** Noski  
**YouTube:** [youtube.com/@noskicoder](https://youtube.com/@noskicoder)  
**Version:** 1.0.0

---

## 🌟 Hakkında

**Noski TikTok User Info Tool**, TikTok kullanıcılarının profil bilgilerini çekmek için geliştirilmiş güçlü bir OSINT aracıdır. Kullanıcı adı ile takipçi sayısı, takip sayısı, beğeni sayısı, video sayısı, biyografi, hesap türü, ülke ve hesap oluşturma tarihi gibi detaylara ulaşabilirsiniz.

Bu araç, **Termux**, **Linux**, **Windows** ve tüm ana terminal ortamlarıyla uyumludur.

---

## ⚡️ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 👤 **Profil Bilgileri** | Kullanıcı adı, isim, ID |
| 📊 **İstatistikler** | Takipçi, takip, beğeni, video sayısı |
| 📝 **Biyografi** | Hesap açıklaması |
| 🔒 **Hesap Türü** | Açık / Özel / Doğrulanmış |
| 🌍 **Konum** | Ülke ve bayrak emojisi |
| 📅 **Kuruluş Tarihi** | Hesap oluşturulma tarihi |
| 🎨 **Renkli Çıktı** | Okunması kolay renkli format |
| 🔄 **Sonsuz Döngü** | Tekrar arama imkanı |

---

## 📦 Kurulum

### Termux / Linux

```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install requests pyfiglet
git clone https://github.com/noskicoder/Tiktokinfo.git
cd Tiktokinfo
python noskitiktokinfo.py
```

Windows

```cmd
pip install requests pyfiglet
git clone https://github.com/noskicoder/Tiktokinfo.git
cd Tiktokinfo
python noskitiktokinfo.py
```

---

🎯 Kullanım

Program başlatıldığında pyfiglet ile oluşturulmuş Noski banneri gösterilir:

```bash
╔══════════════════════════════════════════════════════════════════╗
║                            Noski                                 ║
║                     TikTok User Info Tool                        ║
║                         Dev : Noski                              ║
║              YouTube: youtube.com/@noskicoder                    ║
╚══════════════════════════════════════════════════════════════════╝
```

Adım adım:

1. TikTok kullanıcı adını girin ( @ işareti koymanıza gerek yok )
2. Program profil bilgilerini çekecektir
3. Tekrar arama yapmak için e veya h tuşlayın

---

📁 Örnek Çıktı

```bash
[?] TikTok kullanıcı adını girin:
  >> noskicoder

══════════════════════════════════════════════════════════════════
                    NOSKİ TİKTOK INFO
══════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────┐
│ Kullanıcı Adı: @noskicoder
│ İsim: Noski
│ Kullanıcı ID: 123456789
│ Takipçi: 1,234
│ Takip: 567
│ Beğeni: 8,910
│ Video: 11
│ Bio: My Life, My Rules...
│ Hesap Türü: Açık
│ Ülke: Türkiye 🇹🇷
│ Kuruluş: 01.01.2024 12:00:00
└────────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════
              YouTube: youtube.com/@noskicoder
══════════════════════════════════════════════════════════════════
```

---

📊 Çıktı Bilgileri

Alan Açıklama
Kullanıcı Adı TikTok kullanıcı adı (@ ile)
İsim Hesabın görünen adı
Kullanıcı ID Benzersiz kullanıcı numarası
Takipçi Takipçi sayısı
Takip Takip edilen hesap sayısı
Beğeni Toplam beğeni sayısı
Video Yüklenen video sayısı
Bio Hesap biyografisi
Hesap Türü Açık / Özel / Doğrulanmış
Ülke Hesap bölgesi ve bayrak
Kuruluş Hesap oluşturulma tarihi

---

⚠️ Uyarı

Bu araç eğitim ve bilgi amaçlıdır. Sadece kendi hesaplarınızda veya izin aldığınız hesaplarda kullanın. Yetkisiz veri toplama yasalara aykırı olabilir. Sorumluluk kullanıcıya aittir.

---

🔧 Gereksinimler

· Python 3.6 veya üzeri
· requests
· pyfiglet

---

👨‍💻 Geliştirici

Noski
YouTube: youtube.com/@noskicoder

---

⭐ Destek

Projeyi beğendiyseniz yıldız vermeyi ve kanala abone olmayı unutmayın! ⭐

---

Noski — TikTok bilgilerini keşfet, güvende kal! 🎵
