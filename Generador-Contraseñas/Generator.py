import string;
import random;

#Agregamos todso los simbolos, letras y numeros de odnde se creara la contraseña 
caracteres = string.ascii_letters + string.digits + string.punctuation

while True:
    try:
        #Variable para la longitud
        longitud = int(input("Ingrese la longitud de la contraseña, recuerda que debe ser mayor a 8: "));

        if (longitud <= 7 ):
            print("La longitud de los caracteres debe ser mayor a 8, intente nuevamente");

        else:
            #Elije caracteres aleatorios que esten dentro de la variable caracteres
            contraseña = "".join(random.choice(caracteres)for i in range(longitud));
            print("La contraseña generada por el sistema es: "+ contraseña)

    except ValueError:
        print("Ingrese la longitud nuevamente")
