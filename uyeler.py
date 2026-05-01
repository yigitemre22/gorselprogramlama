import os

from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox,QTableWidgetItem,QSizePolicy,QHeaderView,QVBoxLayout
from PySide6.QtCore import QDate, Qt
from ui_uyeler import Ui_MainWindow  # class adı değişebilir
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon

class UyeEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)# This Python file uses the following encoding: utf-8
        self.conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=.\SQLEXPRESS05;' 
        r'DATABASE=spor_salonu;'
        r'Trusted_Connection=yes;'
        )           

        self.uyelik_tiplerini_getir()
        self.ui.btn_kaydet.clicked.connect(self.uye_kaydet)
        self.ui.btn_Temizle.clicked.connect(self.temizle)
        self.uyelik_durum_guncelle()
        self.uyeleri_listele()
        self.ui.btn_bilgiGetir.clicked.connect(self.uyeleri_listele)
        self.ui.btn_Sil.clicked.connect(self.uye_sil)
        self.ui.tbl_uyeler.cellClicked.connect(self.tablodan_Veri_cek)
        self.ui.btn_Guncelle.clicked.connect(self.uye_guncelle)
        
        # __init__ içindeki diğer kodların altına ekleyin:
      

    def uyelik_tiplerini_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select uyeliktipiID,tipAdi from uyelik_tipleri")
            self.ui.cmb_uyelik.clear()

            rows = cursor.fetchall()
            if not rows:
                print("Veritabanında üyelik tipi bulunamadı!")
            
            for row in rows:
                self.ui.cmb_uyelik.addItem(row[1],row[0])
            
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def uye_kaydet(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            ad=self.ui.txt_Ad.text()
            soyad=self.ui.txt_Soyad.text()
            tel=self.ui.txt_Tel.text()
            mail=self.ui.txt_Mail.text()
            boy=float(self.ui.txt_boy.text()) if self.ui.txt_boy.text() else None
            kilo=float(self.ui.txt_kilo.text()) if self.ui.txt_kilo.text() else None
            uyelik_tipi=self.ui.cmb_uyelik.currentData()
            cinsiyet=self.ui.cmb_cinsiyet.currentText()
            dogum_tarih=self.ui.date_dogum.date().toString("yyyy-MM-dd")
            kayit_qdate=self.ui.date_kayit.date()
            kayit_tarih=kayit_qdate.toString("yyyy-MM-dd")
            
            cursor.execute("select sureGun,fiyat from uyelik_tipleri where uyeliktipiID=?",(uyelik_tipi,))
            sonuc=cursor.fetchone()
            if sonuc:
                sureGun=sonuc[0]
                ucret=sonuc[1]

                bitis_qdate=kayit_qdate.addDays(sureGun)
                uyelik_bitis=bitis_qdate.toString("yyyy-MM-dd")
            else:
                QMessageBox.warning(self, "Hata", "Üyelik süresi bulunamadı")
                return

            if not ad or not soyad:
                QMessageBox.warning(self,"uyarı","ad ve soyad boş geçilemez")
                return
            if not boy or not kilo:
                QMessageBox.warning(self,"uyarı","boy ve kilo alanı boş bırakılamaz")
                return

            sorgu="insert into uyeler(ad,soyad,telefon,email,dogumTarihi,cinsiyet,kayitTarihi,uyelikTipiID,boy,kilo,uyelikBitisTarihi,toplamBorc) values (?,?,?,?,?,?,?,?,?,?,?,?)"
            cursor.execute(sorgu,(ad,soyad,tel,mail,dogum_tarih,cinsiyet,kayit_tarih,uyelik_tipi,boy,kilo,uyelik_bitis,ucret))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı",f"{ad},{soyad} başarıyla kaydedildi")
        except pyodbc.IntegrityError as e:
            if "2627" in str(e):
                QMessageBox.warning(self,"kayıt hatası","bu mail zaten kayıtlı")

        except Exception as e:
            print(f"hata:{e}")
    def uye_sil(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            secili_satir=self.ui.tbl_uyeler.currentRow()
            if secili_satir <0:
                QMessageBox.warning(self,"uyarı","lütfen silmek için bir üye seçin")
                return
            uye_id=self.ui.tbl_uyeler.item(secili_satir,0).text()

            cevap=QMessageBox.question(self,"onay",f"{uye_id} ID'li üyeyi silmek istediğinize eminmisiniz?",QMessageBox.Yes|QMessageBox.No)
            if cevap==QMessageBox.No:
                return
            cursor=conn.cursor()
            cursor.execute("delete from uyeler where uyeID=?",(uye_id))
            cursor.commit()
            conn.close()
            
            QMessageBox.information(self,"başarılı","üye silindi")

            self.uyeleri_listele()

        except Exception as e:
            print(f"hata:{e}")
    def temizle(self):
        try:
            self.ui.txt_Ad.clear()
            self.ui.txt_Soyad.clear()
            self.ui.txt_Tel.clear()
            self.ui.txt_Mail.clear()
            self.ui.txt_boy.clear()
            self.ui.txt_kilo.clear()
            self.ui.date_dogum.clear()
            self.ui.txt_uyelikBitis.clear()
            self.ui.plain_not.clear()
        except Exception as e:
            print(f"hata:{e}")

    def uye_guncelle(self):
        try:
           
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            if not  hasattr(self,"secili_uye_id"):
                QMessageBox.warning(self,"uyarı","lütfen güncellencek üyeyi seçiniz")
                return
            ad = self.ui.txt_Ad.text()
            soyad = self.ui.txt_Soyad.text()
            tel = self.ui.txt_Tel.text()
            mail = self.ui.txt_Mail.text()
            boy = self.ui.txt_boy.text()
            kilo = self.ui.txt_kilo.text()
            uyelik_tipi = self.ui.cmb_uyelik.currentIndex() + 1
            cinsiyet = self.ui.cmb_cinsiyet.currentText()
            saglik_notu = self.ui.plain_not.toPlainText()

            sorgu="update uyeler set ad=?,soyad=?,telefon=?,email=?,cinsiyet=?,uyelikTipiID=?,boy=?,kilo=?,saglik_notu=? where uyeID=?"
            cursor.execute(sorgu,(ad,soyad,tel,mail,cinsiyet,uyelik_tipi,boy,kilo,saglik_notu,self.secili_uye_id))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Başarılı", "Üye güncellendi.")
            self.uyeleri_listele()

        except Exception as e:
            print(f"hata:{e}")

    def uyeleri_listele(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select u.uyeID,u.ad,u.soyad,u.telefon,u.email,u.dogumTarihi,u.cinsiyet,u.kayitTarihi,ut.tipAdi,u.uyelikBitisTarihi,u.boy,u.kilo,u.saglik_notu,u.durum,u.toplamBorc from  uyeler u inner join uyelik_tipleri ut on u.uyelikTipiID=ut.uyelikTipiID")

            self.ui.tbl_uyeler.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_uyeler.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_uyeler.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def tablodan_Veri_cek(self,row,column):
        try:
            self.ui.txt_Ad.setText(self.ui.tbl_uyeler.item(row,1).text())
            self.ui.txt_Soyad.setText(self.ui.tbl_uyeler.item(row,2).text())
            self.ui.txt_Tel.setText(self.ui.tbl_uyeler.item(row,3).text())
            self.ui.txt_Mail.setText(self.ui.tbl_uyeler.item(row,4).text())
            tarih_str=self.ui.tbl_uyeler.item(row,5).text()
            self.ui.date_dogum.setDate(QDate.fromString(tarih_str,"yyyy-MM-dd"))
            cinsiyet=self.ui.tbl_uyeler.item(row,6).text()
            self.ui.cmb_cinsiyet.setCurrentText(cinsiyet)
            kayit_Tarih=self.ui.tbl_uyeler.item(row,7).text()
            self.ui.date_kayit.setDate(QDate.fromString(kayit_Tarih,"yyyy-MM-dd"))
            uyelik_tipi=self.ui.tbl_uyeler.item(row,8).text()
            self.ui.cmb_uyelik.setCurrentText(uyelik_tipi)
            self.ui.txt_uyelikBitis.setText(self.ui.tbl_uyeler.item(row,9).text())
            self.ui.txt_boy.setText(self.ui.tbl_uyeler.item(row,10).text())
            self.ui.txt_kilo.setText(self.ui.tbl_uyeler.item(row,11).text())
            self.ui.plain_not.setPlainText(self.ui.tbl_uyeler.item(row,12).text())
            self.secili_uye_id = self.ui.tbl_uyeler.item(row, 0).text()
        except Exception as e:
            print(f"hata:{e}")

    def uyelik_durum_guncelle(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()

            from datetime import datetime
            bugun=datetime.now().strftime("%Y-%m-%d")

            cursor.execute("update uyeler set durum='Pasif' where uyelikBitisTarihi<?",(bugun,))
            
            cursor.execute("update uyeler set durum='Aktif' where uyelikBitisTarihi>=?",(bugun,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def arka_plan_ayarla(self):
        # Görsel yolunun doğruluğundan emin olun
        resim_yolu = r"C:\Users\yigit\OneDrive\Belgeler\fitness\indir.png"
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = UyeEkrani()
    pencere.show()
    sys.exit(app.exec())
