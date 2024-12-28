# class KişiselBilgi:
#     def __init__(self):
#         # Kullanıcı bilgilerini kaydetmek için bir sözlük
#         self.kullanici_bilgileri = {}

#     def kayıt_ol(self):
#         """Kullanıcının bilgilerini kaydetmek için metot"""
#         print("Kayıt Olma Ekranı".center(30, "-"))
#         isim = input("İsim: ")
#         soyad = input("Soyad: ")
        
#         # Telefon numarası için hata kontrolü
#         while True:
#             try:
#                 telefon_no = int(input("Telefon Numarası: "))
#                 break
#             except ValueError:
#                 print("Lütfen geçerli bir telefon numarası girin!")
        
#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kullanıcı bilgilerini kaydediyoruz
#         self.kullanici_bilgileri["isim"] = isim
#         self.kullanici_bilgileri["soyad"] = soyad
#         self.kullanici_bilgileri["telefon_no"] = telefon_no
#         self.kullanici_bilgileri["gmail"] = gmail
#         self.kullanici_bilgileri["sifre"] = sifre

#         print("Kayıt başarılı!")

#     def giriş_yap(self):
#         """Kullanıcının giriş yapması için metot"""
#         print("Giriş Yapma Ekranı".center(30, "-"))
#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kayıtlı bilgilerle doğrulama yapılıyor
#         if (gmail == self.kullanici_bilgileri.get("gmail") and
#                 sifre == self.kullanici_bilgileri.get("sifre")):
#             print("Başarıyla giriş yaptınız!")
#         else:
#             print("E-posta veya şifre hatalı. Lütfen tekrar deneyin.")


# # Kullanım
# uygulama = KişiselBilgi()
# uygulama.kayıt_ol()
# uygulama.giriş_yap()

            

    
    
    
    
    
    
    
    
    
# class EgitimNotuEkle:
#     def __init__(self):
#         self.ders_notlari = {}  # Her dersin notları için bir sözlük

#     def ders_ekle(self, ders_adi):
#         """Yeni bir ders ekler."""
#         if ders_adi not in self.ders_notlari:
#             self.ders_notlari[ders_adi] =[]
#             print(f"{ders_adi} eklendi.")
#         else:
#             print(f"{ders_adi} zaten mevcut.")

#     def not_ekle(self, ders_adi, not_icerigi):
#         """Belirtilen derse yeni bir not ekler."""
#         if ders_adi in self.ders_notlari:
#             self.ders_notlari[ders_adi].append(not_icerigi)
#             print(f"{ders_adi} için not eklendi.")
#         else:
#             print(f"{ders_adi} bulunamadı. Önce dersi ekleyin.")

#     def notlari_goster(self):
#         """Tüm derslerin notlarını listeler."""
#         if not self.ders_notlari:
#             print("Henüz ders eklenmemiş.")
#         else:
#             for ders, notlar in self.ders_notlari.items():
#                 print(f"\n{ders}:")
#                 for i, not_icerigi in enumerate(notlar, 1):
#                     print(f"  {i}. {not_icerigi}")

#     def ders_notlari_getir(self, ders_adi):
#         """Belirtilen bir derse ait notları gösterir."""
#         if ders_adi in self.ders_notlari:
#             print(f"{ders_adi} için notlar:")
#             for i, not_icerigi in enumerate(self.ders_notlari[ders_adi], 1):
#                 print(f"  {i}. {not_icerigi}")
#         else:
#             print(f"{ders_adi} bulunamadı.")

#     def not_sil(self, ders_adi, not_index):
#         """Bir dersten belirtilen notu siler."""
#         if ders_adi in self.ders_notlari:
#             try:
#                 silinen_not = self.ders_notlari[ders_adi].pop(not_index - 1)
#                 print(f"{ders_adi} dersinden şu not silindi: {silinen_not}")
#             except IndexError:
#                 print("Geçersiz not numarası.")
#         else:
#             print(f"{ders_adi} bulunamadı.")

#     def tum_notlari_sil(self):
#         """Tüm ders notlarını sıfırlar."""
#         self.ders_notlari.clear()
#         print("Tüm ders notları silindi.")

# class KisiselNotEkle:
#     def __init__(self):
#         self.kisisel_notlar = []  # Kişisel notlar listesi

#     def not_ekle(self, not_icerigi):
#         """Kişisel bir not ekler."""
#         self.kisisel_notlar.append(not_icerigi)
#         print("Kişisel not eklendi.")

#     def notlari_goster(self):
#         """Tüm kişisel notları gösterir."""
#         if not self.kisisel_notlar:
#             print("Henüz kişisel not eklenmemiş.")
#         else:
#             print("Kişisel Notlar:")
#             for i, not_icerigi in enumerate(self.kisisel_notlar, 1):
#                 print(f"  {i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir kişisel notu siler."""
#         try:
#             silinen_not = self.kisisel_notlar.pop(not_index - 1)
#             print(f"Şu kişisel not silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm kişisel notları sıfırlar."""
#         self.kisisel_notlar.clear()
#         print("Tüm kişisel notlar silindi.")

# class IsNotuEkle:
#     def __init__(self):
#         self.is_notlari = []  # İş notları listesi

#     def not_ekle(self, not_icerigi):
#         """İşle ilgili bir not ekler."""
#         self.is_notlari.append(not_icerigi)
#         print("İş notu eklendi.")

#     def notlari_goster(self):
#         """Tüm iş notlarını gösterir."""
#         if not self.is_notlari:
#             print("Henüz iş notu eklenmemiş.")
#         else:
#             print("İş Notları:")
#             for i, not_icerigi in enumerate(self.is_notlari, 1):
#                 print(f"  {i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir iş notunu siler."""
#         try:
#             silinen_not = self.is_notlari.pop(not_index - 1)
#             print(f"Şu iş notu silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm iş notlarını sıfırlar."""
#         self.is_notlari.clear()
#         print("Tüm iş notları silindi.")

