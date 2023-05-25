# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guestIvPDhS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_guest(object):
    def setupUi(self, MainWindow_guest):
        if not MainWindow_guest.objectName():
            MainWindow_guest.setObjectName(u"MainWindow_guest")
        MainWindow_guest.resize(731, 369)
        self.centralwidget = QWidget(MainWindow_guest)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout.addWidget(self.label_name)

        self.tableView_name = QTableView(self.centralwidget)
        self.tableView_name.setObjectName(u"tableView_name")

        self.verticalLayout.addWidget(self.tableView_name)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow_guest.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_guest)

        QMetaObject.connectSlotsByName(MainWindow_guest)
    # setupUi

    def retranslateUi(self, MainWindow_guest):
        MainWindow_guest.setWindowTitle(QCoreApplication.translate("MainWindow_guest", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow_guest", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0412\u044b \u0432\u043e\u0448\u043b\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c</span></p><p><br/></p></body></html>", None))
    # retranslateUi

