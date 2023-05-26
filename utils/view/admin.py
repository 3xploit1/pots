import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_admin import * 
from db.db_module import *


class Admin(QMainWindow, DataBase): 
    def __init__(self, user) -> None:
        super(Admin, self).__init__()
        self.ui = Ui_MainWindow_admin()
        self.ui.setupUi(self)
        self.set_connect()
        self.user = user
                
        self.load_name()
        self.load_products()
        # self.ui.verticalLayout_3.addChildWidget(self.ui.pushButton_submit)
        # self.ui.verticalLayout_3.addChildWidget(self.ui.pushButton_add)
        # self.ui.pushButton_submit.clicked.connect(self.)
    
    def load_name(self): 
        '''
        Загрузка информации о пользователе
        '''
        data_user = self.select_user(self.user)
        self.ui.label_fio.setText(data_user[0])
        pixmap = QPixmap('resources\/images\/' + data_user[1])
        self.ui.label_info_img.setPixmap(pixmap)
        self.ui.label_info_img.setScaledContents(True)
        
    
    def load_products(self): 
        self.tableWidget_products = QTableWidget()
        data = self.select_products()
        # вариант 1 
        # использование модели данных 
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
        # product_rows = len(data)
        # products_columns = len(data[0])
        # self.ui.tableWidget_products.setRowCount(product_rows)
        # self.ui.tableWidget_products.setColumnCount(products_columns)
        
        # for i in range(product_rows): 
        #     for j in range(products_columns): 
        #         item = QTableWidgetItem(f"{data[i][j]}")
        #         self.ui.tableWidget_products.setItem(i, j, item)
        # -------------------------------------------------------------------------
        
        # вариант 3 
        # В цикле создание label 
        # -------------------------------------------------------------------------

        # Создание главного виджета и компоновки
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # Создание QScrollArea для добавления колеса прокрутки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Создание контейнера (QWidget) для размещения списка продуктов
        container = QWidget()
        container_layout = QVBoxLayout(container)

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
            container_layout.addWidget(image_label)
            container_layout.addWidget(name_label)
            container_layout.addWidget(price_label)
        
        scroll_area.setWidget(container)

        # Добавление QScrollArea в основную компоновку
        layout.addWidget(scroll_area)

        self.setCentralWidget(main_widget)
        # -------------------------------------------------------------------------
        
                