# # Kullanım Örneği
# if __name__ == "__main__":
#     # Eğitim Notları
#     egitim = EgitimNotuEkle()
#     egitim.ders_ekle("Matematik")
#     egitim.not_ekle("Matematik", "Fonksiyonlar konusuna çalış.")
#     egitim.not_ekle("Fizik", "Newton yasalarını tekrar et.")
#     egitim.ders_notlari_getir("Matematik")
#     egitim.notlari_goster()

#     # Kişisel Notlar
#     kisisel = KisiselNotEkle()
#     kisisel.not_ekle("Alışveriş listesi hazırla.")
#     kisisel.not_ekle("Spor yapmayı unutma.")
#     kisisel.notlari_goster()

#     # İş Notları
#     is_notu = IsNotuEkle()
#     is_notu.not_ekle("Sunum hazırlıkları tamamlanacak.")
#     is_notu.not_ekle("Toplantıya katıl.")
#     is_notu.notlari_goster()

    
    
    
    
    
    
    
    
    
    
    
# import time
# from datetime import datetime
# import threading

# # Taban sınıf: Not yönetimi için temel işlevler
# class NotYonetim:
#     def __init__(self):
#         self.notlar = []  # Genel not listesi

#     def not_ekle(self, not_icerigi):
#         """Yeni bir not ekler."""
#         self.notlar.append(not_icerigi)
#         print(f"Not eklendi: {not_icerigi}")

#     def notlari_goster(self):
#         """Tüm notları gösterir."""
#         if not self.notlar:
#             print("Henüz not eklenmemiş.")
#         else:
#             for i, not_icerigi in enumerate(self.notlar, 1):
#                 print(f"{i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir notu siler."""
#         try:
#             silinen_not = self.notlar.pop(not_index - 1)
#             print(f"Şu not silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm notları sıfırlar."""
#         self.notlar.clear()
#         print("Tüm notlar silindi.")

# # Alt sınıflar: Taban sınıftan türeyen farklı not türleri
# class EgitimNotuEkle(NotYonetim):
#     def __init__(self):
#         super().__init__()
#         self.ders_notlari = {}  # Ders bazında notlar için sözlük

#     def ders_ekle(self, ders_adi):
#         """Yeni bir ders ekler."""
#         if ders_adi not in self.ders_notlari:
#             self.ders_notlari[ders_adi] = []
#             print(f"{ders_adi} eklendi.")
#         else:
#             print(f"{ders_adi} zaten mevcut.")

#     def not_ekle(self, ders_adi, not_icerigi):
#         """Derse özel bir not ekler."""
#         if ders_adi in self.ders_notlari:
#             self.ders_notlari[ders_adi].append(not_icerigi)
#             print(f"{ders_adi} için not eklendi.")
#         else:
#             print(f"{ders_adi} bulunamadı. Önce dersi ekleyin.")

#     def notlari_goster(self):
#         """Tüm derslerin notlarını gösterir."""
#         if not self.ders_notlari:
#             print("Henüz ders eklenmemiş.")
#         else:
#             for ders, notlar in self.ders_notlari.items():
#                 print(f"\n{ders}:")
#                 for i, not_icerigi in enumerate(notlar, 1):
#                     print(f"  {i}. {not_icerigi}")

# # Diğer not türleri (iş, kişisel) aynı tabanı kullanır
# class KisiselNotEkle(NotYonetim):
#     pass

# class IsNotuEkle(NotYonetim):
#     pass

# # Hatırlatıcı sınıfı
# class Hatirlatici:
#     def __init__(self):
#         self.hatirlatmalar = []

#     def hatirlatma_ekle(self, mesaj, zaman):
#         """Hatırlatma ekler."""
#         self.hatirlatmalar.append({"mesaj": mesaj, "zaman": zaman})
#         print(f"Hatırlatma eklendi: {mesaj}, Zaman: {zaman}")

#         # Hatırlatma zamanında çalıştırılacak bir iş parçacığı
#         threading.Thread(target=self.hatirlat, args=(mesaj, zaman), daemon=True).start()

#     def hatirlat(self, mesaj, zaman):
#         """Zamanı geldiğinde hatırlatma yapar."""
#         şimdi = datetime.now()
#         bekleme_suresi = (zaman - şimdi).total_seconds()
#         if bekleme_suresi > 0:
#             time.sleep(bekleme_suresi)
#         print(f"\n[Hatırlatma] {mesaj}")

#     def hatirlatmalari_goster(self):
#         """Tüm hatırlatmaları listeler."""
#         if not self.hatirlatmalar:
#             print("Henüz bir hatırlatma eklenmemiş.")
#         else:
#             for i, hatirlatma in enumerate(self.hatirlatmalar, 1):
#                 zaman = hatirlatma["zaman"].strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"{i}. {hatirlatma['mesaj']} - {zaman}")

#     def hatirlatma_sil(self, index):
#         """Belirtilen hatırlatmayı siler."""
#         try:
#             silinen = self.hatirlatmalar.pop(index - 1)
#             print(f"Şu hatırlatma silindi: {silinen['mesaj']}")
#         except IndexError:
#             print("Geçersiz hatırlatma numarası.")

    













# import time
# from datetime import datetime, timedelta
# import threading


# class KişiselBilgi:
#     def __init__(self):
#         # Kullanıcı bilgilerini kaydetmek için bir sözlük
#         self.kullanici_bilgileri = {}

#     def kayıt_ol(self):
#         """Kullanıcının bilgilerini kaydetmek için metot"""
#         print("Kayıt Olma Ekranı".center(30, "-"))
#         isim = input("İsim: ")
#         soyad = input("Soyad: ")

#         # Telefon numarası için hata kontrolü
#         while True:
#             try:
#                 telefon_no = int(input("Telefon Numarası: "))
#                 break
#             except ValueError:
#                 print("Lütfen geçerli bir telefon numarası girin!")

#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kullanıcı bilgilerini kaydediyoruz
#         self.kullanici_bilgileri["isim"] = isim
#         self.kullanici_bilgileri["soyad"] = soyad
#         self.kullanici_bilgileri["telefon_no"] = telefon_no
#         self.kullanici_bilgileri["gmail"] = gmail
#         self.kullanici_bilgileri["sifre"] = sifre

