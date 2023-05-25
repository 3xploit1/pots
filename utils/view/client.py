import typing
from PySide2.QtCore import *
import PySide2.QtCore
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import PySide2.QtWidgets
from ui.ui_client import *

class Client(QMainWindow): 
    def __init__(self) -> None:
        super(Client, self).__init__()
        self.ui = Ui_MainWindow_client()
        self.ui.setupUi(self)