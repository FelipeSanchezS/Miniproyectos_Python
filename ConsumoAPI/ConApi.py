import requests

#Importamos la URL de la API
URL= "https://pokeapi.co/api/v2/pokemon/"

#Creamos las variables de conexión
#Solicitamos que ingrese el nombre del pokemon
pokemon = input("Ingrese el nombre del pokemon: ")
respuesta = requests.get(URL + pokemon)

#Ingresamos en que formato queremos que nos nuestre los datos
datos = respuesta.json()

print(f"--------- Los movimientos de {pokemon} son: ---------")
for move in datos["moves"]:
    print(move["move"]["name"])

print(f"--------- el tipo de ataque pokemon con nombre {pokemon} es: ---------")
for type in datos["types"]:
    print(type["type"]["name"])