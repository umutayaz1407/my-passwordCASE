import os
import re
from datetime import datetime


class VeriYazici:
    kullanicilar = []  # Tüm kullanıcıları saklayacak sınıf düzeyinde bir liste

    def __init__(self):
        self.ad = ""
        self.sifre = ""
        self.email = ""
        self.tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Kullanıcı kaydının alındığı tarih
        self.site = ""

    def ad_al(self):
        while True:
            ad = input("Adınızı girin (En az 3 harf olmalı, sadece harfler): ")
            if len(ad) >= 3 and ad.isalpha():
                if not any(kullanici["ad"] == ad for kullanici in VeriYazici.kullanicilar):
                    return ad
                else:
                    print("Bu isim zaten alındı, lütfen başka bir isim girin.")
            else:
                print("Ad en az 3 harf olmalı ve sadece harflerden oluşmalı.")

    def sifre_al(self):
        while True:
            sifre = input("Şifrenizi girin (En az 6 karakter olmalı): ")  # Şifreyi normal olarak alıyoruz
            if len(sifre) >= 6:
                return sifre
            else:
                print("Şifre en az 6 karakter olmalıdır.")

    def email_al(self):
        while True:
            email = input("E-posta adresinizi girin: ")
            # E-posta formatı kontrolü
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Geçerli bir e-posta adresi girin.")

    def site_al(self):
        while True:
            site = input("giriceğiniz site adresini yazınız (En az 1 karakter olmalı): ")  # Şifreyi normal olarak alıyoruz
            if len(site) >= 1:
                return site
            else:
                print("Şifre en az 1 karakter olmalıdır.")

    def bilgi_gir(self):
        print("\n--- Bilgilerinizi girin ---")
        self.ad = self.ad_al()
        self.sifre = self.sifre_al()
        self.email = self.email_al()
        self.site = self.site_al()
        VeriYazici.kullanicilar.append({
            "ad": self.ad,
            "sifre": self.sifre,
            "email": self.email,
            "tarih": self.tarih,
            "site" : self.site
        })
        self.save_to_txt()

    def save_to_txt(self):
        # Masaüstü üzerinde bir klasör oluşturuyoruz
        klasor_yolu = os.path.expanduser("~/Desktop/KullaniciBilgileri")
        if not os.path.exists(klasor_yolu):
            os.makedirs(klasor_yolu)

        # Kullanıcı bilgilerini bir txt dosyasına kaydediyoruz
        dosya_yolu = os.path.join(klasor_yolu, f"{self.ad}.txt")
        with open(dosya_yolu, "w") as dosya:
            dosya.write(f"Ad: {self.ad}\n")
            dosya.write(f"Şifre: {self.sifre}\n")
            dosya.write(f"E-posta: {self.email}\n")
            dosya.write(f"Site: {self.site}\n")
            dosya.write(f"Kaydedilme Tarihi: {self.tarih}\n")

    @classmethod
    def dosya_sil(cls): #siler komut dizini lütfen silmeyin VE DİKKATLİ KULLANIN !!!!! os ile çalışır değiştrimeyin
        ad = input("Silmek istediğiniz kullanıcının adını girin: ")
        dosya_yolu = os.path.join(os.path.expanduser("~/Desktop/KullaniciBilgileri"), f"{ad}.txt")
        if os.path.exists(dosya_yolu):
            os.remove(dosya_yolu)
            print(f"{ad} kullanıcısının bilgileri silindi.")
        else:
            print(f"{ad} kullanıcısının bilgileri bulunamadı.")

    @classmethod
    def kalsör_listeleme(cls):
        klasor_yolu = os.path.expanduser("~/Desktop/KullaniciBilgileri")
        if os.path.exists(klasor_yolu):
            print("\nKullanıcı bilgileri klasörü:")
            for dosya in os.listdir(klasor_yolu):
                with open(os.path.join(klasor_yolu, dosya), "r") as dosya:
                    print(dosya.read())
        else:
            print("Kullanıcı bilgileri klasörü bulunamadı.")

    @classmethod
    def listele(cls):
        if cls.kullanicilar:
            print("\nTüm kullanıcılar:")
            for kullanici in cls.kullanicilar:
                print("________________________________________________________________________________________________________________________________________________________\n"
                      f"Ad: {kullanici['ad']}, Şifre: {kullanici['sifre']}, E-posta: {kullanici['email']}, Site: {kullanici['site']}, Kaydedilme Tarihi: {kullanici['tarih']}\n"
                      "--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        else:
            print("[[[[(----------------------Henüz kullanıcı yok isterseniz ekleyebilirsiniz.------------------------)]]]]]]")

    @classmethod
    def bilgi_guncelle(cls):
        ad = input("\nGüncellemek istediğiniz adınızı girin: ")
        for kullanici in cls.kullanicilar:
            if kullanici['ad'] == ad:
                print(f"{ad} için güncelleme yapılıyor...")

                while True:
                    sifre = input("Şifreyi değiştirmek istiyor musunuz? (Evet/Hayır): ").lower()
                    if sifre == "evet":
                        kullanici['sifre'] = input("Yeni şifreyi girin: ")  # Şifreyi normal olarak alıyoruz
                        if len(kullanici['sifre']) < 6:
                            print("Şifre en az 6 karakter olmalıdır. Tekrar deneyin.")
                        else:
                            break
                    elif sifre == "hayır":
                        break
                    else:
                        print("Lütfen 'Evet' ya da 'Hayır' yazın.")

                while True:
                    email = input("E-posta adresini değiştirmek istiyor musunuz? (Evet/Hayır): ").lower()
                    if email == "evet":
                        yeni_email = input("Yeni e-posta adresinizi girin: ")
                        if re.match(r"[^@]+@[^@]+\.[^@]+", yeni_email):
                            kullanici['email'] = yeni_email
                            break
                        else:
                            print("Geçerli bir e-posta adresi girin.")
                    elif email == "hayır":
                        break
                    else:
                        print("Lütfen 'Evet' ya da 'Hayır' yazın.")

                # Güncellenmiş bilgileri tekrar txt dosyasına kaydetme
                cls.save_all_users_to_txt()
                print(f"{ad} için bilgiler başarıyla güncellendi.")
                return
        print(f"{ad} bulunamadı.")

    @classmethod
    def save_all_users_to_txt(cls):
        klasor_yolu = os.path.expanduser("~/Desktop/KullaniciBilgileri")
        if not os.path.exists(klasor_yolu):
            os.makedirs(klasor_yolu)

        for kullanici in cls.kullanicilar:
            dosya_yolu = os.path.join(klasor_yolu, f"{kullanici['ad']}_bilgileri.txt")
            with open(dosya_yolu, "w") as dosya:
                dosya.write(f"Ad: {kullanici['ad']}\n")
                dosya.write(f"Şifre: {kullanici['sifre']}\n")
                dosya.write(f"E-posta: {kullanici['email']}\n")
                dosya.write(f"Site: {kullanici['site']}\n")
                dosya.write(f"Kaydedilme Tarihi: {kullanici['tarih']}\n")


def ana_menu():
    print("\n"                    
               
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░████░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░████████░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░████████░░░░\n"
                "░░██░░████░░████░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░████░░░░░░░░██░░\n"
                "██░░░░░░░░░░░░░░████░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░████░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░░░░░████░░██░░░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░████░░██\n"
                "░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░████░░░░████░░░░░░██░░░░░░░░░░░░░░████████░░\n"
                "░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░████░░░░░░░░░░██░░░░░░░░░░░░░░████████░░\n"
                "░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░████░░░░████░░░░░░██░░░░░░░░░░░░░░░░████░░░░\n"
                "░░░░░░░░████░░░░░░░░░░░░██░░████░░░░░░░░░░░░████░░██░░░░░░░░░░░░████░░░░░░░░\n"
                "░░░░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░██████████░░░░░░░░████████░░░░░░░░██████████░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░██████████░░░░░░░░████████░░░░░░░░██████████░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░████░░░░░░░░░░░░\n"
                "░░░░░░░░████░░░░░░░░░░░░██░░████░░░░░░░░░░░░████░░██░░░░░░░░░░░░████░░░░░░░░\n"
                "░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░████░░░░████░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░\n"
                "░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░████░░░░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░\n"
                "░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░████░░░░████░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░\n"
                "██░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░░░░░████░░██░░░░░░░░░░░░░░░░░░░░██░░████░░░░░░░░░░░░░░░░░░██\n"
                "██░░░░░░░░░░░░░░████░░░░░░██░░░░░░░░░░░░░░░░░░░░██░░░░░░████░░░░░░░░░░░░░░██\n"
                "░░██░░░░░░░░████░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░████░░░░░░░░██░░\n"
                "░░░░████████░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░████████░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    while True:
        print("________________________________________________________________________________________\n"
              "[                        >               log menu             <                        ]\n"
              "[______________________________________________________________________________________]\n"
              "__________{[--- Ana Menü ---}]_______--------------------------------------------------\n"
              "bu programı axlohtle tarafından yapılmıştır\n"
              "şifre alıcı programıdır\n"
              "güvelik başta tutulur\n"
              "hatırlamak yerine depolamak daha iyidir\n"
                "şifrelerinizi unutmayın\n"
              "__________{[--- BY AXLOHTLE ---}]_______\n")
        print("1. Listele")
        print("2. Yeni kullanıcı ekle")
        print("3. Çık")
        print("4. Bilgileri güncelle")
        print("5. sil")
        print("6. Klasördeki bilgileri listele")
        try:
            secim = int(input("Bir işlem seçin (1/2/3/4/5/6): "))
        except ValueError:
            print("Lütfen geçerli bir seçenek girin (1/2/3/4/5/6).")
            continue

        if secim == 1 :
            VeriYazici.listele()
        if secim == "listele" :
            VeriYazici.listele()
        elif secim == 2:
            yeni_kullanici = VeriYazici()
            yeni_kullanici.bilgi_gir()
            while True:
                guncelleme = input(f"Eksik bilgileri daha sonra eklemek ister misiniz? (Evet/Hayır): ").lower()
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                if guncelleme == "evet":
                    yeni_kullanici.bilgi_guncelle()
                    break
                elif guncelleme == "hayır":
                    break
                else:
                    print("Lütfen 'Evet' ya da 'Hayır' yazın.")
        elif secim == "yeni":
            yeni_kullanici = VeriYazici()
            yeni_kullanici.bilgi_gir()
            while True:
                guncelleme = input(f"Eksik bilgileri daha sonra eklemek ister misiniz? (Evet/Hayır): ").lower()
                "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
                if guncelleme == "evet":
                    yeni_kullanici.bilgi_guncelle()
                    break
                elif guncelleme == "hayır":
                    break
                else:
                    print("Lütfen 'Evet' ya da 'Hayır' yazın.")
        elif secim == 3:
            print("Programdan çıkılıyor...")
            break                                                           #remove silmiyor path sorunu var çözülcek hocam
        elif secim == "çık":
            print("Programdan çıkılıyor...")
            break
        elif secim == 4:
            VeriYazici.bilgi_guncelle()
        elif secim == "güncele":
            VeriYazici.bilgi_guncelle()
        elif secim == "sil":
            VeriYazici.dosya_sil()
        elif secim == 5:
            VeriYazici.dosya_sil()
        if secim == 6:
            VeriYazici.kalsör_listeleme()
        if secim == "klasör":
            VeriYazici.kalsör_listeleme()
        else:
            print("Geçersiz seçim. Lütfen 1, 2, 3 , 4 , 5 ya da 6 yazın.")


# Ana Menü'yü başlat
ana_menu()


