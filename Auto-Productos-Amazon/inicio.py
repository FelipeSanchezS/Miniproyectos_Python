import tkinter as tk
from tkinter import messagebox, ttk
import Include.generic as utl
from tkinter.font import BOLD
from SIniciada import MasterPanel
from busqueda_gui import BuscarArticuloGUI
from PIL import Image, ImageTk
#from selenium import webdriver

# Creamos la clase
class App:

    def verificar_usuario(self):
    # Aquí iría la lógica para verificar el usuario y la contraseña
    # Por ahora, solo mostramos un mensaje de éxito
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()

        if usuario == "admin" and contraseña == "admin":
            self.ventana.destroy()
            MasterPanel()
        elif usuario == "root" and contraseña == "root":
            self.ventana.destroy()
            BuscarArticuloGUI()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        def verificar_usuario(self):
            usuario = self.usuario.get()
            contraseña = self.contraseña.get()


    def __init__(self):
        # Creamos ventana inicial
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("800x500")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        # Logo
        # Solo el nombre del archivo (o subruta dentro de Img si hay carpetas)
        logo = utl.leer_imagen("logo.png", (200, 200))

        
        # Frame
        frame_logo = tk.Frame(self.ventana, bg="#3a7ff6", bd=0, width=300, relief=tk.SOLID, padx=10, pady=10)
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#3a7ff6")
        label.image = logo  # MUY IMPORTANTE para evitar que Python lo elimine del garbage collector
        label.place(x=0, y=0, relwidth=1, relheight=1)

        #Sección de la derecha
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        #Parte superior derecha - titulo
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#FFFFFF")
        frame_form_top.pack(side="top", fill=tk.X)
        label_titulo = tk.Label(frame_form_top, text="Iniciar sesión", bg="#FFFFFF", fg="#3a7ff6", font=("Arial", 20))
        label_titulo.pack(expand=tk.YES, fill=tk.BOTH, pady=20)

        #Parte de los datos, contenedor de los campos de entrada
        frame_form_fill = tk.Frame(frame_form, height=50, bg="#ffffff", bd=0, relief=tk.SOLID)
        frame_form_fill.pack(side="top", fill=tk.BOTH, expand=tk.YES, pady=(40, 0))  # <- Aquí lo bajamos con pady


        # Etiquetas y campos de entrada - USUARIO
        ##Primera dos lineas, sección de ubicación el titulo usuario
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", bg="#fcfcfc", fg="#3a7ff6", font=("Arial", 12), justify=tk.CENTER, anchor="w")
        etiqueta_usuario.pack(pady=5, padx=20)
        ##Segundas dos lineas, sección campo de entrada de usuario
        self.usuario = ttk.Entry(frame_form_fill, font=("Arial", 12), justify=tk.CENTER)
        self.usuario.pack(pady=10, padx=40, fill=tk.X)

        # Etiquetas y campos de entrada - CONTRASEÑA
        ##Primera dos lineas, sección de ubicación el titulo password
        etiqueta_contraseña = tk.Label(frame_form_fill, text="Contraseña", bg="#fcfcfc", fg="#3a7ff6", font=("Arial", 12), justify=tk.CENTER, anchor="w")
        etiqueta_contraseña.pack(pady=5, padx=20)
        ##Segundas dos lineas, sección campo de entrada de contraseña
        self.contraseña = ttk.Entry(frame_form_fill, font=("Arial", 12), justify=tk.CENTER, show="*")
        self.contraseña.pack(pady=10, padx=40, fill=tk.X)
        self.contraseña.config(show="*")

        # Botón de inicio de sesión
        boton_iniciar = tk.Button(frame_form_fill, text="Iniciar sesión", bg="#3a7ff6", fg="#FFFFFF", font=("Arial", 12, BOLD), height=2)
        boton_iniciar.pack(pady=45, padx=40, fill=tk.X)
        #Conectamos el boton a la función de verificación creada anteriormente
        boton_iniciar.bind("<Button-1>", lambda event: self.verificar_usuario())

        
        # Finalmente, iniciamos el bucle
        self.ventana.mainloop()
