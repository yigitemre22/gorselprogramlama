# mainwindow.py
import sys
from PySide6.QtWidgets import QMainWindow,QApplication
# ui_form.py içindeki gerçek sınıf adını import ediyoruz
from ui_form import Ui_MainWindowq
from uyeler import UyeEkrani
from odemeler import OdemeEkrani
from antrenorler import AntrenorEkrani
from ayarlar import AyarlarEkrani
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
from raporlar import RaporEkrani
from dersler import DersEkrani
from uyelikTipleri import UyelikTipleriEkrani
from ekipmanlar import EkipmanEkrani
from PySide6.QtCore import Qt
import os
import pyodbc


class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
        # Sınıf ismini Ui_MainWindowq olarak güncelledik
        self.ui = Ui_MainWindowq()
        self.ui.setupUi(self)
        self.ui.btn_uyeler.clicked.connect(self.uye_ac)
        self.ui.btn_odemeler.clicked.connect(self.odemeekrani_Ac)
        self.ui.btn_antrenorler.clicked.connect(self.antrenor_Ac)
        self.ui.btn_ayarlar.clicked.connect(self.ayarlar_Ac)
        self.ui.btn_raporlar.clicked.connect(self.rapor_ac)
        self.ui.btn_dersler.clicked.connect(self.ders_ac)
        self.ui.btn_uyeliktipleri.clicked.connect(self.uyeliktipleri_Ac)
        self.ui.btn_ekipmanlar.clicked.connect(self.ekipman_Ac)
        self.toplam_uye_sayisi()
        self.aktif_uye_sayi()
        self.arka_plan_ayarla()
        self.setMinimumSize(950, 650)
        
        
        
    def uye_ac(self):
        self.uye_pencere = UyeEkrani()
        self.uye_pencere.show()

    def odemeekrani_Ac(self):
        self.odeme_pencere=OdemeEkrani()
        self.odeme_pencere.show()

    def antrenor_Ac(self):
        self.antrenor_pencere=AntrenorEkrani()
        self.antrenor_pencere.show()

    def ayarlar_Ac(self):
        self.ayarlar_pencere=AyarlarEkrani()
        self.ayarlar_pencere.show()
    def rapor_ac(self):
        self.rapor_pencere=RaporEkrani()
        self.rapor_pencere.show()
    def ders_ac(self):
        self.ders_pencere=DersEkrani()
        self.ders_pencere.show()
    def uyeliktipleri_Ac(self):
        self.uyeliktipleri_pencere=UyelikTipleriEkrani()
        self.uyeliktipleri_pencere.show()
    def ekipman_Ac(self):
        self.ekipman_pencere=EkipmanEkrani()
        self.ekipman_pencere.show()
    def toplam_uye_sayisi(self):
        try:
            conn_str=(
            "Driver={ODBC Driver 17 for SQL Server};"
                      "Server=.\\SQLEXPRESS05;"
                      "Database=spor_salonu;"
                      "Trusted_Connection=yes;"
            )
            conn=pyodbc.connect(conn_str)
            cursor=conn.cursor()

            cursor.execute("select count(*) from uyeler")
            sayi=cursor.fetchone()[0]

            conn.close()

            self.ui.label_toplam_uye.setText(str(sayi))

        except Exception as e:
            print("hata:",e)
            self.ui.label_toplam_uye.setText("0")

    def aktif_uye_sayi(self):
        try:
              conn_str = (
                  "Driver={ODBC Driver 17 for SQL Server};"
                  "Server=.\\SQLEXPRESS05;"
                  "Database=spor_salonu;"
                  "Trusted_Connection=yes;"
              )
              conn=pyodbc.connect(conn_str)
              cursor=conn.cursor()

              cursor.execute("""
              select count(*) from uyeler
              where uyelik_Bitis_Tarihi is not null
              and uyelik_Bitis_Tarihi >= getdate()
              """)
              sayi=cursor.fetchone()[0]
              conn.close()

              self.ui.label_aktif_uye.setText(str(sayi))
        except Exception as e:
            print("Hata:",e)
            self.ui.label_aktif_uye.setText("0")
    def arka_plan_ayarla(self):
        # Görsel yolunun doğruluğundan emin olun
        resim_yolu = r"C:\Users\yigit\OneDrive\Belgeler\fitness\resim.jpeg"
        
        if not os.path.exists(resim_yolu):
            print(f"HATA: Resim bulunamadı -> {resim_yolu}")
            return

        oImage = QPixmap(resim_yolu)
        
        # Hata veren kısım düzeltildi: width ve height manuel gönderiliyor
        sImage = oImage.scaled(
            self.width(), 
            self.height(), 
            Qt.AspectRatioMode.IgnoreAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(sImage))
        self.setPalette(palette)

    # Pencere boyutu değişirse arka planın yeniden ölçeklenmesi için:
    def resizeEvent(self, event):
        self.arka_plan_ayarla()
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'old_pos'):
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaEkran()
    pencere.show()
    sys.exit(app.exec())