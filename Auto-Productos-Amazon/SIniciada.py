##Importamos librerias
import io
import tkinter as tk
from tkinter import messagebox
import Include.generic as utl
import requests
import os
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from tkinter.font import BOLD


##Creamos la clase cuando se inicie sesión
class MasterPanel:
    #creación inicial de la ventana
    def __init__(self):
        ventana = tk.Tk()
        ventana.title("Personajes de Rick and Morty")
        ventana.geometry("800x600")

        # Scrollable frame
        canvas = tk.Canvas(ventana)
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas)

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Consumir la API
        url = "https://rickandmortyapi.com/api/character"
        response = requests.get(url).json()
        personajes = response["results"][:22]

        #Recorremos la información de cada personaje de interes
        for i, personaje in enumerate(personajes):
            nombre = personaje["name"]
            estado = personaje["status"]
            especie = personaje["species"]
            imagen_url = personaje["image"]
            genero = personaje["gender"]
            origen = personaje["origin"]["name"]

            # Descargar imagen
            imagen_bytes = requests.get(imagen_url).content
            imagen_pil = Image.open(io.BytesIO(imagen_bytes))
            imagen_pil = imagen_pil.resize((100, 100))
            imagen_tk = ImageTk.PhotoImage(imagen_pil)

            # Frame individual
            card = tk.Frame(frame, bg="white", bd=1, relief="solid", padx=10, pady=10)
    
            fila = i // 2  # División entera: 0, 0, 1, 1, 2, 2...
            columna = i % 2  # 0 o 1
            card.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

            label_img = tk.Label(card, image=imagen_tk)
            label_img.image = imagen_tk  # evitar garbage collection
            label_img.pack(side="left")

            #Mostramos la información
            texto = f"Nombre: {nombre}\nEstado: {estado}\nEspecie: {especie} \nGénero: {genero} \nOrigen: {origen}"
            label_info = tk.Label(card, text=texto, bg="white", justify="left")
            label_info.pack(side="left", padx=10)

        ventana.mainloop()