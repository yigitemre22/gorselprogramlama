import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

class VeriTabaniIslemleri:
    def __init__(self):
        # Bağlantı bilgilerini kendi server adına göre düzenle
        self.conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=.\SQLEXPRESS05;' # Scriptindeki server adı
            r'DATABASE=spor_salonu;'
            r'Trusted_Connection=yes;'
        )

    def baglanti_getir(self):
        return pyodbc.connect(self.conn_str)

    # 1. ComboBox İçin Ekipman Türlerini Çekme
    def ekipman_turlerini_getir(self):
        try:
            with self.baglanti_getir() as conn:
                cursor = conn.cursor()
                # ekipman_turleri tablosundan verileri alıyoruz
                cursor.execute("SELECT ekipmanTuruID, turAdi FROM ekipman_turleri")
                return cursor.fetchall()
        except Exception as e:
            print(f"Hata: {e}")
            return []

    # 2. sp_UyeEkle Prosedürünü Çalıştırma (Yeni Üye ve Otomatik Borç)
    def uye_ekle(self, ad, soyad, tel, email, dogum_tarihi, cinsiyet, uyelik_tipi_id):
        try:
            with self.baglanti_getir() as conn:
                cursor = conn.cursor()
                # Yazdığımız güncel prosedürü çağırıyoruz
                sql = "{CALL sp_UyeEkle (?, ?, ?, ?, ?, ?, ?)}"
                params = (ad, soyad, tel, email, dogum_tarihi, cinsiyet, uyelik_tipi_id)
                cursor.execute(sql, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Ekleme Hatası: {e}")
            return False

# --- UI Tarafında Kullanım Örneği ---
# Türleri ComboBox'a ekleme:
# for id_verisi, isim in db.ekipman_turlerini_getir():
#     self.ui.comboBox_kategori.addItem(isim, id_verisi)

# Üye Kaydetme Butonu:
# db.uye_ekle("Ahmet", "Yılmaz", "555...", "ahmet@mail.com", "1990-01-01", "Erkek", 1)# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
