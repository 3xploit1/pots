from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_manager import *

class Manager(QMainWindow): 
    def __init__(self) -> None:
        super(Manager, self).__init__()
        self.ui = Ui_MainWindow_manager()
        self.ui.setupUi(self)
        
        