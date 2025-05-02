import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont




# Configuración inicial de la aplicación
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de color

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ejemplo CTk con Barra de Menú")
        self.geometry("500x300")
        font_menu = tkFont.Font(family="Roboto", size=12)
        self.option_add("*Menu*Font", font_menu)
        # Crear menú principal
        menu_bar = tk.Menu(self)

        # Crear menú "Archivo"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)

        # Crear menú "Edición"
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Copiar")
        edit_menu.add_command(label="Pegar")
        edit_menu.add_command(label="Cortar")

        # Crear menú "Ayuda"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.mostrar_acerca_de)

        # Agregar menús al menú principal
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        menu_bar.add_cascade(label="Edición", menu=edit_menu)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)

        # Configurar la ventana con el menú
        self.config(menu=menu_bar)

    def nuevo_archivo(self):
        print("Nuevo archivo creado")

    def abrir_archivo(self):
        print("Abrir archivo")

    def guardar_archivo(self):
        print("Guardar archivo")

    def mostrar_acerca_de(self):
        print("Aplicación de ejemplo con CustomTkinter")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()