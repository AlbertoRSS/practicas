import os
os.system("cls")
import time
      

print("Bienvenido a club de deportes “Buena Ventura”")
time.sleep(3)
os.system("cls")
menores = 2500
cont_menores = 0
total_menores = 0
nom_menores = "Menores"
adultos = 5000
cont_adulto = 0
total_adultos = 0
nom_adultos = "Adultos"
adultos_mayores = 1000
cont_adult_mayores = 0
total_adult_mayores = 0
nom_adult_mayores = "Adultos mayores"
des_menores = 0.1
des_adultos= 0.05
  

while True:
    try:
        seleccion = int(input("""Por favor seleccione una opcion de compra
Tipo Entrada          Detalle           Precio
1) Menores             De 5 a 12 años      $2.500
2) Adultos             De 13 a 64 años     $5.000
3) Adultos Mayores     Desde 65 y más      $1.000
4) imprimir boleta
5) Anular compra
6) salir del menu\n"""))
        os.system("cls")
        if seleccion > 0 and seleccion < 7:
            if seleccion == 1:
                print("///Menores de 5 a 12 años///")
                can_menores = int(input("Por favor ingrese la cantidad de entradas:\n"))
                os.system("cls")
                total_menores = total_menores + (can_menores * menores)
                cont_menores = cont_menores + can_menores
                seguir_comprando = int(input("Desea seguir comprando..? 1) si 2) no:\n"))
                os.system("cls")
                print("Devuelta al menu inicial")
                time.sleep(1)
                os.system("cls")
            elif seleccion == 2:
                print("///Adultos de 13 a 64 años///")
                can_adultos = int(input("Por favor ingrese la cantidad de entradas:\n"))
                os.system("cls")
                total_adultos = total_adultos + (can_adultos * adultos)
                cont_adulto = cont_adulto + can_adultos
                seguir_comprando = int(input("Desea seguir comprando..? 1) si 2) no:\n"))
                os.system("cls")
                print("Devuelta al menu inicial")
                time.sleep(1)
                os.system("cls")
            elif seleccion == 3:
                print("///Adultos Mayores desde 65 años y más///")
                can_adultos_mayores = int(input("Por favor ingrese la cantidad de entradas:\n"))
                os.system("cls")
                total_adult_mayores = total_adult_mayores + (can_adultos_mayores * adultos_mayores)
                cont_adult_mayores = cont_adult_mayores + can_adultos_mayores
                seguir_comprando = int(input("Desea seguir comprando..? 1) si 2) no:\n"))
                os.system("cls")
                print("Devuelta al menu inicial")
                time.sleep(1)
                os.system("cls")
            elif seleccion == 4:
                print("Imprimiendo su boleta")
                time.sleep(1)
                os.system("cls")
                break
            elif seleccion == 5:
                print("Su compra fue anulada:\n")
                time.sleep(1)
                os.system("cls")
                can_menores = 0
                total_menores = 0
                cont_menores = 0
                can_adultos = 0
                total_adultos = 0
                cont_adulto = 0
                can_adult_mayores = 0
                total_adult_mayores = 0
                cont_adult_mayores = 0
            elif seleccion == 6:
                print("Gracias por visitarnos, tenga un excelente día!!!")
                time.sleep(2)
                os.system("cls")
                break
        else:
            print("Opcion invalida debe ser entre 1 y 6")
            time.sleep(2)
            os.system("cls")
    except:
        os.system("cls")
        print("Ha ocurrido un error, ha seleccionado una letra o un campo que no esta en las opciones")
        time.sleep(2)
        os.system("cls")
        print("Reiniciando el sistema")
        time.sleep(1)
        os.system("cls")
while seleccion == 4:
    try:
        print("""
Solo por los dias viernes acumula un descuento especial en ciertas entradas:

"Menores De 5 a 12 años  10% de descuento"
"Adultos de 13 a 64 años 5% de descuento"\n """)
        dia = input("Por favor ingresa el dia de asistencia\n")
        os.system("cls")
        dia = dia.lower()
        if dia == "viernes":
            print(f"""
                            Entradas
______________________________________________________________________
Cantidad                Tipo                precio
    {cont_menores}                  {nom_menores}              {total_menores}
    {cont_adulto}                  {nom_adultos}              {total_adultos}
    {cont_adult_mayores}              {nom_adult_mayores}         {total_adult_mayores}
_____________________________________________________________________
Subtotal:                                      {total_menores + total_adultos + total_adult_mayores}
Descuentos:                                    {round(total_menores * des_menores) + round(total_adultos * des_adultos)}
_____________________________________________________________________
Total a pagar                                  {total_menores + total_adultos + total_adult_mayores - (round(total_menores * des_menores) + round(total_adultos * des_adultos))}
        
        Gracias por su compra, disfrute el torneo!!!""")
            break
        elif dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "sabado" or dia == "domingo":
            print(f"""
                            Entradas
______________________________________________________________________
Cantidad                Tipo                precio
    {cont_menores}                  {nom_menores}                {total_menores}
    {cont_adulto}                  {nom_adultos}                {total_adultos}
    {cont_adult_mayores}               {nom_adult_mayores}           {total_adult_mayores}
_____________________________________________________________________
Subtotal:                                     {total_menores + total_adultos + total_adult_mayores}
Descuentos:                                   {0}
_____________________________________________________________________
Total a pagar                                 {total_menores + total_adultos + total_adult_mayores}

        Gracias por su compra, disfrute el torneo!!!""")
            break
        else:
            print("La opcion de dia es incorrecta, debe ser de lunes a domingo")
            time.sleep(2)
            os.system("cls")
    except:
        print("Opcion invalida")


                




                