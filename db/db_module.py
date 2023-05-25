import psycopg2 

class DataBase():
    '''
    Класс взаимодействия с БД
    ''' 
    def __init__(self) -> None:
        ... 

    def set_connect(self): 
        self.conn = psycopg2.connect(
            database='db_pots',
            user='postgres',
            password='hower19',
            host='localhost',
            port='5432'
        ) 
        
        self.cur = self.conn.cursor()
    
    def process_authorization(self, login, password): 
        '''
        param:
        return:  
        '''
        data = self.cur.execute(f"SELECT role_user FROM users WHERE login='{login}' AND password_log='{password}'")
        data = self.cur.fetchone()
        return data 
        
    def select_products(self): 
        data = self.cur.execute('SELECT * FROM products')
        data = self.cur.fetchall()
        return data 
    
    def select_user(self, user: str): 
        data = self.cur.execute(f"SELECT fio FROM users WHERE login='{user}'")
        data = self.cur.fetchone()
        return data
    
    def add_products(self): 
        self.cur.execute('')
        self.conn.commit()
    
    def update_products(self): 
        self.cur.execute('')
        self.conn.commit()
    
    def delete_products(self): 
        self.cur.execute('')
        self.conn.commit()
        