# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(729, 368)
        Form.setStyleSheet(u"/* Ana Panel Tasar\u0131m\u0131 */\n"
"QFrame#frame_login {\n"
"    background-color: rgba(20, 20, 20, 230); /* \u00c7ok koyu gri, az saydam */\n"
"    border: 2px solid #e74c3c; /* Neon K\u0131rm\u0131z\u0131 \u00c7er\u00e7eve */\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Yaz\u0131 Etiketleri (Kullan\u0131c\u0131 Ad\u0131:, \u015eifre:) */\n"
"QLabel {\n"
"    color: #ecf0f1;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Giri\u015f Kutular\u0131 (TextBox) */\n"
"QLineEdit {\n"
"    background-color: #2c3e50;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #e74c3c; /* T\u0131klay\u0131nca k\u0131rm\u0131z\u0131 parlar */\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"/* Giri\u015f Butonu */\n"
"QPushButton {\n"
"    background-color: #e74c3c;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    font-s"
                        "ize: 15px;\n"
"    font-weight: bold;\n"
"    padding: 10px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0392b;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #962d22;\n"
"    padding-left: 12px; /* Bas\u0131lma hissi */\n"
"}")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(219, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 50))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_giris = QPushButton(self.frame)
        self.btn_giris.setObjectName(u"btn_giris")
        self.btn_giris.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255, 255, 255, 20); /* \u00c7ok hafif beyaz saydaml\u0131k */\n"
"    color: #ffffff;\n"
"    border: 2px solid #3498db; /* Mavi \u00e7er\u00e7eve */\n"
"    border-radius: 15px;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* \u00dczerine gelince i\u00e7i mavi dolar */\n"
"    color: white;\n"
"}")

        self.gridLayout.addWidget(self.btn_giris, 2, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_sifre = QLineEdit(self.frame)
        self.lineEdit_sifre.setObjectName(u"lineEdit_sifre")

        self.gridLayout.addWidget(self.lineEdit_sifre, 1, 1, 1, 1)

        self.lineEdit_kullanici = QLineEdit(self.frame)
        self.lineEdit_kullanici.setObjectName(u"lineEdit_kullanici")

        self.gridLayout.addWidget(self.lineEdit_kullanici, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(218, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Giri\u015f Ekran\u0131", None))
        self.btn_giris.setText(QCoreApplication.translate("Form", u"Giri\u015f Yap", None))
        self.label.setText(QCoreApplication.translate("Form", u"Kullan\u0131c\u0131 Ad\u0131:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u015eifre:", None))
    # retranslateUi