#         print("Kayıt başarılı!")

#     def giriş_yap(self):
#         """Kullanıcının giriş yapması için metot"""
#         print("Giriş Yapma Ekranı".center(30, "-"))
#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kayıtlı bilgilerle doğrulama yapılıyor
#         if (gmail == self.kullanici_bilgileri.get("gmail") and
#                 sifre == self.kullanici_bilgileri.get("sifre")):
#             print("Başarıyla giriş yaptınız!")
#         else:
#             print("E-posta veya şifre hatalı. Lütfen tekrar deneyin.")


# class NotYonetim:
#     def __init__(self):
#         self.notlar = []

#     def not_ekle(self, not_icerigi):
#         """Not ekler."""
#         self.notlar.append(not_icerigi)
#         print("Not eklendi.")

#     def notlari_goster(self):
#         """Tüm notları listeler."""
#         if not self.notlar:
#             print("Henüz not eklenmemiş.")
#         else:
#             for i, not_icerigi in enumerate(self.notlar, 1):
#                 print(f"{i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir notu siler."""
#         try:
#             silinen_not = self.notlar.pop(not_index - 1)
#             print(f"Şu not silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm notları sıfırlar."""
#         self.notlar.clear()
#         print("Tüm notlar silindi.")


# class EgitimNotu(NotYonetim):
#     def __init__(self):
#         super().__init__()
#         self.dersler = {}

#     def ders_ekle(self, ders_adi):
#         """Yeni bir ders ekler."""
#         if ders_adi not in self.dersler:
#             self.dersler[ders_adi] = []
#             print(f"{ders_adi} eklendi.")
#         else:
#             print(f"{ders_adi} zaten mevcut.")

#     def not_ekle(self, ders_adi, not_icerigi):
#         """Belirtilen derse yeni bir not ekler."""
#         if ders_adi in self.dersler:
#             self.dersler[ders_adi].append(not_icerigi)
#             print(f"{ders_adi} için not eklendi.")
#         else:
#             print(f"{ders_adi} bulunamadı. Önce dersi ekleyin.")

#     def notlari_goster(self):
#         """Tüm derslerin notlarını listeler."""
#         if not self.dersler:
#             print("Henüz ders eklenmemiş.")
#         else:
#             for ders, notlar in self.dersler.items():
#                 print(f"\n{ders}:")
#                 for i, not_icerigi in enumerate(notlar, 1):
#                     print(f"  {i}. {not_icerigi}")


# class KisiselNot(NotYonetim):
#     """Kişisel notlar için NotYonetim sınıfını genişletir."""
#     pass


# class IsNotu(NotYonetim):
#     """İş notları için NotYonetim sınıfını genişletir."""
#     pass


# class Hatirlatici:
#     def __init__(self):
#         self.hatirlatmalar = []  # Hatırlatmaları saklayacak liste

#     def hatirlatma_ekle(self, mesaj, zaman):
#         """
#         Hatırlatma ekler.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı (datetime objesi olarak)
#         """
#         self.hatirlatmalar.append({"mesaj": mesaj, "zaman": zaman})
#         print(f"Hatırlatma eklendi: {mesaj}, Zaman: {zaman}")

#         # Hatırlatma zamanında uyarı yapmak için bir iş parçacığı başlatılır
#         threading.Thread(target=self.hatirlat, args=(mesaj, zaman), daemon=True).start()

#     def hatirlat(self, mesaj, zaman):
#         """
#         Belirtilen zamanda hatırlatma yapar.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı
#         """
#         şimdi = datetime.now()
#         bekleme_suresi = (zaman - şimdi).total_seconds()

#         if bekleme_suresi > 0:
#             time.sleep(bekleme_suresi)  # Hatırlatma zamanı gelene kadar bekler

#         print(f"\n[Hatırlatma] {mesaj}")

#     def hatirlatmalari_goster(self):
#         """Tüm hatırlatmaları listeler."""
#         if not self.hatirlatmalar:
#             print("Henüz bir hatırlatma eklenmemiş.")
#         else:
#             print("Hatırlatmalar:")
#             for i, hatirlatma in enumerate(self.hatirlatmalar, 1):
#                 zaman = hatirlatma["zaman"].strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"{i}. {hatirlatma['mesaj']} - {zaman}")

#     def hatirlatma_sil(self, index):
#         """Belirtilen hatırlatmayı siler."""
#         try:
#             silinen = self.hatirlatmalar.pop(index - 1)
#             print(f"Şu hatırlatma silindi: {silinen['mesaj']}")
#         except IndexError:
#             print("Geçersiz hatırlatma numarası.")























# import time
# from datetime import datetime, timedelta
# import threading


# class KişiselBilgi:
#     def __init__(self):
#         # Kullanıcı bilgilerini kaydetmek için bir sözlük
#         self.kullanici_bilgileri = {}

#     def kayıt_ol(self):
#         """Kullanıcının bilgilerini kaydetmek için metot"""
#         print("Kayıt Olma Ekranı".center(30, "-"))
#         isim = input("İsim: ")
#         soyad = input("Soyad: ")

#         # Telefon numarası için hata kontrolü
#         while True:
#             try:
#                 telefon_no = int(input("Telefon Numarası: "))
#                 break
#             except ValueError:
#                 print("Lütfen geçerli bir telefon numarası girin!")

#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kullanıcı bilgilerini kaydediyoruz
#         self.kullanici_bilgileri["isim"] = isim
#         self.kullanici_bilgileri["soyad"] = soyad
#         self.kullanici_bilgileri["telefon_no"] = telefon_no
#         self.kullanici_bilgileri["gmail"] = gmail
#         self.kullanici_bilgileri["sifre"] = sifre

#         print("Kayıt başarılı!")

