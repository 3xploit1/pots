# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_upLgjFfc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_sign_up(object):
    def setupUi(self, Dialog_sign_up):
        if not Dialog_sign_up.objectName():
            Dialog_sign_up.setObjectName(u"Dialog_sign_up")
        Dialog_sign_up.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog_sign_up)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_role = QLineEdit(Dialog_sign_up)
        self.lineEdit_role.setObjectName(u"lineEdit_role")

        self.verticalLayout.addWidget(self.lineEdit_role)

        self.lineEdit_fio = QLineEdit(Dialog_sign_up)
        self.lineEdit_fio.setObjectName(u"lineEdit_fio")

        self.verticalLayout.addWidget(self.lineEdit_fio)

        self.lineEdit_login = QLineEdit(Dialog_sign_up)
        self.lineEdit_login.setObjectName(u"lineEdit_login")

        self.verticalLayout.addWidget(self.lineEdit_login)

        self.lineEdit_password = QLineEdit(Dialog_sign_up)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_file_dialog = QPushButton(Dialog_sign_up)
        self.pushButton_file_dialog.setObjectName(u"pushButton_file_dialog")

        self.verticalLayout.addWidget(self.pushButton_file_dialog)

        self.pushButton_req_sign_up = QPushButton(Dialog_sign_up)
        self.pushButton_req_sign_up.setObjectName(u"pushButton_req_sign_up")

        self.verticalLayout.addWidget(self.pushButton_req_sign_up)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog_sign_up)

        QMetaObject.connectSlotsByName(Dialog_sign_up)
    # setupUi

    def retranslateUi(self, Dialog_sign_up):
        Dialog_sign_up.setWindowTitle(QCoreApplication.translate("Dialog_sign_up", u"Dialog", None))
        self.lineEdit_role.setInputMask("")
        self.lineEdit_role.setPlaceholderText(QCoreApplication.translate("Dialog_sign_up", u"\u0420\u043e\u043b\u044c", None))
        self.lineEdit_fio.setPlaceholderText(QCoreApplication.translate("Dialog_sign_up", u"\u0424\u0418\u041e", None))
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("Dialog_sign_up", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_password.setInputMask(QCoreApplication.translate("Dialog_sign_up", u"+7-999-999-99-99", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Dialog_sign_up", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_file_dialog.setText(QCoreApplication.translate("Dialog_sign_up", u"\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430", None))
        self.pushButton_req_sign_up.setText(QCoreApplication.translate("Dialog_sign_up", u"\u041e\u043a", None))
    # retranslateUi

