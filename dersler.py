from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,Qt
from ui_dersler import Ui_MainWindow  # class adı değişebilir
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os
class DersEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)# # This Python file uses the following encoding: utf-8
        self.conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=.\SQLEXPRESS05;' 
        r'DATABASE=spor_salonu;'
        r'Trusted_Connection=yes;'
        )     
        self.antrenor_getir()
        self.ui.btn_bilgiGetir.clicked.connect(self.derse_kayıtlı_uyeler)
        self.ders_listesi_getir()
        self.ui.tbl_dersListesi.clicked.connect(self.tablodan_veri_cek)
        self.ui.btn_temizle.clicked.connect(self.temizle)
        self.ui.btn_Kaydet.clicked.connect(self.ders_ekle)
        self.ui.btn_guncelle.clicked.connect(self.ders_guncelle)
        self.ui.btn_sil.clicked.connect(self.ders_sil)
        
    def ders_listesi_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select d.dersID,d.dersAdi,at.antrenor_Adi,d.kapasite,d.baslangic_saati,d.bitis_saati,d.gun from dersler d inner join antrenorler at on d.antrenorId=at.antrenor_id")

            self.ui.tbl_dersListesi.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_dersListesi.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_dersListesi.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"{e}")

    def tablodan_veri_cek(self,index):
        try:
            row=index.row()
            self.ui.txt_dersAdi.setText(self.ui.tbl_dersListesi.item(row,1).text())
            antrenor=self.ui.tbl_dersListesi.item(row,2).text()
            self.ui.cmb_Antrenor.setCurrentText(antrenor)
            self.ui.txt_kontenjan.setText(self.ui.tbl_dersListesi.item(row,3).text())
            self.ui.txt_gun.setText(self.ui.tbl_dersListesi.item(row,6).text())
            baslangic_Saati=self.ui.tbl_dersListesi.item(row,4).text()
            time_Str=baslangic_Saati.split(":")
            h=int(time_Str[0])
            m=int(time_Str[1])
            s=int(float(time_Str[2]))
            self.ui.time_baslangicSaat.setTime(QTime(h,m,s))
            bitis_saati=self.ui.tbl_dersListesi.item(row,5).text()
            time_str_2=bitis_saati.split(":")
            h_1=int(time_str_2[0])
            m_1=int(time_str_2[1])
            s_1=int(float(time_str_2[2]))
            self.ui.time_bitisSaat.setTime(QTime(h_1,m_1,s_1))
            self.secili_ders_id=self.ui.tbl_dersListesi.item(row,0).text()

        
        except Exception as e:
            print(f"hata:{e}")

    def antrenor_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select antrenor_id,antrenor_Adi from antrenorler")
            self.ui.cmb_Antrenor.clear()

            rows=cursor.fetchall()
            if not rows:
                print("veritabanında antrenör bulunamadı")
            for row in rows:
                self.ui.cmb_Antrenor.addItem(row[1],row[0])
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def derse_kayıtlı_uyeler(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select u.uyeID,u.ad,u.soyad,u.telefon,u.uyelikBitisTarihi from uyeler u inner join uyeDers ud on u.uyeID=ud.uyeID where dersID=?",(self.secili_ders_id,))

            self.ui.tbl_dersekayitliUyeler.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_dersekayitliUyeler.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_dersekayitliUyeler.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def temizle(self):
        self.ui.txt_dersAdi.clear()
        self.ui.txt_gun.clear()
        self.ui.txt_kontenjan.clear()
        self.ui.time_baslangicSaat.clear()
        self.ui.time_bitisSaat.clear()

    def ders_ekle(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            ders_adi=self.ui.txt_dersAdi.text()
            antrenor=self.ui.cmb_Antrenor.currentData()
            kontenjan=self.ui.txt_kontenjan.text()
            gun=self.ui.txt_gun.text()
            baslangic_saat=self.ui.time_baslangicSaat.text()
            bitis_saat=self.ui.time_bitisSaat.text()

            sorgu="insert into dersler(dersAdi,antrenorId,kapasite,baslangic_saati,bitis_saati,gun) values (?,?,?,?,?,?)"
            cursor.execute(sorgu,(ders_adi,antrenor,kontenjan,baslangic_saat,bitis_saat,gun))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı",f"{ders_adi} adlı ders başarıyla eklendi")
            self.ders_listesi_getir()
        except Exception as e:
            print(f"hata:{e}")

    def ders_guncelle(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()

            if not hasattr (self,"secili_ders_id"):
                QMessageBox.warning(self,"uyarı","lütfen güncellenecek dersi seçin")
            ders_adi=self.ui.txt_dersAdi.text()
            antrenor=self.ui.cmb_Antrenor.currentData()
            kontenjan=self.ui.txt_kontenjan.text()
            gun=self.ui.txt_gun.text()
            baslangic_saat=self.ui.time_baslangicSaat.text()
            bitis_saat=self.ui.time_bitisSaat.text()
            sorgu="update dersler set dersAdi=?,antrenorId=?,kapasite=?,baslangic_saati=?,bitis_saati=?,gun=? where dersID=?"
            cursor.execute(sorgu,(ders_adi,antrenor,kontenjan,baslangic_saat,bitis_saat,gun,self.secili_ders_id))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı",f"{ders_adi} adlı dersin bilgileri basarıyla guncellendi")
            self.ders_listesi_getir()
        except Exception as e:
            print(f"hata:{e}")

    def ders_sil(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()

            secili_satir=self.ui.tbl_dersListesi.currentRow()
            if secili_satir<0:
                QMessageBox.warning(self,"uyarı","lütfen silmek istediğiniz dersi seçin")
                return
            cevap=QMessageBox.question(self,"onay",f"{self.secili_ders_id} ID'li dersi silmek istediğinize eminmisiniz?",QMessageBox.Yes|QMessageBox.No)
            if cevap==QMessageBox.No:
                return
            cursor.execute("delete from dersler where dersID=?",(self.secili_ders_id))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı","ders silindi")
            self.ders_listesi_getir()
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

    # Pencere boyutu değişirse arka planın yeniden ölçeklenmesi için:
    def resizeEvent(self, event):
        self.arka_plan_ayarla()
        super().resizeEvent(event)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = DersEkrani()
    pencere.show()
    sys.exit(app.exec())
