from Connection_Postgresql import get_db




def insertar_usuario():
    conn = get_db()
    cursor=conn.cursor()
    try:
        insert_sql = """
                    INSERT INTO usuarios (nombre,email,contraseña)
                    VALUES (%s, %s,%s);
                    """
        cursor.execute(insert_sql, ("Miguel", "miguel@gmail.com","45685"))
        conn.commit()
        conn.close()
        return {"mensaje": "Usuario ingresado correctamente"}
    
    except Exception as ex:
        print(ex)

print(insertar_usuario())


