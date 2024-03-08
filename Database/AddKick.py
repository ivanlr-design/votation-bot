import pymysql
import pymysql.cursors
from utils.Log import Handler
def AddKick(connection : pymysql.connect, id : int, username : str, current_times : int, IsInDatabase : bool):
    times = current_times + 1
    cursor = connection.cursor()

    if IsInDatabase == True:
        consulta = "UPDATE kicked SET times = %s WHERE id = %s"
        VALUES = (int(times), int(id))

        try:
            cursor.execute(consulta, VALUES)
            connection.commit()
            return True
        except Exception as e:
            Handler.Error(f"DATABASE ERROR, failed to UPDATE kicked table!, error : {e}")
    else:
        consulta = "INSERT INTO kicked (id, discordname, times) VALUES (%s, %s, %s)"

        VALUES = (int(id), str(username), int(times),)

        try:
            cursor.execute(consulta, VALUES)
            connection.commit()
            return True
        except Exception as e:
            Handler.Error(f"DATABASE ERROR, failed to INSERT into kicked table!, error : {e}")


    
