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