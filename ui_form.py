# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.TitleMainWindow = QLabel(Widget)
        self.TitleMainWindow.setObjectName(u"TitleMainWindow")
        self.TitleMainWindow.setGeometry(QRect(370, 10, 121, 16))
        self.GenerarPasswordButton = QPushButton(Widget)
        self.GenerarPasswordButton.setObjectName(u"GenerarPasswordButton")
        self.GenerarPasswordButton.setGeometry(QRect(220, 40, 121, 24))
        self.ShowPassword = QPlainTextEdit(Widget)
        self.ShowPassword.setObjectName(u"ShowPassword")
        self.ShowPassword.setGeometry(QRect(350, 30, 161, 41))
        self.SiteAccount = QPlainTextEdit(Widget)
        self.SiteAccount.setObjectName(u"SiteAccount")
        self.SiteAccount.setGeometry(QRect(40, 130, 191, 31))
        self.EmailAccount = QPlainTextEdit(Widget)
        self.EmailAccount.setObjectName(u"EmailAccount")
        self.EmailAccount.setGeometry(QRect(300, 130, 221, 31))
        self.PasswordAccount = QPlainTextEdit(Widget)
        self.PasswordAccount.setObjectName(u"PasswordAccount")
        self.PasswordAccount.setGeometry(QRect(570, 130, 181, 31))
        self.AddAccount = QPushButton(Widget)
        self.AddAccount.setObjectName(u"AddAccount")
        self.AddAccount.setGeometry(QRect(220, 190, 121, 24))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.TitleMainWindow.setText(QCoreApplication.translate("Widget", u"Gestor de contrase\u00f1as", None))
        self.GenerarPasswordButton.setText(QCoreApplication.translate("Widget", u"Generar contrase\u00f1a", None))
        self.AddAccount.setText(QCoreApplication.translate("Widget", u"Agregar cuenta", None))
    # retranslateUi

