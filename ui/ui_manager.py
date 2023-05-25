# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'managerSDqWAy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_manager(object):
    def setupUi(self, MainWindow_manager):
        if not MainWindow_manager.objectName():
            MainWindow_manager.setObjectName(u"MainWindow_manager")
        MainWindow_manager.resize(683, 375)
        self.centralwidget = QWidget(MainWindow_manager)
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

        MainWindow_manager.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_manager)

        QMetaObject.connectSlotsByName(MainWindow_manager)
    # setupUi

    def retranslateUi(self, MainWindow_manager):
        MainWindow_manager.setWindowTitle(QCoreApplication.translate("MainWindow_manager", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow_manager", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
    # retranslateUi

