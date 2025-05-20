import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import threading
import time

class BuscarArticuloGUI:
    ##Se crea la interfaz para que se realicen las busquedas
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Buscar artículos")
        self.root.geometry("800x600")
        self.root.config(bg="#f0f0f0")

        #Sección de buscar el articulo
        tk.Label(self.root, text="Buscar artículo:", font=("Arial", 14)).pack(pady=10)
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=50)
        self.entry.pack(pady=5)

        #Boton de buscar
        btn = tk.Button(self.root, text="Buscar", command=self.iniciar_busqueda, font=("Arial", 12), bg="#3a7ff6", fg="white")
        btn.pack(pady=10)

        #Sección de resultados
        self.resultados = tk.Text(self.root, font=("Arial", 12), wrap=tk.WORD)
        self.resultados.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.root.mainloop()

        #Función para iniciar la búsqueda
    def iniciar_busqueda(self):
        articulo = self.entry.get().strip()
        if articulo:
            self.resultados.delete(1.0, tk.END)
            thread = threading.Thread(target=self.buscar_en_amazon, args=(articulo,))
            thread.start()

        #Función para realizar la busqueda en amazon
    def buscar_en_amazon(self, articulo):
        try:
            #Ruta del chromedriver y de configuraciones
            service = Service("C:\\Users\\pipe-\\Downloads\\136.0.7103.49 chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-software-rasterizer")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
            )

            driver = webdriver.Chrome(service=service, options=options)

            driver.get(f"https://www.amazon.com/s?k={articulo}")
            time.sleep(3)

            productos = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')[:10]

            for prod in productos:
                # Título
                try:
                    titulo = prod.find_element(By.XPATH, './/h2//span').text
                except:
                    titulo = "Sin título"

                # Precio
                try:
                    precio_entero = prod.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
                    precio_decimal = prod.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text
                    precio = f"${precio_entero}.{precio_decimal}"
                except:
                    precio = "Sin precio"

                self.root.after(0, lambda t=titulo, p=precio: self.resultados.insert(tk.END, f"{t}\nPrecio: {p}\n\n"))

            driver.quit()
        except Exception as e:
            self.root.after(0, lambda: self.resultados.insert(tk.END, f"Error en la búsqueda: {e}"))
