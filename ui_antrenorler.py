# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'antrenorler.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1212, 647)
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
        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tbl_antrenorler = QTableWidget(self.groupBox)
        if (self.tbl_antrenorler.columnCount() < 6):
            self.tbl_antrenorler.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_antrenorler.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tbl_antrenorler.setObjectName(u"tbl_antrenorler")

        self.gridLayout_2.addWidget(self.tbl_antrenorler, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.txt_ad = QLineEdit(self.groupBox_2)
        self.txt_ad.setObjectName(u"txt_ad")

        self.gridLayout_3.addWidget(self.txt_ad, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.txt_soyad = QLineEdit(self.groupBox_2)
        self.txt_soyad.setObjectName(u"txt_soyad")

        self.gridLayout_3.addWidget(self.txt_soyad, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)

        self.txt_telefon = QLineEdit(self.groupBox_2)
        self.txt_telefon.setObjectName(u"txt_telefon")

        self.gridLayout_3.addWidget(self.txt_telefon, 0, 5, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 6, 1, 1)

        self.txt_uzmanlik = QLineEdit(self.groupBox_2)
        self.txt_uzmanlik.setObjectName(u"txt_uzmanlik")

        self.gridLayout_3.addWidget(self.txt_uzmanlik, 0, 7, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 8, 1, 1)

        self.txt_maas = QLineEdit(self.groupBox_2)
        self.txt_maas.setObjectName(u"txt_maas")

        self.gridLayout_3.addWidget(self.txt_maas, 0, 9, 1, 1)

        self.splitter = QSplitter(self.groupBox_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.btn_kaydet = QPushButton(self.splitter)
        self.btn_kaydet.setObjectName(u"btn_kaydet")
        self.splitter.addWidget(self.btn_kaydet)
        self.btn_guncelle = QPushButton(self.splitter)
        self.btn_guncelle.setObjectName(u"btn_guncelle")
        self.splitter.addWidget(self.btn_guncelle)
        self.btn_sil = QPushButton(self.splitter)
        self.btn_sil.setObjectName(u"btn_sil")
        self.splitter.addWidget(self.btn_sil)
        self.btn_temizle = QPushButton(self.splitter)
        self.btn_temizle.setObjectName(u"btn_temizle")
        self.splitter.addWidget(self.btn_temizle)

        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 10)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tbl_uye_antrenor = QTableWidget(self.groupBox_3)
        if (self.tbl_uye_antrenor.columnCount() < 4):
            self.tbl_uye_antrenor.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_uye_antrenor.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_uye_antrenor.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_uye_antrenor.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_uye_antrenor.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tbl_uye_antrenor.setObjectName(u"tbl_uye_antrenor")

        self.gridLayout_4.addWidget(self.tbl_uye_antrenor, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1212, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Antren\u00f6rler", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Antren\u00f6rler", None))
        ___qtablewidgetitem = self.tbl_antrenorler.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tbl_antrenorler.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ad", None));
        ___qtablewidgetitem2 = self.tbl_antrenorler.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Soyad", None));
        ___qtablewidgetitem3 = self.tbl_antrenorler.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem4 = self.tbl_antrenorler.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Uzmanl\u0131k", None));
        ___qtablewidgetitem5 = self.tbl_antrenorler.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Maas", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0130\u015flemler", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ad:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soyad:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefon:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Uzmanl\u0131k:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Maa\u015f:", None))
        self.btn_kaydet.setText(QCoreApplication.translate("MainWindow", u"Yeni Kay\u0131t", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Antren\u00f6r-\u00dcye", None))
        ___qtablewidgetitem6 = self.tbl_uye_antrenor.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Ad\u0131", None));
        ___qtablewidgetitem7 = self.tbl_uye_antrenor.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Soyad\u0131", None));
        ___qtablewidgetitem8 = self.tbl_uye_antrenor.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Antren\u00f6r Ad\u0131", None));
        ___qtablewidgetitem9 = self.tbl_uye_antrenor.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Biti\u015f Tarihi", None));
    # retranslateUi

