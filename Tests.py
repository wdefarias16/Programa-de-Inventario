import customtkinter as ctk
from PIL import Image, ImageTk

# Crear la ventana principal
app = ctk.CTk()
app.geometry("400x400")

# Cargar la imagen con Pillow
imagen_pillow = Image.open("tu_imagen.png")  # Cambia "tu_imagen.png" por la ruta de tu imagen
imagen_pillow = imagen_pillow.resize((200, 200))  # Opcional: redimensionar la imagen
imagen_ctk = ImageTk.PhotoImage(imagen_pillow)  # Convertir la imagen para Tkinter

# Crear el Label y asignarle la imagen
label = ctk.CTkLabel(app, image=imagen_ctk, text="")  # El texto vacío es para evitar que aparezca texto junto a la imagen
label.pack(pady=20)

app.mainloop()

#********************************

# Cargar la imagen
imagen = Image.open("tu_imagen.png")

# Definir nuevo ancho
nuevo_ancho = 300
relacion_aspecto = imagen.height / imagen.width
nuevo_alto = int(nuevo_ancho * relacion_aspecto)  # Calculando la altura proporcional

# Redimensionar la imagen
imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

# Guardar la imagen modificada
imagen_redimensionada.save("imagen_redimensionada.png")