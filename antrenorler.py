from datetime import date

from PySide6.QtWidgets import QMainWindow
from ui_antrenorler import Ui_MainWindow  # class adı değişebilir
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,Qt
 # class adı değişebilir
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os
class AntrenorEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)# This Python file uses the following encoding: utf-8# This Python file uses the following encoding: utf-8
        self.conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=.\SQLEXPRESS05;' 
        r'DATABASE=spor_salonu;'
        r'Trusted_Connection=yes;'
        )     
        self.ui.tbl_antrenorler.clicked.connect(self.tablodan_veri_cek)
        self.antrenor_listesi_getir()
        self.ui.btn_temizle.clicked.connect(self.temizle)
        self.uyeantrenor_listesi_getir()
        self.ui.btn_guncelle.clicked.connect(self.antrenor_guncelle)
        self.ui.btn_kaydet.clicked.connect(self.antrenor_ekle)
        self.ui.btn_sil.clicked.connect(self.antrenor_sil)

    def antrenor_sil(self):
        try:
            if not hasattr(self, 'secili_antrenor_id') or self.secili_antrenor_id is None:
                QMessageBox.warning(self, "Uyarı", "Lütfen silmek istediğiniz antrenörü tablodan seçin!")
                return

            # Kullanıcıdan onay alalım
            onay = QMessageBox.question(self, "Silme Onayı", 
                                    f"ID: {self.secili_antrenor_id} olan antrenörü silmek istediğinize emin misiniz?",
                                    QMessageBox.Yes | QMessageBox.No)

            if onay == QMessageBox.Yes:
                conn = pyodbc.connect(self.conn_str)
                cursor = conn.cursor()

                # SQL Sorgusu
                sorgu = "DELETE FROM antrenorler WHERE antrenor_id = ?"
                cursor.execute(sorgu, (self.secili_antrenor_id,))
                
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Başarılı", "Kayıt silindi.")
                self.secili_antrenor_id = None # Seçimi sıfırla
               
                
        except pyodbc.IntegrityError:
            QMessageBox.critical(self, "Hata", "Bu antrenöre bağlı üyeler olduğu için silemezsiniz! Önce üyelerle olan bağını kesin.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Silme hatası: {e}")




    def antrenor_ekle(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
       
            adi = self.ui.txt_ad.text().strip()
            soyadi = self.ui.txt_soyad.text().strip()
            tam_ad = f"{adi} {soyadi}"
            try:
                maas = float(self.ui.txt_maas.text().replace(',', '.'))
            except:
                maas = 0.0
            telefon = self.ui.txt_telefon.text()
            uzmanlik = self.ui.txt_uzmanlik.text()
            bugun_str = date.today().strftime('%Y-%m-%d')
            sorgu = "INSERT INTO antrenorler (telefon, uzmanlik_alani, maas, baslama_tarihi, antrenor_Adi) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(sorgu, (telefon, uzmanlik, maas, bugun_str, tam_ad))
            
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Başarılı", f"{tam_ad} eklendi.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Veritabanı hatası: {e}")

    def antrenor_guncelle(self):
        try:
            if not hasattr(self, 'secili_antrenor_id') or self.secili_antrenor_id is None:
                QMessageBox.warning(self, "Uyarı", "Lütfen önce tablodan bir antrenör seçin!")
                return

            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

          
            ad = self.ui.txt_ad.text()
            soyad = self.ui.txt_soyad.text()
            tam_ad = f"{ad} {soyad}"
            telefon = self.ui.txt_telefon.text()
            uzmanlik = self.ui.txt_uzmanlik.text()
            
            try:
                maas = float(self.ui.txt_maas.text().replace(',', '.'))
            except:
                maas = 0.0

      
            sorgu = """
                UPDATE antrenorler 
                SET telefon = ?, uzmanlik_alani = ?, maas = ?, antrenor_Adi = ? 
                WHERE antrenor_id = ?
            """
            
            cursor.execute(sorgu, (telefon, uzmanlik, maas, tam_ad, self.secili_antrenor_id))
            
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Başarılı", "Antrenör bilgileri güncellendi.")
          
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Güncelleme hatası: {e}")

    def temizle(self):
        self.ui.txt_ad.clear()
        self.ui.txt_maas.clear()
        self.ui.txt_soyad.clear()
        self.ui.txt_telefon.clear()
        self.ui.txt_uzmanlik.clear()
    def uyeantrenor_listesi_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select u.ad,u.soyad,at.antrenor_adi,ua.baslangicTarihi from uye_Antrenor ua inner join antrenorler at on ua.antrenorId=at.antrenor_id inner join uyeler u on ua.uyeID=u.uyeID")

            self.ui.tbl_uye_antrenor.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_uye_antrenor.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_uye_antrenor.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"{e}")
    def antrenor_listesi_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select * from antrenorler")

            self.ui.tbl_antrenorler.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_antrenorler.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_antrenorler.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"{e}")


    def tablodan_veri_cek(self,index):
        try:
            row=index.row()
            self.ui.txt_ad.setText(self.ui.tbl_antrenorler.item(row,1).text())
            self.ui.txt_soyad.setText(self.ui.tbl_antrenorler.item(row,2).text())
            self.ui.txt_telefon.setText(self.ui.tbl_antrenorler.item(row,3).text())
            self.ui.txt_uzmanlik.setText(self.ui.tbl_antrenorler.item(row,4).text())
            self.ui.txt_maas.setText(self.ui.tbl_antrenorler.item(row,5).text())
            self.secili_antrenor_id=self.ui.tbl_antrenorler.item(row,0).text()
        except Exception as e:
            print(f"hata:{e}")
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

    def resizeEvent(self, event):
        self.arka_plan_ayarla()
        super().resizeEvent(event)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AntrenorEkrani()
    pencere.show()
    sys.exit(app.exec())
