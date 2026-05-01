# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dersler.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1315, 634)
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
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.txt_dersAdi = QLineEdit(self.groupBox)
        self.txt_dersAdi.setObjectName(u"txt_dersAdi")

        self.horizontalLayout_2.addWidget(self.txt_dersAdi)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cmb_Antrenor = QComboBox(self.groupBox)
        self.cmb_Antrenor.setObjectName(u"cmb_Antrenor")

        self.horizontalLayout_2.addWidget(self.cmb_Antrenor)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.time_baslangicSaat = QTimeEdit(self.groupBox)
        self.time_baslangicSaat.setObjectName(u"time_baslangicSaat")

        self.horizontalLayout_2.addWidget(self.time_baslangicSaat)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.time_bitisSaat = QTimeEdit(self.groupBox)
        self.time_bitisSaat.setObjectName(u"time_bitisSaat")

        self.horizontalLayout_2.addWidget(self.time_bitisSaat)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.txt_kontenjan = QLineEdit(self.groupBox)
        self.txt_kontenjan.setObjectName(u"txt_kontenjan")

        self.horizontalLayout_2.addWidget(self.txt_kontenjan)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.txt_gun = QLineEdit(self.groupBox)
        self.txt_gun.setObjectName(u"txt_gun")

        self.horizontalLayout_2.addWidget(self.txt_gun)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_bilgiGetir = QPushButton(self.groupBox)
        self.btn_bilgiGetir.setObjectName(u"btn_bilgiGetir")

        self.horizontalLayout.addWidget(self.btn_bilgiGetir)

        self.btn_Kaydet = QPushButton(self.groupBox)
        self.btn_Kaydet.setObjectName(u"btn_Kaydet")

        self.horizontalLayout.addWidget(self.btn_Kaydet)

        self.btn_guncelle = QPushButton(self.groupBox)
        self.btn_guncelle.setObjectName(u"btn_guncelle")

        self.horizontalLayout.addWidget(self.btn_guncelle)

        self.btn_sil = QPushButton(self.groupBox)
        self.btn_sil.setObjectName(u"btn_sil")

        self.horizontalLayout.addWidget(self.btn_sil)

        self.btn_temizle = QPushButton(self.groupBox)
        self.btn_temizle.setObjectName(u"btn_temizle")

        self.horizontalLayout.addWidget(self.btn_temizle)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tbl_dersListesi = QTableWidget(self.groupBox_2)
        if (self.tbl_dersListesi.columnCount() < 7):
            self.tbl_dersListesi.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_dersListesi.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tbl_dersListesi.setObjectName(u"tbl_dersListesi")

        self.gridLayout_3.addWidget(self.tbl_dersListesi, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tbl_dersekayitliUyeler = QTableWidget(self.groupBox_3)
        if (self.tbl_dersekayitliUyeler.columnCount() < 4):
            self.tbl_dersekayitliUyeler.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_dersekayitliUyeler.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_dersekayitliUyeler.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_dersekayitliUyeler.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_dersekayitliUyeler.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tbl_dersekayitliUyeler.setObjectName(u"tbl_dersekayitliUyeler")

        self.gridLayout_2.addWidget(self.tbl_dersekayitliUyeler, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 58, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1315, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dersler", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ders \u0130\u015flemleri", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ders Ad\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Antren\u00f6rler:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flang\u0131\u00e7 Saati:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Biti\u015f Saati:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kontenjan:", None))
        self.txt_kontenjan.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"G\u00fcn:", None))
        self.txt_gun.setText("")
        self.btn_bilgiGetir.setText(QCoreApplication.translate("MainWindow", u"Bilgi Getir", None))
        self.btn_Kaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ders Listesi", None))
        ___qtablewidgetitem = self.tbl_dersListesi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ders Id", None));
        ___qtablewidgetitem1 = self.tbl_dersListesi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ders Ad\u0131", None));
        ___qtablewidgetitem2 = self.tbl_dersListesi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Antren\u00f6r Ad\u0131", None));
        ___qtablewidgetitem3 = self.tbl_dersListesi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kontenjan", None));
        ___qtablewidgetitem4 = self.tbl_dersListesi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flang\u0131\u00e7 Saati", None));
        ___qtablewidgetitem5 = self.tbl_dersListesi.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Biti\u015f Saati", None));
        ___qtablewidgetitem6 = self.tbl_dersListesi.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"G\u00fcn", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Derse Kay\u0131tl\u0131 \u00dcyeler", None))
        ___qtablewidgetitem7 = self.tbl_dersekayitliUyeler.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Ad", None));
        ___qtablewidgetitem8 = self.tbl_dersekayitliUyeler.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Soyad", None));
        ___qtablewidgetitem9 = self.tbl_dersekayitliUyeler.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem10 = self.tbl_dersekayitliUyeler.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Biti\u015f Tarihi", None));
    # retranslateUi

