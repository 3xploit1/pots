from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_authorization import *


class Authorization(QDialog): 
    def __init__(self) -> None:
        super(Authorization, self).__init__()
        self.ui = Ui_DialogAuth
        self.ui.setupUi(self)
        
    def process(self):
        '''
        Процесс авторизаци
        '''
        login = self.ui.line_log_in.text()   
        password = self.ui.line_password.text()

