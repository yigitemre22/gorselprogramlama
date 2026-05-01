# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'odemeler.ui'
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
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1342, 722)
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 220))
        self.txt_uyeAd = QLineEdit(self.groupBox)
        self.txt_uyeAd.setObjectName(u"txt_uyeAd")
        self.txt_uyeAd.setGeometry(QRect(90, 46, 100, 31))
        self.txt_uyeAd.setMaximumSize(QSize(100, 16777215))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(22, 42, 71, 31))
        self.btn_ara = QPushButton(self.groupBox)
        self.btn_ara.setObjectName(u"btn_ara")
        self.btn_ara.setGeometry(QRect(220, 40, 91, 32))
        self.btn_ara.setMaximumSize(QSize(100, 16777215))
        self.tbl_uyeler = QTableWidget(self.groupBox)
        if (self.tbl_uyeler.columnCount() < 7):
            self.tbl_uyeler.setColumnCount(7)
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
        self.tbl_uyeler.setObjectName(u"tbl_uyeler")
        self.tbl_uyeler.setGeometry(QRect(100, 81, 953, 131))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(22, 81, 71, 31))

        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_4.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.txt_tutar = QLineEdit(self.groupBox_2)
        self.txt_tutar.setObjectName(u"txt_tutar")

        self.gridLayout_4.addWidget(self.txt_tutar, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 4, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 0, 5, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 6, 1, 1)

        self.txt_aciklama = QTextEdit(self.groupBox_2)
        self.txt_aciklama.setObjectName(u"txt_aciklama")
        self.txt_aciklama.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.txt_aciklama, 0, 7, 2, 1)

        self.btn_odemeAl = QPushButton(self.groupBox_2)
        self.btn_odemeAl.setObjectName(u"btn_odemeAl")

        self.gridLayout_4.addWidget(self.btn_odemeAl, 1, 3, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 4, 1, 1)

        self.txt_uyeID = QLineEdit(self.groupBox_2)
        self.txt_uyeID.setObjectName(u"txt_uyeID")
        self.txt_uyeID.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.txt_uyeID, 1, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tbl_odemeler = QTableWidget(self.groupBox_3)
        if (self.tbl_odemeler.columnCount() < 4):
            self.tbl_odemeler.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_odemeler.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_odemeler.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_odemeler.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbl_odemeler.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.tbl_odemeler.setObjectName(u"tbl_odemeler")

        self.gridLayout_2.addWidget(self.tbl_odemeler, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1342, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u00d6deme Ekran\u0131", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u00dcyeler", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Ara:", None))
        self.btn_ara.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        ___qtablewidgetitem = self.tbl_uyeler.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ad", None));
        ___qtablewidgetitem1 = self.tbl_uyeler.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Soyad", None));
        ___qtablewidgetitem2 = self.tbl_uyeler.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem3 = self.tbl_uyeler.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u00dcyelik Tipi", None));
        ___qtablewidgetitem4 = self.tbl_uyeler.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Biti\u015f Tarihi", None));
        ___qtablewidgetitem5 = self.tbl_uyeler.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Borcu", None));
        ___qtablewidgetitem6 = self.tbl_uyeler.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Id", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00dcye Se\u00e7:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Yeni \u00d6deme", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00d6deme Tarihi:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tutar:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00d6deme T\u00fcr\u00fc:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Nakit", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Kart", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Havale", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.btn_odemeAl.setText(QCoreApplication.translate("MainWindow", u"\u00d6deme Al", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u00dcye ID:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u00d6deme Ge\u00e7mi\u015fi", None))
        ___qtablewidgetitem7 = self.tbl_odemeler.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tarih", None));
        ___qtablewidgetitem8 = self.tbl_odemeler.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Tutar", None));
        ___qtablewidgetitem9 = self.tbl_odemeler.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u00d6deme T\u00fcr\u00fc", None));
        ___qtablewidgetitem10 = self.tbl_odemeler.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama", None));
    # retranslateUi

