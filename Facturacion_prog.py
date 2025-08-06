import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from PIL import Image, ImageTk

class FacturacionProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        ROWS, COLUMNS = 20, 12
        window_width , window_height = 1920,1080
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        #-------------------------------------------------------------------------------------
        def ClickLista():
            pass
        #-------------------------------------------------------------------------------------
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0,
                                   height=50)
        title_frame.pack(fill='x')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Facturación',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.pack(pady=10)
        # PROG FRAME
        self.prog_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLOR['white_m'])
        self.prog_frame.pack(expand=True,fill='both',side='left')
        self.prog_frame.bind("<Return>",lambda event:self.ProductsHelp())

        # GRID SETUP
        # for rows in range(ROWS):
        #     self.prog_frame.rowconfigure(rows,weight=1,uniform='a')
        # for columns in range(COLUMNS):
        #     self.prog_frame.columnconfigure(columns,weight=1,uniform='a')
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        add_product_btn = ctk.CTkButton(self.prog_frame,
                                        text='+',
                                        fg_color=APP_COLOR['main'],
                                        hover_color=APP_COLOR['sec'],
                                        command=self.ProductsHelp)
        add_product_btn.place(x=20,y=20)
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 100,
            font = FONT['text_small'],
            fieldbackground = APP_COLOR['white_m'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_light'])
        tree_width, tree_height = 1600,400

        self.treeview_main = ttk.Treeview(self.prog_frame,
                                     style='Custom.Treeview',
                                     columns=('Cod','Descripcion','Cantidad','Bolivares',
                                              'Dolares'))
        self.treeview_main.place(relx=0.5, rely=0.6, anchor='center',width=tree_width, height=tree_height)
        self.treeview_main.bind("<<TreeviewSelect>>",ClickLista)
        # IMAGEN
        self.treeview_main.heading('#0',text='img')
        self.treeview_main.column('#0',width=50,anchor='center')
        # CODIGO
        self.treeview_main.heading('Cod',text='Cod.')
        self.treeview_main.column('Cod',width=200,anchor='center')
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
        scrollbar = ctk.CTkScrollbar(self.prog_frame,
                                      width=20,
                                      height=tree_height,
                                     orientation='vertical',
                                     command=self.treeview_main.yview)
        scrollbar.place(x=window_width-(window_width - tree_width), y=tree_height-tree_width)
        self.treeview_main.configure(yscrollcommand=scrollbar.set)
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        print(f"Tamaño actual: {ancho} x {alto}")

    
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS -  
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS -  
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    def ProductsHelp(self):
        # LIST INVENTORY IN TREEVIEW
        def ListInventory():
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
                    values=(producto['nombre'], producto['existencia']),
                    tags=(tag_name,)
                )
                self.product_tv.tag_configure(tag_name, background=color)
        # ------------------------------------------------------------------------------------------------        
    # SEARCH A PRODUCT BY NAME
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
    # SELECT A PRODUCT WHEN CLICK ON TREEVIEW
        def ClickTreeview(event):
            item_id = self.product_tv.selection()
            info = self.product_tv.item(item_id)
            codigo = info['text']
            self.search_bar_entry_var.set(codigo)
            self.search_bar_entry.configure(state='disabled',
                                            fg_color=APP_COLOR['gray'],
                                            border_color=APP_COLOR['gray'])
            AddProduct()
        # -------------------------------------------------------------------------------------------------
    # CANCEL TREEVIEW SELECTION
        def RefreshSelection():
            self.search_bar_entry_var.set('')
            self.search_bar_entry.configure(state='normal',
                                            fg_color=APP_COLOR['white'],
                                            border_color=APP_COLOR['white'])
            self.search_bar_entry.focus()
            ListInventory()
        # -------------------------------------------------------------------------------------------------
    # ADD PRODUCT TO MAIN TREEVIEW
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
            existencia = producto['existencia']
            cantidad = 1
            valor_dolar = 130
            precio_bs = float(producto['precio1']) * valor_dolar

            img = Image.open(producto['image']).resize((90,90))
            image = ImageTk.PhotoImage(img)
            
            # GUARDAR REFERENCIA PARA EVITAR RECOLECCIÓN DE BASURA
            if not hasattr(self, 'image_refs'):
                self.image_refs = {}
            self.image_refs[codigo] = image

            self.treeview_main.insert("", 'end',
                text='',
                image=image,
                values=(producto['codigo'],
                        producto['nombre'],
                        cantidad,
                        precio_bs,
                        producto['precio1']))
            self.product_list.append(str(codigo).strip())
            help_frame.destroy()
        # -------------------------------------------------------------------------------------------------
        # CREATE THE WINDOW
        help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
        help_frame.title('Busqueda de productos')
        help_frame.geometry('800x450')
        help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        help_frame.transient(self)
        help_frame.grab_set()
        # TITLE - TITLE - TITLE - 
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
        
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # SEARCH BAR
        search_bar_label = ctk.CTkLabel(prog_frame,
                                        text='Búsqueda por nombre',
                                        font=FONT['text_light'],
                                        text_color=APP_COLOR['gray'])
        search_bar_label.grid(row=1,column=1,columnspan=2,sticky='w')

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
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREVIEW
        self.product_tv = ttk.Treeview(prog_frame,
                                  style='Custom.Treeview',
                                  columns = ('Descripcion','Existencia'))
        self.product_tv.grid(row=4,column=1,rowspan=6,columnspan=COLUMNS-2,sticky='nswe')
        self.product_tv.bind("<<TreeviewSelect>>",ClickTreeview)
        # CODIGO
        self.product_tv.heading('#0',text='Cod')
        self.product_tv.column('#0',width=25,anchor='center')
        # DESCRIPCION
        self.product_tv.heading('Descripcion',text='Descripción')
        self.product_tv.column('Descripcion',width=60,anchor='w')
        # CODIGO
        self.product_tv.heading('Existencia',text='Existencia')
        self.product_tv.column('Existencia',width=25,anchor='center')
        # LIST INVENTORY WHEN OPENING THE HELP WINDOW
        ListInventory()