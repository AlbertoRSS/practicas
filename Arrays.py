import numpy as np
import os
import time 
os.system("cls")

print("******************************************")
print("Bienvenidos a La inmobiliaria “Casa Feliz”")
print("__________________________________________")
time.sleep(2)
os.system("cls")

depto_tipo_a = 0
cant_tipo_a = 0
depto_tipo_b = 0
cant_tipo_b = 0
depto_tipo_c = 0
cant_tipo_c = 0
depto_tipo_d = 0
cant_tipo_d = 0

listado_compradores = []
departamento = np.zeros((10,4),dtype=object)
a=1
for i in range(10):
    for j in range(1):
        departamento[i][0] = str(a) + "a"
        departamento[i][1] = str(a) + "b"
        departamento[i][2] = str(a) + "c"
        departamento[i][3] = str(a) + "d"
        a=a+1


def comprar_departamento():
    depto_tipo_a = 0
    cant_tipo_a = 0
    depto_tipo_b = 0
    cant_tipo_b = 0
    depto_tipo_c = 0
    cant_tipo_c = 0
    depto_tipo_d = 0
    cant_tipo_d = 0
    cont_departamento = 0
    while cont_departamento == 0:
        print(departamento)
        piso_tipo = input("ingrese el piso y el tipo de departamento que desea comprar:\n")
        os.system("cls")
        c=0
        for i in range(10):
            for j in range(4):
                if departamento[i][j] == piso_tipo:
                    departamento[i][j] = "X"
                    c = 1
                    print(departamento)
        if c == 0:
            print("El departamento no se encuentra disponible")
        else:
            piso_tipo = str(piso_tipo)
            if piso_tipo in ["1a","2a","3a","4a","5a","6a","7a","8a","9a","10a"]:
                depto_tipo_a = depto_tipo_a + 3800
                print("Departamentos Tipo A, 3.800 UF")
            elif piso_tipo in ["1b","2b","3b","4b","5b","6b","7b","8b","9b","10b"]:
                print("Departamentos Tipo B, 3.000 UF")
                depto_tipo_b = depto_tipo_b + 3000
                cant_tipo_b = cant_tipo_b + 1
            elif piso_tipo in ["1c","2c","3c","4c","5c","6c","7c","8c","9c","10c"]:
                print("Departamentos Tipo C, 2.800 UF")
                depto_tipo_c = depto_tipo_c + 2800
                cant_tipo_c = cant_tipo_c + 1
            elif piso_tipo in ["1d","2d","3d","4d","5d","6d","7d","8d","9d","10d"]:
                print("Departamentos Tipo D, 3.500 UF")
                depto_tipo_d = depto_tipo_d + 3500
                cant_tipo_d = cant_tipo_d + 1
            else:
                print("Piso y numero de departamento invalido")
            rut = input("Ingrese rut del comprador:\n")
            rut = rut.replace(".","").replace("-","") 
            rut = rut.lower()
            listado_compradores.append(rut)
            print("Operacion registrada con exito!!!")
            time.sleep(2)
            os.system("cls")
        cont = input("Desea realizar otra reserva?\n 1.SI | 2.NO")
        if cont == "1":
            cont_departamento == 0
        else:
            break
    return depto_tipo_a, cant_tipo_a 

def mostrar_departamentos():
    print(departamento)

def desplegar_listado():
    print("********************************************************")
    print("imprimiendo el listado de compradores de menor a mayor\n")
    time.sleep(3)
    os.system("cls")
    listado_compradores.sort()
    for i in listado_compradores:
        print(i)

def mostrar_ventas():
    print("****************************************")
    print("Descargando datos de ganancias totales\n")
    print(f"""
Tipo de departamento\tcantidad\ttotal
Tipo A {depto_tipo_a} UF\t\t  {cant_tipo_a}\t\t{depto_tipo_a * cant_tipo_a} UF
Tipo B {depto_tipo_b} UF\t\t  {cant_tipo_b}\t\t{depto_tipo_b * cant_tipo_b} UF
Tipo C {depto_tipo_c} UF\t\t  {cant_tipo_c}\t\t{depto_tipo_c * cant_tipo_c} UF
Tipo D {depto_tipo_d} UF\t\t  {cant_tipo_d}\t\t{depto_tipo_d * cant_tipo_d} UF """)

def salir():
    print("******************************************")
    print("Gracias por comprar en inmobiliaria “Casa Feliz”")
    print("__________________________________________")
    time.sleep(2)
    os.system("cls")
    print("Hasta pronto!!!")
            
            
while True:
    print("-----Menú Principal-----")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Por favor seleccione una opción: ")
    if opcion == "1":
        print("---Comprar departamentos")
        comprar_departamento()      
    elif opcion == "2":
        print("---Departamentos disponibles---")
        print(departamento)
        print("""Los precios de los departamentos, son los siguientes:
Tipo A, 3.800 UF
Tipo B, 3.000 UF
Tipo C, 2.800 UF
Tipo D, 3.500 UF """)
    elif opcion == "3":
        desplegar_listado()
    elif opcion == "4":
        mostrar_ventas()
    elif opcion == "5":
        salir()
    else:
        print("Opcion invalida. Por favor ingrese una opcion valida.")
