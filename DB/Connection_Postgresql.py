import psycopg2


def get_db():
    try:
        connection =psycopg2.connect(
            host="localhost",
            user="postgres",
            password="1939Enigma**#",
            database="Modelo_RN"
        )
        """print("connexion exitosa")
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM version()")
        row=cursor.fetchone()
        print(row)"""
        return connection
    except Exception as ex:
        print(ex)
    #finally:
    #    connection.close()
    #    print("Conexion finalizada.")