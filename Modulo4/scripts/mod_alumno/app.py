"""

Realizar una función que permita la carga de n alumnos. 
Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas. 
Las notas deben estar comprendidas entre 0 y 10. 

Registrar cada alumno en la base de datos alumnos


Leer de la base de datos todos los alumnos
"""

from ingreso_datos import ingreso_numero_entero
from alumno import Alumno
import sqlite3

opciones = """
Elija una opcion:
1) Registrar alumnos1
2) Imprimir listado a alumnos

"""

def mostrar_listado_alumnos(ruta_bd):
    with sqlite3.connect(ruta_bd) as conexion:
        cursor = conexion.cursor()
        # Recuperamos los registros de la tabla de usuarios
        cursor.execute("SELECT * FROM alumnos")

        # Recorremos todos los registros con fetchall
        # y los volcamos en una lista de usuarios
        listado_alumnos = cursor.fetchall()

    # Ahora podemos recorrer todos los usuarios
    for alumno in listado_alumnos:
        print(alumno)
    pass


ruta_db = r'/workspaces/ProgramacionPython202401/Modulo4/pythondb.db'

def main():

    while True:

        respuesta = input(opciones)

        if respuesta == '1':
            n = ingreso_numero_entero(msg='Ingrese la cantidad de alumnos a registrar: ')

            for i in range(n):
                print('----------------------------------------')
                nombre = input(f'ingrese nombre Alumno {i}: ')
                objalumno = Alumno(nombre)
                objalumno.registrar_alumno(ruta_db)
        elif respuesta == '2':
            mostrar_listado_alumnos(ruta_db)
        else:
            print('saliendo del menu')
            break
    pass


if __name__ == '__main__':

    main()




