# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ekipmanlar.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 470)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 851, 121))
        self.tblEkipman = QTableWidget(self.groupBox)
        if (self.tblEkipman.columnCount() < 6):
            self.tblEkipman.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblEkipman.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tblEkipman.setObjectName(u"tblEkipman")
        self.tblEkipman.setGeometry(QRect(10, 30, 831, 81))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 841, 151))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 100, 821, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnKaydet = QPushButton(self.layoutWidget)
        self.btnKaydet.setObjectName(u"btnKaydet")

        self.horizontalLayout_2.addWidget(self.btnKaydet)

        self.btn_guncelle = QPushButton(self.layoutWidget)
        self.btn_guncelle.setObjectName(u"btn_guncelle")

        self.horizontalLayout_2.addWidget(self.btn_guncelle)

        self.btn_sil = QPushButton(self.layoutWidget)
        self.btn_sil.setObjectName(u"btn_sil")

        self.horizontalLayout_2.addWidget(self.btn_sil)

        self.btn_listele = QPushButton(self.layoutWidget)
        self.btn_listele.setObjectName(u"btn_listele")

        self.horizontalLayout_2.addWidget(self.btn_listele)

        self.btn_temizle = QPushButton(self.layoutWidget)
        self.btn_temizle.setObjectName(u"btn_temizle")

        self.horizontalLayout_2.addWidget(self.btn_temizle)

        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 40, 810, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_ekipmanAd = QLineEdit(self.layoutWidget1)
        self.txt_ekipmanAd.setObjectName(u"txt_ekipmanAd")

        self.horizontalLayout.addWidget(self.txt_ekipmanAd)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.cmb_kategori = QComboBox(self.layoutWidget1)
        self.cmb_kategori.setObjectName(u"cmb_kategori")

        self.horizontalLayout.addWidget(self.cmb_kategori)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.box_adet = QSpinBox(self.layoutWidget1)
        self.box_adet.setObjectName(u"box_adet")

        self.horizontalLayout.addWidget(self.box_adet)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.cmb_durum = QComboBox(self.layoutWidget1)
        self.cmb_durum.addItem("")
        self.cmb_durum.addItem("")
        self.cmb_durum.addItem("")
        self.cmb_durum.setObjectName(u"cmb_durum")

        self.horizontalLayout.addWidget(self.cmb_durum)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.date_alinmaTarih = QDateEdit(self.layoutWidget1)
        self.date_alinmaTarih.setObjectName(u"date_alinmaTarih")

        self.horizontalLayout.addWidget(self.date_alinmaTarih)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 290, 841, 121))
        self.layoutWidget2 = QWidget(self.groupBox_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 80, 571, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_16 = QLabel(self.layoutWidget2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.layoutWidget3 = QWidget(self.groupBox_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 40, 821, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ekipmanlar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ekipmanlar", None))
        ___qtablewidgetitem = self.tblEkipman.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ekipmanID", None));
        ___qtablewidgetitem1 = self.tblEkipman.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ekipmanAdi", None));
        ___qtablewidgetitem2 = self.tblEkipman.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"alimTarihi", None));
        ___qtablewidgetitem3 = self.tblEkipman.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"durum", None));
        ___qtablewidgetitem4 = self.tblEkipman.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"kategori", None));
        ___qtablewidgetitem5 = self.tblEkipman.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"adet", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ekipman \u0130\u015flemleri", None))
        self.btnKaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_listele.setText(QCoreApplication.translate("MainWindow", u"Listele", None))
        self.btn_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ekipman Ad\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kategori:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Adet:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Durum:", None))
        self.cmb_durum.setItemText(0, QCoreApplication.translate("MainWindow", u"Ar\u0131zal\u0131", None))
        self.cmb_durum.setItemText(1, QCoreApplication.translate("MainWindow", u"Aktif", None))
        self.cmb_durum.setItemText(2, QCoreApplication.translate("MainWindow", u"Bak\u0131mda", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Al\u0131m Tarihi:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Detay", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Aktif Ekipman Say\u0131s\u0131:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bak\u0131mdaki Ekipman Say\u0131s\u0131:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Toplam Ekipman Say\u0131s\u0131:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Toplam Ekipman T\u00fcr\u00fc:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ar\u0131zal\u0131 Ekipman Say\u0131s\u0131:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Null", None))
    # retranslateUi

