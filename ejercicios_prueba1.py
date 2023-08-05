import os
os.system("cls")
import time

amasado = 1500
molde = 1000
baguette = 2000
integral = 3000
total_amasado = 0
total_molde = 0
total_integral = 0
total_baguette = 0
can_molde = 0
can_baguette = 0
can_integral = 0
can_amasado = 0
print("Bienvenido a pan delivery")
time.sleep(2)
os.system("cls")
while True:
    try:
        total_amasado = total_amasado
        total_molde = total_molde
        total_baguette = total_baguette
        total_integral = total_integral
        can_molde = can_molde
        can_amasado = can_amasado
        can_baguette =  can_baguette
        can_integral = can_integral
        seleccion = int(input("""Por favor seleccione la opcion:
    1) Amasado $1.500 
    2) Molde $1.000 
    3) Baguette $2.000 
    4) Integral $3.000
    5) Ir a pagar
    6) Salir del menu\n"""))

        if seleccion > 0 and seleccion <= 6:
            if seleccion == 1:
                can_amasado = int(input("Por favor ingrese la cantidad:\n"))
                time.sleep(1)
                os.system("cls")
                total_amasado = total_amasado + (amasado * can_amasado)
                print(f"has seleccionado pan amasado el precio es de {amasado} la cantidad es de {can_amasado} el total acumulado es de {total_amasado}")
                seguir = int(input("Deseas seguir ordenando..? 1) si 2) no\n"))
                if seguir == 2:
                    False
            elif seleccion == 2:
                can_molde = int(input("Por favor ingrese la cantidad:\n"))
                time.sleep(1)
                os.system("cls")
                total_molde = total_molde + (molde * can_molde)
                print(f"has seleccionado pan molde el precio es de {molde} la cantidad es de {can_molde} el total acumulado es de {total_molde}")
                seguir = int(input("Deseas seguir ordenando..? 1) si 2) no\n"))
                if seguir == 2:
                    False
            elif seleccion == 3:
                can_baguette = int(input("Por favor ingrese la cantidad:\n"))
                time.sleep(1)
                os.system("cls")
                total_baguette = total_baguette + (baguette * can_baguette)
                print(f"has seleccionado pan baguette el precio es de {baguette} la cantidad es de {can_baguette} el total acumulado es de {total_baguette}")
                seguir = int(input("Deseas seguir ordenando..? 1) si 2) no\n"))
                if seguir == 2:
                    False
            elif seleccion == 4:
                can_integral = int(input("Por favor ingrese la cantidad:\n"))
                time.sleep(1)
                os.system("cls")
                total_integral = total_integral + (integral * can_integral)
                print(f"has seleccionado pan integral el precio es de {integral} la cantidad es de {can_integral} el total acumulado es de {total_integral}")
                seguir = int(input("Deseas seguir ordenando..? 1) si 2) no\n"))
                if seguir == 2:
                    False
            elif seleccion == 5:
                can_amasado = can_amasado
                can_molde = can_molde
                can_baguette = can_baguette
                can_integral = can_integral
                print(f"""//////////////////////Factura////////////////////////\n
    tipo            cantidad           precio      total 
    Pan amasado         {can_amasado}              1500        {total_amasado}
    Pan molde           {can_molde}              1000        {total_molde}
    Pan baguette        {can_baguette}              2000        {total_baguette}
    Pan integral        {can_integral}              3000        {total_integral}
                                        _______________
                                        total a pagar {total_amasado + total_baguette + total_integral + total_molde}
                                        
            Gracias por su compra! vuelva pronto.""")
                break
            elif seleccion == 6:
                print("gracias, vuelva pronto!!!")
                break
        else:
            print("No existe esa opcion")
            time.sleep(2)
            os.system("cls")
    except:
        print("Ha ocurrido un error al ingresar la opción")
        time.sleep(2)
        os.system("cls")
            


            





            

