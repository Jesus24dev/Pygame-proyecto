import os

# Obtener la ruta actual del directorio
directorio_actual = os.getcwd()

# Nombre del archivo .bat
nombre_bat = "flatworld.bat"

# Ruta completa del archivo .bat
ruta_bat = os.path.join(directorio_actual, nombre_bat)

# Comando para ejecutar el programa Python
comando_python = "python juego.py"

# Contenido del archivo .bat
contenido_bat = f'@echo off\n{comando_python}'

# Escribir el contenido en el archivo .bat
with open(ruta_bat, "w") as archivo_bat:
    archivo_bat.write(contenido_bat)

print(f"El archivo {nombre_bat} se ha creado exitosamente en {directorio_actual}.")