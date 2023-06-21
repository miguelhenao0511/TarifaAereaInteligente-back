from Connection_Postgresql import get_db


def crear_tabla():
    conn = get_db()
    cursor=conn.cursor()
    try:
        cursor.execute(
            """CREATE TABLE usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100),
                contraseña VARCHAR(100)
            )"""
        )
        conn.commit()
        conn.close()
        return {"mensaje": "tabla creada exitosamente"}
    except Exception as ex:
        print(ex)

print(crear_tabla())