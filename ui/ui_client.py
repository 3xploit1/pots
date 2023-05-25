# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientHdppuh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_client(object):
    def setupUi(self, MainWindow_client):
        if not MainWindow_client.objectName():
            MainWindow_client.setObjectName(u"MainWindow_client")
        MainWindow_client.resize(730, 412)
        self.centralwidget = QWidget(MainWindow_client)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout.addWidget(self.label_name)

        self.tableView_products = QTableView(self.centralwidget)
        self.tableView_products.setObjectName(u"tableView_products")

        self.verticalLayout.addWidget(self.tableView_products)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow_client.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_client)

        QMetaObject.connectSlotsByName(MainWindow_client)
    # setupUi

    def retranslateUi(self, MainWindow_client):
        MainWindow_client.setWindowTitle(QCoreApplication.translate("MainWindow_client", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow_client", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
    # retranslateUi

