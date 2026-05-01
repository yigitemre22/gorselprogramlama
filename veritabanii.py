import pyodbc
import random
from datetime import datetime, timedelta

# Veritabanı bağlantı bilgileri
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=.\SQLEXPRESS05;' 
    r'DATABASE=spor_salonu;'
    r'Trusted_Connection=yes;'
)

import pyodbc
import random

# Bağlantı Ayarları
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=.\SQLEXPRESS05;' 
    r'DATABASE=spor_salonu;'
    r'Trusted_Connection=yes;'
)

def yuz_uye_boy_kilo_ekle():
    isimler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Can", "Zeynep", "Murat", "Elif", "Burak", "Selin"]
    soyisimler = ["Yılmaz", "Kaya", "Demir", "Çelik", "Arslan", "Yıldız", "Öztürk"]
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        cursor.execute("SELECT uyeliktipiID FROM uyelik_tipleri")
        tip_idleri = [row[0] for row in cursor.fetchall()]

        print("100 üye boy ve kilo verileriyle ekleniyor...")

        for i in range(100):
            ad = random.choice(isimler)
            soyad = random.choice(soyisimler)
            tel = f"05{random.randint(30, 55)}{random.randint(1000000, 9999999)}"
            mail = f"{ad.lower()}{random.randint(100,999)}@test.com"
            dogum = f"{random.randint(1980, 2005)}-01-01"
            cinsiyet = random.choice(["Erkek", "Kadın"])
            tip_id = random.choice(tip_idleri)
            
            # Rastgele Boy ve Kilo üretimi
            boy = random.randint(155, 195)
            kilo = random.randint(55, 110)

            # Güncellenmiş prosedürü çağırıyoruz (9 parametre)
            cursor.execute("""
                EXEC [dbo].[sp_UyeEkle] 
                @ad = ?, @soyad = ?, @telefon = ?, @email = ?, 
                @dogumTarihi = ?, @cinsiyet = ?, @uyelikTipiID = ?,
                @boy = ?, @kilo = ?
            """, (ad, soyad, tel, mail, dogum, cinsiyet, tip_id, boy, kilo))

        conn.commit()
        print("İşlem tamamlandı. Artık üyelerin boy ve kilo bilgileri de var!")

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

def on_antrenor_ekle():

    # Örnek veriler
    isimler = ["Hakan", "Merve", "Serkan", "Derya", "Tolga", "Selin", "Burak", "Aslı", "Eren", "Nilay"]
    soyisimler = ["Korkmaz", "Öztürk", "Bulut", "Yılmaz", "Güneş", "Demir", "Aydın", "Şahin", "Aras", "Çetin"]
    uzmanliklar = ["Fitness", "Pilates", "Yoga", "Crossfit", "Vücut Geliştirme", "Yüzme", "Kick Boks"]

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("10 antrenör ekleniyor...")

        for i in range(10):
            ad = isimler[i] # Her birini bir kez kullanalım
            soyad = soyisimler[i]
            uzmanlik = random.choice(uzmanliklar)
            tel = f"05{random.randint(30, 55)}{random.randint(100, 999)}{random.randint(10, 99)}{random.randint(10, 99)}"

            # Prosedürü çağırıyoruz
            cursor.execute("""
                EXEC [dbo].[sp_AntrenorEkle] 
                @ad = ?, @soyad = ?, @uzmanlikAlani = ?, @telefon = ?
            """, (ad, soyad, uzmanlik, tel))

        conn.commit()
        print("10 antrenör başarıyla eklendi!")

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

def on_antrenor_ekle_guncel():
    isimler = ["Hakan", "Merve", "Serkan", "Derya", "Tolga", "Selin", "Burak", "Aslı", "Eren", "Nilay"]
    soyisimler = ["Korkmaz", "Öztürk", "Bulut", "Yılmaz", "Güneş", "Demir", "Aydın", "Şahin", "Aras", "Çetin"]
    uzmanliklar = ["Fitness", "Pilates", "Yoga", "Crossfit", "Vücut Geliştirme"]

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("10 antrenör maaş bilgisiyle ekleniyor...")

        for i in range(10):
            ad = isimler[i]
            soyad = soyisimler[i]
            uzmanlik = random.choice(uzmanliklar)
            tel = f"05{random.randint(30, 55)}{random.randint(100, 999)}{random.randint(1000, 9999)}"
            maas = random.randint(15000, 35000) # Rastgele maaş üretimi

            # 5 Parametre gönderiyoruz: ad, soyad, uzmanlik, tel, maas
            cursor.execute("""
                EXEC [dbo].[sp_AntrenorEkle] 
                @ad = ?, @soyad = ?, @uzmanlikAlani = ?, @telefon = ?, @maas = ?
            """, (ad, soyad, uzmanlik, tel, maas))

        conn.commit()
        print("10 antrenör başarıyla eklendi!")

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

