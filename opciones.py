import pymysql.cursors
from tabulate import tabulate

def case_1(conexion):
    print("Opción 1")

def case_2(conexion):
    case_7(conexion)
    nombreTabla = input("Ingrese nombre de la tabla: ")
    cursor = conexion.cursor()
    describeTable(conexion,nombreTabla)
    insert_query = f"INSERT INTO {nombreTabla} (id, name) VALUES (%s, %s)"
    id = input("Ingrese id: ")
    nombre = input("Ingrese nombre: ")
    values = (id, nombre)  
    cursor.execute(insert_query, values)
    conexion.commit() 

def case_3(conexion):
    print("Opción 3")

def case_4(conexion):
    print("Opción 4")

def case_5(conexion):
    cursor = conexion.cursor()
    cursor.execute("select * from cliente")
    tablas = cursor.fetchall()
    print("Info en la base de datos:")
    for tabla in tablas:
        print(tabla)
    input("teclea para continuar")

def case_6(conexion):
    print("Opción 6")

def case_7(conexion):
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()  
    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla)
    input("teclea para continuar")
    
def case_8(conexion):
    print("Conexion Cerrada")
    conexion.close()
    exit()

def describeTable(conexion,nombreTabla):
    cursor = conexion.cursor()
    cursor.execute(f"DESCRIBE {nombreTabla}")
    infoTabla = cursor.fetchall()
    header = ["Celda", "Tipo", "Null", "Key", "Default", "Extra"]
    table_data = []
    for info in infoTabla:
        table_data.append(info)
    print(tabulate(table_data, headers=header, tablefmt="grid"))

def default_case():
    print("Opción por defecto")

switch_dict = {
    1: case_1,
    2: case_2,
    3: case_3,
    4: case_4,
    5: case_5,
    6: case_6,
    7: case_7,
    8: case_8,
}