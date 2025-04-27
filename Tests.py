import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x200")
root.title("Ejemplo de Placeholder en CTkEntry")

# Crear un CTkEntry con placeholder_text
entry = ctk.CTkEntry(root, placeholder_text="Ingresa tu texto aquí", width=200)
entry.pack(pady=20)

root.mainloop()