import customtkinter as ctk
import tkinter as tk
import ctypes

def create_toplevel():
    # Creamos el CTkToplevel
    top = ctk.CTkToplevel(root)
    top.geometry("300x200")
    top.title("Ventana sin minimizar ni cerrar")

    # Interceptar el cierre (desactivar el botón de cerrar)
    top.protocol("WM_DELETE_WINDOW", lambda: None)

    # Actualizamos para asegurarnos de que la ventana se haya creado
    top.update_idletasks()

    # Usar la API de Windows para modificar los estilos de la ventana.
    # Esto solo funciona en Windows.
    hwnd = ctypes.windll.user32.GetParent(top.winfo_id())

    GWL_STYLE    = -16
    WS_MINIMIZEBOX = 0x20000
    WS_MAXIMIZEBOX = 0x10000

    # Obtiene el estilo actual
    estilo_actual = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

    # Remover el botón de minimizar y de maximizar
    nuevo_estilo = estilo_actual & ~WS_MINIMIZEBOX & ~WS_MAXIMIZEBOX
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, nuevo_estilo)

    # Agregamos contenido de ejemplo al Toplevel
    label = ctk.CTkLabel(top, text="Botones deshabilitados")
    label.pack(pady=30)

# Ventana principal
root = ctk.CTk()
root.geometry("400x300")

open_button = ctk.CTkButton(root, text="Abrir Toplevel", command=create_toplevel)
open_button.pack(pady=50)

root.mainloop()