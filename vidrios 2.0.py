import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageDraw

class CapturadorImagen:
    def __init__(self, ventana, camara_index=0):
        self.ventana = ventana
        self.ventana.title("Capturador de Imágenes")

        self.camara_index = camara_index
        self.camara = cv2.VideoCapture(camara_index)

        self.label_imagen = ttk.Label(self.ventana)
        self.label_imagen.pack(padx=10, pady=10)

        self.boton_capturar = ttk.Button(self.ventana, text="Capturar Imagen", command=self.capturar_imagen)
        self.boton_capturar.pack(pady=10)

        self.direccion_entry = ttk.Entry(self.ventana, width=40)
        self.direccion_entry.pack(pady=5)

        self.boton_seleccionar = ttk.Button(self.ventana, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.boton_seleccionar.pack(pady=10)

        self.actualizar_imagen_camara()

    def capturar_imagen(self):
        ret, imagen = self.camara.read()

        if not ret:
            print("No se pudo capturar la imagen.")
            return

        direccion = self.direccion_entry.get()
        if not direccion:
            print("La dirección de la carpeta no se ha especificado.")
            return

        nombre_archivo = f'{direccion}/imagen_capturada.jpg'
        cv2.imwrite(nombre_archivo, imagen)

        self.mostrar_imagen(nombre_archivo)

    def mostrar_imagen(self, nombre_archivo):
        imagen = Image.open(nombre_archivo)
        imagen = ImageTk.PhotoImage(imagen)

        self.label_imagen.config(image=imagen)
        self.label_imagen.image = imagen

    def seleccionar_carpeta(self):
        carpeta_seleccionada = filedialog.askdirectory(title="Seleccionar Carpeta")
        self.direccion_entry.delete(0, tk.END)
        self.direccion_entry.insert(0, carpeta_seleccionada)

    def actualizar_imagen_camara(self):
        ret, frame = self.camara.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            imagen = Image.fromarray(frame_rgb)
            imagen = ImageTk.PhotoImage(imagen)

            self.label_imagen.config(image=imagen)
            self.label_imagen.image = imagen

        self.ventana.after(10, self.actualizar_imagen_camara)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = CapturadorImagen(ventana_principal)
    ventana_principal.mainloop()
class VentanaDibujo:
    def __init__(self, imagen_path):
        self.ventana = tk.Toplevel()
        self.ventana.title("Herramientas de Dibujo")

        self.imagen_path = imagen_path

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.imagen = Image.open(imagen_path)
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen_tk)
        self.canvas.bind("<B1-Motion>", self.dibujar)

    def dibujar(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill="red", width=2)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = CapturadorImagen(ventana_principal)
    ventana_principal.mainloop()
def capturar_imagen(self):
    ret, imagen = self.camara.read()

    if not ret:
        print("No se pudo capturar la imagen.")
        return

    direccion = self.direccion_entry.get()
    if not direccion:
        print("La dirección de la carpeta no se ha especificado.")
        return

    nombre_archivo = f'{direccion}/imagen_capturada.jpg'
    cv2.imwrite(nombre_archivo, imagen)

    self.mostrar_imagen(nombre_archivo)


    VentanaDibujo(nombre_archivo)
