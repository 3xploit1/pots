from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_admin import * 
from db.db_module import *

class Admin(QMainWindow, DataBase): 
    def __init__(self) -> None:
        super(Admin, self).__init__()
        self.ui = Ui_MainWindow_admin
        self.ui.setupUi(self)
        
    def load(self): 
        '''
        Загрузка данных из БД
        '''
        products = self.select_products()
        
        # вариант 1 
        # использование модели данных 
        # вариант хорош тем что можно изменять данные прямо в tableview
        # для работы нужен импорт модели
        # -------------------------------------------------------------------------
        # from PySide2.QtGui import QStandardItemModel
        # table_model = QStandardItemModel(len(products), len(products[0]), self)
        # for row, rowdata in enumerate(products): 
        #     for col, itemdata in enumerate(rowdata): 
        #         item = QStandardItemModel(str(itemdata))
        #         table_model.setItem(row, col, item)
        # # помещаем модель в tableview 
        # table_view = QTableView(self)
        # table_view.setModel(table_model)
        # -------------------------------------------------------------------------
        
        # вариант 2 
        # обычное заполнение 
        # -------------------------------------------------------------------------
        # table_widget = QTableWidget(self)
        # table_widget.setColumnCount(len(products[0]))  # Установите количество столбцов
        # table_widget.setRowCount(len(products))  # Установите количество строк

        # for row, rowData in enumerate(products):
        #     for col, itemData in enumerate(rowData):
        #         table_item = QTableWidgetItem(str(itemData))
        #         table_widget.setItem(row, col, table_item)
        # -------------------------------------------------------------------------
        
        # вариант 3 
        # В цикле создание label 
        # -------------------------------------------------------------------------
        # for product in products: 
        #     image_label = QLabel(self)
        #     name_label = QLabel(self)
        #     price_label = QLabel(self)
            
        #     pixmap = QPixmap()
        #     image_label.setPixmap(pixmap)
        #     image_label.setScaledContents(True)
            
        #     name_label.setText(product)
        #     price_label.setText(str(product)) 
        # далее помещаем виджеты в layout
        #     horizont = QHBoxLayout()
        #     horizont.addWidget(image_label)
        #     horizont.addWidget(name_label)
        #     horizont.addWidget(price_label)
        # -------------------------------------------------------------------------


