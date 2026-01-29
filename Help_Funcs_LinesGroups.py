from DatabaseManager import *
from style import *
from tkinter import messagebox
# GUI
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

    # LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - LINE HELP - 
    # FRAME DEL TREEVIEW
def Lines_Help_Window(self):
    self.LINE = {}
    # BUSCAR LINEAS POR NOMBRE
    def SearchLine():
        for item in self.line_help_treeview.get_children():
            self.line_help_treeview.delete(item)
        search = self.search_line_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchLineByName(search)
        for line in outcome:
            self.line_help_treeview.insert("", 'end',
                                 text=line['codigo'],
                                 values=(line['linea']))
    # LISTAR LINEAS
    def ListLines():
        self.search_line_bar.focus()
        self.search_line_bar_var.set('')
        lines = LINE_MANAGER.GetLineNames()
        for item in self.line_help_treeview.get_children():
                self.line_help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.line_help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(line.split(' - ')[1].strip(),),
                                       tags=(tag,))  # Asignar el tag a la fila

        # Configurar colores para los tags
        self.line_help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.line_help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
    # SELECCIONAR UNA LINEA Y AGREGARLA AL CAMPO DE LINEA
    def SelectLine(event):
        item_id = self.line_help_treeview.selection()
        info = self.line_help_treeview.item(item_id)
        self.LINE = f'{info['text']} - {info['values'][0]}'
        self.line_help_frame.destroy()
    # ------------------------------------------------------------------------
    self.line_help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
    self.line_help_frame.geometry('600x400')
    self.line_help_frame.title('Ayuda de lineas')
    self.line_help_frame.transient(self)
    # GRID SETUP
    for rows in range(10):
        self.line_help_frame.rowconfigure(rows, weight=1,uniform='row')
    for columns in range(10):
        self.line_help_frame.columnconfigure(columns,weight=1,uniform='column')
    # TITULO
    title_frame = ctk.CTkFrame(self.line_help_frame,corner_radius=0,fg_color=APP_COLOR['sec'])
    title_frame.grid(row=0,column=0,columnspan=10,sticky='nswe')
    title = ctk.CTkLabel(title_frame,
                         text='Ayuda de líneas',
                         bg_color='transparent',
                         text_color=APP_COLOR['white_m'],
                         height=50,
                         font=FONT['text'])
    title.pack(pady=10)   
    # BARRA DE BUSQUEDA
    self.search_line_bar_var = tk.StringVar()
    self.search_line_bar = ctk.CTkEntry(self.line_help_frame,
                                   width=200,
                                   textvariable=self.search_line_bar_var)
    self.search_line_bar.grid(row=1,column=0,columnspan=2,sticky='we',padx=5,pady=5)
    self.search_line_bar.after(100,lambda:self.search_line_bar.focus())
    self.search_line_bar.bind("<Return>",lambda event:SearchLine())
    self.search_line_bar.bind("<Control-BackSpace>", lambda event:ListLines())
    # BOTONES TREEVIEW
    # BUSCAR
    search_btn = ctk.CTkButton(self.line_help_frame,
                               text='Buscar',
                               command=SearchLine,
                               fg_color=APP_COLOR['main'],
                               hover_color=APP_COLOR['sec'])
    search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
    # CANCELAR
    cancel_btn = ctk.CTkButton(self.line_help_frame,
                               text='Cancelar',
                               command=ListLines,
                               fg_color=APP_COLOR['red_m'],
                               hover_color=APP_COLOR['red_s'])
    cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
    self.line_help_treeview = ttk.Treeview(self.line_help_frame,
                                 style='Custom.Treeview',
                                 columns=('Linea'))
    self.line_help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
    # EVENTO DE SELECCIONAR PRODUCTO
    self.line_help_treeview.bind("<<TreeviewSelect>>",SelectLine)
    # CODIGO
    self.line_help_treeview.heading('#0',text='Codigo')
    self.line_help_treeview.column('#0',width=25,anchor='center')
    # LINEA
    self.line_help_treeview.heading('Linea',text='Linea')
    self.line_help_treeview.column('Linea',width=100,anchor='center')
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(self.line_help_frame,
                                 orientation='vertical',
                                 command=self.line_help_treeview.yview)
    scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
    self.line_help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
    ListLines()
    self.line_help_frame.wait_window()
    return self.LINE