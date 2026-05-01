import sys
import pyodbc
import os
import traceback
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
from PySide6.QtGui import QPixmap, QPalette, QBrush, QIcon
from PySide6.QtCore import Qt
from ui_login import Ui_Form


                
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Giriş butonu bağlantısı
        self.ui.btn_giris.clicked.connect(self.giris_kontrol)
        
        # Tasarım ayarları
        self.arka_plan_ayarla()
        self.setWindowIcon(QIcon("empty.icon"))
        
        # Değişkeni önceden tanımlayalım (Hata almamak için)
        self.aktif_pencere = None

    def giris_kontrol(self):
        kadi = self.ui.lineEdit_kullanici.text().strip()
        sifre_girilen = self.ui.lineEdit_sifre.text().strip()

        if not kadi or not sifre_girilen:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun!")
            return

        try:
            conn_str = (
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=.\\SQLEXPRESS05;"
                "Database=spor_salonu;"
                "Trusted_Connection=yes;"
            )

            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                # rol ve uyeID sütunlarını çekiyoruz
                query = "SELECT rol, uyeID FROM kullanicilar WHERE kullanici_adi = ? AND sifre = ?"
                cursor.execute(query, (kadi, sifre_girilen))
                kullanici = cursor.fetchone()

                if kullanici:
                    rol = kullanici[0]
                    uye_id = kullanici[1]
                    print(f"Giriş Başarılı! Rol: {rol}, ID: {uye_id}")
                    self.ekranlari_yonet(rol, uye_id)
                else:
                    QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Veritabanı Hatası", f"Bağlantı Hatası: {ex}")

    def ekranlari_yonet(self, rol, uye_id):
        try:
            if rol == "admin":
                from mainwindow import AnaEkran
                self.aktif_pencere = AnaEkran()
            
            elif rol == "Antrenör":
                from Antrenor_Ekran import antrenor_ekran
                self.aktif_pencere = antrenor_ekran() 
                
            elif rol == "Üye":
                from uyeEkran import uye_ekran
                # Artık uyeEkran __init__ içinde uye_id beklediği için hata vermeyecek
                self.aktif_pencere = uye_ekran(uye_id) 
            
            if self.aktif_pencere:
                self.aktif_pencere.show()
                self.close()

        except Exception as e:
            print(traceback.format_exc())
            QMessageBox.critical(self, "Hata", f"Ekran açılırken hata oluştu: {e}")
    def arka_plan_ayarla(self):
        resim_yolu = r"C:\Users\yigit\OneDrive\Belgeler\fitness\resim.jpeg"
        if not os.path.exists(resim_yolu):
            return

        oImage = QPixmap(resim_yolu)
        sImage = oImage.scaled(
            self.width(), self.height(), 
            Qt.AspectRatioMode.IgnoreAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(sImage))
        self.setPalette(palette)

    def resizeEvent(self, event):
        self.arka_plan_ayarla()
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())