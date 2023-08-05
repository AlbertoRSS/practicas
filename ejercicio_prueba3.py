import os
os.system("cls")
import time

ENT_I = "Infantil"
ENT_G = "General"
ENT_M = "Adulto Mayor"
valor_final_i, valor_final_g, valor_final_m = 0, 0, 0
cont_i, cont_g, cont_m = 0, 0, 0
total_i, total_g, total_m = 0, 0, 0
fin = True
d_i, d_g, d_m = True, True, True
anul_i, anul_g, anul_m = True, True, True
continue_i, continue_g, continue_m = True, True, True
menu = True

while menu == True:
    print("Bienvenido al menú de compra del club deportivo Buena Ventura")
    print("Venta de entradas para las finales del torneo interescolar")
    print("Las opciones de entradas son las siguientes:")
    print("(1) Entrada Infantil (De 5 a 12 años)")
    print("(2) Entrada General (De 13 a 64 años)")
    print("(3) Entrada Adulto Mayor (Desde 65 años)")
    print("(4) Finalizar compra")
    try:
        opcion = int(input("Ingrese una opción:\n"))
        if (opcion > 0 and opcion <5):
            if (opcion == 1):
                print("Entrada Infantil")
                print("Valor $2500 c/u")
                valor_i = 2500
                cant_i = int(input("Ingrese cantidad de entradas:\n"))
                valor_final_i = valor_i * cant_i
                cont_i = cont_i + cant_i
                while d_i == True:
                    print("Entradas para encuentros de día viernes tienen descuento de un 10%")
                    dia_i = int(input("Indique día del encuentro:\n(1) Lunes\n(2) Martes\n(3) Miércoles\n(4) Jueves\n(5) Viernes\n(6) Sábado\n(7) Domingo\n"))
                    if (dia_i > 0 and dia_i < 8):
                        if (dia_i == 5):
                            DSCTO_I = 0.9
                            valor_final_i = valor_i * DSCTO_I * cant_i
                            d_i = False
                        elif (dia_i == 1 or dia_i == 2 or dia_i == 3 or dia_i == 4 or dia_i == 6 or dia_i == 7):
                            valor_final_i = valor_i * cant_i
                            d_i = False
                    else:
                        print("Ingrese una opción válida.")
                while anul_i == True:
                    anular = int(input("¿Desea confirmar la compra?\n(1) Sí\n(2) No\n"))
                    if (anular > 0 and anular < 3):
                        if (anular == 1):
                            valor_final_i = valor_final_i
                            total_i = total_i + cont_i
                            anul_i = False
                        elif (anular == 2):
                            valor_final_i = 0
                            cont_i = 0
                            total_i = total_i + cont_i
                            anul_i = False
                    else:
                        print("Ingrese una opción válida.")  
            elif opcion == 2:
                print("Entrada General")
                print("Valor $5000 c/u")
                valor_g = 5000
                cant_g = int(input("Ingrese cantidad de entradas:\n"))
                valor_final_g = valor_g * cant_g
                cont_g = cont_g + cant_g
                while d_g == True:
                    print("Entradas para encuentros de día viernes tienen descuento de un 5%")
                    dia_g = int(input("Indique día del encuentro:\n(1) Lunes\n(2) Martes\n(3) Miércoles\n(4) Jueves\n(5) Viernes\n(6) Sábado\n(7) Domingo\n"))
                    if (dia_g > 0 and dia_g < 8):
                        if (dia_g == 5):
                            DSCTO_G = 0.95
                            valor_final_g = valor_g * DSCTO_G * cant_g
                            d_g = False
                        elif (dia_g == 1 or dia_g == 2 or dia_g == 3 or dia_g == 4 or dia_g == 6 or dia_g == 7):
                            valor_final_g = valor_g * cant_g
                            d_g = False
                    else:
                        print("Ingrese una opción válida.")
                while anul_g == True:
                    anular = int(input("¿Desea confirmar la compra?\n(1) Sí\n(2) No\n"))
                    if (anular > 0 and anular < 3):
                        if (anular == 1):
                            valor_final_g = valor_final_g
                            total_g = total_g + cont_g
                            anul_g = False
                        elif (anular == 2):
                            valor_final_g = 0
                            cont_g = 0
                            total_g = total_g + cont_g
                            anul_g = False
                    else:
                        print("Ingrese una opción válida.")
            elif opcion == 3:
                print("Entrada Adulto Mayor")
                print("Valor $1000 c/u")
                valor_m = 1000
                cant_m = int(input("Ingrese cantidad de entradas:\n"))
                valor_final_m = valor_m * cant_m
                cont_m = cont_m + cant_m
                while d_m == True:
                    dia_m = int(input("Indique día del encuentro:\n(1) Lunes\n(2) Martes\n(3) Miércoles\n(4) Jueves\n(5) Viernes\n(6) Sábado\n(7) Domingo\n"))
                    if (dia_m > 0 and dia_m < 8):
                        d_m = False
                    else:
                        print("Ingrese una opción válida.")
                while anul_m == True:
                    anular = int(input("¿Desea confirmar la compra?\n(1) Sí\n(2) No\n"))
                    if (anular > 0 and anular < 3):
                        if (anular == 1):
                            valor_final_m = valor_final_m
                            total_m = total_m + cont_m
                            anul_m = False
                        elif (anular == 2):
                            valor_final_m = 0
                            cont_m = 0
                            total_m = total_m + cont_m
                            anul_m = False
                    else:
                        print("Ingrese una opción válida.")
            elif opcion == 4:
                while fin == True:
                    finalizar = int(input("¿Desea finalizar la compra?\n(1) Sí\n(2) No\n"))
                    if (finalizar > 0 and finalizar < 3):
                        if (finalizar == 1):
                            fin = False
                            menu = False
                        elif (finalizar == 2):
                            fin = False
                    else:
                        print("Ingrese una opción válida.")
    except:
        print("Opción inválida, vuelva a ingresar.")

os.system("cls")
print("Boleta Buena Ventura")
print("Entradas")
print("------------------------------------------------------------")
print(f"Entradas {ENT_I}        : {total_i}                 $ {valor_final_i}")
print(f"Entradas {ENT_G}         : {total_g}                 $ {valor_final_g}")
print(f"Entradas {ENT_M}    : {total_m}                 $ {valor_final_m}")
print("------------------------------------------------------------")
    