import tkinter as tk
import customtkinter as ctk
from tkinter import ttk,messagebox
from style import*
from DatabaseManager import*



class AjustesInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.configure(fg_color=APP_COLORS[0],corner_radius=0)
        self.validate = self.register(self.ValidateDigit)
        self.inventory_codes = []
        self.product_list = []
        ROWS, COLUMNS = 40, 12
        # GRID SETUP
        for rows in range(ROWS):
            self.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(COLUMNS):
            self.columnconfigure(columns,weight=1,uniform='column')
        
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLORS[3],
                                   corner_radius=0,
                                   height=50)
        title_frame.grid(row=0,column=0,rowspan=4,columnspan=COLUMNS,sticky='nswe')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Ajustes de inventario',
                                   bg_color='transparent',
                                   text_color=APP_COLORS[0],
                                   font=FONTS[0])
        title_label.pack(expand=True,fill='both',pady=5)
        # GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - 
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # NUM DOC
        self.num_doc_entry_var = tk.StringVar()
        self.num_doc_entry = ctk.CTkEntry(self,
                                          textvariable=self.num_doc_entry_var,
                                          fg_color=APP_COLORS[6],
                                          border_color=APP_COLORS[2],
                                          width=30)
        self.num_doc_entry.grid(row=11,column=1,rowspan=2,columnspan=2,sticky='we')
        
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # NUM DOC
        num_doc_label = ctk.CTkLabel(self,
                                     text='Documento',
                                     text_color=APP_COLORS[1],
                                     font=FONTS[1])
        num_doc_label.grid(row=10,column=1,columnspan=2,sticky='w')
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        self.btn_add_product = ctk.CTkButton(self,
                                            text="Agregar producto",
                                            width=25,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.Products)
        self.btn_add_product.grid(row=11,column=COLUMNS-3,columnspan=2,sticky='we')

        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        self.treeview_main = ttk.Treeview(self,
                                     style='Custom.Treeview',
                                     columns=('Descripcion','Linea','Grupo',
                                              'Existencia','Ajuste','Final'))
        self.treeview_main.grid(row=13,column=1,sticky='nswe',pady=10,rowspan=10,columnspan=COLUMNS-2)
        self.treeview_main.bind("<<TreeviewSelect>>",self.ClickAjuste)
        # CODIGO
        self.treeview_main.heading('#0',text='Cod')
        self.treeview_main.column('#0',width=50,anchor='center')
        # DESCRIPCION
        self.treeview_main.heading('Descripcion',text='Descripción')
        self.treeview_main.column('Descripcion',width=200,anchor='center')
        # LINEA
        self.treeview_main.heading('Linea',text='Línea')
        self.treeview_main.column('Linea',width=50,anchor='center')
        # GRUPO
        self.treeview_main.heading('Grupo',text='Grupo')
        self.treeview_main.column('Grupo',width=50,anchor='center')
        # EXISTENCIA
        self.treeview_main.heading('Existencia',text='Existencia')
        self.treeview_main.column('Existencia',width=50,anchor='center')
        # AJUSTE
        self.treeview_main.heading('Ajuste',text='Ajuste')
        self.treeview_main.column('Ajuste',width=50,anchor='center')
        # FINAL
        self.treeview_main.heading('Final',text='Final')
        self.treeview_main.column('Final',width=50,anchor='center')
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLORS[0],
            foreground = APP_COLORS[1],
            rowheight = 30,
            font = FONTS[2],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONTS[1])
        # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self,
                                     orientation='vertical',
                                     command=self.treeview_main.yview)
        scrollbar.grid(row=13,column=COLUMNS-1,sticky='nsw',padx=5,pady=5,rowspan=10)
        self.treeview_main.configure(yscrollcommand=scrollbar.set)

    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    def ClickAjuste(self):
        pass
    def Products(self):
    # TREEVIEW - TREEVIEW
    # FRAME DEL TREEVIEW
        # LIST INVENTORY IN TREEVIEW
        def ListInventory():
            self.cantidad_var.set('')
            self.search_bar.after(100,
                lambda:  self.search_bar.configure(state='normal',
                                                   fg_color=APP_COLORS[6],border_color=APP_COLORS[6]))
            self.search_bar_var.set('')
            self.search_bar.after(100,self.search_bar.focus())

            inventario = INVENTARIO.GetInventory()
            for item in self.treeview.get_children():
                    self.treeview.delete(item)
            for producto in inventario.values():
                self.treeview.insert("",'end',
                                     text=producto['codigo'],
                                     values=(producto['nombre'],
                                             producto['existencia']))
        # ------------------------------------------------------------------------------------------------        
        # SEARCH A PRODUCT BY NAME
        def SearchProductName():
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            busqueda = self.search_bar_var.get().lower()
            resultados = INVENTARIO.BuscarNombres(busqueda)
            for producto in resultados:
                self.treeview.insert("", 'end',
                                     text=producto['codigo'],
                                     values=(producto['nombre'],
                                             producto['existencia']))
        # -------------------------------------------------------------------------------------------------
        # SELECT A PRODUCT WHEN CLICK ON TREEVIEW
        def ClickTreeview(event):
            item_id = self.treeview.selection()
            info = self.treeview.item(item_id)
            codigo = info['text']
            self.search_bar_var.set(codigo)
            self.search_bar.configure(state='disabled',fg_color=APP_COLORS[4],
                                      border_color=APP_COLORS[4])
            self.cantidad_entry.configure(state='normal',fg_color=APP_COLORS[0],
                                          border_color=APP_COLORS[4])
            self.cantidad_entry.focus_set()
        # -------------------------------------------------------------------------------------------------
        self.btn_add_product.configure(state='disabled')
        self.tree_frame = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[5])
        self.tree_frame.geometry('800x550')
        self.tree_frame.title('Busqueda de productos')
        self.tree_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        self.tree_frame.transient(self)
    # GRID SETUP
        for rows in range(16):
            self.tree_frame.rowconfigure(rows, weight=1,uniform='a')
        for columns in range(24):
            self.tree_frame.columnconfigure(columns,weight=1,uniform='a')

        # TITULO
        title_frame = ctk.CTkFrame(self.tree_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,columnspan=24,sticky='nswe')
        title = ctk.CTkLabel(title_frame,
                             text='Busqueda de productos',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONTS[3])
        title.pack(pady=10)  
    # ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - ENTRADAS - 
        # BARRA DE BUSQUEDA
        self.search_bar_var = tk.StringVar()
        self.search_bar = ctk.CTkEntry(self.tree_frame,
                                       width=200,
                                       textvariable=self.search_bar_var,
                                       fg_color=APP_COLORS[6],
                                       border_color=APP_COLORS[6])
        self.search_bar.grid(row=2,column=0,columnspan=2,sticky='we',padx=20)
        self.search_bar.bind("<Return>",lambda event:SearchProductName())
        self.search_bar.bind("<Control-BackSpace>", lambda event: ListInventory())
        # CANTIDAD
        self.cantidad_var = tk.StringVar()
        self.cantidad_entry = ctk.CTkEntry(self.tree_frame,
                                     state='disabled',
                                     validate = 'key',
                                     validatecommand = (self.validate,'%P'),
                                     textvariable = self.cantidad_var,
                                     width=100,
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
        self.cantidad_entry.grid(row=4,column=0,columnspan=2,sticky='wns',padx=20,pady=5)
        self.cantidad_entry.bind("<Return>",lambda event:self.AddProduct())
        
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # BUSQUEDA
        label_busqueda = ctk.CTkLabel(self.tree_frame,
                             text='Busqueda por nombre',
                             font=FONTS[1],
                                        text_color=APP_COLORS[4])
        label_busqueda.grid(row=1,column=0,columnspan=3,sticky='w',padx=20)
        # CANTIDAD
        label_cantidad = ctk.CTkLabel(self.tree_frame,
                                      text='Cantidad',
                                      font=FONTS[1],
                                      text_color=APP_COLORS[4])
        label_cantidad.grid(row=4,column=1,columnspan=3,sticky='w',padx=20)
    # BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - BOTONES TREEVIEW - 
        # LIMPIAR BUSQUEDA
        clear_btn = ctk.CTkButton(self.tree_frame,
                                    text='Limpiar Búsqueda',
                                    command=ListInventory,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        clear_btn.grid(row=1,column=5,columnspan=2,sticky='w',padx=10)
        # CANCELAR
        def CloseAddProdWindow():
            self.tree_frame.destroy()
            self.btn_add_product.configure(state='enabled')
        cancel_btn = ctk.CTkButton(self.tree_frame,
                                    text='Cancelar',
                                    command=CloseAddProdWindow,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        cancel_btn.grid(row=14,column=0,columnspan=2,sticky='w',padx=10)
    # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        self.treeview = ttk.Treeview(self.tree_frame,
                                     style='Custom.Treeview',
                                columns=('Descripcion','Existencia'))
        self.treeview.grid(row=2,column=2,sticky='nswe',padx=10,rowspan=13,columnspan=21)
        # EVENTO DE SELECCIONAR PRODUCTO 
        self.treeview.bind("<<TreeviewSelect>>",ClickTreeview)
        # CODIGO
        self.treeview.heading('#0',text='Código')
        self.treeview.column('#0',width=50,anchor='center')
        # DESCRIPCION
        self.treeview.heading('Descripcion',text='Descripción')
        self.treeview.column('Descripcion',width=50,anchor='center')
        # EXISTENCIA
        self.treeview.heading('Existencia',text='Existencia')
        self.treeview.column('Existencia',width=50,anchor='center')
    # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLORS[0],
            foreground = APP_COLORS[1],
            rowheight = 30,
            font = FONTS[2],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONTS[1])
        # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.tree_frame,
                                     orientation='vertical',
                                     command=self.treeview.yview)
        scrollbar.grid(row=2,column=23,sticky='nsw',pady=5,rowspan=13)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
        ListInventory()
        
        

    def AddProduct(self):
        # GET INVENTORY CODES
        if not self.inventory_codes:
            self.inventory_codes = INVENTARIO.GetCodigos()
        # GET CURRENT PRODUCT CODE
        codigo = self.search_bar_var.get()
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
        # GET ADJUSTMENT
        ajuste = self.cantidad_var.get()
        try:
            ajuste = int(ajuste)
        except ValueError:
            messagebox.showerror('Error', 'Verifica que el campo "Cantidad" este correcto.')
            self.cantidad_entry.focus()
            return
        ajuste_final = existencia + ajuste
        if ajuste_final < 0:
            messagebox.showerror('Error', 'La existencia quedaría en negativo, verifique el ajuste.')
            self.cantidad_entry.focus()
            return

        self.treeview_main.insert("", 'end',
            text=producto['codigo'],
            values=(producto['nombre'],
                    producto['linea'],
                    producto['grupo'],
                    existencia,
                    ajuste,
                    ajuste_final))
        self.btn_add_product.configure(state='enabled')
        self.product_list.append(str(codigo).strip())
        self.tree_frame.destroy()
            
    def ValidateDigit(self,text):
        text = text.replace("-", "", 1)
        if text == '':
            return True
        return text.isdigit()