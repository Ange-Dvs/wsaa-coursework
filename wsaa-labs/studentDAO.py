import mysql.connector 
from config import DB_CONFIG  # Import database config from config.py file


class StudentDAO:      
    def __init__(self):
        self.host = DB_CONFIG["host"]         
        self.user = DB_CONFIG["user"]         
        self.password = DB_CONFIG["password"]         
        self.database = DB_CONFIG["database"]        
        
    def getCursor(self):          
        self.connection = mysql.connector.connect(
            host=self.host,             
            user=self.user,             
            password=self.password,
            database=self.database
            )       
        self.cursor = self.connection.cursor()         
        return self.cursor      
    
    def closeAll(self):         
        self.connection.close()         
        self.cursor.close()          
        
    def create(self, values):         
        cursor = self.getCursor()         
        sql="insert into student (firstname, age) values (%s,%s)"         
        cursor.execute(sql, values)          
        self.connection.commit()         
        newid = cursor.lastrowid         
        self.closeAll()         
        return newid      
    
    def getAll(self):         
        cursor = self.getCursor()         
        sql="select * from student" 
        cursor.execute(sql) 
        result_all = cursor.fetchall() 
        self.closeAll()         
        return result_all     
        
    def findByID(self, id):   
        cursor = self.getCursor()   
        sql = "SELECT * FROM student WHERE id = %s"
        values = (id,)  
        cursor.execute(sql, values) 
        result_byID = cursor.fetchone()  # Fetch one row
        self.closeAll()  
        return result_byID  # Returns a dictionary or None
    
    def update(self, values):   
        cursor = self.getCursor()  
        sql = "UPDATE student SET firstname = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()  
        return True  # Indicate success     
        
    def delete(self, id):   
        cursor = self.getCursor()  
        sql = "DELETE FROM student WHERE id = %s"
        values = (id,)  
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()  
        return True  # Indicate success
    
studentDAO = StudentDAO() 