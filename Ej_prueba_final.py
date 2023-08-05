# pip install numpy (para instalar numpy)

import numpy as np
import os
import time
os.system('cls')

print("*************************")
print("Bienvenido a Vuelos-Duoc")
print("________________________")
time.sleep(2)
os.system("cls")

datos_cliente = []
avion=np.zeros((7,6), dtype=object)
a=1
for i in range(7):
    for j in range(6):
        avion[i][j]= str(a)
        a=a+1

def comprar_asiento():
    cont_asientos= 0
    while cont_asientos == 0:
        print(avion)
        asiento = input(" ¿Qué asiento desea comprar?\n")
        c=0
        for i in range(7):
            for j in range(6):
                if avion[i][j] == asiento:
                    avion[i][j] = "X"
                    print(avion)
                    c = 1
        if c == 0:
            print("ASIENTO OCUPADO")
        else:
            asiento = int(asiento)
            if asiento > 0 and asiento < 31:
                print("Asientos normales $78.900")
                precio = 78900
            else:
                print("Asientos VIP $240.000")
                precio = 240000
            nombre = input("Ingrese el nombre del pasajero: ")
            rut = input("Ingrese el RUT del pasajero: ")
            telefono = input("Ingrese el teléfono del pasajero: ")
            banco = input("Ingrese el banco del pasajero: ")
            if banco.lower() == "bancoduoc":
                precio = precio - (precio * 0.15)
            datos_cliente.append([nombre,rut,telefono,banco,asiento,precio])
            print("Asiento reservado")
            time.sleep(1)
            os.system("cls") 
                  
        cont = input("desea seguir comprando?n\ 1.- SI 2. NO\n")
        if cont == "1":
            cont_asientos == 0
        else:
            break

def anular_vuelo ():
    anular = input("Ingrese en numero de asiento que desea anular")
    y = 0
    numero = 1
    for y in range(7):
        x = 0
        for x in range(6):
            if int(anular) == numero:
                avion[y][x]=anular
            numero = numero + 1
            x = x + 1
        y = y + 1
    for i in datos_cliente:
        if anular == str(i[4]):
            datos_cliente.remove(i)
    print("Vuelo anulado")
    time.sleep(1)
    os.system("cls") 

def modificar_datos_pasajero():
    rut_persona = input("Ingrese el rut de la persona a modificar: ")
    for i in datos_cliente:
        if rut_persona == i[1]:
            modify = input("""Digite "0" para cambiar el nombre |||| "2" para cambiar el telefono:\n""")
            if modify in ["0", "2"]:
                if modify == "0":
                    nuevo_nombre = input("Ingrese el nombre del nuevo pasajero: ")
                    i[0] = nuevo_nombre
                    print("Nombre modificado correctamente.")
                elif modify == "2":
                    nuevo_telefono = input("Ingrese el número de teléfono del nuevo pasajero: ")
                    i[2] = nuevo_telefono
                    print("Teléfono modificado correctamente.")
            else:
                print("Opción inválida.")
            return
    print("El rut ingresado no se encuentra en la lista de datos_cliente.")

def salir ():
    print("*************************")
    print("Gracias por viajar en Vuelos-Duoc")
    print("________________________")
    print("Hasta pronto!!!")
    time.sleep(3)
    os.system("cls")
while True:
    print("\n--- Menú Principal ---")
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Asientos Disponibles ---")
        print(avion)
        print("Asientos normales $78.900 | del 1 al 30")
        print("Asientos VIP $240.000 | del 31 al 42")
    elif opcion == "2":
        print("\n--- Comprar Asiento ---")
        comprar_asiento()
    elif opcion == "3":
        print("\n--- Anular Vuelo ---")
        anular_vuelo()
    elif opcion == "4":
        print("\n--- Modificar Datos de Pasajero ---")
        modificar_datos_pasajero()
    elif opcion == "5":
        salir()
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


