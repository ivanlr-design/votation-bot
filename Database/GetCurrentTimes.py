import pymysql
import pymysql.cursors

def Times(connection: pymysql.connect, id : int):
    cursor = connection.cursor()

    try:
        consulta = "SELECT * FROM kicked WHERE id = %s"
        VALUES = (id, )
        cursor.execute(consulta, VALUES)
        resultados = cursor.fetchall()
        if resultados:
            return resultados[0]['times']
        else:
            return 0
    except: 
        return 0