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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 640)
        MainWindow.setStyleSheet(u"QFrame, QGroupBox {\n"
"    background-color: rgba(20, 24, 35, 150); /* Yar\u0131 \u015feffaf koyu lacivert */\n"
"    border: 1px solid rgba(255, 255, 255, 15);\n"
"    border-radius: 15px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"/* Ba\u015fl\u0131k Yaz\u0131lar\u0131 */\n"
"QLabel {\n"
"    color: #E0E6ED;\n"
"    font-weight: 600;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Modern Input Alanlar\u0131 */\n"
"QLineEdit, QDateTimeEdit, QComboBox {\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"    border: 1px solid rgba(79, 209, 197, 50); /* Hafif turkuaz kenarl\u0131k */\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4FD1C5;\n"
"    background-color: rgba(0, 0, 0, 150);\n"
"}\n"
"\n"
"/* Tablo Tasar\u0131m\u0131 (Transparan ve Temiz) */\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    alternate-background-color: rgba(255, 255, 255, 5);\n"
"    border: none;\n"
"    gridline-color: rgba(255, 255, 25"
                        "5, 10);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(30, 41, 59, 180);\n"
"    color: #4FD1C5;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"/* Ana Aksiyon Butonu (\u00d6deme Al) */\n"
"QPushButton#btn_odeme_al {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4FD1C5, stop:1 #2C7A7B);\n"
"    color: #0F172A;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;\n"
"    padding: 12px;\n"
"}\n"
"\n"
"QPushButton#btn_odeme_al:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #64FFDA, stop:1 #4FD1C5);\n"
"}\n"
"\n"
"/* \u0130kincil Buton (Ara) */\n"
"QPushButton#btn_ara {\n"
"    background-color: rgba(79, 209, 197, 30);\n"
"    border: 1px solid #4FD1C5;\n"
"    color: #4FD1C5;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btn_ara:hover {\n"
"    background-color: #4FD1C5;\n"
"    color: #0F172A;\n"
"}\n"
"\n"
"/* Scrollbar (Zarif ve \u0130"
                        "nce) */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(79, 209, 197, 80);\n"
"    border-radius: 2px;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"QGroupBox {\n"
"    background-color: transparent; /* \u0130\u00e7indeki siyahl\u0131\u011f\u0131 tamamen kald\u0131r\u0131r */\n"
"    border: 1px solid rgba(255, 255, 255, 30); /* \u0130nce beyaz\u0131ms\u0131 bir \u00e7er\u00e7eve */\n"
"    border-radius: 15px;\n"
"    margin-top: 20px; /* Ba\u015fl\u0131k yaz\u0131s\u0131n\u0131n yerle\u015fmesi i\u00e7in */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 10px;\n"
"    color: #4FD1C5; /* Ba\u015fl\u0131k rengi (Turkuaz) */\n"
"    font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tblEkipman = QTableWidget(self.groupBox)
        if (self.tblEkipman.columnCount() < 5):
            self.tblEkipman.setColumnCount(5)
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
        self.tblEkipman.setObjectName(u"tblEkipman")

        self.gridLayout_2.addWidget(self.tblEkipman, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_ekipmanAd = QLineEdit(self.groupBox_2)
        self.txt_ekipmanAd.setObjectName(u"txt_ekipmanAd")
        self.txt_ekipmanAd.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.txt_ekipmanAd)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.cmb_kategori = QComboBox(self.groupBox_2)
        self.cmb_kategori.setObjectName(u"cmb_kategori")

        self.horizontalLayout.addWidget(self.cmb_kategori)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.cmb_durum = QComboBox(self.groupBox_2)
        self.cmb_durum.addItem("")
        self.cmb_durum.addItem("")
        self.cmb_durum.addItem("")
        self.cmb_durum.setObjectName(u"cmb_durum")

        self.horizontalLayout.addWidget(self.cmb_durum)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.date_alinmaTarih = QDateEdit(self.groupBox_2)
        self.date_alinmaTarih.setObjectName(u"date_alinmaTarih")

        self.horizontalLayout.addWidget(self.date_alinmaTarih)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnKaydet = QPushButton(self.groupBox_2)
        self.btnKaydet.setObjectName(u"btnKaydet")

        self.horizontalLayout_2.addWidget(self.btnKaydet)

        self.btn_guncelle = QPushButton(self.groupBox_2)
        self.btn_guncelle.setObjectName(u"btn_guncelle")

        self.horizontalLayout_2.addWidget(self.btn_guncelle)

        self.btn_sil = QPushButton(self.groupBox_2)
        self.btn_sil.setObjectName(u"btn_sil")

        self.horizontalLayout_2.addWidget(self.btn_sil)

        self.btn_listele = QPushButton(self.groupBox_2)
        self.btn_listele.setObjectName(u"btn_listele")

        self.horizontalLayout_2.addWidget(self.btn_listele)

        self.btn_temizle = QPushButton(self.groupBox_2)
        self.btn_temizle.setObjectName(u"btn_temizle")

        self.horizontalLayout_2.addWidget(self.btn_temizle)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lbl_toplamekipman = QLabel(self.groupBox_3)
        self.lbl_toplamekipman.setObjectName(u"lbl_toplamekipman")

        self.horizontalLayout_4.addWidget(self.lbl_toplamekipman)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.lbl_ekipmanTuru = QLabel(self.groupBox_3)
        self.lbl_ekipmanTuru.setObjectName(u"lbl_ekipmanTuru")

        self.horizontalLayout_4.addWidget(self.lbl_ekipmanTuru)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.lbl_arizaliekipman = QLabel(self.groupBox_3)
        self.lbl_arizaliekipman.setObjectName(u"lbl_arizaliekipman")

        self.horizontalLayout_4.addWidget(self.lbl_arizaliekipman)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.lbl_aktifekipman = QLabel(self.groupBox_3)
        self.lbl_aktifekipman.setObjectName(u"lbl_aktifekipman")

        self.horizontalLayout_3.addWidget(self.lbl_aktifekipman)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.lbl_bakimdaekipman = QLabel(self.groupBox_3)
        self.lbl_bakimdaekipman.setObjectName(u"lbl_bakimdaekipman")

        self.horizontalLayout_3.addWidget(self.lbl_bakimdaekipman)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1047, 25))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ekipman \u0130\u015flemleri", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ekipman Ad\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kategori:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Durum:", None))
        self.cmb_durum.setItemText(0, QCoreApplication.translate("MainWindow", u"Ar\u0131zal\u0131", None))
        self.cmb_durum.setItemText(1, QCoreApplication.translate("MainWindow", u"Aktif", None))
        self.cmb_durum.setItemText(2, QCoreApplication.translate("MainWindow", u"Bak\u0131mda", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Al\u0131m Tarihi:", None))
        self.btnKaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_listele.setText(QCoreApplication.translate("MainWindow", u"Listele", None))
        self.btn_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Detay", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Toplam Ekipman Say\u0131s\u0131:", None))
        self.lbl_toplamekipman.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Toplam Ekipman T\u00fcr\u00fc:", None))
        self.lbl_ekipmanTuru.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Ar\u0131zal\u0131 Ekipman Say\u0131s\u0131:", None))
        self.lbl_arizaliekipman.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Aktif Ekipman Say\u0131s\u0131:", None))
        self.lbl_aktifekipman.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bak\u0131mdaki Ekipman Say\u0131s\u0131:", None))
        self.lbl_bakimdaekipman.setText(QCoreApplication.translate("MainWindow", u"Null", None))
    # retranslateUi

