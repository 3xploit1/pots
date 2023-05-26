from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_authorization import *
from db.db_module import *
from utils.view.admin import *
from utils.view.client import *
from utils.view.guest import *
from utils.view.manager import *

class Authorization(QDialog, DataBase): 
    def __init__(self) -> None:
        super(Authorization, self).__init__()
        self.ui = Ui_DialogAuth()
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_guest.clicked.connect(self.move_guest)
        self.ui.btn_log_in.clicked.connect(self.log_in)
        self.setWindowIcon(QIcon('resources\/assets\/icon.ico'))
        pix = QPixmap('resources\/assets\/logo.png')
        self.ui.label.setPixmap(pix)
        self.ui.label.setScaledContents(True)
        

    def move_admin(self): 
        '''
        Закрывает окно авторизации. Создает экземпляр класса Admin
        Запускает новый цикл событий
        '''
        self.accept()
        admin = Admin(self.ui.line_log_in.text())
        admin.show()
        admin.exec_()
    
    def move_client(self): 
        '''
        Закрывает окно авторизации. Создает экземпляр класса Client
        Запускает новый цикл событий
        '''
        self.accept()
        client = Client(self.ui.line_log_in.text())
        client.show()
        client.exec_()
    
    def move_guest(self): 
        '''
        Закрывает окно авторизации. Создает экземпляр класса Guest
        Запускает новый цикл событий
        '''
        self.accept()
        guest = Guest()
        guest.show()
        guest.exec_()

    def move_manager(self): 
        '''
        Закрывает окно авторизации. Создает экземпляр класса Manager
        Запускает новый цикл событий
        '''
        self.accept()
        manager = Manager(self.ui.line_log_in.text())
        manager.show()
        manager.exec_()

    def log_in(self) -> None: 
        '''
        Создание и вызов объекта авторизации
        '''
        
        log_in = self.ui.line_log_in.text()
        password = self.ui.line_password.text()
        # try: 
        if (log_in != '') and (password != ''):
            data = self.process_authorization(login=log_in, password=password)
            if (data[0] == 'Администратор'): 
                self.move_admin()
            elif (data[0] == 'Клиент'): 
                    self.move_client()  
            elif (data[0] == 'Менеджер'):
                self.move_manager()
                # else: raise ValueError
        # except (ValueError): 
        #     QMessageBox.warning(
        #         QMessageBox(),
        #         'Ошибка авторизации',
        #         'Произошла обишка авторизации'
        #     )

