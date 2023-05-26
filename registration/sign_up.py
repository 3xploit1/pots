from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_sign_up import *
from db.db_module import *

class Registration(QDialog, DataBase): 
    def __init__(self) -> None:
        super(Registration, self).__init__()
        self.ui = Ui_Dialog_sign_up()
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.pushButton_file_dialog.clicked.connect(self.openFileDialog)
        self.ui.pushButton_req_sign_up.clicked.connect(self.sign_up)
        
    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        file_dialog.selectNameFilter("Image Files (*.png *.jpg *.bmp)")
        self.file_path, _ = file_dialog.getOpenFileName()
    
    def sign_up(self): 
        role = self.ui.lineEdit_role.text()
        fio = self.ui.lineEdit_fio.text()
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        img = self.file_path.split("/")[-1]
       
        try: 
            if role != '' and fio != '' and login != '' and password != '' and img != '': 
                self.process_registration(role, fio, login, password, img)
                QMessageBox.information(QMessageBox(), 'Успешно', 'Регистрация окончена')
                self.accept()
            else: raise ValueError
        except ValueError: 
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Заполните все поля')
        