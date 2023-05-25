from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_guest import * 


class Guest(QMainWindow):
    def __init__(self) -> None:
        super(Guest, self).__init__() 
        self.ui = Ui_MainWindow_guest()
        self.ui.setupUi(self)
