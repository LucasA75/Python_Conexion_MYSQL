import pymysql.cursors
from opciones import switch_dict
from decouple import config
import sys

while True:
    try:
        myConexion = pymysql.connect(user=config("USER"), password=config("PASS"), database=config("DATABASE"))
        if myConexion:
            print("Conexión establecida correctamente.")
            print("###################################")
            print("Opciones disponibles: \n Opcion 1 = Crear Tabla \n Opcion 2 = Ingresar datos \n Opcion 3 = Modificar Datos \n Opcion 4 = Eliminar datos \n Opcion 5 = Mostrar Todos los datos \n Opcion 6 = Eliminar Tabla \n Opcion 7 = Mostrar todas las tablas \n Opcion 8 = Salir \n")
            print("###################################")
            num = int(input("Ingrese el número de la opción que deseas: "))
            if num in switch_dict:
                switch_dict[num](myConexion)
                sys.stdout.flush()
            cursor = myConexion.cursor()
            
    except pymysql.Error as e:
        print("Error durante la conexión:", e)

