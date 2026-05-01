# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindowq(object):
    def setupUi(self, MainWindowq):
        if not MainWindowq.objectName():
            MainWindowq.setObjectName(u"MainWindowq")
        MainWindowq.resize(1209, 693)
        MainWindowq.setStyleSheet(u"QFrame, QGroupBox {\n"
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
"}\n"
"/* \u0130statistik Kartlar\u0131 i\u00e7in \u00d6zel "
                        "Panel */\n"
"QFrame#istatistik_kart {\n"
"    background-color: rgba(30, 41, 59, 120); /* Hafif lacivert cam efekti */\n"
"    border: 1px solid rgba(79, 209, 197, 60); /* Turkuaz parlayan kenarl\u0131k */\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"/* Kart \u0130\u00e7indeki Ba\u015fl\u0131k (\u00d6rn: Toplam \u00dcye Say\u0131s\u0131) */\n"
"QLabel#label{\n"
"    color: #94A3B8; /* Daha s\u00f6n\u00fck gri/mavi tonu */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"/* Kart \u0130\u00e7indeki Veri (\u00d6rn: 150) */\n"
"QLabel#label_toplam_uye{\n"
"    color: #4FD1C5; /* Parlak Turkuaz */\n"
"    font-size: 24px;\n"
"    font-weight: 800;\n"
"}")
        self.centralwidget = QWidget(MainWindowq)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(48, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"  \n"
"    \n"
"	background-color: transparent; /* %60 \u015feffaf siyah */\n"
"   \n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_antrenorler = QPushButton(self.frame)
        self.btn_antrenorler.setObjectName(u"btn_antrenorler")
        self.btn_antrenorler.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_antrenorler, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 11, 1, 1, 1)

        self.btn_uyeler = QPushButton(self.frame)
        self.btn_uyeler.setObjectName(u"btn_uyeler")
        self.btn_uyeler.setMinimumSize(QSize(0, 45))
        self.btn_uyeler.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.btn_uyeler, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.label_toplam_uye = QLabel(self.frame)
        self.label_toplam_uye.setObjectName(u"label_toplam_uye")
        sizePolicy.setHeightForWidth(self.label_toplam_uye.sizePolicy().hasHeightForWidth())
        self.label_toplam_uye.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_toplam_uye)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_aktif_uye = QLabel(self.frame)
        self.label_aktif_uye.setObjectName(u"label_aktif_uye")
        sizePolicy.setHeightForWidth(self.label_aktif_uye.sizePolicy().hasHeightForWidth())
        self.label_aktif_uye.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_aktif_uye)


        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 1, 1, 1)

        self.btn_raporlar = QPushButton(self.frame)
        self.btn_raporlar.setObjectName(u"btn_raporlar")
        self.btn_raporlar.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_raporlar, 7, 0, 1, 1)

        self.btn_odemeler = QPushButton(self.frame)
        self.btn_odemeler.setObjectName(u"btn_odemeler")
        self.btn_odemeler.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_odemeler, 6, 0, 1, 1)

        self.btn_ayarlar = QPushButton(self.frame)
        self.btn_ayarlar.setObjectName(u"btn_ayarlar")
        self.btn_ayarlar.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_ayarlar, 9, 0, 1, 1)

        self.btn_uyeliktipleri = QPushButton(self.frame)
        self.btn_uyeliktipleri.setObjectName(u"btn_uyeliktipleri")
        self.btn_uyeliktipleri.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_uyeliktipleri, 4, 0, 1, 1)

        self.btn_ekipmanlar = QPushButton(self.frame)
        self.btn_ekipmanlar.setObjectName(u"btn_ekipmanlar")
        self.btn_ekipmanlar.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_ekipmanlar, 5, 0, 1, 1)

        self.btn_dersler = QPushButton(self.frame)
        self.btn_dersler.setObjectName(u"btn_dersler")
        self.btn_dersler.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.btn_dersler, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 2, 1)

        MainWindowq.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowq)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1209, 25))
        MainWindowq.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowq)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowq.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowq)

        QMetaObject.connectSlotsByName(MainWindowq)
    # setupUi

    def retranslateUi(self, MainWindowq):
        MainWindowq.setWindowTitle(QCoreApplication.translate("MainWindowq", u"Giri\u015f Ekran\u0131", None))
        self.btn_antrenorler.setText(QCoreApplication.translate("MainWindowq", u"Antren\u00f6rler", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowq", u"Bug\u00fcnk\u00fc \u00d6deme Say\u0131s\u0131:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindowq", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowq", u"Ayl\u0131k Gelir:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindowq", u"TextLabel", None))
        self.btn_uyeler.setText(QCoreApplication.translate("MainWindowq", u"\u00dcyeler", None))
        self.label.setText(QCoreApplication.translate("MainWindowq", u"Toplam \u00dcye Say\u0131s\u0131:", None))
        self.label_toplam_uye.setText(QCoreApplication.translate("MainWindowq", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowq", u"Aktif \u00dcye Say\u0131s\u0131:", None))
        self.label_aktif_uye.setText(QCoreApplication.translate("MainWindowq", u"TextLabel", None))
        self.btn_raporlar.setText(QCoreApplication.translate("MainWindowq", u"Raporlar", None))
        self.btn_odemeler.setText(QCoreApplication.translate("MainWindowq", u"\u00d6demeler", None))
        self.btn_ayarlar.setText(QCoreApplication.translate("MainWindowq", u"Ayarlar", None))
        self.btn_uyeliktipleri.setText(QCoreApplication.translate("MainWindowq", u"\u00dcyelik Tipleri", None))
        self.btn_ekipmanlar.setText(QCoreApplication.translate("MainWindowq", u"Ekipmanlar", None))
        self.btn_dersler.setText(QCoreApplication.translate("MainWindowq", u"Dersler", None))
    # retranslateUi

