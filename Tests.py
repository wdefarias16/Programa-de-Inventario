import customtkinter as ctk

# Función para borrar el texto cuando el usuario hace clic
def on_entry_click(event):
    if entry.get() == "Usuario":
        entry.delete(0, "end")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Usuario")

# Crear ventana
root = ctk.CTk()
root.geometry("300x200")

# Crear Entry con texto predeterminado
entry = ctk.CTkEntry(root)
entry.insert(0, "Usuario")
entry.pack(pady=20)

password = ctk.CTkEntry(root)
password.insert(0, "password")
password.pack(pady=20)


# Asociar eventos
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)

# Ejecutar la ventana
root.mainloop()