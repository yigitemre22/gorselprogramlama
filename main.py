import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMessageBox
from login import Login

def veritabani_kontrol():
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=.\\SQLEXPRESS05;" # Nokta bu makineyi, SQLEXPRESS05 servisi temsil eder
        "Database=spor_salonu;"
        "Trusted_Connection=yes;"
    )
    try:
        conn = pyodbc.connect(conn_str, timeout=3)
        conn.close()
        return True
    except Exception as e:
        print(f"KRİTİK HATA: {e}")
        return False

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if veritabani_kontrol():
        pencere = Login()
        pencere.show()
        sys.exit(app.exec())
    else:
        QMessageBox.critical(None, "Sistem Hatası",
                             "SQLEXPRESS05 servisine bağlanılamadı!\n\n"
                             "Lütfen veritabanı adının 'spor_salonu' olduğundan emin olun.")
        sys.exit()
