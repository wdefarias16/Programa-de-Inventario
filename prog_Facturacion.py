import tkinter as tk
import customtkinter as ctk
import datetime
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from Help_Funcs_Products import Products_Help_Window
from Help_Funcs_Customer import Add_Customer_Window
from PIL import Image, ImageTk

class FacturacionProg(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        self.DOLAR = ACCOUNTING_MANAGER.GetLastDolarValue()
    # -----------------------------------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
    # -----------------------------------------------------------------------------------------------
        # FRAME
        title_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['sec'],
                        corner_radius=0,)
        title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
        title_label = ctk.CTkLabel(title_frame,
                        text='Facturación',
                        text_color=APP_COLOR['white_m'],
                        font=FONT['title_bold'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
        home_btn = ctk.CTkButton(title_frame,
                        image=ICONS['home'],
                        text='',
                        width=40,
                        height=40,
                        fg_color=APP_COLOR['black_m'],
                        hover_color=APP_COLOR['black'])
        home_btn.place(relx=0.05,rely=0.5,anchor='center')
        # GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON - GO BACK BUTTON -
        self.go_back_btn = ctk.CTkButton(title_frame,
                text='',
                image=ICONS['back'],
                width=40,
                height=40,
                text_color=APP_COLOR['black_m'],
                font=FONT['text_small'],
                fg_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['black'],
                command=lambda: self.GoBack())
        self.go_back_btn.place(relx=0.1,rely=0.5,anchor='center')
    # ---------------------------------------------------------------
    # INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME - INFO FRAME 
    # ---------------------------------------------------------------
        # -----------------------------------------------------------
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        # -----------------------------------------------------------
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
    # ---------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME 
    # ---------------------------------------------------------------
        # ---------------------------------------------------------------
        # FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - FRAME - 
        main_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['white_m'],
                        corner_radius=0)
        main_frame.place(relx=0,y=69.5,relwidth=0.75,relheight=1,anchor='nw')
    # -------------------------------------------------------------------
    # CUSTOMER DATA - CUSTOMER DATA - CUSTOMER DATA - CUSTOMER DATA - CUS
    # -------------------------------------------------------------------
        # ---------------------------------------------------------------
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENT
        # ---------------------------------------------------------------
        # CEDULA DE CLIENTE 
        self.cedula_client_entry_var = tk.StringVar()
        self.cedula_client_entry = ctk.CTkEntry(main_frame,
                        textvariable = self.cedula_client_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.cedula_client_entry.place(relx=0.075,rely=0.2,relwidth=0.2,anchor='nw')
        self.cedula_client_entry.bind("<Return>",lambda event:self.SearchClient())
        # ---------------------------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS 
        # ---------------------------------------------------------------
        # CODIGO DE CLIENTE
        cod_label = ctk.CTkLabel(main_frame,
                        text='Cedula cliente',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        cod_label.place(relx=0.075,rely=0.15,anchor='nw')
        # Nombre del cliente
        self.nombre_cliente_label = ctk.CTkLabel(main_frame,
                        text='Cliente: ',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        self.nombre_cliente_label.place(relx=0.075,rely=0.25,anchor='nw')
        # ---------------------------------------------------------------
        # BOTONES - 
        # ---------------------------------------------------------------
        search_customer_btn = ctk.CTkButton(main_frame,
                                text='',
                                width=30,
                                height=30,
                                image=ICONS['search'],
                                command=self.Add_Customer_Window_CB,
                                fg_color=APP_COLOR['main'],
                                hover_color=APP_COLOR['sec'])
        search_customer_btn.place(relx=0.30,rely=0.18,anchor='w')
    # -------------------------------------------------------------------
    # ENTRIES PRODUCT DATA - ENTRIES PRODUCT DATA -
    # -------------------------------------------------------------------
        # CODIGO DE PRODUCTO
        self.product_code_entry_var = tk.StringVar()
        self.product_code_entry = ctk.CTkEntry(main_frame,
                        width=150,
                        height=30,
                        textvariable = self.product_code_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.product_code_entry.place(relx=0.60,rely=0.27,anchor='nw')
        self.product_code_entry.bind("<Return>",lambda event:self.SearchProductByCode())
        # CANTIDAD DE PRODUCTO
        self.product_qty_entry_var = tk.StringVar()
        self.product_qty_entry = ctk.CTkEntry(main_frame,
                        width=65,
                        height=30,
                        textvariable = self.product_qty_entry_var,
                        border_width = 0,
                        fg_color = APP_COLOR['white'])
        self.product_qty_entry.place(relx=0.78,rely=0.27,anchor='nw')
        # ---------------------------------------------------------------
        # LABELS PRODUCT DATA - LABELS PRODUCT DATA - LABELS PRODUCT DATA
        # ---------------------------------------------------------------
        # CODIGO DE PRODUCTO
        product_code_label = ctk.CTkLabel(main_frame,
                        text='Producto',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        product_code_label.place(relx=0.60,rely=0.22,anchor='nw')
        # CANTIDAD DE PRODUCTO
        product_qty_label = ctk.CTkLabel(main_frame,
                        text='Cantidad',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        product_qty_label.place(relx=0.78,rely=0.22,anchor='nw')
        # ---------------------------------------------------------------
        # TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT - TOTAL FACT
        # ---------------------------------------------------------------
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
        # ---------------------------------------------------------------
        # BOTONES - BOTONES - BOTONES - BOTONES - BOTONES - BOTONES -
        # ---------------------------------------------------------------
        # ADD PRODUCT
        self.btn_add_product = ctk.CTkButton(main_frame,
                        text="+",
                        width=50,
                        height=30,
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'],
                        command=self.Products_Help_Window_CB)
        self.btn_add_product.place(relx=0.87,y=190,anchor='nw')
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
        # ---------------------------------------------------------------
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW
        # ---------------------------------------------------------------
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.theme_use("alt")
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 40,
            font = FONT['text'],
            fieldbackground = APP_COLOR['white'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['white_m'],
            font = FONT['text'])

        self.treeview_main = ttk.Treeview(main_frame,
                                    style='Custom.Treeview',
                                    columns=('Descripcion','Cantidad','Unidad',
                                             'Bolivares','Dolares'))
        self.treeview_main.place(relx=0.5,rely=0.34,relwidth=0.85,relheight=0.3,anchor='n')
        self.treeview_main.bind("<<TreeviewSelect>>",self.ClickLista)
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
        # ---------------------------------------------------------------
        # FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR - FOOTER BAR
        # ---------------------------------------------------------------
        # FRAME
        footer_frame = ctk.CTkFrame(self,
                                    height=30,
                                    fg_color=APP_COLOR['sec'],
                                    corner_radius=0)
        footer_frame.place(relx=0.5,rely=1,relwidth=1,anchor='s')
    # -------------------------------------------------------------------
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # -------------------------------------------------------------------
        # ---------------------------------------------------------------
        # AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - AYUDA DE PRODUCTOS - 
        # ---------------------------------------------------------------
    def Products_Help_Window_CB(self):
        self.SELECTED_PRODUCT = Products_Help_Window(self)
        if not self.SELECTED_PRODUCT:
            return
        "Obtener la cantidad"
        try:
            qty = int(self.product_qty_entry_var.get())
        except Exception:
            qty = 1
        "Verificar y ajustar existencia"
        if not ACCOUNTING_MANAGER.SellProduct(self.SELECTED_PRODUCT['codigo'], qty):
            return
        "Agregar producto a treeview"
        self.Load_In_Treeview(self.SELECTED_PRODUCT,qty)


    def Fill_Entry_Fields(self,producto):
        pass

    def Load_In_Treeview(self,product_data,qty):
        #ADD QTY IF PRODUCT ALREADY IN LIST
        if product_data['codigo'] in self.product_list:
            for item in self.treeview_main.get_children():
                values = self.treeview_main.item(item)
                print(values)
                if values['text'] == product_data['codigo']:
                    name = values['values'][0]
                    current_qty = values['values'][1]
                    cost = float(values['values'][2].split(' ')[1].strip())
                    new_qty = int(current_qty) + qty
                    cost_dolar = new_qty * cost
                    cost_bs = cost_dolar * self.DOLAR
                    self.treeview_main.item(item, 
                        values=(name,new_qty,f'$ {cost}',
                                f'Bs. {cost_bs:,.2f}',f'$ {cost_dolar:,.2f}'))
            #RECALCULATE TOTAL
            self.UpdateTotal()
            # CLEAN ENTRIES
            self.product_code_entry_var.set('')
            self.product_qty_entry_var.set('')
            self.product_code_entry.focus()
            return
        # ELSE ADD THE PRODUCT
        costo = float(product_data['precio1'])
        total_dol = costo * qty
        total_bs = total_dol * self.DOLAR
        self.treeview_main.insert('','end',
                                  text = product_data['codigo'],
                                  values=(product_data['nombre'],
                                          qty,
                                          f'$ {product_data['precio1']}',
                                          f'Bs. {total_bs:.2f}',
                                          f'$ {total_dol:.2f}'))
        self.product_list.append(product_data['codigo'])
        #RECALCULATE TOTAL
        self.UpdateTotal()
        # CLEAN ENTRIES
        self.product_code_entry_var.set('')
        self.product_qty_entry_var.set('')
        self.product_code_entry.focus()

# ----------------------------------------------------------------------------------------------
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
            if not ACCOUNTING_MANAGER.SellProduct(codigo, qty):
                self.product_code_entry_var.set('')
                self.product_code_entry.focus()
                return
            
            self.Load_In_Treeview(producto,qty)

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
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT -
        # PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT - PROCESS PAYMENT -
        def ProcessPayment():
            pass
        # ----------------------------------------------------------------
        # ----------------------------------------------------------------
        # SI NO HAY PRODUCTOS, NO DEJA COBRAR
        if self.product_list == []:
            messagebox.showerror('Error','No hay productos cargados.')
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
        # TOTAL LABEL - TOTAL LABEL - TOTAL LABEL - TOTAL LABEL - TOTAL LABEL -
        total_label = ctk.CTkLabel(prog_frame,
                        text='Total a pagar:',
                        font=FONT['subtitle_bold'],
                        text_color=APP_COLOR['gray'])
        total_label.place(relx=0.6,rely=0.1,anchor='w')
        # TOTAL BOLIVARES LABEL - TOTAL BOLIVARES LABEL - TOTAL BOLIVARES LABEL -
        total_bs_label = ctk.CTkLabel(prog_frame,
                        text=f'Bs. {format(self.total_BOLIVAR,",.2f")}',
                        font=FONT['text_big'],
                        text_color=APP_COLOR['black_m'])
        total_bs_label.place(relx=0.6,rely=0.2,anchor='w')
        # TOTAL DOLARES LABEL - TOTAL DOLARES LABEL - TOTAL DOLARES LABEL -
        total_dolar_label = ctk.CTkLabel(prog_frame,
                        text=f'$ {format(self.total_DOLAR,",.2f")}',
                        font=FONT['text_big2'],
                        text_color=APP_COLOR['green_s'])
        total_dolar_label.place(relx=0.6,rely=0.3,anchor='w')
        # COBRO LABEL - COBRO LABEL - COBRO LABEL - COBRO LABEL - COBRO LABEL -
        cobro_label = ctk.CTkLabel(prog_frame,
                        text='Monto recibido:',
                        font=FONT['subtitle_bold'],
                        text_color=APP_COLOR['gray'])
        cobro_label.place(relx=0.2,rely=0.1,anchor='w')
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES -
        # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES -
        # ENTRADA DE COBRO - ENTRADA DE COBRO - ENTRADA DE COBRO - ENTRADA DE COBRO -
        cobro_entry_var = tk.StringVar()
        cobro_entry = ctk.CTkEntry(prog_frame,
                        textvariable=cobro_entry_var,
                        width=200,
                        height=80,
                        fg_color=APP_COLOR['gray'],
                        border_color=APP_COLOR['gray'])
        cobro_entry.place(relx=0.2,rely=0.3,anchor='w')
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS -
        # BOTONES DE METODOS DE PAGO - BOTONES DE METODOS DE PAGO - BOTONES DE METODOS DE PAGO -
        # BOTONES DE METODOS DE PAGO - BOTONES DE METODOS DE PAGO - BOTONES DE METODOS DE PAGO -
        # EFECTIVO DOLAR - EFECTIVO DOLAR -  EFECTIVO DOLAR -  EFECTIVO DOLAR -  EFECTIVO DOLAR -
        efectivo_dolar_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=50,
                        height=50,
                        image=ICONS['dolar'],
                        anchor='center',
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'])
        efectivo_dolar_btn.place(relx=0.05,rely=0.1,anchor='w')
        # PAGO MOVIL - PAGO MOVIL - PAGO MOVIL - PAGO MOVIL - PAGO MOVIL - PAGO MOVIL -
        pago_movil_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=50,
                        height=50,
                        image=ICONS['pagomovil'],
                        anchor='center',
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'])
        pago_movil_btn.place(relx=0.05,rely=0.25,anchor='w')
        # TARJETA DE DEBITO - TARJETA DE DEBITO - TARJETA DE DEBITO - TARJETA DE DEBITO -
        tarjeta_debito_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=50,
                        height=50,
                        image=ICONS['tdd'],
                        anchor='center',
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'])
        tarjeta_debito_btn.place(relx=0.05,rely=0.40,anchor='w')
        # TARJETA DE CREDITO - TARJETA DE CREDITO - TARJETA DE CREDITO - TARJETA DE CREDITO -
        tarjeta_credito_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=50,
                        height=50,
                        image=ICONS['tdc'],
                        anchor='center',
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'])
        tarjeta_credito_btn.place(relx=0.05,rely=0.55,anchor='w')
        # ----------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
        # CLOSE WINDOW
        close_btn = ctk.CTkButton(prog_frame,
                        text='',
                        width=10,
                        image=ICONS['cancel'],
                        command=lambda:cashout_frame.destroy(),
                        fg_color=APP_COLOR['red_m'],
                        hover_color=APP_COLOR['red_s'])
        close_btn.place(relx=0.95,rely=0.02,anchor='ne')
        # PROCESS PAYMENT
        process_payment_btn = ctk.CTkButton(prog_frame,
                        text='Procesar pago',
                        width=200,
                        command=ProcessPayment,
                        fg_color=APP_COLOR['main'],
                        hover_color=APP_COLOR['sec'])
        process_payment_btn.place(relx=0.6,rely=0.8,anchor='w')

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
        code = self.cedula_client_entry_var.get().strip()
        try:
            code = int(code)
        except ValueError:
            messagebox.showerror('Error','Ingrese un codigo de cliente valido')
            self.cedula_client_entry_var.set('')
            self.cedula_client_entry.focus()
            return
        client_data = CLIENT_MANAGER.GetClientByCode(code)
        
    def Add_Customer_Window_CB(self):
        self.CUSTOMER = Add_Customer_Window(self)
        if not self.CUSTOMER:
            return
        self.cedula_client_entry_var.set(self.CUSTOMER['id_fiscal'])
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
            if ACCOUNTING_MANAGER.ReturnProducts(productos_a_revertir):
                # Limpiar interfaz
                self.ClearInterface()
                messagebox.showinfo("Éxito", "Factura cancelada y stock revertido correctamente")
                self.GoBack_CB()
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
            if ACCOUNTING_MANAGER.ReturnProducts([(codigo, cantidad)]):
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
    
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
    # GO BACK
    def GoBack(self):
        if self.product_list:
            respuesta = messagebox.askyesno(
                '¡Atención!',
                'Hay productos en la factura. ¿Desea cancelar la factura y volver atrás?')
            if respuesta:
                self.CancelFact()
        else:
            self.GoBack_CB()

    def ClickLista(self,event):
        pass