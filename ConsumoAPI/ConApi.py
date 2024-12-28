import requests

#Importamos la URL de la API
URL= "https://pokeapi.co/api/v2/pokemon/"

#Creamos las variables de conexión
#Solicitamos que ingrese el nombre del pokemon
pokemon = input("Ingrese el nombre del pokemon: ")
respuesta = requests.get(URL + pokemon)

#Ingresamos en que formato queremos que nos nuestre los datos
datos = respuesta.json()

#Creamos el archivo .xtx
with open(f"{pokemon}.txt", "w", encoding="utf-8") as archivo:
    print(f"--------- Los movimientos de {pokemon} son: ---------")
    archivo.write(f"--------- Los movimientos de {pokemon} son: --------- \n")#titulo de sección de las habilidades en el archivo txt
    for move in datos["moves"]:
        print(move["move"]["name"])
        archivo.write(move["move"]["name"] + "\n") #Tomamos la ruta de donde esta el dato que queremos capturatr la información
        

    print(f"--------- el tipo de ataque pokemon con nombre {pokemon} es: ---------")
    archivo.write(f"--------- el tipo de ataque pokemon con nombre {pokemon} es: --------- \n")#titulo de sección de las habilidades en el archivo txt
    for type in datos["types"]:
        print(type["type"]["name"])
        archivo.write(type["type"]["name"] + "\n")#Tomamos la ruta de donde esta el dato que queremos capturatr la información


    print(f"--------- Las estadisticas del pokemon {pokemon} son: ---------")
    archivo.write(f"--------- Las estadisticas del pokemon {pokemon} son: --------- \n")#titulo de sección de las habilidades en el archivo txt
    for stat in datos["stats"]:
        print(stat["stat"]["name"])
        archivo.write(f"{stat['stat']['name']}: {stat['base_stat']}\n")#Tomamos la ruta de donde esta el dato que queremos capturatr la información

#Mostramos y descargamos el archivo con la información ingresada y capturada
print(f"La información del Pokémon {pokemon.capitalize()} se ha guardado en el archivo '{pokemon}.txt'.")