def ekipmanlari_doldur():
    # Kategori ve içindeki örnek cihazlar
    kategoriler = {
        "Kardiyo": ["Koşu Bandı", "Kondisyon Bisikleti", "Eliptik Bisiklet", "Kürek Makinesi"],
        "Ağırlık": ["Bench Press Sehpası", "Dumbbell Seti", "Leg Press Makinesi", "Lat Pulldown"],
        "Serbest Alan": ["Yoga Matı", "Pilates Topu", "Kettlebell", "Zıplama Kutusu"],
        "Crossfit": ["Barfix Demiri", "Battle Rope", "Kum Torbası", "Halter Barı"]
    }

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("Ekipman türleri ve ekipmanlar ekleniyor...")

        for tur_adi, cihazlar in kategoriler.items():
            # 1. Önce Türü Ekle
            cursor.execute("EXEC [dbo].[sp_EkipmanTuruEkle] @turAdi = ?", (tur_adi,))
            conn.commit()

            # 2. Eklenen Türün ID'sini Al
            cursor.execute("SELECT ekipmanTuruID FROM ekipman_turleri WHERE turAdi = ?", (tur_adi,))
            tur_id = cursor.fetchone()[0]

            # 3. Bu Türün Altına Rastgele Cihazlar Ekle
            for cihaz in cihazlar:
                adet = random.randint(1, 10)
                durum = random.choice(["Aktif", "Aktif", "Bakımda", "Arızalı"]) # Aktif olma olasılığı daha yüksek
                
                # Ekipmanlar tablosuna direkt insert (Prosedürün yoksa direkt insert güvenlidir)
                cursor.execute("""
                    INSERT INTO ekipmanlar (ekipmanAdi, alimTarihi, durum, kategori, adet)
                    VALUES (?, GETDATE(), ?, ?, ?)
                """, (cihaz, durum, tur_id, adet))

        conn.commit()
        print("Tüm ekipmanlar başarıyla kategorize edilerek eklendi!")

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

def dersleri_uret_saatli():
    ders_isimleri = ["Sabah Yogası", "Crossfit", "Fitness", "Pilates", "Kick Boks", "Zumba"]
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"]
    # Başlangıç saatleri listesi
    baslangic_saatleri = ["08:00", "10:00", "13:00", "15:00", "18:00", "20:00"]

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        cursor.execute("SELECT antrenor_id FROM antrenorler")
        antrenor_idleri = [row[0] for row in cursor.fetchall()]

        print("Başlangıç ve bitiş saatli 20 ders üretiliyor...")

        for i in range(20):
            ders_adi = random.choice(ders_isimleri)
            antrenor_id = random.choice(antrenor_idleri)
            gun = random.choice(gunler)
            
            # Saat hesaplama
            b_saat_str = random.choice(baslangic_saatleri)
            # String'i saat objesine çevirip 1 saat ekliyoruz
            b_saat_obj = datetime.strptime(b_saat_str, "%H:%M")
            bitis_saat_obj = b_saat_obj + timedelta(hours=1)
            
            bitis_saat_str = bitis_saat_obj.strftime("%H:%M")
            kapasite = random.randint(12, 25)

            # Prosedürü yeni parametrelerle çağırıyoruz
            cursor.execute("""
                EXEC [dbo].[sp_DersEkle] 
                @dersAdi = ?, @antrenorID = ?, @gun = ?, 
                @baslangic_saati = ?, @bitis_saati = ?, @kapasite = ?
            """, (ders_adi, antrenor_id, gun, b_saat_str, bitis_saat_str, kapasite))

        conn.commit()
        print("Ders programı (saat aralıklarıyla) başarıyla oluşturuldu!")

    except Exception as e:
        print(f"Hata: {e}")
    finally:
        conn.close()

def giris_cikis_saat_uret():
    try:
        conn=pyodbc.connect(conn_str)
        cursor=conn.cursor()

        cursor.execute("select uyeID from uyeler")
        uye_idleri=[row[0] for row in cursor.fetchall()]

        if not uye_idleri:
            print("üye bulunamadı")
            return
        print("150 adet giriş çıkış kaydı üretiliyor")

        for i in range (150):
            uye_id=random.choice(uye_idleri)

            gun_farki=random.randint(0,7)
            saat_farki=random.randint(8,22)
            dakika_farki=random.randint(0,59)

            giris_zamani=datetime.now()-timedelta(days=gun_farki)
            giris_zamani=giris_zamani.replace(hour=saat_farki,minute=dakika_farki)

            if random.random()<0.2:
                cikis_zamani=None
            else:
                kalma_suresi=random.randint(45,120)
                cikis_zamani=giris_zamani+timedelta(minutes=kalma_suresi)
            
            cursor.execute("insert into girisCikisKayitlari (uyeID,giriszamani,cikiszamani) values(?,?,?)",(uye_id,giris_zamani,cikis_zamani))

        conn.commit()
        print("giriş çıkış kayıtlrı başarıyla oluşturuldu")

    except Exception as e:
        print(f"Hata:{e}")
    finally:
        conn.close()

