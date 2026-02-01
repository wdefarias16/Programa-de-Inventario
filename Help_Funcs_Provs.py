from DatabaseManager import *
from style import *
from tkinter import messagebox
# GUI
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
 
def ProvHelp(self):
    self.help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
    self.help_frame.geometry('600x400')
    self.help_frame.title('Ayuda de Proveedores')
    self.help_frame.transient(self)
    # GRID SETUP
    for rows in range(10):
        self.help_frame.rowconfigure(rows, weight=1,uniform='row')
    for columns in range(10):
        self.help_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
    title_frame = ctk.CTkFrame(self.help_frame,corner_radius=0,fg_color=APP_COLOR['sec'])
    title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
    title = ctk.CTkLabel(title_frame,
                         text='Ayuda de Proveedores',
                         bg_color='transparent',
                         text_color=APP_COLOR['white_m'],
                         height=50,
                         font=FONT['text'])
    title.pack(pady=10)   
    # BARRA DE BUSQUEDA
    self.search_help_bar_var = tk.StringVar()
    self.search_help_bar = ctk.CTkEntry(self.help_frame,
                                   width=200,
                                   textvariable=self.search_help_bar_var)
    self.search_help_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
    self.search_help_bar.after(100,lambda:self.search_help_bar.focus())
    self.search_help_bar.bind("<Return>",lambda event:self.SearchProv())
    self.search_help_bar.bind("<Control-BackSpace>", lambda event: self.ListProvs())
    # BOTONES TREEVIEW
    # BUSCAR
    search_btn = ctk.CTkButton(self.help_frame,
                               text='Buscar',
                               command=self.SearchLine,
                               fg_color=APP_COLOR['main'],
                               hover_color=APP_COLOR['sec'])
    search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
    # CANCELAR
    cancel_btn = ctk.CTkButton(self.help_frame,
                               text='Cancelar',
                               command=self.ListLines,
                               fg_color=APP_COLOR['red_m'],
                               hover_color=APP_COLOR['red_s'])
    cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
    self.help_treeview = ttk.Treeview(self.help_frame,
                                 style='Custom.Treeview',
                                 columns=('Proveedor'))
    self.help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
    # EVENTO DE SELECCIONAR PRODUCTO
    self.help_treeview.bind("<<TreeviewSelect>>",self.SelectProv)
    # CODIGO
    self.help_treeview.heading('#0',text='Código')
    self.help_treeview.column('#0',width=25,anchor='center')
    # PROVEEDOR
    self.help_treeview.heading('Proveedor',text='Proveedor')
    self.help_treeview.column('Proveedor',width=100,anchor='center')
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(self.help_frame,
                                 orientation='vertical',
                                 command=self.help_treeview.yview)
    scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
    self.help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR LOS PROVEEDORES
    self.ListProvs()
# BUSCAR PROVEEDORES POR NOMBRE
def SearchProv(self):
    for item in self.help_treeview.get_children():
        self.help_treeview.delete(item)
    search = self.search_help_bar_var.get().lower()
    outcome = PROV_MANAGER.SearchProvByName(search)
    for prov in outcome:
        self.help_treeview.insert("", 'end',
                             text=prov['codigo'],
                             values=(prov['nombre']))
# LISTAR PROVEEDORES
def ListProvs(self):
    self.search_help_bar.focus()
    self.search_help_bar_var.set('')
    lines = PROV_MANAGER.GetProvNames()
    for item in self.help_treeview.get_children():
            self.help_treeview.delete(item)
    for i, line in enumerate(lines):
        tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
        self.help_treeview.insert("", 'end',
                                   text=line.split(' - ')[0].strip(),
                                   values=(line.split(' - ')[1].strip(),),
                                   tags=(tag,))
    self.help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
    self.help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
# SELECCIONAR UN PROVEEDOR Y AGREGARLO AL CAMPO DE PROVEEEDOR
def SelectProv(self,event):
    item_id = self.help_treeview.selection()
    info = self.help_treeview.item(item_id)
    self.prove_var.set(f'{info['text']} - {info['values'][0]}')
    self.nombre_entry.focus()
    self.help_frame.destroy()