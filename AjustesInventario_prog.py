import tkinter as tk
import customtkinter as ctk
from tkinter import ttk,messagebox
from style import FONT, ICONS, APP_COLORS
from DatabaseManager import*

import os
from datetime import datetime

from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle,
    Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT



class AjustesInventarioProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRAS
        self.GoBack_CB = GoBack_CB
        self.validate = self.register(self.ValidateDigit)
        self.inventory_codes = []
        self.product_list = []
        ROWS, COLUMNS = 20, 12
        self.inventory_codes = INVENTARIO.GetCodigos()

        
        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLORS[3],
                                   corner_radius=0,
                                   height=50)
        title_frame.pack(fill='x')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Ajustes de inventario',
                                   bg_color='transparent',
                                   text_color=APP_COLORS[0],
                                   font=FONT['title_light'])
        title_label.pack(pady=10)
        # PROG FRAME
        self.prog_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.prog_frame.pack(expand=True,fill='both',side='left')
        self.prog_frame.bind("<Return>",lambda event:self.ProductsHelp())

        # GRID SETUP
        for rows in range(ROWS):
            self.prog_frame.rowconfigure(rows,weight=1,uniform='a')
        for columns in range(COLUMNS):
            self.prog_frame.columnconfigure(columns,weight=1,uniform='a')
        # GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - GUI - 
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # NUM DOC
        self.num_doc_entry_var = tk.StringVar()
        self.num_doc_entry = ctk.CTkEntry(self.prog_frame,
                                          textvariable=self.num_doc_entry_var,
                                          fg_color=APP_COLORS[6],
                                          border_color=APP_COLORS[2],
                                          width=30)
        self.num_doc_entry.grid(row=4,column=1,rowspan=2,columnspan=2,sticky='nwe',pady=5)
        self.num_doc_entry.bind("<Return>", self.ObtenerAjuste)
        self.num_doc_entry.focus()
        # MANAGER ENTRY
        self.hidden_entry = ctk.CTkEntry(self.prog_frame, width=0,
                                         state='disabled',
                                         fg_color=APP_COLORS[0],
                                         border_color=APP_COLORS[0])
        self.hidden_entry.grid(row=0,column=0)
        self.hidden_entry.bind("<Return>", lambda event: self.ProductsHelp())
        # LOG TXT BOX
        self.text_box = ctk.CTkTextbox(self.prog_frame)
        self.text_box.grid(row=16,column=1,columnspan=COLUMNS-2,sticky='nswe')
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # NUM DOC
        num_doc_label = ctk.CTkLabel(self.prog_frame,
                                     text='Documento',
                                     text_color=APP_COLORS[1],
                                     font=FONT['text_light'])
        num_doc_label.grid(row=3,column=1,columnspan=2,sticky='ws')
        # LOG TEXT BOX
        log_label = ctk.CTkLabel(self.prog_frame,
                                     text='Motivo del ajuste',
                                     text_color=APP_COLORS[1],
                                     font=FONT['text_light'])
        log_label.grid(row=15,column=1,columnspan=2,sticky='w')
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # ADD PRODUCT
        self.btn_add_product = ctk.CTkButton(self.prog_frame,
                                            text="Agregar producto",
                                            width=50,
                                            fg_color=APP_COLORS[2],
                                            hover_color=APP_COLORS[3],
                                            command=self.ProductsHelp)
        self.btn_add_product.grid(row=4,column=9,columnspan=2,sticky='nse')
        # GO BACK
        go_back_btn = ctk.CTkButton(self.prog_frame,
                                    text="Volver atrás",
                                    width=50,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3],
                                    command=self.GoBack_CB)
        go_back_btn.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)
        # PRINT ADJUSTMENT
        imprimir_btn = ctk.CTkButton(
            self.prog_frame,
            text='Imprimir Ajuste',
            fg_color=APP_COLORS[8],
            hover_color=APP_COLORS[3],
            command=self.ImprimirAjustes)
        imprimir_btn.grid(row=1, column=7, columnspan=2, sticky='we', padx=5)
        # SAVE
        self.btn_guardar_ajuste = ctk.CTkButton(
            self.prog_frame,
            text="Guardar Ajuste",
            fg_color=APP_COLORS[8],
            hover_color=APP_COLORS[3],
            command=self.GuardarAjustes)
        self.btn_guardar_ajuste.grid(row=1, column=9, columnspan=2, sticky='we', padx=5)

        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLORS[0],
            foreground = APP_COLORS[1],
            rowheight = 30,
            font = FONT['text_small'],
            fieldbackground = APP_COLORS[0])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLORS[1],
            foreground = APP_COLORS[1],
            font = FONT['text_light'])
        self.treeview_main = ttk.Treeview(self.prog_frame,
                                     style='Custom.Treeview',
                                     columns=('Descripcion','Linea','Grupo',
                                              'Existencia','Ajuste','Final'))
        self.treeview_main.grid(row=5,column=1,sticky='nswe',pady=10,rowspan=9,columnspan=COLUMNS-2)
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
        
        # SCROLLBAR DEL TV
        scrollbar = ctk.CTkScrollbar(self.prog_frame,
                                     orientation='vertical',
                                     command=self.treeview_main.yview)
        scrollbar.grid(row=5,column=COLUMNS-1,sticky='nsw',padx=5,pady=5,rowspan=9)
        self.treeview_main.configure(yscrollcommand=scrollbar.set)
        self.update_idletasks()
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - 
# OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - OPEN PRODUCT HELP FRAME - 
    def ProductsHelp(self):
        # LIST INVENTORY IN TREEVIEW
        def ListInventory():
            self.qty_entry_var.set('')
            self.search_bar_entry.after(100,
                lambda:  self.search_bar_entry.configure(state='normal',
                fg_color=APP_COLORS[6],border_color=APP_COLORS[6]))
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
                                            fg_color=APP_COLORS[4],
                                            border_color=APP_COLORS[4])
            self.qty_entry.configure(state='normal',
                                     fg_color=APP_COLORS[6],
                                     border_color=APP_COLORS[6])
            self.qty_entry.focus_set()
        # -------------------------------------------------------------------------------------------------
    # CANCEL TREEVIEW SELECTION
        def RefreshSelection():
            self.qty_entry_var.set('')
            self.qty_entry.configure(state='disabled',
                                     fg_color=APP_COLORS[4],
                                     border_color=APP_COLORS[4])
            self.search_bar_entry_var.set('')
            self.search_bar_entry.configure(state='normal',
                                            fg_color=APP_COLORS[6],
                                            border_color=APP_COLORS[6])
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
            # GET ADJUSTMENT
            ajuste = self.qty_entry_var.get()
            try:
                ajuste = int(ajuste)
            except ValueError:
                messagebox.showerror('Error', 'Verifica que el campo "Cantidad" este correcto.')
                self.qty_entry.focus()
                return
            ajuste_final = existencia + ajuste
            if ajuste_final < 0:
                messagebox.showerror('Error', 'La existencia quedaría en negativo, verifique el ajuste.')
                self.qty_entry.focus()
                return

            self.treeview_main.insert("", 'end',
                text=producto['codigo'],
                values=(producto['nombre'],
                        producto['linea'],
                        producto['grupo'],
                        existencia,
                        ajuste,
                        ajuste_final))
            self.product_list.append(str(codigo).strip())
            help_frame.destroy()
            self.hidden_entry.focus()
        # -------------------------------------------------------------------------------------------------
        # CREATE THE WINDOW
        help_frame = ctk.CTkToplevel(self,fg_color=APP_COLORS[0])
        help_frame.title('Busqueda de productos')
        help_frame.geometry('800x450')
        help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
        help_frame.transient(self)
        help_frame.grab_set()
        # TITLE - TITLE - TITLE - 
        # TITLE FRAME
        title_frame = ctk.CTkFrame(help_frame,
                                   fg_color=APP_COLORS[3],
                                   height=50,
                                   corner_radius=0)
        title_frame.pack(expand=False,fill='x')
        # TITLE LABEL - TITLE LABEL - TITLE LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Búsqueda de productos',
                                   bg_color='transparent',
                                   text_color=APP_COLORS[0],
                                   font=FONT['text'])
        title_label.pack(expand=True,fill='x',pady=5)
        # PROG FRAME - PROG FRAME - PROG FRAME - PROG FRAME - 
        prog_frame = ctk.CTkFrame(help_frame,
                                   fg_color=APP_COLORS[0],
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
                                        fg_color=APP_COLORS[4],
                                        border_color=APP_COLORS[4])
        self.search_bar_entry.grid(row=2,column=1,columnspan=2,sticky='we')
        
        self.search_bar_entry.bind("<Return>",lambda event:SearchProductName())
        self.search_bar_entry.bind("<Control-BackSpace>",lambda event:RefreshSelection())
        # QUANTITY
        self.qty_entry_var = tk.StringVar()
        self.qty_entry = ctk.CTkEntry(prog_frame,
                                        state='disabled',
                                        textvariable=self.qty_entry_var,
                                        fg_color=APP_COLORS[4],
                                        border_color=APP_COLORS[4])
        self.qty_entry.grid(row=2,column=6,sticky='we')
        self.qty_entry.bind("<Control-BackSpace>",lambda event:RefreshSelection())
        self.qty_entry.bind("<Return>",lambda event:AddProduct())
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # SEARCH BAR
        search_bar_label = ctk.CTkLabel(prog_frame,
                                        text='Búsqueda por nombre',
                                        font=FONT['text_light'],
                                        text_color=APP_COLORS[4])
        search_bar_label.grid(row=1,column=1,columnspan=2,sticky='w')
        # QUANTITY
        qty_label = ctk.CTkLabel(prog_frame,
                                text='Cantidad',
                                font=FONT['text_light'],
                                text_color=APP_COLORS[4])
        qty_label.grid(row=1,column=6,columnspan=2,sticky='w')
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # CLOSE WINDOW
        close_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['cancel'],
                                  command=lambda:help_frame.destroy(),
                                  fg_color=APP_COLORS[9],
                                  hover_color=APP_COLORS[10])
        close_btn.grid(row=0,column=COLUMNS-1,sticky='we',padx=10,pady=10)
        # SEARCH
        search_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['search'],
                                  command=SearchProductName,
                                  fg_color=APP_COLORS[2],
                                  hover_color=APP_COLORS[3])
        search_btn.grid(row=2,column=3,sticky='w',padx=5)
        # REFRESH OR CANCEL SELECTION
        cancel_slct_btn = ctk.CTkButton(prog_frame,
                                  text='',
                                  image=ICONS['refresh'],
                                  command=RefreshSelection,
                                  fg_color=APP_COLORS[2],
                                  hover_color=APP_COLORS[3])
        cancel_slct_btn.grid(row=2,column=4,sticky='w')
        # ACCEPT
        accept_btn = ctk.CTkButton(prog_frame,
                                  text='Aceptar',
                                  command=AddProduct,
                                  fg_color=APP_COLORS[2],
                                  hover_color=APP_COLORS[3])
        accept_btn.grid(row=2,column=7,sticky='w',padx=5)
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
# MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - 
# MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - MODIFY A ADDED PRODUCT - 
    def ClickAjuste(self,event):
        item_id = self.treeview_main.selection()
        if not item_id:
            print("Advertencia: No hay ningún elemento seleccionado.")
            return
        info = self.treeview_main.item(item_id)
        codigo = str(info['text']).strip()
    # MODE ADJUSTMENT
        def ModAdjustmentMode():
            self.ajuste_edit_entry.configure(state='normal')
            self.ajuste_edit_entry.focus()
        # -------------------------------------------------------------------------------
    # MODIFY ADJUSTMENT
        def ModAdjustment():
            producto = INVENTARIO.GetProducto(codigo)
            ajuste = self.ajuste_edit_var.get()
            try:
                ajuste = int(ajuste)
            except ValueError:
                messagebox.showerror('Error', 'Verifica que el campo "Cantidad" este correcto.')
                self.ajuste_edit_entry.focus()
                return
            ajuste_final = existencia + ajuste
            if ajuste_final < 0:
                messagebox.showerror('Error', 'La existencia quedaría en negativo, verifique el ajuste.')
                self.ajuste_edit_entry.focus()
                return
            self.treeview_main.item(item_id,
                values=(producto['nombre'],
                        producto['linea'],
                        producto['grupo'],
                        existencia,
                        ajuste,
                        ajuste_final))
            self.btn_add_product.configure(state='enabled')
            self.edit_window.destroy()
        # -------------------------------------------------------------------------------
    # DELETE ADJUSTMENT
        def DelAdjustment():
            if not item_id:
                messagebox.showerror("Error", "Debe seleccionar un producto para eliminarlo.")
                return
            answer = messagebox.askyesno("Eliminar producto",f"¿Está seguro que desea eliminar el producto '{self.nombre}' de la lista?")
            if answer:
                if self.codigo in self.product_list:
                    self.product_list.remove(self.codigo)
                else:
                    print('No existe el codigo')
                self.treeview_main.delete(item_id)
                messagebox.showinfo("Ajustes", "Producto eliminado correctamente.")
                self.edit_window.destroy()
        # -------------------------------------------------------------------------------
        item_id = self.treeview_main.selection()
        if not item_id:
            print("Advertencia: No hay ningún elemento seleccionado.")
            return
        info = self.treeview_main.item(item_id)
        self.codigo = str(info['text']).strip()
        datos = info['values']
        self.nombre = datos[0]
        existencia = datos[3]
        ajuste = datos[4]
        # FRAME DE EDICION DE AJUSTES
        self.edit_window = ctk.CTkToplevel(self,
                                   fg_color=APP_COLORS[0])
        self.edit_window.geometry('600x350')
        self.edit_window.title('Editar')
        self.edit_window.protocol("WM_DELETE_WINDOW", lambda: None)
        self.edit_window.transient(self)
        edit_frame = ctk.CTkFrame(self.edit_window,corner_radius=5,fg_color=APP_COLORS[0])
        edit_frame.pack(expand=True,fill='both')
    # GRID SETUP
        ROWS, COLUMNS = 12,10
        for rows in range(ROWS):
            edit_frame.rowconfigure(rows, weight=1,uniform='a')
        for columns in range(COLUMNS):
            edit_frame.columnconfigure(columns,weight=1,uniform='a')
    # TITULO
        title_frame = ctk.CTkFrame(edit_frame,corner_radius=0,fg_color=APP_COLORS[3])
        title_frame.grid(row=0,column=0,rowspan=2,columnspan=10,sticky='nwe')
        title = ctk.CTkLabel(title_frame,
                             text='Editar existencia',
                             bg_color='transparent',
                             text_color=APP_COLORS[0],
                             height=50,
                             font=FONT['text'])
        title.pack(pady=10)
    # PRODUCTO
        producto_label = ctk.CTkLabel(edit_frame,
                                      text=self.nombre,
                                      font=FONT['title_bold'],
                                      text_color=APP_COLORS[4],
                                      bg_color='transparent')
        producto_label.grid(row = 3, column = 1, columnspan = 6, padx = 10, sticky = 'w')
        existencia_label = ctk.CTkLabel(edit_frame,
                                      text=f'Existencia actual: {existencia}',
                                      font=FONT['subtitle_bold'],
                                      text_color=APP_COLORS[4],
                                      bg_color='transparent')
        existencia_label.grid(row = 4, column = 1, columnspan = 6, padx = 10, sticky = 'w')
    # ENTRADAS
        # AJUSTE
        self.ajuste_edit_var = tk.StringVar()
        self.ajuste_edit_var.set(ajuste)
        self.ajuste_edit_entry = ctk.CTkEntry(edit_frame,
                                                state='disabled',
                                                textvariable=self.ajuste_edit_var,
                                                validate = 'key',
                                                validatecommand = (self.validate,'%P'),
                                                fg_color=APP_COLORS[6],
                                                border_width=0)
        self.ajuste_edit_entry.grid(row = 7, column = 1, columnspan = 2, sticky = 'we',padx = 10)
        self.ajuste_edit_entry.bind("<Return>",lambda event:ModAdjustment())
    # LABELS 
        # AJUSTE
        ajuste_label = ctk.CTkLabel(edit_frame,
                                      text=f'Ajuste',
                                      font=FONT['text_light'],
                                      text_color=APP_COLORS[4])
        ajuste_label.grid(row = 6, column = 1, columnspan = 2, sticky = 'w',padx = 10)
    # BOTONES
        # EDITAR
        editar_btn = ctk.CTkButton(edit_frame,
                                   text='Editar',
                                   command=ModAdjustmentMode,
                                   fg_color=APP_COLORS[2],
                                   hover_color=APP_COLORS[3])
        editar_btn.grid(row=9,column=1,columnspan=2,sticky='we',padx=10)
        # ELIMINAR
        eliminar_btn = ctk.CTkButton(edit_frame,
                                     text='',
                                     image=ICONS['trash'],
                                     command=DelAdjustment,
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        eliminar_btn.grid(row=9,column=3,sticky='we')
        # ACEPTAR
        aceptar_btn = ctk.CTkButton(edit_frame,
                                    text='Aceptar',
                                    command=ModAdjustment,
                                    fg_color=APP_COLORS[2],
                                    hover_color=APP_COLORS[3])
        aceptar_btn.grid(row=7,column=3,columnspan=2,sticky='we',padx=10)
        # CANCELAR
        cancelar_btn = ctk.CTkButton(edit_frame,
                                     text='',
                                     image=ICONS['cancel'],
                                     command=lambda: self.edit_window.destroy(),
                                     fg_color=APP_COLORS[9],
                                     hover_color=APP_COLORS[10])
        cancelar_btn.grid(row=3,column=COLUMNS-2,sticky='w')

    # VALIDATE DIGITS
    def ValidateDigit(self,text):
        text = text.replace("-", "", 1)
        if text == '':
            return True
        return text.isdigit()
    



    def ImprimirAjustes(self):
        """
        Recorre el Treeview de ajustes, valida datos y llama a GenerarPDFAjustes().
        """
        num_doc = self.num_doc_entry_var.get().strip()
        if not num_doc:
            messagebox.showerror('Error', 'Agregue un número de documento.')
            self.num_doc_entry.focus()
            return

        # Recoger motivo
        motivo = self.text_box.get('0.0', 'end').strip()
        if not motivo:
            messagebox.showerror('Error', 'Debe indicar el motivo del ajuste.')
            self.text_box.focus()
            return

        # Recoger ajustes
        ajustes = []
        for iid in self.treeview_main.get_children():
            info = self.treeview_main.item(iid)
            codigo = info['text']
            desc, linea, grupo, existencia, ajuste, final = info['values']
            ajustes.append([codigo, desc, linea, grupo, existencia, ajuste, final])

        if not ajustes:
            messagebox.showerror('Error', 'No hay ajustes para imprimir.')
            return

        # Crear carpeta y ruta de archivo
        carpeta = 'Data/AjustesInventario'
        os.makedirs(carpeta, exist_ok=True)
        ruta = os.path.join(carpeta, f'Ajuste_{num_doc}.pdf')

        # Generar y abrir el PDF
        self.GenerarPDFAjustes(
            path=ruta,
            documento=num_doc,
            motivo=motivo,
            fecha = datetime.now().strftime('%Y-%m-%d'),
            ajustes=ajustes
        )
        os.startfile(ruta)

    def GenerarPDFAjustes(self, path, documento, motivo, fecha, ajustes):
        """
        Crea un PDF con ReportLab que incluye:
        - Título
        - Número de documento, fecha y motivo
        - Tabla de ajustes realizados
        """
        doc = SimpleDocTemplate(
            path,
            pagesize=LETTER,
            leftMargin=50, rightMargin=50,
            topMargin=40, bottomMargin=30
        )

        styles = getSampleStyleSheet()
        title_style = styles['Heading2']
        normal = styles['Normal']
        wrap_desc = ParagraphStyle(
            name='wrap',
            parent=styles['BodyText'],
            fontSize=8, leading=10
        )

        story = []
        # Cabecera
        story.append(Paragraph('Ajuste de Inventario', title_style))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f'Documento: {documento}', normal))
        story.append(Paragraph(f'Fecha: {fecha}', normal))
        story.append(Spacer(1, 8))
        story.append(Paragraph('Motivo:', normal))
        story.append(Paragraph(motivo, wrap_desc))
        story.append(Spacer(1, 20))

        # Preparar datos de la tabla
        encabezados = ['Cod', 'Descripción', 'Línea', 'Grupo',
                       'Existencia', 'Ajuste', 'Final']
        data = [encabezados] + ajustes

        # Construir tabla
        table = Table(data, repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('GRID',            (0, 0), (-1, -1),   0.5, colors.grey),
            ('BACKGROUND',      (0, 0), (-1, 0),    colors.HexColor('#333333')),
            ('TEXTCOLOR',       (0, 0), (-1, 0),    colors.whitesmoke),
            ('FONTNAME',        (0, 0), (-1, 0),    'Helvetica-Bold'),
            ('FONTSIZE',        (0, 0), (-1, -1),   8),
            ('ALIGN',           (0, 0), (-1, -1),   'CENTER'),
            ('VALIGN',          (0, 0), (-1, -1),   'MIDDLE'),
            ('BACKGROUND',      (0, -1), (-1, -1),  colors.HexColor('#f0f0f0')),
        ]))

        story.append(table)
        story.append(Spacer(1, 20))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.grey))

        doc.build(story)

    def ModoVisualizacion(self, flag: bool):
        state = 'normal' if flag else 'disabled'
        # cabecera
        self.num_doc_entry.configure(state=state)
        # motivo
        self.text_box.configure(state=state)
        # botones
        self.btn_add_product.configure(state=state)
        self.btn_guardar_ajuste.configure(state=state)
        # Treeview principal: permitir o no selección
        selectmode = 'browse' if flag else 'none'
        self.treeview_main.configure(selectmode=selectmode)

    def CancelarVisualizacion(self):
        if hasattr(self, 'cancel_btn'):
            self.cancel_btn.destroy()
        # limpiar campos
        self.num_doc_entry_var.set('')
        self.text_box.configure(state='normal')
        self.text_box.delete('0.0', 'end')
        for iid in self.treeview_main.get_children():
            self.treeview_main.delete(iid)
        # volver al estado interactivo
        self.ModoVisualizacion(True)
        self.num_doc_entry.focus()

    def ObtenerAjuste(self, event=None):
        num_doc = self.num_doc_entry_var.get().strip()
        if not num_doc:
            return

        data = INVENTARIO.ObtenerAjuste(num_doc)
        if data is None:
            # si no existe, abrir búsqueda de productos
            return self.ProductsHelp()

        # deshabilitar UI para solo visualización
        self.ModoVisualizacion(False)

        # rellenar motivo
        self.text_box.configure(state='normal')                 # Activar edición
        self.text_box.delete('0.0', 'end')
        self.text_box.insert('0.0', data['motivo'])
        self.text_box.configure(state='disabled')

        # limpiar y rellenar Treeview
        for iid in self.treeview_main.get_children():
            self.treeview_main.delete(iid)

        for item in data['detalle']:
            prod = INVENTARIO.GetProducto(item['codigo'])
            self.treeview_main.insert(
                '', 'end',
                text=item['codigo'],
                values=(
                    prod['nombre'],
                    prod['linea'],
                    prod['grupo'],
                    item['cantidad'],
                    item['ajuste'],
                    item['final']
                )
            )

        # botón Cancelar (modo visualización)
        self.cancel_btn = ctk.CTkButton(
            self.prog_frame,
            text="Cancelar",
            fg_color=APP_COLORS[9],
            hover_color=APP_COLORS[10],
            command=self.CancelarVisualizacion
        )
        self.cancel_btn.grid(row=0, column=1, sticky='nw', padx=5, pady=5)

    def GuardarAjustes(self):
        num_doc = self.num_doc_entry_var.get().strip()
        if not num_doc:
            messagebox.showerror('Error', 'Agregue un número de documento.')
            self.num_doc_entry.focus()
            return

        motivo = self.text_box.get('0.0', 'end').strip()
        if not motivo:
            messagebox.showerror('Error', 'Indique el motivo del ajuste.')
            self.text_box.focus()
            return

        detalle = []
        for iid in self.treeview_main.get_children():
            info = self.treeview_main.item(iid)
            codigo = info['text']
            vals = info['values']
            existencia, ajuste, final = vals[3], vals[4], vals[5]
            detalle.append({
                'codigo': codigo,
                'cantidad': existencia,
                'ajuste': ajuste,
                'final': final
            })

        if not detalle:
            messagebox.showerror('Error', 'No hay productos para ajustar.')
            return

        fecha = datetime.now().strftime('%Y-%m-%d')
        try:
            INVENTARIO.GuardarAjusteInventario(
                num_documento=num_doc,
                motivo=motivo,
                fecha=fecha,
                detalle_ajuste=detalle
            )
            # volver a la vista anterior
            self.GoBack_CB()
        except Exception:
            # el mensaje ya lo muestra el DataManager
            pass