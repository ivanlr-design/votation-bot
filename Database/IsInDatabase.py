import pymysql
import pymysql.cursors
from utils.Log import Handler
def IsInDatabase(connection: pymysql.connect, id : int):
    cursor = connection.cursor()

    consulta1 = "SELECT * FROM kicked WHERE id = %s"
    VALUES = (id, )

    try:
        cursor.execute(consulta1, VALUES)
        results = cursor.fetchall()
        if results:
            return True
        else:
            return False
        
    except Exception as e:
        Handler.Error(f"ERROR in IS IN DATABASE QUERY: {e}")
        return False