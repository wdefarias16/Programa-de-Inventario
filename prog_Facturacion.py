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
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        self.DOLAR = INVENTARIO.GetLastDolarValue()
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   height=70,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.place(relx=0.5,rely=0,relwidth=1,anchor='n')

        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Facturación',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME -  
    # PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME - PRODUCTS FRAME -  
        # FRAME
        product_frame = ctk.CTkFrame(self,
                                     fg_color=APP_COLOR['main'],
                                     corner_radius=0)
        product_frame.place(relx=0,y=69.5,relwidth=0.25,relheight=1,anchor='nw')
        # PRODUCT IMAGE
        # IMAGE
        self.image_path = 'Recursos/Imagenes/Productos'
        default_image = Image.open(f"{self.image_path}/Default.png")
        self.default_image = ctk.CTkImage(light_image=default_image, size=(200,200))
        # IMAGE FRAME
        image_frame = ctk.CTkFrame(product_frame,
                                   fg_color=APP_COLOR['white'],
                                   width=220,
                                   height=220,
                                   corner_radius=0)
        image_frame.place(relx=0.5,y=140,anchor='center')
        # IMAGE DISPLAY
        self.image_label = ctk.CTkLabel(image_frame,
                                        text='',
                                        image=self.default_image)
        self.image_label.pack()
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # FUNCTIONS
        def ClickLista():
            pass
        # --------------------------------------------------------------------
        # --------------------------------------------------------------------
        # FRAME
        main_frame = ctk.CTkFrame(self,
                                     fg_color=APP_COLOR['white_m'],
                                     corner_radius=0)
        main_frame.place(relx=0.25,y=69.5,relwidth=0.75,relheight=1,anchor='nw')
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS -
        # CODIGO DE CLIENTE 
        self.cod_client_entry_var = tk.StringVar()
        self.cod_client_entry = ctk.CTkEntry(main_frame,
                                            width=70,
                                            height=30,
                                            textvariable = self.cod_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.cod_client_entry.place(x=70,y=70,anchor='nw')
        # NOMBRE
        self.name_client_entry_var = tk.StringVar()
        self.name_client_entry = ctk.CTkEntry(main_frame,
                                            width=150,
                                            height=30,
                                            textvariable = self.name_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.name_client_entry.place(x=70,y=130,anchor='nw')
        # TELEFONO
        self.phone_client_entry_var = tk.StringVar()
        self.phone_client_entry = ctk.CTkEntry(main_frame,
                                            width=150,
                                            height=30,
                                            textvariable = self.phone_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.phone_client_entry.place(x=70,y=190,anchor='nw')
        # ID FISCAL
        self.fiscal_client_entry_var = tk.StringVar()
        self.fiscal_client_entry = ctk.CTkEntry(main_frame,
                                            width=150,
                                            height=30,
                                            textvariable = self.fiscal_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.fiscal_client_entry.place(x=155,y=70,anchor='nw')
        # MAIL
        self.mail_client_entry_var = tk.StringVar()
        self.mail_client_entry = ctk.CTkEntry(main_frame,
                                            width=150,
                                            height=30,
                                            textvariable = self.mail_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.mail_client_entry.place(x=235,y=130,anchor='nw')
        # DIRECCION
        self.address_client_entry_var = tk.StringVar()
        self.address_client_entry = ctk.CTkEntry(main_frame,
                                            width=150,
                                            height=30,
                                            textvariable = self.address_client_entry_var,
                                            border_width = 0,
                                            fg_color = APP_COLOR['white'])
        self.address_client_entry.place(x=235,y=190,anchor='nw')
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # CODIGO
        cod_label = ctk.CTkLabel(main_frame,
                                 text='Código',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        cod_label.place(x=70,y=40,anchor='nw')
        # NOMBRE
        name_label = ctk.CTkLabel(main_frame,
                                 text='Nombre',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        name_label.place(x=70,y=100,anchor='nw')
        # PHONE
        phone_label = ctk.CTkLabel(main_frame,
                                 text='Teléfono',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        phone_label.place(x=70,y=160,anchor='nw')
        # ID FISCAL
        fiscal_label = ctk.CTkLabel(main_frame,
                                 text='Cédula/RIF',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        fiscal_label.place(x=155,y=40,anchor='nw')
        # MAIL
        mail_label = ctk.CTkLabel(main_frame,
                                 text='Correo',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        mail_label.place(x=235,y=100,anchor='nw')
        # DIRECION
        address_label = ctk.CTkLabel(main_frame,
                                 text='Dirección',
                                 text_color=APP_COLOR['gray'],
                                 font=FONT['text'])
        address_label.place(x=235,y=160,anchor='nw')
        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
        # ADD PRODUCT
        self.btn_add_product = ctk.CTkButton(main_frame,
                                            text="+",
                                            width=50,
                                            height=30,
                                            fg_color=APP_COLOR['main'],
                                            hover_color=APP_COLOR['sec'],
                                            command=self.ProductsHelp)
        self.btn_add_product.place(x=500,y=30,anchor='nw')
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 40,
            font = FONT['text'],
            fieldbackground = APP_COLOR['white_m'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_light'])

        self.treeview_main = ttk.Treeview(main_frame,
                                    style='Custom.Treeview',
                                    columns=('Descripcion','Cantidad','Unidad','Bolivares',
                                             'Dolares'))
        self.treeview_main.place(relx=0.5,rely=0.34,relwidth=0.85,height=300,anchor='n')
        self.treeview_main.bind("<<TreeviewSelect>>",ClickLista)
        # CODIGO
        self.treeview_main.heading('#0',text='Cod.',anchor='w')
        self.treeview_main.column('#0', width=120, anchor='w', stretch=False)
        # DESCRIPCION
        self.treeview_main.heading('Descripcion',text='Descripción',anchor='w')
        self.treeview_main.column('Descripcion', width=300, anchor='w', minwidth=200, stretch=True)
        # CANTIDAD
        self.treeview_main.heading('Cantidad',text='Cant.',anchor='w')
        self.treeview_main.column('Cantidad', width=100, anchor='w', stretch=False)
        # UNIDAD
        self.treeview_main.heading('Unidad',text='Unidad',anchor='w')
        self.treeview_main.column('Unidad', width=120, anchor='w', stretch=False)
        # BOLIVARES
        self.treeview_main.heading('Bolivares',text='Bs.',anchor='w')
        self.treeview_main.column('Bolivares', width=200, anchor='w', stretch=False)
        # DOLARES
        self.treeview_main.heading('Dolares',text='$',anchor='w')
        self.treeview_main.column('Dolares', width=200, anchor='w', stretch=False)
        # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(main_frame,
                                     orientation='vertical',
                                     width=20,
                                     height=205,
                                     command=self.treeview_main.yview)
        scrollbar.place(relx=0.94,rely=0.34,anchor='n')
        self.treeview_main.configure(yscrollcommand=scrollbar.set)
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - 
    # FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - 
        # FRAME
        footer_frame = ctk.CTkFrame(self,
                                    height=30,
                                    fg_color=APP_COLOR['sec'],
                                    corner_radius=0)
        footer_frame.place(relx=0.5,rely=1,relwidth=1,anchor='s')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS
# AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS
    def ProductsHelp(self):
        # LIST INVENTORY IN TREEVIEW - LIST INVENTORY IN TREEVIEW - LIST INVENTORY IN TREEVIEW -
        # LIST INVENTORY IN TREEVIEW - LIST INVENTORY IN TREEVIEW - LIST INVENTORY IN TREEVIEW -
        def ListInventory():
            self.qty_entry_var.set('')
            self.search_bar_entry.after(100,
                lambda:  self.search_bar_entry.configure(state='normal',
                fg_color=APP_COLOR['white'],border_color=APP_COLOR['white']))
            self.search_bar_entry_var.set('')
            self.search_bar_entry.after(100,self.search_bar_entry.focus())
            inventario = INVENTARIO.GetInventory()
            for item in self.product_tv.get_children():
                    self.product_tv.delete(item) 
            for i, producto in enumerate(inventario.values()):
                color = '#eaeaea' if i % 2 == 0 else '#ffffff'
                tag_name = f'row{i}'
                self.product_tv.insert(
                    "", 'end',
                    text=producto['codigo'],
                    values=(producto['nombre'],f'${producto['precio1']}' ,producto['existencia']),
                    tags=(tag_name,)
                )
                self.product_tv.tag_configure(tag_name, background=color)
        # ------------------------------------------------------------------------------------------------        
        # ------------------------------------------------------------------------------------------------        
        # SEARCH A PRODUCT BY NAME - SEARCH A PRODUCT BY NAME - SEARCH A PRODUCT BY NAME - 
        # SEARCH A PRODUCT BY NAME - SEARCH A PRODUCT BY NAME - SEARCH A PRODUCT BY NAME - 
        def SearchProductName():
            for item in self.product_tv.get_children():
                self.product_tv.delete(item)
            busqueda = self.search_bar_entry_var.get().lower()
            resultados = INVENTARIO.BuscarNombres(busqueda)
            for i, producto in enumerate(resultados):
                color = '#eaeaea' if i % 2 == 0 else '#ffffff'
                tag_name = f'search_row{i}'
                self.product_tv.insert(
                    "", 'end',
                    text=producto['codigo'],
                    values=(producto['nombre'], producto['existencia']),
                    tags=(tag_name,)
                )
                self.product_tv.tag_configure(tag_name, background=color)
        # -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------
        # SELECT A PRODUCT WHEN CLICK ON TREEVIEW - SELECT A PRODUCT WHEN CLICK ON TREEVIEW - 
        # SELECT A PRODUCT WHEN CLICK ON TREEVIEW - SELECT A PRODUCT WHEN CLICK ON TREEVIEW - 
        def ClickTreeview(event):
            item_id = self.product_tv.selection()
            info = self.product_tv.item(item_id)
            codigo = info['text']
            self.search_bar_entry_var.set(codigo)
            self.search_bar_entry.configure(state='disabled',
                                            fg_color=APP_COLOR['gray'],
                                            border_color=APP_COLOR['gray'])
            self.qty_entry.configure(state='normal',
                                     fg_color=APP_COLOR['white'],
                                     border_color=APP_COLOR['white'])
            self.qty_entry.focus_set()
        # -------------------------------------------------------------------------------------------------
    # CANCEL TREEVIEW SELECTION - CANCEL TREEVIEW SELECTION - CANCEL TREEVIEW SELECTION -
    # CANCEL TREEVIEW SELECTION - CANCEL TREEVIEW SELECTION - CANCEL TREEVIEW SELECTION -
        def RefreshSelection():
            self.qty_entry_var.set('')
            self.qty_entry.configure(state='disabled',
                                     fg_color=APP_COLOR['gray'],
                                     border_color=APP_COLOR['gray'])
            self.search_bar_entry_var.set('')
            self.search_bar_entry.configure(state='normal',
                                            fg_color=APP_COLOR['white'],
                                            border_color=APP_COLOR['white'])
            self.search_bar_entry.focus()
            ListInventory()
        # -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------
        # GET AND DISPLAY PRODUCT IMAGE - GET AND DISPLAY PRODUCT IMAGE -
        # GET AND DISPLAY PRODUCT IMAGE - GET AND DISPLAY PRODUCT IMAGE -
        def GetImage(image):
            if not image:
                image = 'Recursos/Imagenes/Productos/Default.png'
            img = Image.open(image)
            w, h = img.size
            photo = ctk.CTkImage(light_image=img, size=(200,200))
            self.image_label.configure(image=photo)
        # -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------
        # ADD PRODUCT TO MAIN TREEVIEW - ADD PRODUCT TO MAIN TREEVIEW -
        # ADD PRODUCT TO MAIN TREEVIEW - ADD PRODUCT TO MAIN TREEVIEW -
        def AddProduct():
            # GET CURRENT PRODUCT CODE
            codigo = self.search_bar_entry_var.get()
            # IF CODE ALREADY IN MAIN TREEVIEW, CANNOT BE ADDED
            if codigo in self.product_list:
                messagebox.showerror('Error', f'Producto con código {codigo} ya se encuentra en la lista.')
                return
            if codigo not in self.inventory_codes:
                messagebox.showerror('Error', f'Producto con código {codigo} no se encuentra en la base de datos.')
                return
            # GET PRODUCT DATA
            producto = INVENTARIO.GetProducto(codigo)
            # GET ADJUSTMENT
            qty = self.qty_entry_var.get()
            try:
                qty = int(qty)
            except ValueError:
                messagebox.showerror('Error', 'Verifica que el campo "Cantidad" este correcto.')
                self.qty_entry.focus()
                return
            # PRECIO POR UNIDAD EN DOLARES CON FORMATO '000,000.00'
            precio_unidad = "{:,.2f}".format(producto['precio1'])
            # -----------------------------------------------------
            # PRECIO FINAL EN DOLARES
            precio_dolar = float(producto['precio1']) * qty
            # FORMATO AL PRECIO FINAL EN DOLARES
            precio_dolar_format = "{:,.2f}".format(precio_dolar)
            # -----------------------------------------------------
            # PRECIO FINAL EN BOLIVARES
            precio_bs = float(self.DOLAR * precio_dolar)
            # FORMATO AL PRECIO FINAL EN BOLIVARES
            precio_bs_format = "{:,.2f}".format(precio_bs)
            # -----------------------------------------------------
            # INSERT PRODUCT IN MAIN TREEVIEW
            self.treeview_main.insert("", 'end',
                text=producto['codigo'],
                values=(producto['nombre'],
                        qty,
                        f'$ {precio_unidad}',
                        f'Bs. {precio_bs_format}',
                        f'$ {precio_dolar_format}'))
            self.product_list.append(str(codigo).strip())
            # GET AND DISPLAY PRODUCT IMAGE
            image = producto['image']
            GetImage(image)
            # CERRAR EL PRODUCT HELP FRAME
            help_frame.destroy()
        # -------------------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
        help_frame.title('Busqueda de productos')
        help_frame.geometry('800x450')
        help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        help_frame.transient(self)
        help_frame.grab_set()
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # TITLE FRAME
        title_frame = ctk.CTkFrame(help_frame,
                                   fg_color=APP_COLOR['sec'],
                                   height=50,
                                   corner_radius=0)
        title_frame.pack(expand=False,fill='x')
        # TITLE LABEL - TITLE LABEL - TITLE LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Búsqueda de productos',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['text'])
        title_label.pack(expand=True,fill='x',pady=5)
        # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
        # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
        prog_frame = ctk.CTkFrame(help_frame,
                                   fg_color=APP_COLOR['white_m'],
                                   height=50,
                                   corner_radius=0)
        prog_frame.pack(expand=True,fill='both')
        # PROG FRAME GRID SETUP
        ROWS, COLUMNS = 12,10
        for rows in range(ROWS):
            prog_frame.rowconfigure(rows,weight=1,uniform='rows')
        for columns in range(COLUMNS):
            prog_frame.columnconfigure(columns,weight=1,uniform='rows')
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # SEARCH BAR
        self.search_bar_entry_var = tk.StringVar()
        self.search_bar_entry = ctk.CTkEntry(prog_frame,
                                        textvariable=self.search_bar_entry_var,
                                        fg_color=APP_COLOR['gray'],
                                        border_color=APP_COLOR['gray'])
        self.search_bar_entry.grid(row=2,column=1,columnspan=2,sticky='we')
        
        self.search_bar_entry.bind("<Return>",lambda event:SearchProductName())
        self.search_bar_entry.bind("<Control-BackSpace>",lambda event:RefreshSelection())
        # QUANTITY
        self.qty_entry_var = tk.StringVar()
        self.qty_entry = ctk.CTkEntry(prog_frame,
                                        state='disabled',
                                        textvariable=self.qty_entry_var,
                                        fg_color=APP_COLOR['gray'],
                                        border_color=APP_COLOR['gray'])
        self.qty_entry.grid(row=2,column=6,sticky='we')
        self.qty_entry.bind("<Control-BackSpace>",lambda event:RefreshSelection())
        self.qty_entry.bind("<Return>",lambda event:AddProduct())
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # SEARCH BAR
        search_bar_label = ctk.CTkLabel(prog_frame,
                                        text='Búsqueda por nombre',
                                        font=FONT['text_light'],
                                        text_color=APP_COLOR['gray'])
        search_bar_label.grid(row=1,column=1,columnspan=2,sticky='w')
        # QUANTITY
        qty_label = ctk.CTkLabel(prog_frame,
                                text='Cantidad',
                                font=FONT['text_light'],
                                text_color=APP_COLOR['gray'])
        qty_label.grid(row=1,column=6,columnspan=2,sticky='w')
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # CLOSE WINDOW
        close_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['cancel'],
                                  command=lambda:help_frame.destroy(),
                                  fg_color=APP_COLOR['red_m'],
                                  hover_color=APP_COLOR['red_s'])
        close_btn.grid(row=0,column=COLUMNS-1,sticky='we',padx=10,pady=10)
        # SEARCH
        search_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['search'],
                                  command=SearchProductName,
                                  fg_color=APP_COLOR['main'],
                                  hover_color=APP_COLOR['sec'])
        search_btn.grid(row=2,column=3,sticky='w',padx=5)
        # REFRESH OR CANCEL SELECTION
        cancel_slct_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['refresh'],
                                  command=RefreshSelection,
                                  fg_color=APP_COLOR['main'],
                                  hover_color=APP_COLOR['sec'])
        cancel_slct_btn.grid(row=2,column=4,sticky='w')
        # ACCEPT
        accept_btn = ctk.CTkButton(prog_frame,
                                  text='Aceptar',
                                  command=AddProduct,
                                  fg_color=APP_COLOR['main'],
                                  hover_color=APP_COLOR['sec'])
        accept_btn.grid(row=2,column=7,sticky='w',padx=5)
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREVIEW
        self.product_tv = ttk.Treeview(prog_frame,
                                  style='Custom.Treeview',
                                  columns = ('Descripcion','Precio','Existencia'))
        self.product_tv.grid(row=4,column=1,rowspan=6,columnspan=COLUMNS-2,sticky='nswe')
        self.product_tv.bind("<<TreeviewSelect>>",ClickTreeview)
        # CODIGO
        self.product_tv.heading('#0',text='Cod',anchor='w')
        self.product_tv.column('#0',width=200,anchor='w',minwidth=20, stretch=False)
        # DESCRIPCION
        self.product_tv.heading('Descripcion',text='Descripción',anchor='w')
        self.product_tv.column('Descripcion',width=500,anchor='w',minwidth=50,stretch=True)
        # PRECIO
        self.product_tv.heading('Precio',text='Precio',anchor='w')
        self.product_tv.column('Precio',width=130,anchor='w',minwidth=15, stretch=False)
        # EXISTENCIA
        self.product_tv.heading('Existencia',text='Existencia',anchor='w')
        self.product_tv.column('Existencia',width=130,anchor='w',minwidth=15, stretch=False)
        # LIST INVENTORY WHEN OPENING THE HELP WINDOW
        ListInventory()