#     def giriş_yap(self):
#         """Kullanıcının giriş yapması için metot"""
#         print("Giriş Yapma Ekranı".center(30, "-"))
#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kayıtlı bilgilerle doğrulama yapılıyor
#         if (gmail == self.kullanici_bilgileri.get("gmail") and
#                 sifre == self.kullanici_bilgileri.get("sifre")):
#             print("Başarıyla giriş yaptınız!")
#         else:
#             print("E-posta veya şifre hatalı. Lütfen tekrar deneyin.")


# class NotYonetim:
#     def __init__(self):
#         self.notlar = []

#     def not_ekle(self, not_icerigi):
#         """Not ekler."""
#         self.notlar.append(not_icerigi)
#         print("Not eklendi.")

#     def notlari_goster(self):
#         """Tüm notları listeler."""
#         if not self.notlar:
#             print("Henüz not eklenmemiş.")
#         else:
#             for i, not_icerigi in enumerate(self.notlar, 1):
#                 print(f"{i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir notu siler."""
#         try:
#             silinen_not = self.notlar.pop(not_index - 1)
#             print(f"Şu not silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm notları sıfırlar."""
#         self.notlar.clear()
#         print("Tüm notlar silindi.")


# class EgitimNotu(NotYonetim):
#     def __init__(self):
#         super().__init__()
#         self.dersler = {}

#     def ders_ekle(self, ders_adi):
#         """Yeni bir ders ekler."""
#         if ders_adi not in self.dersler:
#             self.dersler[ders_adi] = []
#             print(f"{ders_adi} eklendi.")
#         else:
#             print(f"{ders_adi} zaten mevcut.")

#     def not_ekle(self, ders_adi, not_icerigi):
#         """Belirtilen derse yeni bir not ekler."""
#         if ders_adi in self.dersler:
#             self.dersler[ders_adi].append(not_icerigi)
#             print(f"{ders_adi} için not eklendi.")
#         else:
#             print(f"{ders_adi} bulunamadı. Önce dersi ekleyin.")

#     def notlari_goster(self):
#         """Tüm derslerin notlarını listeler."""
#         if not self.dersler:
#             print("Henüz ders eklenmemiş.")
#         else:
#             for ders, notlar in self.dersler.items():
#                 print(f"\n{ders}:")
#                 for i, not_icerigi in enumerate(notlar, 1):
#                     print(f"  {i}. {not_icerigi}")


# class KisiselNot(NotYonetim):
#     """Kişisel notlar için NotYonetim sınıfını genişletir."""
#     pass


# class IsNotu(NotYonetim):
#     """İş notları için NotYonetim sınıfını genişletir."""
#     pass


# class Hatirlatici:
#     def __init__(self):
#         self.hatirlatmalar = []  # Hatırlatmaları saklayacak liste

#     def hatirlatma_ekle(self, mesaj, zaman):
#         """
#         Hatırlatma ekler.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı (datetime objesi olarak)
#         """
#         self.hatirlatmalar.append({"mesaj": mesaj, "zaman": zaman})
#         print(f"Hatırlatma eklendi: {mesaj}, Zaman: {zaman}")

#         # Hatırlatma zamanında uyarı yapmak için bir iş parçacığı başlatılır
#         threading.Thread(target=self.hatirlat, args=(mesaj, zaman), daemon=True).start()

#     def hatirlat(self, mesaj, zaman):
#         """
#         Belirtilen zamanda hatırlatma yapar.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı
#         """
#         şimdi = datetime.now()
#         bekleme_suresi = (zaman - şimdi).total_seconds()

#         if bekleme_suresi > 0:
#             time.sleep(bekleme_suresi)  # Hatırlatma zamanı gelene kadar bekler

#         print(f"\n[Hatırlatma] {mesaj}")

#     def hatirlatmalari_goster(self):
#         """Tüm hatırlatmaları listeler."""
#         if not self.hatirlatmalar:
#             print("Henüz bir hatırlatma eklenmemiş.")
#         else:
#             print("Hatırlatmalar:")
#             for i, hatirlatma in enumerate(self.hatirlatmalar, 1):
#                 zaman = hatirlatma["zaman"].strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"{i}. {hatirlatma['mesaj']} - {zaman}")

#     def hatirlatma_sil(self, index):
#         """Belirtilen hatırlatmayı siler."""
#         try:
#             silinen = self.hatirlatmalar.pop(index - 1)
#             print(f"Şu hatırlatma silindi: {silinen['mesaj']}")
#         except IndexError:
#             print("Geçersiz hatırlatma numarası.")











# def ana_menu():
#     print("\n" + "Ana Menü".center(30, "-"))
#     print("1. Kullanıcı İşlemleri")
#     print("2. Not Yönetimi")
#     print("3. Hatırlatıcı")
#     print("4. Çıkış")


# def not_yonetim_menu():
#     print("\n" + "Not Yönetimi Menüsü".center(30, "-"))
#     print("1. Eğitim Notları")
#     print("2. Kişisel Notlar")
#     print("3. İş Notları")
#     print("4. Geri Dön")


# def kullanıcı_islemleri():
#     kullanici = KişiselBilgi()
#     while True:
#         print("\n" + "Kullanıcı İşlemleri".center(30, "-"))
#         print("1. Kayıt Ol")
#         print("2. Giriş Yap")
#         print("3. Geri Dön")

#         secim = input("Seçiminiz: ")
#         if secim == "1":
#             kullanici.kayıt_ol()
#         elif secim == "2":
#             kullanici.giriş_yap()
#         elif secim == "3":
#             break
#         else:
#             print("Geçersiz seçim!")


# def not_yonetim():
#     egitim_notlari = EgitimNotu()
#     kisisel_notlar = KisiselNot()
#     is_notlari = IsNotu()

#     while True:
#         not_yonetim_menu()
#         secim = input("Seçiminiz: ")

#         if secim == "1":
#             not_turu = egitim_notlari
#             print("Eğitim Notları seçildi.")
#         elif secim == "2":
#             not_turu = kisisel_notlar
#             print("Kişisel Notlar seçildi.")
#         elif secim == "3":
#             not_turu = is_notlari
#             print("İş Notları seçildi.")
#         elif secim == "4":
#             break
#         else:
#             print("Geçersiz seçim!")
#             continue

