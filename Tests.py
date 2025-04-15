<<<<<<< HEAD
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
=======
import os
import json
import customtkinter as ctk
import tkinter as tk
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class LineasGrupos:
    def __init__(self, filename="Data/Lineas.json"):
        self.filename = filename
        self.lineas_grupos = {}
        self.load_lines()  # Carga automáticamente los datos al inicializar la clase

    def load_lines(self):
        """Carga el diccionario de líneas y grupos desde el archivo JSON."""
        # Crear la carpeta 'Data' si no existe
        if not os.path.exists("Data"):
            os.makedirs("Data")

        try:
            with open(self.filename, "r") as file:
                self.lineas_grupos = json.load(file)
        except FileNotFoundError:
            # Si el archivo no existe, inicializamos el diccionario y lo guardamos
            self.lineas_grupos = {}
            self.save_lines()

    def save_lines(self):
        """Guarda el diccionario de líneas y grupos en el archivo JSON."""
        with open(self.filename, "w") as file:
            json.dump(self.lineas_grupos, file, indent=4)

    def get_line_names(self):
        """Devuelve una lista de nombres de líneas con su código, por ejemplo: '001 - Bebidas'."""
        return [f"{codigo} - {info['linea']}" for codigo, info in self.lineas_grupos.items()]

    def add_line(self, codigo, linea, grupo=None):
        """
        Agrega una nueva línea si el código y la línea no existen.
        :param codigo: Código único de la línea (se maneja como cadena).
        :param linea: Nombre de la línea.
        :param grupo: (Opcional) Una lista o un grupo inicial. Si no se pasa nada, se usa lista vacía.
        :return: True si se agregó correctamente, False si ya existía.
        """
        codigo = str(codigo)  # Aseguramos que el código sea cadena
        if codigo in self.lineas_grupos:
            print("El código ya se encuentra registrado.")
            return False

        # Opcional: Verificar si el nombre también existe (para evitar duplicados)
        for info in self.lineas_grupos.values():
            if info["linea"].strip().lower() == linea.strip().lower():
                print("El nombre de la línea ya existe.")
                return False

        # Si no se especifica grupo, se inicializa con una lista vacía
        if grupo is None:
            grupo = []

        self.lineas_grupos[codigo] = {"linea": linea, "grupo": grupo}
        self.save_lines()  # Guarda los cambios
        print("Nueva línea agregada correctamente.")
        return True

    def add_group_to_line(self, codigo, grupo):
        """
        Agrega un grupo a la línea indicada.
        :param codigo: Código de la línea a la que se le agregará el grupo.
        :param grupo: Nombre del grupo a agregar.
        :return: True si se agregó, False en caso contrario.
        """
        codigo = str(codigo)
        if codigo not in self.lineas_grupos:
            print("El código indicado no existe.")
            return False

        self.lineas_grupos[codigo]["grupo"].append(grupo)
        self.save_lines()
        print(f"Grupo '{grupo}' añadido a la línea {codigo}.")
        return True

# Ejemplo de integración con una interfaz creada con customtkinter:
class LineasGruposProg(ctk.CTkFrame):
    def __init__(self, parent, line_manager: LineasGrupos):
        super().__init__(parent)
        self.line_manager = line_manager  # referencia a la instancia de LineasGrupos

        # TITULO
        title_frame = ctk.CTkFrame(self, corner_radius=5, fg_color=APP_COLORS[3])
        title_frame.pack(fill='x')
        title = ctk.CTkLabel(
            title_frame,
            text='Carga de líneas y grupos',
            bg_color='transparent',
            text_color=APP_COLORS[0],
            height=50,
            font=FONTS[0]
        )
        title.pack()

        # FRAME PARA LINEAS
        lines_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=APP_COLORS[0])
        lines_frame.pack(expand=True, fill='both', side='left')
        for row in range(5):
            lines_frame.rowconfigure(row, weight=1)
        for col in range(5):
            lines_frame.columnconfigure(col, weight=1)

        # Etiqueta e inputs para agregar línea
        label_lin = ctk.CTkLabel(lines_frame, text='Líneas', font=FONTS[0])
        label_lin.grid(row=0, column=2, sticky='nw', pady=20, padx=5)

        # Opción de menú con las líneas existentes
        self.lin_menu = ctk.CTkOptionMenu(lines_frame, values=self.line_manager.get_line_names())
        self.lin_menu.grid(row=1, column=1, sticky='swe', pady=5)

        # Entrada para el código de línea
        self.codigo_var = tk.IntVar()
        lin_entry = ctk.CTkEntry(lines_frame, textvariable=self.codigo_var)
        lin_entry.grid(row=1, column=2, sticky='swe', pady=5)

        label_lin_cod = ctk.CTkLabel(lines_frame, text='Código de línea', font=FONTS[1])
        label_lin_cod.grid(row=1, column=3, sticky='sw', padx=5)

        # Entrada para el nombre de la línea
        self.nombre_var = tk.StringVar()
        lin_entry_nom = ctk.CTkEntry(lines_frame, textvariable=self.nombre_var)
        lin_entry_nom.grid(row=2, column=2, sticky='nwe')

        label_lin_nom = ctk.CTkLabel(lines_frame, text='Nombre de línea', font=FONTS[1])
        label_lin_nom.grid(row=2, column=3, sticky='nw', padx=5)

        # Botón para agregar la línea
        addl_btn = ctk.CTkButton(lines_frame, text='Agregar', font=FONTS[0], command=self.agregar_lineas)
        addl_btn.grid(row=3, column=2)

        # (Aquí iría la sección de grupos, similar en estructura)

    def agregar_lineas(self):
        """Función llamada al presionar el botón 'Agregar' para líneas."""
        codigo = self.codigo_var.get()
        nombre = self.nombre_var.get().strip()

        if not codigo or not nombre:
            print("Debe ingresar un código y un nombre válidos.")
            return

        # Agrega la línea usando el método de la instancia de LineasGrupos
        if self.line_manager.add_line(codigo, nombre):
            # Si se agregó, actualizamos el menú con las nuevas líneas
            nuevas_lineas = self.line_manager.get_line_names()
            self.lin_menu.configure(values=nuevas_lineas)
        else:
            print("No se pudo agregar la línea.")

# Uso general:
if __name__ == "__main__":
    # Creamos una instancia de la clase que gestiona las líneas y grupos.
    line_manager = LineasGrupos()

    # Configuración de la ventana principal con customtkinter
    root = ctk.CTk()
    root.title("Programa de Líneas y Grupos")
    root.geometry("800x600")

    app = LineasGruposProg(root, line_manager=line_manager)
    app.pack(expand=True, fill='both')

    root.mainloop()
>>>>>>> 0cc25e7d4c0cd6e94ffe2d4c9fe3e901c1db2a9c
