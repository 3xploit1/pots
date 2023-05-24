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
    
    def __del__(self): 
        self.conn.close()
    
    def process_authorization(self, login, password): 
        self.cur.execute(f'SELCT role FROM users WHERE login={login} AND password_log={password}')
        self.cur.fetchone()
        
    def select_products(self): 
        self.cur.execute('SELECT * FROM products')
        self.cur.fetchall()
    
    def add_products(self): 
        self.cur.execute('')
        self.conn.commit()
    
    def update_products(self): 
        self.cur.execute('')
        self.conn.commit()
    
    def delete_products(self): 
        self.cur.execute('')
        self.conn.commit()
        