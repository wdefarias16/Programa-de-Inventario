import tkinter as tk
import customtkinter as ctk
import datetime
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import*
from Help_Funcs_Products import Products_Help_Window
from Help_Funcs_Customer import Add_Customer_Window,Customer_Help_Window
from PIL import Image, ImageTk

import os
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

class FacturacionProg(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.inventory_codes = INVENTARIO.GetCodigos()
        self.product_list = []
        self.DOLAR = ACCOUNTING_MANAGER.GetLastDolarValue()
        
        self.NRO_FACTURA = None
        self.CUSTOMER = None
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
        self.cedula_client_entry.place(relx=0.075,rely=0.2,relwidth=0.2,anchor='w')
        self.cedula_client_entry.bind("<Return>",lambda event:self.SearchClient())
        # ---------------------------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS 
        # ---------------------------------------------------------------
        # CODIGO DE CLIENTE
        cod_label = ctk.CTkLabel(main_frame,
                        text='Cedula cliente',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        cod_label.place(relx=0.075,rely=0.15,anchor='w')
        # Nombre del cliente
        self.nombre_cliente_label = ctk.CTkLabel(main_frame,
                        text='Cliente: ',
                        text_color=APP_COLOR['gray'],
                        font=FONT['text'])
        self.nombre_cliente_label.place(relx=0.075,rely=0.25,anchor='w')
        # ---------------------------------------------------------------
        # BOTONES - 
        # ---------------------------------------------------------------
        add_customer_btn = ctk.CTkButton(main_frame,
                                text='+',
                                width=40,
                                height=40,
                                command=self.Add_Customer_Window_CB,
                                fg_color=APP_COLOR['black_m'],
                                hover_color=APP_COLOR['black'])
        add_customer_btn.place(relx=0.3,rely=0.2,anchor='w')

        search_customer_btn = ctk.CTkButton(main_frame,
                                text='',
                                width=40,
                                height=40,
                                image=ICONS['search'],
                                command=self.Add_Customer_Window_CB,
                                fg_color=APP_COLOR['black_m'],
                                hover_color=APP_COLOR['black'])
        search_customer_btn.place(relx=0.35,rely=0.2,anchor='w')
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
                        height=45,
                        corner_radius=10,
                        font=FONT['subtitle_bold'],
                        text_color=APP_COLOR['white'],
                        fg_color=APP_COLOR['gray_s'])
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
        # 1. Validaciones iniciales
        if not self.product_list:
            messagebox.showerror('Error', 'No hay productos cargados.')
            return

        if not self.CUSTOMER:
            messagebox.showerror('¡Atención!','Debe cargar un cliente para la factura.')
            return

        confirmar = messagebox.askyesno("Confirmar Pago", "¿Desea proceder con el cobro y guardar la factura?")
        if not confirmar:
            return

        try:
            # 2. Generar número de factura (Obtenido de la DB)
            self.NRO_FACTURA = ACCOUNTING_MANAGER.GetNextFacturaNumber()
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 3. Preparar datos para la base de datos y el PDF
            productos_para_db = []
            lista_para_pdf = []
            
            for item in self.treeview_main.get_children():
                info = self.treeview_main.item(item)
                codigo = info['text']
                descripcion = info['values'][0]
                cantidad = int(info['values'][1])
                
                # Limpiamos los símbolos de moneda y comas para convertirlos a float
                precio_u = float(info['values'][2].replace('$ ', '').replace(',', ''))
                sub_bs = float(info['values'][3].replace('Bs. ', '').replace(',', ''))
                sub_dol = float(info['values'][4].replace('$ ', '').replace(',', ''))

                # Diccionario para SaveFactura
                productos_para_db.append({
                    'codigo': codigo,
                    'cantidad': cantidad,
                    'precio_unitario': precio_u,
                    'subtotal_dolares': sub_dol,
                    'subtotal_bolivares': sub_bs
                })

                # Diccionario para GenerateInvoicePDF (mantiene el formato visual)
                lista_para_pdf.append({
                    'codigo': codigo,
                    'descripcion': descripcion,
                    'cantidad': cantidad,
                    'precio_u': info['values'][2],
                    'sub_bs': info['values'][3],
                    'sub_dol': info['values'][4]
                })

            # 4. Estructura completa para ACCOUNTING_MANAGER.SaveFactura
            factura_data_db = {
                'numero_factura': self.NRO_FACTURA,
                'cliente_codigo': self.CUSTOMER['id_fiscal'],
                'fecha': fecha_actual,
                'total_dolares': self.total_DOLAR,
                'total_bolivares': self.total_BOLIVAR,
                'productos': productos_para_db
            }

            # 5. GUARDAR EN BASE DE DATOS
            if ACCOUNTING_MANAGER.SaveFactura(factura_data_db):
                # 6. Si el guardado fue exitoso, generar el PDF
                totales = {'dolar': self.total_DOLAR, 'bolivar': self.total_BOLIVAR}
                ruta_pdf = self.GenerateInvoicePDF(self.CUSTOMER, lista_para_pdf, totales, self.NRO_FACTURA)

                messagebox.showinfo("Éxito", f"Factura {self.NRO_FACTURA} guardada y generada con éxito.")
                
                # Abrir el PDF
                os.startfile(ruta_pdf)
                
                # Limpiar la interfaz
                self.ClearInterface()
            else:
                messagebox.showerror("Error", "No se pudo guardar la factura en la base de datos. La operación fue cancelada.")

        except Exception as e:
            messagebox.showerror("Error de Cobro", f"No se pudo procesar la factura: {str(e)}")

    def ClearInterface(self):
        """Limpia todos los campos para una nueva transacción"""
        self.treeview_main.delete(*self.treeview_main.get_children())
        self.product_list = []
        self.total_DOLAR = 0
        self.total_BOLIVAR = 0
        self.cedula_client_entry.configure(state='normal')
        self.cedula_client_entry_var.set('')
        self.nombre_cliente_label.configure(text='Cliente: ')
        self.product_code_entry_var.set('')
        self.product_qty_entry_var.set('')
        self.UpdateTotal()
        if hasattr(self, 'CUSTOMER'):
            del self.CUSTOMER
# -------------------------------------------------------------------------------
# UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - UPDATE TOTAL - 
# -------------------------------------------------------------------------------
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
        search = self.cedula_client_entry_var.get().strip()
        self.CUSTOMER = CLIENT_MANAGER.Search_Customer_By_IdOrFiscal(search)
        if self.CUSTOMER:
            self.nombre_cliente_label.configure(text=f'Cliente: {self.CUSTOMER['nombre']}')
            self.cedula_client_entry.configure(fg_color=APP_COLOR['gray'],
                                               border_color = APP_COLOR['gray'],state='disabled')
            
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

    # GENERAR NUMERO DE FACTURA

    


    def GenerateInvoicePDF(self, customer_info, products, totals, invoice_num):
        # Crear carpeta de facturas si no existe
        if not os.path.exists("facturas"):
            os.makedirs("facturas")

        
        filename = os.path.join("facturas", f"{invoice_num}.pdf")
        doc = SimpleDocTemplate(filename, pagesize=LETTER)
        styles = getSampleStyleSheet()
        story = []

        # Estilos personalizados
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, fontSize=18, spaceAfter=10)
        header_style = ParagraphStyle('HeaderStyle', parent=styles['Normal'], fontSize=10, leading=12)
        
        # 1. ENCABEZADO Y TÍTULO
        fecha_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        story.append(Paragraph("FACTURA", title_style))
        story.append(Spacer(1, 0.2*inch))
        
        # 2. INFORMACIÓN DE LA FACTURA Y CLIENTE
        # Extraer nombre del label si CUSTOMER no está definido

        cliente_nombre = customer_info.get('nombre')
        cliente_id = customer_info.get('id_fiscal')
        
        info_data = [
            [f'{CLIENT_INFO[0]}'],
            [f"Nro. Factura: {invoice_num}", f"Fecha: {fecha_hora}"],
            [f"Cliente: {cliente_nombre} - R.I.F / Cédula: {cliente_id}"],
        ]
        
        info_table = Table(info_data, colWidths=[3.5*inch, 3.5*inch])
        info_table.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('ALIGN', (0,0), (0,-1), 'LEFT'),
            ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ]))
        story.append(info_table)
        story.append(Spacer(1, 0.3*inch))

        # 3. TABLA DE PRODUCTOS
        # Cabecera de la tabla
        table_data = [['Cod.', 'Descripción', 'Cant.', 'P. Unit $', 'Subtotal $', 'Subtotal Bs.']]
        
        for p in products:
            table_data.append([
                p['codigo'],
                p['descripcion'],
                p['cantidad'],
                p['precio_u'],
                p['sub_dol'],
                p['sub_bs']
            ])

        # Crear tabla
        product_table = Table(table_data, colWidths=[0.8*inch, 2.5*inch, 0.6*inch, 1.1*inch, 1.1*inch, 1.4*inch])
        product_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.black),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.white),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('ALIGN', (1,0), (1,-1), 'LEFT'), # Descripción a la izquierda
        ]))
        story.append(product_table)
        story.append(Spacer(1, 0.2*inch))

        # 4. TOTALES
        # Cálculo de IVA (16%)
        subtotal_gral = totals['dolar']
        # iva_dol = subtotal_gral * 0.16
        # total_con_iva_dol = subtotal_gral + iva_dol
        total_bs = totals['dolar'] * self.DOLAR

        totals_data = [
            ["", "", "SUBTOTAL:", f"$ {subtotal_gral:,.2f}"],
            #["", "", "I.V.A (16%):", f"$ {iva_dol:,.2f}"],
            ["", "", "TOTAL REF:", f"$ {subtotal_gral:,.2f}"],
            ["", "", "TOTAL BS:", f"Bs. {total_bs:,.2f}"]
        ]
        
        totals_table = Table(totals_data, colWidths=[1*inch, 3*inch, 1.5*inch, 2*inch])
        totals_table.setStyle(TableStyle([
            ('FONTNAME', (2,0), (2,-1), 'Helvetica-Bold'),
            ('ALIGN', (3,0), (3,-1), 'RIGHT'),
            ('FONTSIZE', (2,2), (3,3), 12), # Resaltar el total
            ('TEXTCOLOR', (2,3), (3,3), colors.darkgreen),
        ]))
        story.append(totals_table)

        # Generar PDF
        doc.build(story)
        return filename