import pymysql
import pymysql.cursors

def Setup(connector: pymysql.connect):
    cursor = connector.cursor()
    consulta1 = "CREATE TABLE IF NOT EXISTS admins (id BIGINT NOT NULL, discordname VARCHAR(32) NOT NULL)"

    cursor.execute(consulta1)
    try:
        connector.commit()
        
    except Exception as e:
        return str(e)
    
    consulta2 = "CREATE TABLE IF NOT EXISTS kicked (id BIGINT NOT NULL, discordname VARCHAR(32) NOT NULL, times INT NOT NULL)"

    cursor.execute(consulta2)
    try:
        connector.commit()
    except Exception as e:
        return str(e)
    
    return True