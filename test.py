import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Entradas dinámicas")
        self.geometry("400x500")

        self.vars = []     # Lista de StringVar
        self.entries = []  # Lista de widgets Entry

        self.entries_frame = ctk.CTkFrame(self)
        self.entries_frame.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Añadir entrada", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self, text="Eliminar último", command=self.delete_last_entry)
        self.delete_button.pack(pady=5)

        self.show_button = ctk.CTkButton(self, text="Mostrar valores", command=self.show_values)
        self.show_button.pack(pady=5)

    def add_entry(self):
        new_var = tk.StringVar()
        new_entry = ctk.CTkEntry(self.entries_frame, textvariable=new_var)
        new_entry.pack(pady=5)
        self.vars.append(new_var)
        self.entries.append(new_entry)

    def delete_last_entry(self):
        if self.entries:
            last_entry = self.entries.pop()
            last_entry.destroy()
            self.vars.pop()

    def show_values(self):
        for i, var in enumerate(self.vars, start=1):
            print(f"Entrada {i}: {var.get()}")

app = App()
app.mainloop()