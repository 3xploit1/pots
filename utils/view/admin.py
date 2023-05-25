from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QStandardItemModel
from ui.ui_admin import * 
from db.db_module import *


class Admin(QMainWindow, DataBase): 
    def __init__(self, user) -> None:
        super(Admin, self).__init__()
        self.ui = Ui_MainWindow_admin()
        self.ui.setupUi(self)
        self.set_connect()
        self.user = user
        # self.load_name()
        self.load_products()
        # self.ui.verticalLayout_3.addChildWidget(self.ui.pushButton_submit)
        # self.ui.verticalLayout_3.addChildWidget(self.ui.pushButton_add)
        # self.ui.pushButton_submit.clicked.connect(self.)
    
    # def load_name(self): 
    #     '''
    #     Загрузка информации о пользователе
    #     '''
    #     data_user = self.select_user(self.user)
    #     self.ui.label_name.setText(data_user[0])
        
    
    def load_products(self): 
        data = self.select_products()
        # вариант 1 
        # использование модели данных 
        # вариант хорош тем что можно изменять данные прямо в tableview
        # для работы нужен импорт модели
        # -------------------------------------------------------------------------
        # self.table_model = QStandardItemModel(len(data), len(data[0]), self)
        # for row, rowdata in enumerate(data): 
        #     for col, itemdata in enumerate(rowdata): 
        #         item = QStandardItem(str(itemdata))
        #         self.table_model.setItem(row, col, item)
        # self.ui.tableView_products.setModel(self.table_model)
        # -------------------------------------------------------------------------
                  
        # вариант 2 
        # обычное заполнение 
        # -------------------------------------------------------------------------
        # self.ui.tableWidget_products.setColumnCount(len(data[0]))  # Установите количество столбцов
        # self.ui.tableWidget_products.setRowCount(len(data))  # Установите количество строк

        # for row, rowData in enumerate(data):
        #     for col, itemData in enumerate(rowData):
        #         table_item = QTableWidgetItem(str(itemData))
        #         self.ui.tableWidget_products.setItem(row, col, table_item)
        # -------------------------------------------------------------------------
        
        # вариант 3 
        # В цикле создание label 
        # -------------------------------------------------------------------------
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setCentralWidget(central_widget)
        for product in data: 
            image_label = QLabel(self)
            name_label = QLabel(self)
            price_label = QLabel(self)
            
            name_label.setText(product[0])
            price_label.setText(str(product[3])) 
            if (isinstance(product[11],  str)): 
                pixmap = QPixmap('resources\/images\/' + product[11])
                image_label.setPixmap(pixmap)
                image_label.setScaledContents(True)
            else:
                pixmap = QPixmap('resources\/assets\/picture.png')  
                image_label.setPixmap(pixmap)
                image_label.setScaledContents(True) 

        # далее помещаем виджеты в layout
            layout.addWidget(image_label)
            layout.addWidget(name_label)
            layout.addWidget(price_label)
        # -------------------------------------------------------------------------


