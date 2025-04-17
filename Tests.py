import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear el Treeview
tree = ttk.Treeview(root, columns=("Col1", "Col2"))
tree.heading("#0", text="Índice")
tree.heading("Col1", text="Columna 1")
tree.heading("Col2", text="Columna 2")
tree.grid(row=0, column=0, sticky="nsew")  # Ubicar el Treeview

# Añadir algunos datos de ejemplo
for i in range(20):
    tree.insert("", "end", text=f"Item {i+1}", values=(f"Dato1-{i+1}", f"Dato2-{i+1}"))

# Crear el Scrollbar directamente vinculado al Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")  # Ubicar el Scrollbar al lado del Treeview

# Asociar el Treeview con el Scrollbar
tree.configure(yscrollcommand=scrollbar.set)

# Ajustar el diseño de la ventana principal
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()