from PySide6.QtWidgets import QMainWindow,QTableWidgetItem,QApplication,QTimeEdit,QMessageBox
from PySide6.QtCore import QTime,Qt
from ui_Antrenor_Ekran import Ui_MainWindow  # class adı değişebilir
import pyodbc
import sys
from PySide6.QtGui import QPixmap, QPalette, QBrush,QIcon
import os

# uyeEkran.py dosyanın başı şu şekilde olmalı:
class antrenor_ekran(QMainWindow): # veya QWidget
    def __init__(self): # uye_id parametresini buraya ekledik!
        super().__init__()
        self.ui = Ui_MainWindow() # Kendi UI sınıf adın neyse
        self.ui.setupUi(self)
        
      
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = antrenor_ekran()
    pencere.show()
    sys.exit(app.exec())
