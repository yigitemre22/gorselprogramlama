from datetime import datetime

from PySide6.QtWidgets import QMainWindow,QApplication, QMessageBox, QTableWidgetItem
from ui_odemeler import Ui_MainWindow  
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os
from PySide6.QtCore import QTime,Qt
import sys
import pyodbc
class OdemeEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=.\SQLEXPRESS05;' 
            r'DATABASE=spor_salonu;'
            r'Trusted_Connection=yes;'
        )
     
        self.ui.txt_uyeAd.textChanged.connect(self.uye_ara) 
        self.ui.tbl_uyeler.itemClicked.connect(self.odeme_gecmisi_yukle)
        self.uye_ara() 
        self.ui.btn_odemeAl.clicked.connect(self.odeme_al) 
        self.ui.txt_uyeAd.textChanged.connect(self.uye_ara) 
        self.ui.btn_ara.clicked.connect(self.uye_ara) 
       

    def odeme_al(self):
        try:
          
            secili_satir = self.ui.tbl_uyeler.currentRow()
            if secili_satir == -1:
                QMessageBox.warning(self, "Hata", "Lütfen önce tablodan bir üye seçin!")
                return

         
            uye_id_item = self.ui.tbl_uyeler.item(secili_satir, 6)
            if not uye_id_item or not uye_id_item.text().isdigit():
                QMessageBox.warning(self, "Hata", "Seçilen üyenin ID'si geçersiz!")
                return
            uye_id = int(uye_id_item.text())

            try:
                miktar = float(self.ui.txt_tutar.text().replace(",", "."))  
            except ValueError:
                QMessageBox.warning(self, "Hata", "Geçersiz tutar girdiniz!")
                return

            kategori = self.ui.comboBox.currentText()  
            aciklama = self.ui.txt_aciklama.toPlainText()

            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()

  
            cursor.execute("""
                EXEC sp_OdemeAl ?, ?, ?, ?, ?
            """, (uye_id, miktar, datetime.now(), 1, kategori))

    
            cursor.execute("""
            INSERT INTO kasa (islemTarihi, islemTuru, kategori, miktar, aciklama, uyeId) 
            VALUES (GETDATE(), 'Gelir', ?, ?, ?, ?)
            """, ("Üyelik", miktar, aciklama, uye_id))

   
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Başarılı", "Ödeme başarıyla kaydedildi.")

   
            self.odeme_gecmisi_yukle()

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Beklenmedik bir hata oluştu:\n{e}")
            print("HATA:", e)
    def uye_ara(self):
        try:
            arama_metni = self.ui.txt_uyeAd.text() #
            conn = pyodbc.connect(self.conn_str) #
            cursor = conn.cursor()
            
            sorgu = """
                SELECT ut.ad, ut.soyad, ut.telefon, t.tipAdi, 
                    ut.uyelikBitisTarihi, ut.toplamBorc, ut.uyeID
                FROM uyeler ut
                INNER JOIN uyelik_tipleri t ON ut.uyelikTipiID = t.uyeliktipiID
                WHERE (ut.ad + ' ' + ut.soyad LIKE ?) AND ut.toplamBorc > 0
                """
            cursor.execute(sorgu, (f"%{arama_metni}%",))
            veriler = cursor.fetchall()

            self.ui.tbl_uyeler.setRowCount(0) #
            for row_idx, row_data in enumerate(veriler):
                self.ui.tbl_uyeler.insertRow(row_idx)
              
                for col_idx, value in enumerate(row_data):
                    self.ui.tbl_uyeler.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
            
            conn.close()
        except Exception as e:
            print(f"Arama Hatası: {e}")
    def odeme_gecmisi_yukle(self):
        try:
            secili_satir = self.ui.tbl_uyeler.currentRow()
            if secili_satir == -1:
                return
            
            uye_id = int(self.ui.tbl_uyeler.item(secili_satir,6).text())
            self.ui.txt_uyeID.setText(str(uye_id))

            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
            sorgu = """
            SELECT odemeTarihi, miktar, odemeTuru, aciklama 
            FROM odemeler 
            WHERE uyeID = ? 
            ORDER BY odemeTarihi DESC
            """

            cursor.execute(sorgu, (uye_id,))
            odemeler = cursor.fetchall()

            print("Kayıt sayısı:", len(odemeler))

            self.ui.tbl_odemeler.setRowCount(0)

            for row_idx, row_data in enumerate(odemeler):
                self.ui.tbl_odemeler.insertRow(row_idx)

                self.ui.tbl_odemeler.setItem(row_idx, 0, QTableWidgetItem(str(row_data[0])))
                self.ui.tbl_odemeler.setItem(row_idx, 1, QTableWidgetItem(f"{row_data[1]} TL"))
                self.ui.tbl_odemeler.setItem(row_idx, 2, QTableWidgetItem(str(row_data[2])))
                self.ui.tbl_odemeler.setItem(row_idx, 3, QTableWidgetItem(str(row_data[3])))

            conn.close()

        except Exception as e:
         print("HATA:", e)

    def arka_plan_ayarla(self):
         resim_yolu = r"C:\Users\yigit\OneDrive\Belgeler\fitness\resim.jpeg"
        
         if not os.path.exists(resim_yolu):
             print(f"HATA: Resim bulunamadı -> {resim_yolu}")
             return
         oImage = QPixmap(resim_yolu)
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
    pencere = OdemeEkrani()
    pencere.show()
    sys.exit(app.exec())