#         while True:
#             print("\n1. Not Ekle")
#             print("2. Notları Göster")
#             print("3. Not Sil")
#             print("4. Tüm Notları Sil")
#             print("5. Geri Dön")
#             alt_secim = input("Seçiminiz: ")

#             if alt_secim == "1":
#                 if isinstance(not_turu, EgitimNotu):
#                     ders_adi = input("Ders adı: ")
#                     not_icerigi = input("Not içeriği: ")
#                     not_turu.ders_ekle(ders_adi)
#                     not_turu.not_ekle(ders_adi, not_icerigi)
#                 else:
#                     not_icerigi = input("Not içeriği: ")
#                     not_turu.not_ekle(not_icerigi)
#             elif alt_secim == "2":
#                 if isinstance(not_turu, EgitimNotu):
#                     not_turu.notlari_goster()
#                 else:
#                     not_turu.notlari_goster()
#             elif alt_secim == "3":
#                 try:
#                     not_index = int(input("Silmek istediğiniz not numarası: "))
#                     not_turu.not_sil(not_index)
#                 except ValueError:
#                     print("Geçerli bir sayı girin!")
#             elif alt_secim == "4":
#                 not_turu.tum_notlari_sil()
#             elif alt_secim == "5":
#                 break
#             else:
#                 print("Geçersiz seçim!")


# def hatirlatici_islemleri():
#     hatirlatici = Hatirlatici()
#     while True:
#         print("\n" + "Hatırlatıcı İşlemleri".center(30, "-"))
#         print("1. Hatırlatma Ekle")
#         print("2. Hatırlatmaları Göster")
#         print("3. Hatırlatma Sil")
#         print("4. Geri Dön")

#         secim = input("Seçiminiz: ")
#         if secim == "1":
#             mesaj = input("Hatırlatma mesajı: ")
#             try:
#                 saat = int(input("Kaç saniye sonra hatırlatılacak: "))
#                 zaman = datetime.now() + timedelta(seconds=saat)
#                 hatirlatici.hatirlatma_ekle(mesaj, zaman)
#             except ValueError:
#                 print("Geçerli bir sayı girin!")
#         elif secim == "2":
#             hatirlatici.hatirlatmalari_goster()
#         elif secim == "3":
#             try:
#                 index = int(input("Silmek istediğiniz hatırlatma numarası: "))
#                 hatirlatici.hatirlatma_sil(index)
#             except ValueError:
#                 print("Geçerli bir sayı girin!")
#         elif secim == "4":
#             break
#         else:
#             print("Geçersiz seçim!")


# # Ana Program
# while True:
#     ana_menu()
#     secim = input("Seçiminiz: ")

#     if secim == "1":
#         kullanıcı_islemleri()
#     elif secim == "2":
#         not_yonetim()
#     elif secim == "3":
#         hatirlatici_islemleri()
#     elif secim == "4":
#         print("Programdan çıkılıyor...")
#         break
#     else:
#         print("Geçersiz seçim!")




# import time
# from datetime import datetime, timedelta
# import threading
# import hashlib


# class KişiselBilgi:
#     def __init__(self):
#         # Kullanıcı bilgilerini kaydetmek için bir sözlük
#         self.kullanici_bilgileri = {}

#     def hash_sifre(self, sifre):
#         """Şifreyi hashler."""
#         return hashlib.sha256(sifre.encode()).hexdigest()

#     def kayıt_ol(self):
#         """Kullanıcının bilgilerini kaydetmek için metot."""
#         print("Kayıt Olma Ekranı".center(30, "-"))
#         isim = input("İsim: ")
#         soyad = input("Soyad: ")

#         # Telefon numarası için hata kontrolü
#         while True:
#             telefon_no = input("Telefon Numarası: ")
#             if telefon_no.isdigit() and len(telefon_no) == 10:
#                 break
#             else:
#                 print("Lütfen 10 haneli geçerli bir telefon numarası girin!")

#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Kullanıcı bilgilerini kaydediyoruz
#         self.kullanici_bilgileri["isim"] = isim
#         self.kullanici_bilgileri["soyad"] = soyad
#         self.kullanici_bilgileri["telefon_no"] = telefon_no
#         self.kullanici_bilgileri["gmail"] = gmail
#         self.kullanici_bilgileri["sifre"] = self.hash_sifre(sifre)

#         print("Kayıt başarılı!")

#     def giriş_yap(self):
#         """Kullanıcının giriş yapması için metot."""
#         print("Giriş Yapma Ekranı".center(30, "-"))
#         gmail = input("E-Posta: ")
#         sifre = input("Şifre: ")

#         # Şifre hashlenerek doğrulanır
#         if (gmail == self.kullanici_bilgileri.get("gmail") and
#                 self.hash_sifre(sifre) == self.kullanici_bilgileri.get("sifre")):
#             print("Başarıyla giriş yaptınız!")
#         else:
#             print("E-posta veya şifre hatalı. Lütfen tekrar deneyin.")


# class NotYonetim:
#     def __init__(self):
#         self.notlar = []

#     def not_ekle(self, not_icerigi):
#         """Not ekler."""
#         self.notlar.append(not_icerigi)
#         print("Not eklendi.")

#     def notlari_goster(self):
#         """Tüm notları listeler."""
#         if not self.notlar:
#             print("Henüz not eklenmemiş.")
#         else:
#             for i, not_icerigi in enumerate(self.notlar, 1):
#                 print(f"{i}. {not_icerigi}")

#     def not_sil(self, not_index):
#         """Bir notu siler."""
#         try:
#             silinen_not = self.notlar.pop(not_index - 1)
#             print(f"Şu not silindi: {silinen_not}")
#         except IndexError:
#             print("Geçersiz not numarası.")

#     def tum_notlari_sil(self):
#         """Tüm notları sıfırlar."""
#         self.notlar.clear()
#         print("Tüm notlar silindi.")


