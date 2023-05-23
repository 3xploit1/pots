import psycopg2 

class DataBase():
    '''
    Класс взаимодействия с БД
    ''' 
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            database='db_pots',
            user='postgres',
            password='hower19',
            host='localhost',
            port='5432'
        ) 
        
        self.cur = self.conn.cursor()