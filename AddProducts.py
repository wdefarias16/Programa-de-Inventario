import customtkinter as ctk
import tkinter as tk
from ProductDataBase import*

fonts = [('Roboto light',25),('Roboto light',15)]
app_colors = ['#eaeaea','#1d1d1d','#1c9bac','#166c78','#5d5d5d']

class AddProductsTab(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        # TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - TITULO - 
        title_frame = ctk.CTkFrame(self,corner_radius=5,fg_color=app_colors[3])
        title_frame.pack(fill='x')

        title = ctk.CTkLabel(title_frame,
                             text='Carga de productos',
                             bg_color='transparent',
                             text_color=app_colors[0],
                             height=50,
                             font=fonts[0])
        title.pack()

        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        entry_frame = ctk.CTkFrame(self,fg_color=app_colors[0],corner_radius=5)
        entry_frame.pack(expand=True,fill='both',side='left')


        codigo_variable = tk.IntVar()
        codigo_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=codigo_variable,
                                    border_color='#fff')
        codigo_entry.pack(fill='x',padx=5,pady=5)

        linea_variable = tk.IntVar()
        linea_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=linea_variable,
                                   border_color='#fff')
        linea_entry.pack(fill='x',padx=5,pady=5)

        grupo_variable = tk.IntVar()
        grupo_entry = ctk.CTkEntry(entry_frame,
                                   textvariable=grupo_variable,
                                   border_color='#fff')
        grupo_entry.pack(fill='x',padx=5,pady=5)

        nombre_variable = tk.StringVar()
        nombre_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=nombre_variable,
                                    border_color='#fff')
        nombre_entry.pack(fill='x',padx=5,pady=5)


        precio_variable = tk.DoubleVar()
        precio_entry = ctk.CTkEntry(entry_frame,
                                    textvariable=precio_variable,
                                    border_color='#fff')
        precio_entry.pack(fill='x',padx=5,pady=5)

        cantidad_variable = tk.IntVar()
        cantidad_entry = ctk.CTkEntry(entry_frame,
                                      textvariable=cantidad_variable,
                                      border_color='#fff')
        cantidad_entry.pack(fill='x',padx=5,pady=5)

        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        entry_frame = ctk.CTkFrame(self,fg_color=app_colors[0],corner_radius=0)
        entry_frame.pack(expand=True,fill='both',side='left')

        codigo_label = ctk.CTkLabel(entry_frame,anchor='w',text='Codigo')
        codigo_label.pack(fill='x',padx=5,pady=5)

        linea_label = ctk.CTkLabel(entry_frame,anchor='w',text='Linea')
        linea_label.pack(fill='x',padx=5,pady=5)

        grupo_label = ctk.CTkLabel(entry_frame,anchor='w',text='Grupo')
        grupo_label.pack(fill='x',padx=5,pady=5)

        nombre_label = ctk.CTkLabel(entry_frame,anchor='w',text='Nombre')
        nombre_label.pack(fill='x',padx=5,pady=5)

        precio_label = ctk.CTkLabel(entry_frame,anchor='w',text='Precio')
        precio_label.pack(fill='x',padx=5,pady=5)

        cantidad_label = ctk.CTkLabel(entry_frame,anchor='w',text='Cantidad')
        cantidad_label.pack(fill='x',padx=5,pady=5)
