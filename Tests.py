import tkinter as tk
from tkinter import ttk

def obtener_info(event):
    # Obtener el ID del ítem seleccionado
    item_id = tree.selection()[0]
    # Obtener la información del ítem
    info = tree.item(item_id)
    print("Texto:", info["text"])
    print("Valores:", info["values"])

# Crear ventana principal
root = tk.Tk()
root.title("TreeView Ejemplo")

# Crear TreeView
tree = ttk.Treeview(root, columns=("Columna1", "Columna2"), show="headings")
tree.heading("Columna1", text="Columna 1")
tree.heading("Columna2", text="Columna 2")

# Agregar ítems
tree.insert("", "end", text="Item1", values=("Valor1", "Valor2"))
tree.insert("", "end", text="Item2", values=("Valor3", "Valor4"))

tree.pack()

# Asociar evento de selección
tree.bind("<<TreeviewSelect>>", obtener_info)

root.mainloop()