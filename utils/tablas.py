Class Jugador():
    def __init__(self, juego, nickname, clave, avatar):
        self.juego = 'FLAT WORLD'
        self.nickname = nickname
        self.clave = clave
        self. avatar = avatar

    def ingresarDatos(self):
        query = f'INSERT INTO jugador (JUEGO, NICKNAME, CLAVE, ID_AVATAR) values({self.juego, self.nickname, self.clave, self.avatar})'
        return query

    def mostrarDatos(self):
        query = 'SELECT ID_JUGADOR, NICKNAME, CLAVE, ID_AVATAR FROM jugador'
        return query
    
    def actualizarDatos(self, nickname, clave, avatar):
        query = f'UPDATE jugador SET (NICKNAME, CLAVE, ID_AVATAR) = ({nickname}, {clave}, {avatar}) where NICKNAME = {self.nickname}'
        return query

    def borrarDatos(self):
        query = f'DELETE FROM jugador WHERE NICKNAME = {nickname}'
        return query 

Class Nivel():
    def __init__(self, juego, descripcion, nombre, dificultad, objetivos, puntajeMaximo):
        self.juego = 'FLAT WORLD'
        self.descripcion = descripcion
        self.nombre = nombre
        self.dificultad = dificultad
        self.objetivos = objetivos
        self.puntajeMaximo = puntajeMaximo

    def ingresarDatos(self):
        query = f'INSERT INTO nivel (JUEGO, DESCRIPCION, NOMBRE, DIFICULTAD, OBJETIVOS, PUNTAJE_MAXIMO) values({self.juego, self.descripcion, self.nombre, self.dificultad, self.objetivos self.puntajeMaximo})'
        return query

    def mostrarDatos(self):
        query = 'SELECT ID_NIVEL, DESCRIPCION, NOMBRE, DIFICULTAD, OBJETIVOS, PUNTAJE MAXIMO FROM nivel'
        return query
    
    def actualizarDatos(self, descripcion, nombre, dificultad, objetivos, puntajeMaximo, ID_NIVEL):
        query = f'UPDATE nivel SET (DESCRIPCION, NOMBRE, DIFICULTAD, OBJETIVOS, PUNTAJE_MAXIMO) = ({descripcion}, {nombre}, {dificultad}, {objetivos}, {puntajeMaximo}) where ID_NIVEL = {ID_NIVEL}'
        return query

    def borrarDatos(self, ID_NIVEL):
        query = f'DELETE FROM nivel WHERE ID_NIVEL = {ID_NIVEL}'
        return query 

Class DatosJuego():
    def __init__(self, juego, id_jugador, aciertos, fallos, precision, niveles_completados, puntaje_total): 
        self.juego = 'FLAT WORLD'
        self.id_jugador = id_jugador
        self.aciertos = aciertos
        self.fallos = fallos
        self.precision = precision
        self.niveles_completados = niveles_completados
        self.puntaje_total puntaje_total

    def ingresarDatos(self):
        query = f'INSERT INTO datos_juego (JUEGO, ID_JUGADOR, ACIERTOS, FALLOS, PRECISION, NIVELES_COMPLETADOS, PUNTAJE_TOTAL) values({self.juego, self.id_jugador, self.aciertos, self.fallos, self.precision, self.niveles_completados, self.puntaje_total})'
        return query

    def mostrarDatos(self):
        query = 'SELECT ID_DATOS, ID_JUGADOR, ACIERTOS, FALLOS, PRECISION, NIVELES_COMPLETADOS, PUINTAJE_TOTAL FROM datos_juego'
        return query
    
    def actualizarDatos(self, ID_JUGADOR):
        query = f'UPDATE datos_juego SET (ACIERTOS, FALLOS, PRECISION, NIVELES_COMPLETADOS, PUNTAJE_TOTAL) = ({self.aciertos}, {self.fallos}, {self.precision}, {self.niveles_completados}, {self.puntaje_total}) where ID_JUGADOR = {ID_JUGADOR}'
        return query

    def borrarDatos(self, ID_DATOS):
        query = f'DELETE FROM datos_juego WHERE ID_DATOS = {ID_DATOS}'
        return query 

Class ProgresoNivel():
    def __init__(self, id_jugador, id_nivel, puntaje, estado): 
        self.juego = 'FLAT WORLD'
        self.id_jugador = id_jugador
        self.id_nivel = id_nivel
        self.puntaje = puntaje
        self.estado = estado

    def ingresarDatos(self):
        query = f'INSERT INTO progreso_nivel (ID_JUGADOR, ID_NIVEL, PUNTAJE, ESTADO) values ({self.id_jugador, self.id_nivel, self.puntaje, self.estado})'
        return query

    def mostrarDatos(self):
        query = 'SELECT ID_PROGRESO, ID_JUGADOR, ID_NIVEL, PUNTAJE, ESTADO FROM progeso_nivel'
        return query
    
    def actualizarDatos(self, ID_JUGADOR):
        query = f'UPDATE progreso_nivel SET (PUNTAJE, ESTADO) = ({self.puntaje}, {self.estado}) where ID_JUGADOR = {ID_JUGADOR}'
        return query

    def borrarDatos(self, ID_DATOS):
        query = f'DELETE FROM progreso_nivel WHERE ID_PROGRESO = {ID_PROGRESO}'
        return query 