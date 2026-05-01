# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uyeler.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 738)
        MainWindow.setStyleSheet(u"/* GENEL PENCERE */\n"
"QWidget {\n"
"    background: transparent; /* Her \u015feyin arkas\u0131n\u0131 bo\u015falt\u0131r */\n"
"    color: white;\n"
"}\n"
"\n"
"/* GRUP KUTULARI (Cam Efekti) */\n"
"QGroupBox {\n"
"    background-color: rgba(20, 20, 20, 80); /* \u015eeffafl\u0131\u011f\u0131 art\u0131rd\u0131k (80/255) */\n"
"    border: 1px solid rgba(255, 255, 255, 40); /* \u0130nce beyaz cam s\u0131n\u0131r\u0131 */\n"
"    border-radius: 15px;\n"
"    margin-top: 20px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* BUTONLAR (Neon ve \u015eeffaf) */\n"
"QPushButton {\n"
"    background-color: rgba(0, 170, 255, 150); /* Yar\u0131 \u015feffaf mavi */\n"
"    border: 1px solid #00AAFF;\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 170, 255, 200); /* \u00dcst\u00fcne gelince belirginle\u015fir */\n"
"}\n"
"\n"
"/* G\u0130R\u0130\u015e ALANLARI */\n"
"QLineEdit, QComboBox, QSpinBox {\n"
"    b"
                        "ackground-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"/* TABLO */\n"
"QTableWidget {\n"
"    background-color: rgba(0, 0, 0, 60);\n"
"    gridline-color: rgba(255, 255, 255, 20);\n"
"    border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 300))
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cmb_uyelik = QComboBox(self.groupBox_2)
        self.cmb_uyelik.setObjectName(u"cmb_uyelik")

        self.gridLayout_4.addWidget(self.cmb_uyelik, 1, 1, 1, 1)

        self.txt_uyelikBitis = QLineEdit(self.groupBox_2)
        self.txt_uyelikBitis.setObjectName(u"txt_uyelikBitis")

        self.gridLayout_4.addWidget(self.txt_uyelikBitis, 2, 1, 1, 1)

        self.date_kayit = QDateEdit(self.groupBox_2)
        self.date_kayit.setObjectName(u"date_kayit")

        self.gridLayout_4.addWidget(self.date_kayit, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 3, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 100))
        self.groupBox_4.setMaximumSize(QSize(16777215, 75))
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_kaydet = QPushButton(self.groupBox_4)
        self.btn_kaydet.setObjectName(u"btn_kaydet")

        self.horizontalLayout.addWidget(self.btn_kaydet)

        self.btn_bilgiGetir = QPushButton(self.groupBox_4)
        self.btn_bilgiGetir.setObjectName(u"btn_bilgiGetir")

        self.horizontalLayout.addWidget(self.btn_bilgiGetir)

        self.btn_Guncelle = QPushButton(self.groupBox_4)
        self.btn_Guncelle.setObjectName(u"btn_Guncelle")

        self.horizontalLayout.addWidget(self.btn_Guncelle)

        self.btn_Sil = QPushButton(self.groupBox_4)
        self.btn_Sil.setObjectName(u"btn_Sil")

        self.horizontalLayout.addWidget(self.btn_Sil)

        self.btn_Temizle = QPushButton(self.groupBox_4)
        self.btn_Temizle.setObjectName(u"btn_Temizle")

        self.horizontalLayout.addWidget(self.btn_Temizle)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 3)

        self.groupBox_5 = QGroupBox(self.frame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 150))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tbl_uyeler = QTableWidget(self.groupBox_5)
        if (self.tbl_uyeler.columnCount() < 15):
            self.tbl_uyeler.setColumnCount(15)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbl_uyeler.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tbl_uyeler.setObjectName(u"tbl_uyeler")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tbl_uyeler.sizePolicy().hasHeightForWidth())
        self.tbl_uyeler.setSizePolicy(sizePolicy)
        self.tbl_uyeler.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.tbl_uyeler)


        self.gridLayout_2.addWidget(self.groupBox_5, 2, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 300))
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_3.addWidget(self.label_16)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_3.addWidget(self.label_17)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)


        self.gridLayout_8.addLayout(self.verticalLayout_3, 0, 0, 3, 2)

        self.txt_boy = QLineEdit(self.groupBox_3)
        self.txt_boy.setObjectName(u"txt_boy")

        self.gridLayout_8.addWidget(self.txt_boy, 0, 2, 1, 1)

        self.txt_kilo = QLineEdit(self.groupBox_3)
        self.txt_kilo.setObjectName(u"txt_kilo")

        self.gridLayout_8.addWidget(self.txt_kilo, 1, 2, 1, 1)

        self.plain_not = QPlainTextEdit(self.groupBox_3)
        self.plain_not.setObjectName(u"plain_not")
        self.plain_not.setMaximumSize(QSize(250, 50))

        self.gridLayout_8.addWidget(self.plain_not, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 300))
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 6, 1)

        self.txt_Ad = QLineEdit(self.groupBox)
        self.txt_Ad.setObjectName(u"txt_Ad")

        self.gridLayout_3.addWidget(self.txt_Ad, 0, 1, 1, 1)

        self.txt_Soyad = QLineEdit(self.groupBox)
        self.txt_Soyad.setObjectName(u"txt_Soyad")

        self.gridLayout_3.addWidget(self.txt_Soyad, 1, 1, 1, 1)

        self.txt_Tel = QLineEdit(self.groupBox)
        self.txt_Tel.setObjectName(u"txt_Tel")

        self.gridLayout_3.addWidget(self.txt_Tel, 2, 1, 1, 1)

        self.txt_Mail = QLineEdit(self.groupBox)
        self.txt_Mail.setObjectName(u"txt_Mail")

        self.gridLayout_3.addWidget(self.txt_Mail, 3, 1, 1, 1)

        self.date_dogum = QDateEdit(self.groupBox)
        self.date_dogum.setObjectName(u"date_dogum")

        self.gridLayout_3.addWidget(self.date_dogum, 4, 1, 1, 1)

        self.cmb_cinsiyet = QComboBox(self.groupBox)
        self.cmb_cinsiyet.addItem("")
        self.cmb_cinsiyet.addItem("")
        self.cmb_cinsiyet.setObjectName(u"cmb_cinsiyet")

        self.gridLayout_3.addWidget(self.cmb_cinsiyet, 5, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1164, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u00dcyeler", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyelik Bilgileri", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Kay\u0131t Tarihi:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik T\u00fcr\u00fc:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Biti\u015f Tarihi:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0130\u015flemler", None))
        self.btn_kaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btn_bilgiGetir.setText(QCoreApplication.translate("MainWindow", u"Bilgi Getir", None))
        self.btn_Guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_Sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_Temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyeler", None))
        ___qtablewidgetitem = self.tbl_uyeler.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"uyeID", None));
        ___qtablewidgetitem1 = self.tbl_uyeler.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ad", None));
        ___qtablewidgetitem2 = self.tbl_uyeler.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Soyad", None));
        ___qtablewidgetitem3 = self.tbl_uyeler.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem4 = self.tbl_uyeler.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Mail", None));
        ___qtablewidgetitem5 = self.tbl_uyeler.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Do\u011fum Tarihi", None));
        ___qtablewidgetitem6 = self.tbl_uyeler.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cinsiyet", None));
        ___qtablewidgetitem7 = self.tbl_uyeler.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kay\u0131t Tarihi", None));
        ___qtablewidgetitem8 = self.tbl_uyeler.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Tipi", None));
        ___qtablewidgetitem9 = self.tbl_uyeler.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Biti\u015f Tarihi", None));
        ___qtablewidgetitem10 = self.tbl_uyeler.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Boy", None));
        ___qtablewidgetitem11 = self.tbl_uyeler.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Kilo", None));
        ___qtablewidgetitem12 = self.tbl_uyeler.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sa\u011fl\u0131k Notu", None));
        ___qtablewidgetitem13 = self.tbl_uyeler.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Durum", None));
        ___qtablewidgetitem14 = self.tbl_uyeler.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Toplam Bor\u00e7", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Sa\u011fl\u0131k Bilgileri", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Boy:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Kilo:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Not:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ki\u015fisel Bilgiler", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ad:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soyad:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefon:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mail:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Do\u011fum Tarihi:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cinsiyet:", None))
        self.cmb_cinsiyet.setItemText(0, QCoreApplication.translate("MainWindow", u"Erkek", None))
        self.cmb_cinsiyet.setItemText(1, QCoreApplication.translate("MainWindow", u"Kad\u0131n", None))

    # retranslateUi