def odeme_uret():    
    try:
        conn=pyodbc.connect(conn_str)
        cursor=conn.cursor()

        cursor.execute("select odemeyontemiID,yontemAdi from odeme_yontemleri")

        tum_yontemler=cursor.fetchall()

        yontemler=[row[0] for row in tum_yontemler]
        yontemAdlari=[row[1] for row in tum_yontemler]
        if not yontemler:
            print("ödeme yöntemi bulunamadı")
            return
        print()

        cursor.execute("select uyeID ,toplamBorc from uyeler where toplamBorc > 0")
        borclu_uyeler=cursor.fetchall()
        if not borclu_uyeler:
            print("borçlu üye bulunamadı")
            return

        for i in range(50):
            uye=random.choice(borclu_uyeler)
            uye_id=uye[0]
            mevcut_borc=float(uye[1])

            miktar=round(mevcut_borc*random.uniform(0.1,0.5),2)

            odeme_tarihi=datetime.now()-timedelta(days=random.randint(0,15))
            secilen_yontem=random.choice(yontemler)
            secilen_ad=random.choice(yontemAdlari)


            cursor.execute("exec [dbo].[sp_OdemeAl] @uyeID=?,@miktar=?,@odemeTarihi=?,@odemeYontemiID=?,@odemeTuru=?",uye_id,miktar,odeme_tarihi,secilen_yontem,secilen_ad)

        conn.commit()
        print("işlem tamamlandı.ödemeler sql'de ki yöntem tablosuna göre yapıldı")    
    except Exception as e:
        print(f"hata:{e}")
    finally:
        conn.close()

def uye_antrenor_iliski_uret():
    try:
        conn=pyodbc.connect(conn_str)
        cursor=conn.cursor()

        cursor.execute("select uyeID from uyeler")
        uyeler=[row[0] for row in cursor.fetchall()]

        cursor.execute("select antrenor_id from antrenorler")
        antrenorler=[row[0] for row in cursor.fetchall()]

        if not uyeler or not antrenorler:
            print("üye veya antrenör tablosu boş")
            return
    
        print(f"{len(uyeler)} üye ve {len(antrenorler)} antenör arasında bağ kuruluyor")

        eklenen_baglar=set()
        kayit_sayisi=0

        while kayit_sayisi<101:
            uye_id=random.choice(uyeler)
            antrenor_id=random.choice(antrenorler)

            if(uye_id,antrenor_id) not in eklenen_baglar:
                baslangic=datetime.now()-timedelta(days=random.randint(10,60))

                cursor.execute("insert into uye_Antrenor (uyeID,antrenorId,baslangicTarihi) values (?,?,?)",(uye_id,antrenor_id,baslangic))
                eklenen_baglar.add((uye_id,antrenor_id))
                kayit_sayisi+=1
        conn.commit()
        print(f"başarıyla {kayit_sayisi} adet üye-antrenör eşleşmesi oluşturuldu")

    except Exception as e:
        print(f"hata:{e}")
    finally:
        conn.close()

def uye_ders_uret():
    try:
        conn=pyodbc.connect(conn_str)
        cursor=conn.cursor()
        
        cursor.execute("select uyeID from uyeler")
        uye_ID=[row[0] for row in cursor.fetchall()]

        cursor.execute("select dersID from dersler")
        ders_id=[row[0] for row in cursor.fetchall()]

        if not uye_ID or not ders_id:
            print("üyeid veya ders id bulunamadı")
            return
        print(f"{len(uye_ID)} üye ve {len(ders_id)} ders arasında bağ kuruluor")

        cursor.execute("SELECT uyeID, dersID FROM uyeDers")
        mevcut_kayitlar = set(cursor.fetchall())

        kayit_sayisi=0
        while kayit_sayisi<61:
            uye_id=random.choice(uye_ID)
            ders_Id=random.choice(ders_id)

            if(uye_id,ders_Id) not in mevcut_kayitlar:
                tarih=datetime.now() - timedelta(days=(random.randint(1,30)))

                cursor.execute("insert into uyeDers (uyeID,dersID,katilimTarihi) values (?,?,?)",(uye_id,ders_Id,tarih))
                mevcut_kayitlar.add((uye_id,ders_Id))
                kayit_sayisi+=1
        conn.commit()
        print(f"başarıyla {kayit_sayisi} adet üye-ders kaydı oluşturuldu")
    except Exception as e:
        print(f"hata:{e}")
    finally:
        conn.close()

if __name__ == "__main__":
   uye_ders_uret()
