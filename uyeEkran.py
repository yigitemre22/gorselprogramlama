from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,Qt
from ui_uyeEkran import Ui_MainWindow  # class adı değişebilir
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os

# uyeEkran.py dosyanın başı şu şekilde olmalı:
class uye_ekran(QMainWindow): # veya QWidget
    def __init__(self, uye_id): # uye_id parametresini buraya ekledik!
        super().__init__()
        self.ui = Ui_MainWindow() # Kendi UI sınıf adın neyse
        self.ui.setupUi(self)
        
        self.kullanici_id = uye_id # Bu ID'yi ileride SQL sorguları için kullanacağız
        print(f"Üye ekranı ID {self.kullanici_id} için hazırlandı.")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = uye_ekran()
    pencere.show()
    sys.exit(app.exec())
