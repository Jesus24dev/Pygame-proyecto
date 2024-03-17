import pymysql

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def crearConexion(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def mostrarDatos(self,query, cantidad):
        with self.crearConexion().cursor() as cursor:
            if(cantidad):        
                cursor.execute(query)
                return cursor.fetchone()
            else:
                cursor.execute(query)
                return cursor.fetchall()
    
    def guardarDatos(self, query):
        conexion = self.crearConexion()
        with conexion.cursor() as cursor:
            cursor.execute(query)
        conexion.commit()

    def actualizarDatos(self, query):
        conexion = self.crearConexion()
        with conexion.cursor() as cursor:
            cursor.execute(query)
        conexion.commit()

    def eliminarDatos(self, query):
        conexion = self.crearConexion()
        with conexion.cursor() as cursor:
            cursor.execute(query)
        conexion.commit()
