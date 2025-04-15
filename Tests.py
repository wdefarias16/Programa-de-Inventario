<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_items = tree.selection()
    for item in selected_items:
        item_data = tree.item(item)
        print("Seleccionado:", item_data)

root = tk.Tk()
root.title("Ejemplo de Treeview")

# Configurar el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2"))
tree.heading("#0", text="Nombre")
tree.column("#0", width=150, anchor="w")
tree.heading("col1", text="Descripción")
tree.column("col1", width=100, anchor="center")
tree.heading("col2", text="Valor")
tree.column("col2", width=80, anchor="center")
tree.bind("<<TreeviewSelect>>", on_select)

# Insertar datos a nivel raíz
folder1 = tree.insert("", "end", text="Carpeta 1", values=("Info Carpeta", "001"))
folder2 = tree.insert("", "end", text="Carpeta 2", values=("Otro Info", "002"))

# Insertar datos con jerarquía (ítems hijos)
tree.insert(folder1, "end", text="Archivo 1A.txt", values=("Detalle A", "101"))
tree.insert(folder1, "end", text="Archivo 1B.txt", values=("Detalle B", "102"))
tree.insert(folder2, "end", text="Documento 2A.pdf", values=("Detalle C", "201"))

# Agregar scrollbar vertical
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Posicionar widgets
tree.pack(side="left", expand=True, fill="both")
vsb.pack(side="right", fill="y")

root.mainloop()
=======
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
>>>>>>> e62cb9d98ca936f8e9e8418f5bfb85b59b0bdf81