# class EgitimNotu(NotYonetim):
#     def __init__(self):
#         super().__init__()
#         self.dersler = {}

#     def ders_ekle(self, ders_adi):
#         """Yeni bir ders ekler."""
#         if ders_adi not in self.dersler:
#             self.dersler[ders_adi] = []
#             print(f"{ders_adi} eklendi.")
#         else:
#             print(f"{ders_adi} zaten mevcut.")

#     def not_ekle(self, ders_adi, not_icerigi):
#         """Belirtilen derse yeni bir not ekler."""
#         if ders_adi not in self.dersler:
#             print(f"{ders_adi} bulunamadı. Ders otomatik olarak ekleniyor.")
#             self.ders_ekle(ders_adi)
#         self.dersler[ders_adi].append(not_icerigi)
#         print(f"{ders_adi} için not eklendi.")

#     def notlari_goster(self):
#         """Tüm derslerin notlarını listeler."""
#         if not self.dersler:
#             print("Henüz ders eklenmemiş.")
#         else:
#             for ders, notlar in self.dersler.items():
#                 print(f"\n{ders}:")
#                 for i, not_icerigi in enumerate(notlar, 1):
#                     print(f"  {i}. {not_icerigi}")

#     def not_sil(self, ders_adi, not_index):
#         """Belirtilen dersten bir not siler."""
#         if ders_adi in self.dersler:
#             try:
#                 silinen_not = self.dersler[ders_adi].pop(not_index - 1)
#                 print(f"{ders_adi} dersinden şu not silindi: {silinen_not}")
#                 if not self.dersler[ders_adi]:
#                     print(f"{ders_adi} dersinin tüm notları silindi. Ders kaldırılıyor.")
#                     del self.dersler[ders_adi]
#             except IndexError:
#                 print("Geçersiz not numarası.")
#         else:
#             print(f"{ders_adi} bulunamadı.")


# class Hatirlatici:
#     def __init__(self):
#         self.hatirlatmalar = []  # Hatırlatmaları saklayacak liste

#     def hatirlatma_ekle(self, mesaj, zaman):
#         """
#         Hatırlatma ekler.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı (datetime objesi olarak)
#         """
#         if zaman < datetime.now():
#             print("Geçmiş bir tarih seçemezsiniz!")
#             return
#         self.hatirlatmalar.append({"mesaj": mesaj, "zaman": zaman})
#         print(f"Hatırlatma eklendi: {mesaj}, Zaman: {zaman}")

#         # Hatırlatma zamanında uyarı yapmak için bir iş parçacığı başlatılır
#         threading.Thread(target=self.hatirlat, args=(mesaj, zaman), daemon=True).start()

#     def hatirlat(self, mesaj, zaman):
#         """
#         Belirtilen zamanda hatırlatma yapar.
#         :param mesaj: Hatırlatma mesajı
#         :param zaman: Hatırlatma zamanı
#         """
#         şimdi = datetime.now()
#         bekleme_suresi = (zaman - şimdi).total_seconds()

#         if bekleme_suresi > 0:
#             time.sleep(bekleme_suresi)  # Hatırlatma zamanı gelene kadar bekler

#         print(f"\n[Hatırlatma] {mesaj}")

#     def hatirlatmalari_goster(self):
#         """Tüm hatırlatmaları listeler."""
#         if not self.hatirlatmalar:
#             print("Henüz bir hatırlatma eklenmemiş.")
#         else:
#             print("Hatırlatmalar:")
#             for i, hatirlatma in enumerate(self.hatirlatmalar, 1):
#                 zaman = hatirlatma["zaman"].strftime("%Y-%m-%d %H:%M:%S")
#                 print(f"{i}. {hatirlatma['mesaj']} - {zaman}")

#     def hatirlatma_sil(self, index):
#         """Belirtilen hatırlatmayı siler."""
#         try:
#             silinen = self.hatirlatmalar.pop(index - 1)
#             print(f"Şu hatırlatma silindi: {silinen['mesaj']}")
#         except IndexError:
#             print("Geçersiz hatırlatma numarası.")





# def ana_menu():
#     print("\n" + "Ana Menü".center(30, "-"))
#     print("1. Kullanıcı İşlemleri")
#     print("2. Not Yönetimi")
#     print("3. Hatırlatıcı")
#     print("4. Çıkış")


# def not_yonetim_menu():
#     print("\n" + "Not Yönetimi Menüsü".center(30, "-"))
#     print("1. Eğitim Notları")
#     print("2. Kişisel Notlar")
#     print("3. İş Notları")
#     print("4. Geri Dön")


# def kullanıcı_islemleri():
#     kullanici = KişiselBilgi()
#     while True:
#         print("\n" + "Kullanıcı İşlemleri".center(30, "-"))
#         print("1. Kayıt Ol")
#         print("2. Giriş Yap")
#         print("3. Geri Dön")

#         secim = input("Seçiminiz: ")
#         if secim == "1":
#             kullanici.kayıt_ol()
#         elif secim == "2":
#             kullanici.giriş_yap()
#         elif secim == "3":
#             break
#         else:
#             print("Geçersiz seçim!")


# def not_yonetim():
#     egitim_notlari = EgitimNotu()
#     kisisel_notlar = KisiselNot()
#     is_notlari = IsNotu()

#     while True:
#         not_yonetim_menu()
#         secim = input("Seçiminiz: ")

#         if secim == "1":
#             not_turu = egitim_notlari
#             print("Eğitim Notları seçildi.")
#         elif secim == "2":
#             not_turu = kisisel_notlar
#             print("Kişisel Notlar seçildi.")
#         elif secim == "3":
#             not_turu = is_notlari
#             print("İş Notları seçildi.")
#         elif secim == "4":
#             break
#         else:
#             print("Geçersiz seçim!")
#             continue

#         while True:
#             print("\n1. Not Ekle")
#             print("2. Notları Göster")
#             print("3. Not Sil")
#             print("4. Tüm Notları Sil")
#             print("5. Geri Dön")
#             alt_secim = input("Seçiminiz: ")

