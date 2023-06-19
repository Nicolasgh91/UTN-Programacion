import sqlite3

#Creo la tabla
with sqlite3.connect("config/galaxy_best_players.db") as conexion:
    try:
        query = '''
            create table if not exists jugadores (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
        '''
        conexion.execute(query)
        conexion.commit()
        print("Tabla creada exitosamente")

    except sqlite3.OperationalError:
        print("La tabla no se creo")



