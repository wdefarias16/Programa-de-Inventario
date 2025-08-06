import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import INVENTARIO

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class FacturacionPlace(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Facturación con Imágenes")
        self.geometry("840x620")
        self.image_refs = {}  # Guarda las referencias a PhotoImage

        # --- Barra de búsqueda ---
        self.search_var = tk.StringVar()
        self.search_entry = ctk.CTkEntry(
            master=self,
            textvariable=self.search_var,
            fg_color=APP_COLOR['gray'],
            border_color=APP_COLOR['gray'],
            width=300,
            height=32
        )
        self.search_entry.place(x=20, y=20)
        self.search_entry.bind("<Return>", lambda e: self.list_search_results())

        self.search_btn = ctk.CTkButton(
            master=self,
            text="",
            image=ICONS['search'],
            fg_color=APP_COLOR['main'],
            hover_color=APP_COLOR['sec'],
            width=32,
            height=32,
            command=self.list_search_results
        )
        self.search_btn.place(x=330, y=20)

        # --- Configuración del Treeview ---
        estilo = ttk.Style(self)
        estilo.configure(
            "Custom.Treeview",
            rowheight=100,
            font=FONT['text_small'],
            fieldbackground=APP_COLOR['white_m']
        )
        estilo.configure(
            "Custom.Treeview.Heading",
            font=FONT['text_light'],
            background=APP_COLOR['black_m'],
            foreground=APP_COLOR['white_m']
        )

        self.tree = ttk.Treeview(
            master=self,
            columns=("cod", "desc", "exist", "bs", "dol"),
            show="tree headings",
            style="Custom.Treeview"
        )
        # Columna de imágenes
        self.tree.heading("#0", text="Imagen")
        self.tree.column("#0", width=100, anchor="center")

        # Columnas de datos
        cols = [
            ("cod", "Código", 80),
            ("desc", "Descripción", 300),
            ("exist", "Existencia", 80),
            ("bs", "Bs", 80),
            ("dol", "$", 80),
        ]
        for col, text, w in cols:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=w, anchor="center")

        self.tree.place(x=20, y=70, width=780, height=520)

        # Scrollbar vertical
        self.scrollbar = ttk.Scrollbar(
            master=self,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=800, y=70, width=20, height=520)

        # Carga inicial
        self.list_all_products()

    def load_image(self, path):
        """Abre, redimensiona y devuelve un PhotoImage."""
        img = Image.open(path).resize((90, 90))
        return ImageTk.PhotoImage(img)

    def list_all_products(self):
        self.tree.delete(*self.tree.get_children())
        for producto in INVENTARIO.GetInventory().values():
            cod = producto['codigo']
            img_ref = self.load_image(producto['image'])
            self.image_refs[cod] = img_ref

            name = producto['nombre']
            exist = producto['existencia']
            precio_usd = float(producto['precio1'])
            precio_bs = precio_usd * 130

            self.tree.insert(
                "",
                "end",
                image=img_ref,
                values=(cod, name, exist, f"{precio_bs:.2f}", precio_usd)
            )

    def list_search_results(self):
        query = self.search_var.get().lower().strip()
        resultados = INVENTARIO.BuscarNombres(query)

        self.tree.delete(*self.tree.get_children())
        for producto in resultados:
            cod = producto['codigo']
            img_ref = self.load_image(producto['image'])
            self.image_refs[cod] = img_ref

            name = producto['nombre']
            exist = producto['existencia']
            precio_usd = float(producto['precio1'])
            precio_bs = precio_usd * 130

            self.tree.insert(
                "",
                "end",
                image=img_ref,
                values=(cod, name, exist, f"{precio_bs:.2f}", precio_usd)
            )

if __name__ == "__main__":
    app = FacturacionPlace()
    app.mainloop()