#             if alt_secim == "1":
#                 if isinstance(not_turu, EgitimNotu):
#                     ders_adi = input("Ders adı: ")
#                     not_icerigi = input("Not içeriği: ")
#                     not_turu.ders_ekle(ders_adi)
#                     not_turu.not_ekle(ders_adi, not_icerigi)
#                 else:
#                     not_icerigi = input("Not içeriği: ")
#                     not_turu.not_ekle(not_icerigi)
#             elif alt_secim == "2":
#                 if isinstance(not_turu, EgitimNotu):
#                     not_turu.notlari_goster()
#                 else:
#                     not_turu.notlari_goster()
#             elif alt_secim == "3":
#                 try:
#                     not_index = int(input("Silmek istediğiniz not numarası: "))
#                     not_turu.not_sil(not_index)
#                 except ValueError:
#                     print("Geçerli bir sayı girin!")
#             elif alt_secim == "4":
#                 not_turu.tum_notlari_sil()
#             elif alt_secim == "5":
#                 break
#             else:
#                 print("Geçersiz seçim!")


# def hatirlatici_islemleri():
#     hatirlatici = Hatirlatici()
#     while True:
#         print("\n" + "Hatırlatıcı İşlemleri".center(30, "-"))
#         print("1. Hatırlatma Ekle")
#         print("2. Hatırlatmaları Göster")
#         print("3. Hatırlatma Sil")
#         print("4. Geri Dön")

#         secim = input("Seçiminiz: ")
#         if secim == "1":
#             mesaj = input("Hatırlatma mesajı: ")
#             try:
#                 saat = int(input("Kaç saniye sonra hatırlatılacak: "))
#                 zaman = datetime.now() + timedelta(seconds=saat)
#                 hatirlatici.hatirlatma_ekle(mesaj, zaman)
#             except ValueError:
#                 print("Geçerli bir sayı girin!")
#         elif secim == "2":
#             hatirlatici.hatirlatmalari_goster()
#         elif secim == "3":
#             try:
#                 index = int(input("Silmek istediğiniz hatırlatma numarası: "))
#                 hatirlatici.hatirlatma_sil(index)
#             except ValueError:
#                 print("Geçerli bir sayı girin!")
#         elif secim == "4":
#             break
#         else:
#             print("Geçersiz seçim!")


# # Ana Program
# while True:
#     ana_menu()
#     secim = input("Seçiminiz: ")

#     if secim == "1":
#         kullanıcı_islemleri()
#     elif secim == "2":
#         not_yonetim()
#     elif secim == "3":
#         hatirlatici_islemleri()
#     elif secim == "4":
#         print("Programdan çıkılıyor...")
#         break
#     else:
#         print("Geçersiz seçim!")
















import time
from datetime import datetime, timedelta
import threading
import hashlib


class KişiselBilgi:
    def __init__(self):
        self.kullanici_bilgileri = {}

    def hash_sifre(self, sifre):
        """Şifreyi hashler."""
        return hashlib.sha256(sifre.encode()).hexdigest()

    def kayıt_ol(self):
        print("Kayıt Olma Ekranı".center(30, "-"))
        isim = input("İsim: ")
        soyad = input("Soyad: ")

        while True:
            telefon_no = input("Telefon Numarası: ")
            if telefon_no.isdigit() and len(telefon_no) == 10:
                break
            else:
                print("Lütfen 10 haneli geçerli bir telefon numarası girin!")

        gmail = input("E-Posta: ")
        sifre = input("Şifre: ")
        self.kullanici_bilgileri["isim"] = isim
        self.kullanici_bilgileri["soyad"] = soyad
        self.kullanici_bilgileri["telefon_no"] = telefon_no
        self.kullanici_bilgileri["gmail"] = gmail
        self.kullanici_bilgileri["sifre"] = self.hash_sifre(sifre)
        print("Kayıt başarılı!")

    def giriş_yap(self):
        print("Giriş Yapma Ekranı".center(30, "-"))
        gmail = input("E-Posta: ")
        sifre = input("Şifre: ")

        if (gmail == self.kullanici_bilgileri.get("gmail") and
                self.hash_sifre(sifre) == self.kullanici_bilgileri.get("sifre")):
            print("Başarıyla giriş yaptınız!")
        else:
            print("E-posta veya şifre hatalı. Lütfen tekrar deneyin.")


class NotYonetim:
    def __init__(self):
        self.notlar = []

    def not_ekle(self, not_icerigi):
        self.notlar.append(not_icerigi)
        print("Not eklendi.")

    def notlari_goster(self):
        if not self.notlar:
            print("Henüz not eklenmemiş.")
        else:
            for i, not_icerigi in enumerate(self.notlar, 1):
                print(f"{i}. {not_icerigi}")

    def not_sil(self, not_index):
        try:
            silinen_not = self.notlar.pop(not_index - 1)
            print(f"Şu not silindi: {silinen_not}")
        except IndexError:
            print("Geçersiz not numarası.")

    def tum_notlari_sil(self):
        self.notlar.clear()
        print("Tüm notlar silindi.")


class EgitimNotu(NotYonetim):
    def __init__(self):
        super().__init__()
        self.dersler = {}

    def ders_ekle(self, ders_adi):
        if ders_adi not in self.dersler:
            self.dersler[ders_adi] = []
            print(f"{ders_adi} eklendi.")
        else:
            print(f"{ders_adi} zaten mevcut.")

    def not_ekle(self, ders_adi, not_icerigi):
        if ders_adi not in self.dersler:
            self.ders_ekle(ders_adi)
        self.dersler[ders_adi].append(not_icerigi)
        print(f"{ders_adi} için not eklendi.")

    def notlari_goster(self):
        if not self.dersler:
            print("Henüz ders eklenmemiş.")
        else:
            for ders, notlar in self.dersler.items():
                print(f"\n{ders}:")
                for i, not_icerigi in enumerate(notlar, 1):
                    print(f"  {i}. {not_icerigi}")

    def not_sil(self, ders_adi, not_index):
        if ders_adi in self.dersler:
            try:
                silinen_not = self.dersler[ders_adi].pop(not_index - 1)
                print(f"{ders_adi} dersinden şu not silindi: {silinen_not}")
                if not self.dersler[ders_adi]:
                    del self.dersler[ders_adi]
            except IndexError:
                print("Geçersiz not numarası.")
        else:
            print(f"{ders_adi} bulunamadı.")


