# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uyelikTipleri.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 554)
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

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lbl_tipAdi = QLineEdit(self.groupBox)
        self.lbl_tipAdi.setObjectName(u"lbl_tipAdi")

        self.horizontalLayout.addWidget(self.lbl_tipAdi)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lbl_fiyat_2 = QLineEdit(self.groupBox)
        self.lbl_fiyat_2.setObjectName(u"lbl_fiyat_2")

        self.horizontalLayout.addWidget(self.lbl_fiyat_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lbl_fiyat = QLineEdit(self.groupBox)
        self.lbl_fiyat.setObjectName(u"lbl_fiyat")

        self.horizontalLayout.addWidget(self.lbl_fiyat)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_kaydet = QPushButton(self.groupBox)
        self.btn_kaydet.setObjectName(u"btn_kaydet")

        self.horizontalLayout_2.addWidget(self.btn_kaydet)

        self.btn_guncelle = QPushButton(self.groupBox)
        self.btn_guncelle.setObjectName(u"btn_guncelle")

        self.horizontalLayout_2.addWidget(self.btn_guncelle)

        self.btn_sil = QPushButton(self.groupBox)
        self.btn_sil.setObjectName(u"btn_sil")

        self.horizontalLayout_2.addWidget(self.btn_sil)

        self.btn_temizle = QPushButton(self.groupBox)
        self.btn_temizle.setObjectName(u"btn_temizle")

        self.horizontalLayout_2.addWidget(self.btn_temizle)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tbl_uyelikler = QTableWidget(self.groupBox_2)
        if (self.tbl_uyelikler.columnCount() < 4):
            self.tbl_uyelikler.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_uyelikler.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_uyelikler.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_uyelikler.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_uyelikler.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_uyelikler.setObjectName(u"tbl_uyelikler")

        self.gridLayout_4.addWidget(self.tbl_uyelikler, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1058, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u00dcyelikler", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyelik T\u00fcr\u00fc \u0130\u015flemleri", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tip Ad\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S\u00fcre:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fiyat:", None))
        self.btn_kaydet.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.btn_sil.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.btn_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyelik T\u00fcr\u00fc Listesi", None))
        ___qtablewidgetitem = self.tbl_uyelikler.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"uyelikTipiID", None));
        ___qtablewidgetitem1 = self.tbl_uyelikler.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"tipAdi", None));
        ___qtablewidgetitem2 = self.tbl_uyelikler.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"sureGun", None));
        ___qtablewidgetitem3 = self.tbl_uyelikler.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"fiyat", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyeler", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ayl\u0131k \u00dcye Say\u0131s\u0131:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y\u0131\u0131l\u0131k \u00dcye Say\u0131s\u0131:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Haftal\u0131k \u00dcye Say\u0131s\u0131:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"G\u00fcnl\u00fck \u00dcye Say\u0131s\u0131:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Null", None))
    # retranslateUi

