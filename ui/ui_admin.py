# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminJRKteF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_admin(object):
    def setupUi(self, MainWindow_admin):
        if not MainWindow_admin.objectName():
            MainWindow_admin.setObjectName(u"MainWindow_admin")
        MainWindow_admin.resize(663, 342)
        self.centralwidget = QWidget(MainWindow_admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_products = QTableWidget(self.centralwidget)
        self.tableWidget_products.setObjectName(u"tableWidget_products")

        self.verticalLayout_2.addWidget(self.tableWidget_products)

        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)

        QMetaObject.connectSlotsByName(MainWindow_admin)
    # setupUi

    def retranslateUi(self, MainWindow_admin):
        MainWindow_admin.setWindowTitle(QCoreApplication.translate("MainWindow_admin", u"MainWindow", None))
    # retranslateUi