class Hatirlatici:
    def __init__(self):
        self.hatirlatmalar = []

    def hatirlatma_ekle(self, mesaj, zaman):
        if zaman < datetime.now():
            print("Geçmiş bir tarih seçemezsiniz!")
            return
        self.hatirlatmalar.append({"mesaj": mesaj, "zaman": zaman})
        print(f"Hatırlatma eklendi: {mesaj}, Zaman: {zaman}")
        threading.Thread(target=self.hatirlat, args=(mesaj, zaman), daemon=True).start()

    def hatirlat(self, mesaj, zaman):
        şimdi = datetime.now()
        bekleme_suresi = (zaman - şimdi).total_seconds()
        if bekleme_suresi > 0:
            time.sleep(bekleme_suresi)
        print(f"\n[Hatırlatma] {mesaj}")

    def hatirlatmalari_goster(self):
        if not self.hatirlatmalar:
            print("Henüz bir hatırlatma eklenmemiş.")
        else:
            for i, hatirlatma in enumerate(self.hatirlatmalar, 1):
                zaman = hatirlatma["zaman"].strftime("%Y-%m-%d %H:%M:%S")
                print(f"{i}. {hatirlatma['mesaj']} - {zaman}")

    def hatirlatma_sil(self, index):
        try:
            silinen = self.hatirlatmalar.pop(index - 1)
            print(f"Şu hatırlatma silindi: {silinen['mesaj']}")
        except IndexError:
            print("Geçersiz hatırlatma numarası.")


class KisiselNot(NotYonetim):
    pass


class IsNotu(NotYonetim):
    pass


def ana_menu():
    print("\n" + "Ana Menü".center(30, "-"))
    print("1. Kullanıcı İşlemleri")
    print("2. Not Yönetimi")
    print("3. Hatırlatıcı")
    print("4. Çıkış")


def not_yonetim_menu():
    print("\n" + "Not Yönetimi Menüsü".center(30, "-"))
    print("1. Eğitim Notları")
    print("2. Kişisel Notlar")
    print("3. İş Notları")
    print("4. Geri Dön")


def kullanıcı_islemleri():
    kullanici = KişiselBilgi()
    while True:
        print("\n" + "Kullanıcı İşlemleri".center(30, "-"))
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Geri Dön")

        secim = input("Seçiminiz: ")
        if secim == "1":
            kullanici.kayıt_ol()
        elif secim == "2":
            kullanici.giriş_yap()
        elif secim == "3":
            break
        else:
            print("Geçersiz seçim!")


def not_yonetim():
    egitim_notlari = EgitimNotu()
    kisisel_notlar = KisiselNot()
    is_notlari = IsNotu()

    while True:
        not_yonetim_menu()
        secim = input("Seçiminiz: ")

        if secim == "1":
            not_turu = egitim_notlari
            print("Eğitim Notları seçildi.")
        elif secim == "2":
            not_turu = kisisel_notlar
            print("Kişisel Notlar seçildi.")
        elif secim == "3":
            not_turu = is_notlari
            print("İş Notları seçildi.")
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim!")
            continue

        while True:
            print("\n1. Not Ekle")
            print("2. Notları Göster")
            print("3. Not Sil")
            print("4. Tüm Notları Sil")
            print("5. Geri Dön")
            alt_secim = input("Seçiminiz: ")

            if alt_secim == "1":
                if isinstance(not_turu, EgitimNotu):
                    ders_adi = input("Ders adı: ")
                    not_icerigi = input("Not içeriği: ")
                    not_turu.not_ekle(ders_adi, not_icerigi)
                else:
                    not_icerigi = input("Not içeriği: ")
                    not_turu.not_ekle(not_icerigi)
            elif alt_secim == "2":
                not_turu.notlari_goster()
            elif alt_secim == "3":
                if isinstance(not_turu, EgitimNotu):
                    ders_adi = input("Ders adı: ")
                    not_index = int(input("Silmek istediğiniz not numarası: "))
                    not_turu.not_sil(ders_adi, not_index)
                else:
                    not_index = int(input("Silmek istediğiniz not numarası: "))
                    not_turu.not_sil(not_index)
            elif alt_secim == "4":
                not_turu.tum_notlari_sil()
            elif alt_secim == "5":
                break
            else:
                print("Geçersiz seçim!")

def hatirlatici_menu():
    hatirlatici = Hatirlatici()
    while True:
        print("\n" + "Hatırlatıcı Menüsü".center(30, "-"))
        print("1. Hatırlatma Ekle")
        print("2. Hatırlatmaları Göster")
        print("3. Hatırlatma Sil")
        print("4. Geri Dön")
        secim = input("Seçiminiz: ")

        if secim == "1":
            mesaj = input("Hatırlatma mesajı: ")
            tarih_saat = input("Tarih ve saat (YYYY-MM-DD HH:MM:SS): ")
            try:
                zaman = datetime.strptime(tarih_saat, "%Y-%m-%d %H:%M:%S")
                hatirlatici.hatirlatma_ekle(mesaj, zaman)
            except ValueError:
                print("Geçersiz tarih formatı! Lütfen doğru formatta girin.")
        elif secim == "2":
            hatirlatici.hatirlatmalari_goster()
        elif secim == "3":
            try:
                index = int(input("Silmek istediğiniz hatırlatma numarası: "))
                hatirlatici.hatirlatma_sil(index)
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        elif secim == "4":
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    while True:
        ana_menu()
        secim = input("Seçiminiz: ")

        if secim == "1":
            kullanıcı_islemleri()
        elif secim == "2":
            not_yonetim()
        elif secim == "3":
            hatirlatici_menu()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim!")
