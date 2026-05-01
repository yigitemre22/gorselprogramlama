from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,QDate,Qt,Qt
import pyodbc
import sys
import os
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon

from ui_ekipmanlar import Ui_MainWindow  # class adı değişebilir

class EkipmanEkrani(QMainWindow):
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

        self.label_veri()
        self.kategori_getir()
        self.ekipmanlari_getir()
        self.ui.tblEkipman.cellClicked.connect(self.tablodan_Veri_al)
        self.ui.btnKaydet.clicked.connect(self.ekipman_kaydet)
        self.ui.btn_guncelle.clicked.connect(self.ekipman_guncelle)
        self.ui.btn_sil.clicked.connect(self.ekipman_sil)
        self.ui.btn_listele.clicked.connect(self.ekipmanlari_getir)
        self.ui.btn_temizle.clicked.connect(self.temizle)
        
        # Ana layout'un tüm boşluğu kaplaması ve içeriği ortalaması için
        

    def ekipmanlari_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select e.ekipmanID,e.ekipmanAdi,e.alimTarihi,e.durum,et.turAdi from ekipmanlar e inner join ekipman_turleri et on e.kategori=et.ekipmanTuruID")

            self.ui.tblEkipman.setRowCount(0)

            for row_index,row_data in enumerate(cursor.fetchall()):
                self.ui.tblEkipman.insertRow(row_index)
                for col_index,data in enumerate (row_data):
                    self.ui.tblEkipman.setItem(row_index,col_index,QTableWidgetItem(str(data)))
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def tablodan_Veri_al(self,row,column):
        try:
            self.ui.txt_ekipmanAd.setText(self.ui.tblEkipman.item(row,1).text())
            alinma_tarih=self.ui.tblEkipman.item(row,2).text()
            self.ui.date_alinmaTarih.setDate(QDate.fromString(alinma_tarih,"yyyy-MM-dd"))
            durum=self.ui.tblEkipman.item(row,3).text()
            self.ui.cmb_durum.setCurrentText(durum)
            kategori=self.ui.tblEkipman.item(row,4).text()
            self.ui.cmb_kategori.setCurrentText(kategori)
            self.secili_ekipman_id=self.ui.tblEkipman.item(row,0).text()
        except Exception as e:
            print(f"hata:{e}")
    
    def kategori_getir(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            cursor.execute("select ekipmanTuruID,turAdi from ekipman_turleri")
            self.ui.cmb_kategori.clear()

            rows=cursor.fetchall()
            if not rows:
                print("veritabanında kategori bulunamadı")
            for row in rows:
                self.ui.cmb_kategori.addItem(row[1],row[0])
            conn.close()
        except Exception as e:
            print(f"hata{e}")

    def label_veri(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            sorgu="select count(*),count(DISTINCT kategori),sum(case when durum='Aktif' then 1 else 0 end),sum(case when durum='Arızalı' then 1 else 0 end),sum(case when durum='Bakımda' then 1 else 0 end)from ekipmanlar"
            cursor.execute(sorgu)
            sonuc=cursor.fetchone()
            if sonuc: 
                self.ui.lbl_toplamekipman.setText(str(sonuc[0] or 0)) 
                self.ui.lbl_ekipmanTuru.setText(str(sonuc[1] or 0)) 
                self.ui.lbl_aktifekipman.setText(str(sonuc[2] or 0)) 
                self.ui.lbl_arizaliekipman.setText(str(sonuc[3] or 0)) 
                self.ui.lbl_bakimdaekipman.setText(str(sonuc[4] or 0))
        
            conn.close()
        except Exception as e:
            print(f"hata:{e}")

    def ekipman_kaydet(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            ad=self.ui.txt_ekipmanAd.text()
            kategori=self.ui.cmb_kategori.currentData()
            durum=self.ui.cmb_durum.currentText()
            alim_tarih=self.ui.date_alinmaTarih.date().toString("yyyy-MM-dd")

            sorgu="insert into ekipmanlar(ekipmanAdi,alimTarihi,durum,kategori) values(?,?,?,?)"
            cursor.execute(sorgu,(ad,alim_tarih,durum,kategori))
            conn.commit()
            conn.close()
            QMessageBox.information(self,"başarılı","ekipman başarıyla kaydedildi")
        except Exception as e:
            print(f"hata{e}")

    def ekipman_guncelle(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            cursor=conn.cursor()
            if not hasattr(self,"secili_ekipman_id"):
                QMessageBox.warning(self,"uyarı",)
                return
            ad=self.ui.txt_ekipmanAd.text()
            kategori=self.ui.cmb_kategori.currentData()
            durum=self.ui.cmb_durum.currentText()
            alim_tarih=self.ui.date_alinmaTarih.date().toString("yyyy-MM-dd")
            
            sorgu="update ekipmanlar set ekipmanAdi=?,alimTarihi=?,durum=?,kategori=? where ekipmanID=?"
            cursor.execute(sorgu,(ad,alim_tarih,durum,kategori,self.secili_ekipman_id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"hata{e}")

    def ekipman_sil(self):
        try:
            conn=pyodbc.connect(self.conn_str)
            secili_satir=self.ui.tblEkipman.currentRow()
            if secili_satir <0:
                    QMessageBox.warning(self,"uyarı","lütfen silmek için bir ekipman seçin")
                    return
            ekipman_id=self.ui.tblEkipman.item(secili_satir,0).text()

            cevap=QMessageBox.question(self,"onay",f"{ekipman_id} ID'li üyeyi silmek istediğinize eminmisiniz?",QMessageBox.Yes|QMessageBox.No)
            if cevap==QMessageBox.No:
                    return
            cursor=conn.cursor()
            cursor.execute("delete from ekipmanlar where ekipmanID=?",(ekipman_id))
            cursor.commit()
            conn.close()
                
            QMessageBox.information(self,"başarılı","ekipman silindi")

            self.ekipmanlari_getir()

        except Exception as e:
            print(f"hata:{e}")

    def temizle(self):
        try:
            self.ui.txt_ekipmanAd.clear()
            self.ui.date_alinmaTarih.clear()
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
    pencere = EkipmanEkrani()
    pencere.show()
    sys.exit(app.exec())