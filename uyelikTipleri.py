from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,QDate, Qt
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os
from ui_uyelikTipleri import Ui_MainWindow  # class adı değişebilir

class UyelikTipleriEkrani(QMainWindow):
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
        self.ui.tbl_uyelikler.cellClicked.connect(self.tablodan_Veri_cek)
        self.uyelikleri_getir()
        self.istatistikler()
        self.ui.btn_kaydet.clicked.connect(self.uyelik_kaydet)
        self.ui.btn_guncelle.clicked.connect(self.uyelik_guncelle)
        self.ui.btn_sil.clicked.connect(self.uyelik_sil)
        self.ui.btn_temizle.clicked.connect(self.temizle)
    
    def uyelikleri_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select * from uyelik_tipleri")

            self.ui.tbl_uyelikler.setRowCount(0)
            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tbl_uyelikler.insertRow(row_index)
                for col_index,data in enumerate(row_data):
                    self.ui.tbl_uyelikler.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def tablodan_Veri_cek(self,row,column):
        try:
            self.ui.lbl_tipAdi.setText(self.ui.tbl_uyelikler.item(row,1).text())
            self.ui.lbl_fiyat_2.setText(self.ui.tbl_uyelikler.item(row,2).text())
            self.ui.lbl_fiyat.setText(self.ui.tbl_uyelikler.item(row,3).text())
            self.secili_uyelik_id=self.ui.tbl_uyelikler.item(row,0).text()
        except Exception as e:
            print(f"hata{e}")

    def istatistikler(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            cursor = conn.cursor()
        
        # Sorguda 'GunlukUye' ve 'FROM' arasına boşluk eklendi
            sorgu = """
                SELECT 
                    SUM(CASE WHEN ut.tipAdi = 'Aylık' THEN 1 ELSE 0 END) AS AylikUye,
                    SUM(CASE WHEN ut.tipAdi = 'Yıllık' THEN 1 ELSE 0 END) AS YillikUye,
                    SUM(CASE WHEN ut.tipAdi = 'Haftalık' THEN 1 ELSE 0 END) AS HaftalikUye,
                    SUM(CASE WHEN ut.tipAdi = 'Günlük' THEN 1 ELSE 0 END) AS GunlukUye
                FROM uyeler u 
                JOIN uyelik_tipleri ut ON u.uyelikTipiID = ut.uyeliktipiID;
            """
            cursor.execute(sorgu)
            sonuc = cursor.fetchone()
        
            if sonuc: 
                # .setText() metodunu eklemeyi unutma!
                # 'or 0' kullanımı veritabanı boşsa (None gelirse) hatayı engeller.
                self.ui.label_5.setText(str(sonuc[0] or 0)) 
                self.ui.label_7.setText(str(sonuc[1] or 0)) 
                self.ui.label_9.setText(str(sonuc[2] or 0)) 
                self.ui.label_11.setText(str(sonuc[3] or 0))
            
        except Exception as e:
            print(f"Veri çekme hatası: {e}")

    def uyelik_kaydet(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            ad=self.ui.lbl_tipAdi.text()
            sure=self.ui.lbl_fiyat_2.text()
            fiyat=self.ui.lbl_fiyat.text()
           
            sorgu="insert into uyelik_tipleri(tipAdi,sureGun,fiyat) values(?,?,?)"
            cursor.execute(sorgu,(ad,sure,fiyat))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı","üyelik başarıyla kaydedildi")
        except Exception as e:
            print(f"hata{e}")
    def uyelik_guncelle(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            if not hasattr(self,"secili_uyelik_id"):
                QMessageBox.warning(self,"uyarı",)
                return
            ad=self.ui.lbl_tipAdi.text()
            sure=self.ui.lbl_fiyat_2.text()
            fiyat=self.ui.lbl_fiyat.text()
       
            sorgu="update uyelik_tipleri set tipAdi=?,sureGun=?,fiyat=? where uyeliktipiID=?"
            cursor.execute(sorgu,(ad,sure,fiyat,self.secili_uyelik_id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"hata{e}")
    
    def uyelik_sil(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            secili_satir=self.ui.tbl_uyelikler.currentRow()
            if secili_satir <0:
                    QMessageBox.warning(self,"uyarı","lütfen silmek için bir üyelik seçin")
                    return
            uyelik_id=self.ui.tbl_uyelikler.item(secili_satir,0).text()

            cevap=QMessageBox.question(self,"onay",f"{uyelik_id} ID'li üyeyi silmek istediğinize eminmisiniz?",QMessageBox.Yes|QMessageBox.No)
            if cevap==QMessageBox.No:
                    return
            cursor=conn.cursor()
            cursor.execute("delete from uyelik_tipleri where uyeliktipiID=?",(uyelik_id))
            cursor.commit()
            conn.close()
                
            QMessageBox.information(self,"başarılı","üyelik silindi")

            self.uyelikleri_getir()

        except Exception as e:
            print(f"hata:{e}")

    def temizle(self):
        try:
            self.ui.lbl_fiyat.clear()
            self.ui.lbl_fiyat_2.clear()
            self.ui.lbl_tipAdi.clear()
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
    pencere = UyelikTipleriEkrani()
    pencere.show()
    sys.exit(app.exec())
