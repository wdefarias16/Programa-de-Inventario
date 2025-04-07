import customtkinter as ctk

# Configuración inicial
ventana = ctk.CTk()
ventana.geometry("400x200")
ventana.title("Separar Widgets con pack")

# Frame contenedor
frame = ctk.CTkFrame(ventana, width=400, height=100, corner_radius=0)
frame.pack(fill="x", pady=20)

# Widgets dentro del frame
widget_izquierda = ctk.CTkLabel(frame, text="Izquierda", fg_color="blue")
widget_izquierda.pack(side="left", padx=20)

widget_derecha = ctk.CTkLabel(frame, text="Derecha", fg_color="green")
widget_derecha.pack(side="right", padx=20)

ventana.mainloop()
