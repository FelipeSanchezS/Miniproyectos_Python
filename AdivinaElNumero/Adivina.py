import random

#Establecemos rangos
minimo = int(input("Ingrese el numero minimo del rango del numero a crear "))
maximo = int(input("Ingrese el numero maximo del rango del numero a crear "))

#Maquina crea el numero al azar
numero_azar = random.randint(minimo, maximo)
print(numero_azar)

#Creamos contador de intentos
intentos = 0

while True:
    intentos = intentos+1;
    numero_usuario = int(input(f"Ingrese el numero que cree y pueda ser, entre {minimo} y {maximo}: "))

    if(numero_usuario > numero_azar):
        print("El nunmero ingresado esta por encima del numero creado al azar")
    elif(numero_usuario < numero_azar):
        print("El nunmero ingresado esta por debajo del numero creado al azar")
    else:
        break;

print("Numero correcto!!!")
print("La cantidad de intentos usados fueron "+ str(intentos))
