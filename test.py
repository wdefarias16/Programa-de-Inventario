import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")

# Crear el CTkTextbox
textbox = ctk.CTkTextbox(app, width=300, height=150)
textbox.pack(pady=20)

# Función para obtener el texto
def obtener_texto():
    contenido = textbox.get("1.0", "end").strip()  # .strip() para quitar saltos de línea extra
    print("Texto ingresado:", contenido)

# Botón para activar la lectura del texto
boton = ctk.CTkButton(app, text="Obtener texto", command=obtener_texto)
boton.pack(pady=10)

app.mainloop()
