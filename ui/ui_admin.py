# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminZRRxBd.ui'
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_fio = QLabel(self.centralwidget)
        self.label_fio.setObjectName(u"label_fio")
        self.label_fio.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.label_fio)

        self.label_info_img = QLabel(self.centralwidget)
        self.label_info_img.setObjectName(u"label_info_img")
        self.label_info_img.setMinimumSize(QSize(0, 100))

        self.verticalLayout.addWidget(self.label_info_img)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)

        QMetaObject.connectSlotsByName(MainWindow_admin)
    # setupUi

    def retranslateUi(self, MainWindow_admin):
        MainWindow_admin.setWindowTitle(QCoreApplication.translate("MainWindow_admin", u"MainWindow", None))
        self.label_fio.setText(QCoreApplication.translate("MainWindow_admin", u"TextLabel", None))
        self.label_info_img.setText(QCoreApplication.translate("MainWindow_admin", u"TextLabel", None))
    # retranslateUi

