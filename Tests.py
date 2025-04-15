import customtkinter as ctk
import tkinter as tk

# Diccionario de ejemplo
lineas_grupos = {
    "000": {"linea": "sin linea", "grupo": []},
    "001": {"linea": "Linea 1", "grupo": ["Grupo 1"]},
    "002": {"linea": "Linea 2", "grupo": ["Grupo 2"]}
}

# Crear la lista de opciones en el formato deseado "Código - Nombre de línea"
opciones = [f"{codigo} - {datos['linea']}" for codigo, datos in lineas_grupos.items()]

# Crear la ventana principal
root = ctk.CTk()
root.geometry("400x200")
root.title("Ejemplo de OptionMenu y Entry")

# Variables de control
# Esta variable se usa para actualizar el valor en el Entry
codigo_var = tk.StringVar()

# Callback que se ejecuta al seleccionar una opción del OptionMenu
def opcion_seleccionada(valor):
    # Separamos la cadena en la posición del guion y tomamos el primer elemento (el código)
    codigo = valor.split(" - ")[0]
    # Actualizamos el Entry con el código extraído
    codigo_var.set(codigo)

# Crear el OptionMenu: pasar la lista de valores y asignar el callback
option_menu = ctk.CTkOptionMenu(root, values=opciones, command=opcion_seleccionada)
option_menu.pack(pady=20)

# Crear el Entry en el que se mostrará el código extraído
entry_codigo = ctk.CTkEntry(root, textvariable=codigo_var, width=200)
entry_codigo.pack(pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()
