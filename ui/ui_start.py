# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startDXoRbR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_start(object):
    def setupUi(self, MainWindow_start):
        if not MainWindow_start.objectName():
            MainWindow_start.setObjectName(u"MainWindow_start")
        MainWindow_start.resize(318, 234)
        self.centralwidget = QWidget(MainWindow_start)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMinimumSize(QSize(300, 150))

        self.verticalLayout_2.addWidget(self.label_info)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_sign_in = QPushButton(self.centralwidget)
        self.pushButton_sign_in.setObjectName(u"pushButton_sign_in")

        self.verticalLayout.addWidget(self.pushButton_sign_in)

        self.pushButton_sign_up = QPushButton(self.centralwidget)
        self.pushButton_sign_up.setObjectName(u"pushButton_sign_up")

        self.verticalLayout.addWidget(self.pushButton_sign_up)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow_start.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_start)

        QMetaObject.connectSlotsByName(MainWindow_start)
    # setupUi

    def retranslateUi(self, MainWindow_start):
        MainWindow_start.setWindowTitle(QCoreApplication.translate("MainWindow_start", u"MainWindow", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow_start", u"TextLabel", None))
        self.pushButton_sign_in.setText(QCoreApplication.translate("MainWindow_start", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton_sign_up.setText(QCoreApplication.translate("MainWindow_start", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

