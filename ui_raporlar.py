# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'raporlar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 567)
        MainWindow.setStyleSheet(u"/* Ana Pencere Arka Plan\u0131 */\n"
"QMainWindow {\n"
"    background-color: #1e1e27;\n"
"}\n"
"\n"
"/* Grafiklerin durdu\u011fu widget'lar */\n"
"QWidget#widget_gelir, QWidget#widget_pasta,QWidget#widget_doluluk_analiz {\n"
"    background-color: #2b2b36;\n"
"    border-radius: 15px;\n"
"    border: 1px solid #3d3d4d;\n"
"}\n"
"\n"
"/* Tablolar\u0131 modernle\u015ftir */\n"
"QTableWidget {\n"
"    background-color: #2b2b36;\n"
"    alternate-background-color: #323240;\n"
"    color: #ffffff;\n"
"    gridline-color: #3d3d4d;\n"
"    border-radius: 10px;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"/* Ba\u015fl\u0131klar */\n"
"QHeaderView::section {\n"
"    background-color: #3d3d4d;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Butonlar */\n"
"QPushButton {\n"
"    background-color: #556ee6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4458b8;\n"
"}\n"
"\n"
"QP"
                        "ushButton#btn_excel_aktar {\n"
"    background-color: #34c38f; /* Excel Ye\u015fili */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_pasta = QWidget(self.tab)
        self.widget_pasta.setObjectName(u"widget_pasta")

        self.gridLayout.addWidget(self.widget_pasta, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_gelir = QWidget(self.tab_2)
        self.widget_gelir.setObjectName(u"widget_gelir")
        self.gridLayout_7 = QGridLayout(self.widget_gelir)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_gelir_2 = QWidget(self.widget_gelir)
        self.widget_gelir_2.setObjectName(u"widget_gelir_2")

        self.gridLayout_7.addWidget(self.widget_gelir_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_gelir, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_doluluk_analiz = QWidget(self.tab_3)
        self.widget_doluluk_analiz.setObjectName(u"widget_doluluk_analiz")

        self.gridLayout_5.addWidget(self.widget_doluluk_analiz, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_2 = QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_borclular = QTableWidget(self.tab_4)
        if (self.tableWidget_borclular.columnCount() < 4):
            self.tableWidget_borclular.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_borclular.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_borclular.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_borclular.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_borclular.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_borclular.setObjectName(u"tableWidget_borclular")

        self.gridLayout_2.addWidget(self.tableWidget_borclular, 0, 0, 1, 2)

        self.btn_disa_aktar = QPushButton(self.tab_4)
        self.btn_disa_aktar.setObjectName(u"btn_disa_aktar")

        self.gridLayout_2.addWidget(self.btn_disa_aktar, 1, 0, 1, 1)

        self.btn_excel_aktar = QPushButton(self.tab_4)
        self.btn_excel_aktar.setObjectName(u"btn_excel_aktar")

        self.gridLayout_2.addWidget(self.btn_excel_aktar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_3 = QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.progressBar = QProgressBar(self.tab_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_3.addWidget(self.progressBar, 0, 0, 1, 2)

        self.lbl_detay = QLabel(self.tab_5)
        self.lbl_detay.setObjectName(u"lbl_detay")

        self.gridLayout_3.addWidget(self.lbl_detay, 0, 2, 1, 1)

        self.tableWidget_riskli = QTableWidget(self.tab_5)
        if (self.tableWidget_riskli.columnCount() < 3):
            self.tableWidget_riskli.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_riskli.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_riskli.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_riskli.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_riskli.setObjectName(u"tableWidget_riskli")

        self.gridLayout_3.addWidget(self.tableWidget_riskli, 1, 0, 1, 3)

        self.btn_disa_aktar_2 = QPushButton(self.tab_5)
        self.btn_disa_aktar_2.setObjectName(u"btn_disa_aktar_2")

        self.gridLayout_3.addWidget(self.btn_disa_aktar_2, 2, 0, 1, 1)

        self.btn_excel_aktar_2 = QPushButton(self.tab_5)
        self.btn_excel_aktar_2.setObjectName(u"btn_excel_aktar_2")

        self.gridLayout_3.addWidget(self.btn_excel_aktar_2, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_antrenor_analiz = QWidget(self.tab_6)
        self.widget_antrenor_analiz.setObjectName(u"widget_antrenor_analiz")

        self.gridLayout_9.addWidget(self.widget_antrenor_analiz, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_10 = QGridLayout(self.tab_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_kantin_analiz = QWidget(self.tab_7)
        self.widget_kantin_analiz.setObjectName(u"widget_kantin_analiz")

        self.gridLayout_10.addWidget(self.widget_kantin_analiz, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_12 = QGridLayout(self.tab_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_hedef_analiz = QWidget(self.tab_9)
        self.widget_hedef_analiz.setObjectName(u"widget_hedef_analiz")

        self.gridLayout_12.addWidget(self.widget_hedef_analiz, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_11 = QGridLayout(self.tab_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_stok = QTableWidget(self.tab_8)
        if (self.tableWidget_stok.columnCount() < 3):
            self.tableWidget_stok.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_stok.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_stok.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_stok.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.tableWidget_stok.setObjectName(u"tableWidget_stok")

        self.gridLayout_11.addWidget(self.tableWidget_stok, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 1, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Raporlar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u00dcyelik Anaizi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Mali Durum Analizi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Saatlik Salon Yo\u011funlu\u011fu", None))
        ___qtablewidgetitem = self.tableWidget_borclular.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ad", None));
        ___qtablewidgetitem1 = self.tableWidget_borclular.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Soyad", None));
        ___qtablewidgetitem2 = self.tableWidget_borclular.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem3 = self.tableWidget_borclular.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Bor\u00e7", None));
        self.btn_disa_aktar.setText(QCoreApplication.translate("MainWindow", u"PDF olarak \u00e7\u0131kt\u0131 al", None))
        self.btn_excel_aktar.setText(QCoreApplication.translate("MainWindow", u"Excel olarak \u00e7\u0131kt\u0131 al", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Bor\u00e7lular L\u0130stesi", None))
        self.lbl_detay.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem4 = self.tableWidget_riskli.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ad Soyad", None));
        ___qtablewidgetitem5 = self.tableWidget_riskli.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem6 = self.tableWidget_riskli.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Son Giri\u015f Tarihi", None));
        self.btn_disa_aktar_2.setText(QCoreApplication.translate("MainWindow", u"PDF olarak \u00e7\u0131kt\u0131 al", None))
        self.btn_excel_aktar_2.setText(QCoreApplication.translate("MainWindow", u"Excel olarak \u00e7\u0131kt\u0131 al", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Riskli \u00dcyeler", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Antren\u00f6r \u00dcye Y\u00fck Analizi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Kantin Nakit Ak\u0131\u015f\u0131", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Ayl\u0131k Hedef", None))
        ___qtablewidgetitem7 = self.tableWidget_stok.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u00dcr\u00fcn Ad\u0131", None));
        ___qtablewidgetitem8 = self.tableWidget_stok.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Stok Adedi", None));
        ___qtablewidgetitem9 = self.tableWidget_stok.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Kritik Seviye", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Kritik Stok", None))
    # retranslateUi

