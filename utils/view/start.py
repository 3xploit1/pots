from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_start import *
from auth.authorization import * 
from registration.sign_up import *

class Start(QMainWindow): 
    def __init__(self) -> None:
        super(Start, self).__init__()
        self.ui = Ui_MainWindow_start()
        self.ui.setupUi(self)
        self.ui.pushButton_sign_in.clicked.connect(self.move_sign_in)
        self.ui.pushButton_sign_up.clicked.connect(self.move_sign_up)
    
    def move_sign_in(self):
        window = Authorization()
        window.show()
        window.exec_()
        
    def move_sign_up(self): 
        window = Registration()
        window.show()
        window.exec_()
        