# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorizationdkJBKh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAuth(object):
    def setupUi(self, DialogAuth):
        if not DialogAuth.objectName():
            DialogAuth.setObjectName(u"DialogAuth")
        DialogAuth.resize(318, 174)
        DialogAuth.setMinimumSize(QSize(318, 174))
        self.verticalLayout_3 = QVBoxLayout(DialogAuth)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_log_in = QLineEdit(DialogAuth)
        self.line_log_in.setObjectName(u"line_log_in")

        self.verticalLayout.addWidget(self.line_log_in)

        self.line_password = QLineEdit(DialogAuth)
        self.line_password.setObjectName(u"line_password")

        self.verticalLayout.addWidget(self.line_password)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.label = QLabel(DialogAuth)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_log_in = QPushButton(DialogAuth)
        self.btn_log_in.setObjectName(u"btn_log_in")

        self.verticalLayout_2.addWidget(self.btn_log_in)

        self.btn_guest = QPushButton(DialogAuth)
        self.btn_guest.setObjectName(u"btn_guest")

        self.verticalLayout_2.addWidget(self.btn_guest)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(DialogAuth)

        QMetaObject.connectSlotsByName(DialogAuth)
    # setupUi

    def retranslateUi(self, DialogAuth):
        DialogAuth.setWindowTitle(QCoreApplication.translate("DialogAuth", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogAuth", u"TextLabel", None))
        self.btn_log_in.setText(QCoreApplication.translate("DialogAuth", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btn_guest.setText(QCoreApplication.translate("DialogAuth", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
    # retranslateUi

