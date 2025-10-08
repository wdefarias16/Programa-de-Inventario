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
# INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - 
# INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - 
# INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - 
# INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - 
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        info_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['main'],
                        corner_radius=0)
        info_frame.place(relx=0.75,y=69.5,relwidth=0.25,relheight=1,anchor='nw')
        # DOLLAR RATE - DOLLAR RATE - DOLLAR RATE - DOLLAR RATE - DOLLAR RATE - 
        # DOLLAR RATE - DOLLAR RATE - DOLLAR RATE - DOLLAR RATE - DOLLAR RATE -
        # LABEL TITLE
        dolar_rate_title_label = ctk.CTkLabel(info_frame,
                        text='Tasa del dolar',
                        font=FONT['subtitle_bold'],
                        text_color=APP_COLOR['white_m'])
        dolar_rate_title_label.place(relx=0.5,rely=0.05,anchor='center')
        # LABEL RATE
        dolar_rate_label = ctk.CTkLabel(info_frame,
                        text=f'$ {self.DOLAR}',
                        height=60,
                        corner_radius=5,
                        font=FONT['text_big'],
                        text_color=APP_COLOR['gray'],
                        fg_color=APP_COLOR['white_m'])
        dolar_rate_label.place(relx=0.5,rely=0.12,relwidth=0.90,anchor='center')
        # SEPARATOR
        separator = ctk.CTkFrame(info_frame,
                        height=5,
                        fg_color=APP_COLOR['white_m'],
                        corner_radius=10)
        separator.place(relx=0.5,rely=0.18,relwidth=0.90,anchor='center')
        # CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - 
        # CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - 
        cashout_btn = ctk.CTkButton(info_frame,
                        text='Cobrar',
                        height=30,
                        font=FONT['text_big'],
                        text_color=APP_COLOR['white'],
                        fg_color=APP_COLOR['green_m'],
                        hover_color=APP_COLOR['green_s'],
                        command=self.CobrarFactura)
        cashout_btn.place(relx=0.5,rely=0.80,relwidth=0.90,anchor='center')
        # --------------------------------------------------------------------
        # --------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
# MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
# MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
# MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
# MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # FUNCTIONS
        def ClickLista(event):
            pass
        # --------------------------------------------------------------------
        # --------------------------------------------------------------------
        # GO BACK
        # Reemplazar la función GoBack existente
        def GoBack():
            if self.product_list:
                respuesta = messagebox.askyesno(
                    '¡Atención!',
                    'Hay productos en la factura. ¿Desea cancelar la factura y volver atrás?')
                if respuesta:
                    self.CancelFact()
                    self.GoBack_CB()
            else:
                self.GoBack_CB()
        # --------------------------------------------------------------------
        # --------------------------------------------------------------------
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        main_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['white_m'],
                        corner_radius=0)
        main_frame.place(relx=0,y=69.5,relwidth=0.75,relheight=1,anchor='nw')
# ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - 
# ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS -
# ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS -
# ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS - ENTRIES CLIENTS -
        # CODIGO DE CLIENTE 
        self.cod_client_entry_var = tk.StringVar()
        self.cod_client_entry = ctk.CTkEntry(main_frame,
                        width=70,
                        height=30,
                        textvariable = self.cod_client_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.cod_client_entry.place(x=70,y=70,anchor='nw')
        self.cod_client_entry.bind("<Return>",lambda event:self.SearchClient())
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
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
# LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
# LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
# LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
# LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
    # CLIENT DATA - CLIENT DATA - CLIENT DATA - CLIENT DATA - CLIENT DATA - 
    # CLIENT DATA - CLIENT DATA - CLIENT DATA - CLIENT DATA - CLIENT DATA - 
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
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
# ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - 
# ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA -
# ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA -
# ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA -
        # CODIGO DE PRODUCTO
        self.product_code_entry_var = tk.StringVar()
        self.product_code_entry = ctk.CTkEntry(main_frame,
                        width=150,
                        height=30,
                        textvariable = self.product_code_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.product_code_entry.place(relx=0.60,y=190,anchor='nw')
        self.product_code_entry.bind("<Return>",lambda event:self.SearchProductByCode())
        # CANTIDAD DE PRODUCTO
        self.product_qty_entry_var = tk.StringVar()
        self.product_qty_entry = ctk.CTkEntry(main_frame,
                        width=65,
                        height=30,
                        textvariable = self.product_qty_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.product_qty_entry.place(relx=0.78,y=190,anchor='nw')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
# LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA -
# LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA -
# LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA -
# LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA -
        # CODIGO DE PRODUCTO
        product_code_label = ctk.CTkLabel(main_frame,
                        text='Producto',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        product_code_label.place(relx=0.60,y=160,anchor='nw')
        # CANTIDAD DE PRODUCTO
        product_qty_label = ctk.CTkLabel(main_frame,
                        text='Cantidad',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        product_qty_label.place(relx=0.78,y=160,anchor='nw')
    # TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - 
    # TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - 
        # TOTAL DOLARES
        self.total_fact_dolar_label = ctk.CTkLabel(main_frame,
                        text='$ 000.00',
                        width=180,
                        height=60,
                        corner_radius=10,
                        font=FONT['text_big'],
                        text_color=APP_COLOR['white'],
                        fg_color=APP_COLOR['green_m'])
        self.total_fact_dolar_label.place(relx=0.925,rely=0.70,anchor='e')
        # TOTAL BOLIVARES
        self.total_fact_bs_label = ctk.CTkLabel(main_frame,
                        text='Bs. 000.00',
                        width=180,
                        height=60,
                        corner_radius=10,
                        font=FONT['text_big2'],
                        text_color=APP_COLOR['white'],
                        fg_color=APP_COLOR['green_m'])
        self.total_fact_bs_label.place(relx=0.925,rely=0.80,anchor='e')
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
# BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
# BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - 
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
        self.btn_add_product.place(relx=0.87,y=190,anchor='nw')
        # GO BACK
        self.btn_goback = ctk.CTkButton(main_frame,
                        text="Volver atrás",
                        corner_radius=0,
                        fg_color=APP_COLOR['gray'],
                        hover_color=APP_COLOR['sec'],
                        command=GoBack)
        self.btn_goback.place(relx=0,y=0,anchor='nw')
        # CANCEL FACT
        self.btn_cancel_fact = ctk.CTkButton(main_frame,
                        text="",
                        image=ICONS['cancel'],
                        width=10,
                        fg_color=APP_COLOR['red_m'],
                        hover_color=APP_COLOR['red_s'],
                        command=self.CancelFact)
        self.btn_cancel_fact.place(relx=0.08,rely=0.65,anchor='nw')
        # DEL PRODUCT
        self.btn_del_product = ctk.CTkButton(main_frame,
                        text="",
                        image=ICONS['trash'],
                        width=10,
                        fg_color=APP_COLOR['red_m'],
                        hover_color=APP_COLOR['red_s'],
                        command=self.DeleteSelectedProduct)
        self.btn_del_product.place(relx=0.15,rely=0.65,anchor='nw')
# TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
# TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
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
                                    columns=('Descripcion','Cantidad','Unidad',
                                             'Bolivares','Dolares'))
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
                    tags=(tag_name,))
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
        # ADD PRODUCT TO MAIN TREEVIEW - ADD PRODUCT TO MAIN TREEVIEW -
        # ADD PRODUCT TO MAIN TREEVIEW - ADD PRODUCT TO MAIN TREEVIEW -
        def AddProduct():
            # GET CURRENT PRODUCT CODE
            codigo = self.search_bar_entry_var.get()
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
            if qty > producto['existencia']:
                messagebox.showerror('Error', 'La cantidad supera la existencia.')
                self.qty_entry_var.set('')
                return
            
            # IF THE PRODUCT IS ALREADY IN THE LIST, IT ADDS THE QTY
            if codigo in self.product_list:
                for item in self.treeview_main.get_children():
                    values = self.treeview_main.item(item)
                    if values['text'] == codigo:
                        name = values['values'][0]
                        current_qty = values['values'][1]
                        cost = values['values'][2].split(' ')[1].strip()
                        cost = float(cost)
                        new_qty = int(current_qty) + qty
                        cost_bs = new_qty * self.DOLAR
                        cost_dolar = new_qty * cost
                        self.treeview_main.item(item, values=(name,new_qty,f'$ {cost}',f'Bs. {cost_bs:,.2f}',f'$ {cost_dolar:,.2f}'))
                        # RECALCULATE TOTAL
                        self.UpdateTotal()
                        # CLEAN ENTRIES
                        self.product_code_entry_var.set('')
                        self.product_code_entry.focus()
                        # SUBTRACT IN STOCK
                        INVENTARIO.SellProduct(codigo,qty)
                        help_frame.destroy()
                        return
            if codigo not in self.inventory_codes:
                messagebox.showerror('Error', f'Producto con código {codigo} no se encuentra en la base de datos.')
                return
            
            
            # -----------------------------------------------------
            # -----------------------------------------------------
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
            INVENTARIO.SellProduct(codigo,qty)
            # CERRAR EL PRODUCT HELP FRAME
            help_frame.destroy()
            self.UpdateTotal()
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
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# SEARCH PRODUCT BY CODE - SEARCH PRODUCT BY CODE - SEARCH PRODUCT BY CODE -
# SEARCH PRODUCT BY CODE - SEARCH PRODUCT BY CODE - SEARCH PRODUCT BY CODE -
    def SearchProductByCode(self):
        # GET DATA
        codigo = self.product_code_entry_var.get()
        qty = self.product_qty_entry_var.get()
        # CATCH QTY ERROR
        try:
            qty = int(qty)
        except ValueError:
            qty = 1
        # GET PRODUCT INFO
        if codigo in self.inventory_codes:
            producto = INVENTARIO.GetProducto(codigo)

            # Validar stock antes de vender
            if producto['existencia'] < qty:
                messagebox.showerror('Error', 'No hay suficiente stock disponible.')
                self.product_code_entry_var.set('')
                self.product_code_entry.focus()
                return

            # Intentar vender el producto
            if not INVENTARIO.SellProduct(codigo, qty):
                messagebox.showerror('Error', 'No se pudo procesar la venta. Intente nuevamente.')
                self.product_code_entry_var.set('')
                self.product_code_entry.focus()
                return
            
            # IF THE PRODUCT IS ALREADY IN THE LIST, IT ADDS ONE MORE TO QTY
            if codigo in self.product_list:
                for item in self.treeview_main.get_children():
                    values = self.treeview_main.item(item)
                    if values['text'] == codigo:
                        name = values['values'][0]
                        current_qty = values['values'][1]
                        cost = values['values'][2].split(' ')[1].strip()
                        cost = float(cost)
                        new_qty = int(current_qty) + qty
                        cost_bs = new_qty * self.DOLAR
                        cost_dolar = new_qty * cost
                        self.treeview_main.item(item, values=(name,new_qty,f'$ {cost}',f'Bs. {cost_bs:,.2f}',f'$ {cost_dolar:,.2f}'))
                        # RECALCULATE TOTAL
                        self.UpdateTotal()
                        # CLEAN ENTRIES
                        self.product_code_entry_var.set('')
                        self.product_qty_entry_var.set('')
                        self.product_code_entry.focus()
                        return

            # Resto del código igual...
            self.treeview_main.insert("", 'end',
                text=producto['codigo'],
                values=(producto['nombre'],
                        qty,
                        f'$ {producto['precio1']}',
                        f'Bs. {format(float(self.DOLAR * float(producto['precio1'])*qty),',.2f')}',
                        f'$ {format(producto['precio1'] * qty,',.2f')}'))
            self.product_list.append(str(codigo).strip())

            # CLEAR ENTRY
            self.product_code_entry_var.set('')
            self.product_qty_entry_var.set('')
            self.product_code_entry.focus()
            # UPDATE TOTAL
            self.UpdateTotal()
        else:
            messagebox.showerror('Error', f'Producto con código {codigo} no se encuentra en la base de datos.')
            self.product_code_entry_var.set('')
            self.product_code_entry.focus()
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - 
# CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - CASHOUT - 
    def CobrarFactura(self):
        # GENERAR NUMERO DE FACTURA
        def GenerateInvoiceNumber():
            """Genera un número de factura único basado en timestamp"""
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            return f"FACT-{timestamp}"
        # PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT -
        # PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT -
        def ProcessPayment():
            monto_dolar = cash_received_dolar_var.get()
            monto_bs = cash_received_bs_var.get()
            cliente = self.cod_client_entry_var.get()
            # VALIDAR QUE SEAN NUMEROS
            try:
                monto_dolar = float(monto_dolar) if monto_dolar else 0.0
                monto_bs = float(monto_bs) if monto_bs else 0.0
            except ValueError:
                messagebox.showerror('Error', 'Verifica que los montos ingresados sean correctos.')
                return
            # CALCULAR MONTO TOTAL PAGADO EN DOLARES
            total_pagado_dolar = monto_dolar + (monto_bs / self.DOLAR)
            # VALIDAR QUE EL MONTO PAGADO SEA SUFICIENTE
            if total_pagado_dolar < self.total_DOLAR:
                # SI NO ES SUFICIENTE, REBAJAR EL MONTO PAGADO Y ACTUALIZAR EL LABEL DEL FALANTE
                faltante = self.total_DOLAR - total_pagado_dolar
                messagebox.showerror('Error', f'Faltan $ {faltante:,.2f}')
                return
            # CALCULAR CAMBIO
            cambio_dolar = total_pagado_dolar - self.total_DOLAR
            cambio_bs = cambio_dolar * self.DOLAR
            # GENERAR NUMERO DE FACTURA
            numero_factura = GenerateInvoiceNumber()
            # GUARDAR FACTURA EN LA BASE DE DATOS
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            factura = {
                'numero': numero_factura,
                'cliente': cliente,
                'fecha_hora': fecha_hora,
                'total_dolar': self.total_DOLAR,
                'total_bs': self.total_BOLIVAR,
                'productos': [],
            }
            for item in self.treeview_main.get_children():
                values = self.treeview_main.item(item)
                producto = {
                    'codigo': values['text'],
                    'cantidad': values['values'][1],
                    'precio_unidad': values['values'][2],
                    'precio_dolar': values['values'][4],
                    'precio_bs': values['values'][3]
                }
                factura['productos'].append(producto)
            INVENTARIO.SaveFactura(factura)
            # IMPRIMIR FACTURA
            self.ImprimirFactura(factura)
            # CERRAR VENTANA DE COBRO
            cashout_frame.destroy()
        # ----------------------------------------------------------------
        # ----------------------------------------------------------------
        # SI NO HAY PRODUCTOS, NO DEJA COBRAR
        if self.product_list == []:
            messagebox.showerror('Error','No hay productos en la factura.')
            return
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        # CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW - CREATE THE WINDOW -
        cashout_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
        cashout_frame.title('Cobrar factura')
        cashout_frame.geometry('800x450')
        cashout_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        cashout_frame.transient(self)
        cashout_frame.grab_set()
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE -
        # TITLE FRAME
        title_frame = ctk.CTkFrame(cashout_frame,
                        fg_color=APP_COLOR['sec'],
                        height=50,
                        corner_radius=0)
        title_frame.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        # TITLE LABEL - TITLE LABEL - TITLE LABEL
        title_label = ctk.CTkLabel(title_frame,
                        text='Cobrar factura',
                        bg_color='transparent',
                        text_color=APP_COLOR['white_m'],
                        font=FONT['text'])
        title_label.pack(expand=True,fill='x',pady=5)
        # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
        # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
        prog_frame = ctk.CTkFrame(cashout_frame,
                        fg_color=APP_COLOR['white_m'],
                        height=50,
                        corner_radius=0)
        prog_frame.place(relx=0,rely=0.1,relwidth=1,relheight=0.9)
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS -
        # TOTAL A PAGAR EN DOLARES
        total_to_pay_dolar_label = ctk.CTkLabel(prog_frame,
                        text='Total a pagar en $',
                        font=FONT['text_light'],
                        text_color=APP_COLOR['gray'])
        total_to_pay_dolar_label.place(relx=0.1,rely=0.2,anchor='w')
        total_to_pay_dolar_value = ctk.CTkLabel(prog_frame,
                        text=f'$ {format(self.total_DOLAR,",.2f")}',
                        font=FONT['text_big'],
                        text_color=APP_COLOR['black_m'])
        total_to_pay_dolar_value.place(relx=0.1,rely=0.3,anchor='w')
        # TOTAL A PAGAR EN BOLIVARES
        total_to_pay_bs_label = ctk.CTkLabel(prog_frame,
                        text='Total a pagar en Bs.',
                        font=FONT['text_light'],
                        text_color=APP_COLOR['gray'])
        total_to_pay_bs_label.place(relx=0.1,rely=0.5,anchor='w')
        total_to_pay_bs_value = ctk.CTkLabel(prog_frame,
                        text=f'Bs. {format(self.total_BOLIVAR,",.2f")}',
                        font=FONT['text_big'],
                        text_color=APP_COLOR['black_m'])
        total_to_pay_bs_value.place(relx=0.1,rely=0.6,anchor='w')
        # EFECTIVO RECIBIDO EN DOLARES
        cash_received_dolar_label = ctk.CTkLabel(prog_frame,
                        text='Efectivo recibido en $',
                        font=FONT['text_light'],
                        text_color=APP_COLOR['gray'])
        cash_received_dolar_label.place(relx=0.6,rely=0.2,anchor='w')
        # EFECTIVO RECIBIDO EN BOLIVARES
        cash_received_bs_label = ctk.CTkLabel(prog_frame,
                        text='Efectivo recibido en Bs.',
                        font=FONT['text_light'],
                        text_color=APP_COLOR['gray'])
        cash_received_bs_label.place(relx=0.6,rely=0.5,anchor='w')
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES -
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES -
        # EFECTIVO RECIBIDO EN DOLARES
        cash_received_dolar_var = tk.StringVar()
        cash_received_dolar_entry = ctk.CTkEntry(prog_frame,
                        textvariable=cash_received_dolar_var,
                        fg_color=APP_COLOR['white'],
                        border_color=APP_COLOR['gray'])
        cash_received_dolar_entry.place(relx=0.6,rely=0.3,anchor='w',width=200)
        cash_received_dolar_entry.focus()
        cash_received_dolar_entry.bind("<Return>",lambda event:ProcessPayment())
        # EFECTIVO RECIBIDO EN BOLIVARES
        cash_received_bs_var = tk.StringVar()
        cash_received_bs_entry = ctk.CTkEntry(prog_frame,
                        textvariable=cash_received_bs_var,
                        fg_color=APP_COLOR['white'],
                        border_color=APP_COLOR['gray'])
        cash_received_bs_entry.place(relx=0.6,rely=0.6,anchor='w',width=200)
        cash_received_bs_entry.bind("<Return>",lambda event:ProcessPayment())
                                        
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # CLOSE WINDOW
        close_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=10,
                        image=ICONS['cancel'],
                        command=lambda:cashout_frame.destroy(),
                        fg_color=APP_COLOR['red_m'],
                        hover_color=APP_COLOR['red_s'])
        close_btn.place(relx=0.95,rely=0.02,anchor='ne')
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------
# UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - 
# UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - 
    def UpdateTotal(self):
        self.total_DOLAR = 0
        self.total_BOLIVAR = 0
        for item in self.treeview_main.get_children():
            info = self.treeview_main.item(item)
            # DOLARS
            subtotal_dolar = info['values'][4].split(' ')[1].strip()
            subtotal_dolar = float(subtotal_dolar.replace(',', ''))
            self.total_DOLAR += subtotal_dolar
            # BOLIVARES
            subtotal_bolivar = info['values'][3].split(' ')[1].strip()
            subtotal_bolivar = float(subtotal_bolivar.replace(',', ''))
            self.total_BOLIVAR += subtotal_bolivar
        # UPDATE LABELS
        self.total_fact_dolar_label.configure(text=f'$ {format(self.total_DOLAR,',.2f')}')
        self.total_fact_bs_label.configure(text=f'Bs. {format(self.total_BOLIVAR,',.2f')}')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - 
# SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - SEARCH CLIENT - 
    def SearchClient(self):
        code = self.cod_client_entry_var.get().strip()
        try:
            code = int(code)
        except ValueError:
            messagebox.showerror('Error','Ingrese un codigo de cliente valido')
            self.cod_client_entry_var.set('')
            self.cod_client_entry.focus()
            return
        client_data = CLIENT_MANAGER.GetClientByCode(code)
        self.name_client_entry_var.set(client_data['nombre'])
        self.fiscal_client_entry_var.set(client_data['id_fiscal'])
        self.phone_client_entry_var.set(client_data['telefono'] or '')
        self.address_client_entry_var.set(client_data['direccion1'] or '')
        self.mail_client_entry_var.set(client_data['email'] or '')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - 
# CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - CANCEL BILL - 
    # Agregar en la clase FacturacionProg, en la sección FUNCTIONS
    def CancelFact(self):
        """
        Cancela la factura actual, revierte el stock y limpia la interfaz
        """
        if not self.product_list:
            messagebox.showinfo("Información", "No hay productos para cancelar")
            return
        
        # Confirmar cancelación
        respuesta = messagebox.askyesno(
            "Cancelar Factura", 
            "¿Está seguro de cancelar la factura?\nSe revertirá el stock de todos los productos."
        )
        
        if not respuesta:
            return
        
        try:
            # Preparar lista de productos a revertir (código, cantidad)
            productos_a_revertir = []
            for item in self.treeview_main.get_children():
                info = self.treeview_main.item(item)
                codigo = info['text']
                cantidad = int(info['values'][1])  # La cantidad está en el índice 1
                
                productos_a_revertir.append((codigo, cantidad))
            
            # Llamar a la función de la base de datos
            if INVENTARIO.ReturnProducts(productos_a_revertir):
                # Limpiar interfaz
                self.ClearInterface()
                messagebox.showinfo("Éxito", "Factura cancelada y stock revertido correctamente")
            else:
                messagebox.showerror("Error", "No se pudo revertir el stock. Contacte al administrador.")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al cancelar factura: {str(e)}")
# DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - 
# DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - DELETE PRODUCT - 
    # DELETE A PRODUCT ON THE LIST
    def DeleteSelectedProduct(self):
        """Elimina un producto seleccionado del treeview y revierte su stock"""
        selected = self.treeview_main.selection()
        if not selected:
            messagebox.showinfo("Seleccionar", "Seleccione un producto para eliminar")
            return

        item = selected[0]
        info = self.treeview_main.item(item)
        codigo = info['text']
        cantidad = int(info['values'][1])

        # Confirmar eliminación
        respuesta = messagebox.askyesno(
            "Eliminar Producto", 
            f"¿Eliminar {info['values'][0]} de la factura?"
        )

        if not respuesta:
            return

        try:
            # Revertir stock
            if INVENTARIO.ReturnProducts([(codigo, cantidad)]):
                # Eliminar de la lista y treeview
                if codigo in self.product_list:
                    self.product_list.remove(codigo)
                self.treeview_main.delete(item)
                self.product_code_entry_var.set('')
                self.product_qty_entry_var.set('')
                self.UpdateTotal()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo revertir el stock")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar producto: {str(e)}")
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
    def ClearInterface(self):
        """Limpia toda la interfaz de facturación"""
        # Limpiar treeview
        for item in self.treeview_main.get_children():
            self.treeview_main.delete(item)
        # Limpiar lista de productos
        self.product_list.clear()
        # Limpiar campos de cliente
        self.cod_client_entry_var.set('')
        self.name_client_entry_var.set('')
        self.phone_client_entry_var.set('')
        self.fiscal_client_entry_var.set('')
        self.mail_client_entry_var.set('')
        self.address_client_entry_var.set('')
        # Limpiar campos de producto
        self.product_code_entry_var.set('')
        self.product_qty_entry_var.set('')
        # Actualizar totales a cero
        self.UpdateTotal()
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
    