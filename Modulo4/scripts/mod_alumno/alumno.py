from ingreso_datos import ingreso_numero_decimal
import sqlite3

class Alumno:
    aprobado = True
    def __init__(self, nombre_alumno) -> None:
        self.nombre = nombre_alumno
        self.listado_notas = [
            self.ingreso_nota('Ingrese la 1ra nota: '),
            self.ingreso_nota('Ingrese la 2da nota: '),
            self.ingreso_nota('Ingrese la 3ra nota: ')
        ]
        self.promedio_notas = sum(self.listado_notas)/3
        self.aprobado = self.bool_aprobado()
        pass

    def ingreso_nota(self, msg:str):
        try:
            nota = ingreso_numero_decimal(msg=msg)
            assert nota<=10 and nota>=0
            return nota
        except:
            print('Nota invalida, vuelva a intentar!!!')
            return self.ingreso_nota(msg)

    def bool_aprobado(self):
        """Indica 1 si alumno aprobado o 0 si alumno desaprobado"""
        prom_notas = self.promedio_notas
        if prom_notas >=6:
            return 1
        return 0
    
    def registrar_alumno(self, ruta_bd):
        """Se encarga del registro del alumno en la base de datos"""

        registros_alumnos = [
            (self.nombre, *self.listado_notas, self.aprobado),
        ]

        # Inserto registros 
        with sqlite3.connect(ruta_bd) as conexion:
            cursor = conexion.cursor()
            # Ahora utilizamos el método executemany() para insertar varios
            cursor.executemany("INSERT INTO alumnos(nombre,nota1,nota2, nota3, aprobo) VALUES (?,?,?, ?, ?)", registros_alumnos)
            # Guardamos los cambios haciendo un commit
            conexion.commit()
        print('Se registraron datos alumno ...')
        self.imprimir_alumno()

    def imprimir_alumno(self):
        print(f'Nombre_alumno: {self.nombre}\nNotas: {self.listado_notas}\nAprobo: {self.aprobado}')

