import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from PIL import Image, ImageTk
import datetime

class FacturacionProg(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        self.grid_propagate(False)

        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        # GRID SIN ELASTICIDAD
        for r in range(21):
            self.grid_rowconfigure(r,weight=0)
        for c in range(21):
            self.grid_columnconfigure(c,weight=0)
        # FILAS DE ALTURA FIJA, HEADER Y BARRA INFERIOR
        self.grid_rowconfigure(0,weight=0,minsize=100)
        self.grid_rowconfigure(20,weight=0,minsize=10)
        # ZONA DE TRABAJO AJUSTABLE
        for r in range(1,19):
            self.grid_rowconfigure(r, weight=1)
        # COLUMNA LATERAL
        self.grid_columnconfigure((0,1,2,3),  weight=0, minsize=100)  # panel lateral (fijo)
        #self.grid_columnconfigure(1,  weight=0)               # margen/col auxiliar si la usas
        for c in range(4, 20):                                # contenido principal (flex)
            self.grid_columnconfigure(c, weight=1)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.grid(row=0,column=0,columnspan=20,sticky='nswe')

        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Ajustes de inventario',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.pack(expand=True)
    # PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - 
    # PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - PRODUCT FRAME - 
        # FRAME
        self.product_frame = ctk.CTkFrame(self,
                                     width=300,
                                     corner_radius=0,
                                     fg_color=APP_COLOR['main'])
        self.product_frame.grid(row=1,column=0,rowspan=18,columnspan=4,sticky='nswe')
        self.product_frame.grid_propagate(False)
        # GRID SET UP
        for r in range(12):
            self.product_frame.rowconfigure(r,weight=1)
        for c in range(4):
            self.product_frame.columnconfigure(c,weight=1)
        # IMAGE
        # PHOTOFRAME
        self.image_path = 'Recursos/Imagenes/Productos'
        default_image = Image.open(f"{self.image_path}/Default.png")
        self.default_image = ctk.CTkImage(light_image=default_image, size=(200,200))
        
        image_frame = ctk.CTkFrame(self.product_frame,
                                   corner_radius=0)
        image_frame.grid(row=1,column=1,rowspan=3,columnspan=2)
    
        self.image_label = ctk.CTkLabel(image_frame,
                                        text='',
                                        image=self.default_image)
        self.image_label.grid(row=1,column=0,rowspan=4,columnspan=4)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        self.main_frame = ctk.CTkFrame(self,
                                     corner_radius=0,
                                     fg_color=APP_COLOR['white_m'])
        self.main_frame.grid(row=1,column=4,rowspan=18,columnspan=16,sticky='nswe')
        # GRID SIN ELASTICIDAD
        for r in range(16):
            self.main_frame.grid_rowconfigure(r,weight=0,minsize=56)
        for c in range(12):
            self.main_frame.grid_columnconfigure(c,weight=0,minsize=110)

        # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
        def ClickLista():
            pass
        # -----------------------------------
        # -----------------------------------
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS -
        # CODIGO DE CLIENTE 
        self.cod_client_entry_var = tk.StringVar()
        self.cod_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.cod_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.cod_client_entry.grid(row=1,column=2,sticky='w')
        # NOMBRE
        self.name_client_entry_var = tk.StringVar()
        self.name_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.name_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.name_client_entry.grid(row=2,column=2,sticky='we')
        # ID FISCAL
        self.fiscal_client_entry_var = tk.StringVar()
        self.fiscal_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.fiscal_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.fiscal_client_entry.grid(row=3,column=2,sticky='we')
        # TELEFONO
        self.phone_client_entry_var = tk.StringVar()
        self.phone_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.phone_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.phone_client_entry.grid(row=4,column=2,sticky='we')
        # MAIL
        self.mail_client_entry_var = tk.StringVar()
        self.mail_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.mail_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.mail_client_entry.grid(row=5,column=2,sticky='we')
        # DIRECCION
        self.address_client_entry_var = tk.StringVar()
        self.address_client_entry = ctk.CTkEntry(self.main_frame,
                                             textvariable = self.address_client_entry_var,
                                             fg_color = APP_COLOR['white'],
                                             border_color = APP_COLOR['gray'])
        self.address_client_entry.grid(row=6,column=2,sticky='we')
        # LABEL -LABEL -LABEL -LABEL -LABEL -LABEL - 
        # LABEL -LABEL -LABEL -LABEL -LABEL -LABEL -
        client_data = [
            'Cod.',
            'Nombre',
            'Ced.',
            'Telf.',
            'Mail',
            'Dir.'
        ]
        '''client_data_label = ctk.CTkLabel(self.main_frame,
                                         text = '',
                                         text_color = APP_COLOR['black_m'],
                                         font = FONT['text'])'''
        for i,text in enumerate(client_data):
            client_data_label = ctk.CTkLabel(self.main_frame,
                                         text = text,
                                         text_color = APP_COLOR['black_m'],
                                         font = FONT['text'])
            client_data_label.grid(row=i+1,column=1,sticky='e',padx=5)
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 30,
            font = FONT['text_small'],
            fieldbackground = APP_COLOR['white_m'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_light'])

        self.treeview_main = ttk.Treeview(self.main_frame,
                                     style='Custom.Treeview',
                                     columns=('Descripcion','Cantidad','Bolivares',
                                              'Dolares'))
        self.treeview_main.grid(row=8,column=1,rowspan=2,columnspan=10,sticky='nswe')
        self.treeview_main.bind("<<TreeviewSelect>>",ClickLista)
        # CODIGO
        self.treeview_main.heading('#0',text='Cod.')
        self.treeview_main.column('#0',width=200,anchor='center')
        # DESCRIPCION
        self.treeview_main.heading('Descripcion',text='Descripción')
        self.treeview_main.column('Descripcion',width=200,anchor='center')
        # CANTIDAD
        self.treeview_main.heading('Cantidad',text='Cant.')
        self.treeview_main.column('Cantidad',width=200,anchor='center')
        # BOLIVARES
        self.treeview_main.heading('Bolivares',text='Bs.')
        self.treeview_main.column('Bolivares',width=50,anchor='center')
        # DOLARES
        self.treeview_main.heading('Dolares',text='$')
        self.treeview_main.column('Dolares',width=50,anchor='center')
        
        # SCROLLBAR DEL TV
        '''scrollbar = ctk.CTkScrollbar(self.main_frame,
                                      width=20,
                                      height=200,
                                     orientation='vertical',
                                     command=self.treeview_main.yview)
        scrollbar.grid(row=10,column=17,rowspan=6,sticky='w')
        self.treeview_main.configure(yscrollcommand=scrollbar.set)'''

        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------
    # FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - 
    # FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - FOOTER FRAME - 
        footer_frame = ctk.CTkFrame(self,
                                    corner_radius=0,
                                    fg_color=APP_COLOR['sec'])
        footer_frame.grid(row=20,column=0,columnspan=21,sticky='nswe')
        footer_frame.configure(height=32)
        footer_frame.grid_propagate(False)
        # -----------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        btn = ctk.CTkButton(self.main_frame,
                            text='a',
                            width=10,
                            command=self.visualizar_grilla)
        btn.grid(row=0,column=0)

    def visualizar_grilla(self):
        for r in range(16):
            for c in range(12):
                marcador = ctk.CTkLabel(self.main_frame, text=f"{r},{c}", 
                                        fg_color="#dddddd", 
                                        text_color="gray", 
                                        corner_radius=5)
                marcador.grid(row=r, column=c, sticky="nsew")