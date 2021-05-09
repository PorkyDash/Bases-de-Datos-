import psycopg2

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(host="localhost",port="5432",dbname="proyecto_bucaramanga",user="postgres",password="postgres")
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()