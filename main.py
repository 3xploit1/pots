import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from utils.view.start import *

class Application(): 
    def __init__(self) -> None:
        ... 

    def main(self) -> None:  
        '''
        Создание и вызов объекта авторизации
        '''       
        app = QApplication(sys.argv)
        window = Start()
        window.show()
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    app = Application()
    app.main()