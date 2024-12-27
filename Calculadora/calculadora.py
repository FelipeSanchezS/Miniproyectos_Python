import math

while True:
    #Solicitamos numeros
        Num1 = int(input("Ingrese el PRIMER numero a operar: "))
        Num2 = int(input("Ingrese el SEGUNDO numero a operar: "));


        print("-------------------------------")
        print("1 Suma")
        print("2 Resta")
        print("3 Multiplcación")
        print("4 División")
        print("5 Potencia")
        print("6 Salir")
        print("-------------------------------")
        Op=int(input("Ingrese la operacion a realizar: "))

        if Op == 1:
            print("Eligio la suma")
            print(f"La suma de {Num1} y {Num2} es: {Num1+Num2}")
        elif Op == 2:
            print("Eligio la resta")
            print(f"La resta de {Num1} y {Num2} es: {Num1-Num2}")
        elif Op == 3:
            print("Eligio la multiplicación")
            print(f"La multiplicación de {Num1} y {Num2} es: {Num1*Num2}")
        elif Op == 4:
            print("Eligio la división")
            if Num2 == 0:
                print("No es posible dividir entre 0")
            else:
                print(f"La división de {Num1} y {Num2} es: {Num1/Num2}")
        elif Op == 5:
            print("Eligio potenciación")
            print(f"La potencia de {Num1} a la {Num2} es: {Num1**Num2}")
        elif Op == 6:
             print("Saliendo del programa. ¡Gracias por usarlo!")
        break  # Rompe el bucle para salir del programa