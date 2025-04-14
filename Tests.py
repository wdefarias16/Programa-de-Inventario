from customtkinter import *

# Inicializar la ventana
root = CTk()
root.title("Ejemplo CTkOptionMenu")

# Función a ejecutar al seleccionar una opción
def mostrar_seleccion(opcion):
    print(f"Has seleccionado: {opcion}")

# Crear el CTkOptionMenu
opciones = ["Opción 1", "Opción 2", "Opción 3"]
menu_opciones = CTkOptionMenu(root, values=opciones, command=mostrar_seleccion)
menu_opciones.pack(pady=20)

root.mainloop()