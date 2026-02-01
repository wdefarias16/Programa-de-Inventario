from DatabaseManager import *
from style import *
from tkinter import messagebox
# GUI
from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
# --------------------------------------------------------
# LINE HELP WINDOW - LINE HELP WINDOW - LINE HELP WINDOW - 
# --------------------------------------------------------
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
    # LISTAR TODOS LOS PRODUCTOS CARGADOS AL INICIO DEL PROGRAMA
    ListLines()
    self.line_help_frame.wait_window()
    return self.LINE

# --------------------------------------------------------
# GROUP HELP WINDOW - GROUP HELP WINDOW - GROUP HELP WINDOW - 
# --------------------------------------------------------
def Groups_Help_Window(self,linea_id):
    self.GRUPO = {}
    # BUSCAR GRUPO POR NOMBRE
    def SearchGroup():
        for item in self.help_treeview.get_children():
            self.help_treeview.delete(item)
        search = self.search_help_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchGroupByName(search,line=linea_id)
        for group in outcome:
            self.help_treeview.insert("", 'end',
                                 text=group['codigo'],
                                 values=(group['linea'],
                                         group['grupo']))
    # LISTAR PROVEEDORES
    def ListGroups():
        self.search_help_bar.focus()
        self.search_help_bar_var.set('')
        lines = LINE_MANAGER.GetGroupNames(linea_id)
        for item in self.help_treeview.get_children():
                self.help_treeview.delete(item)
        for i, line in enumerate(lines):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
            self.help_treeview.insert("", 'end',
                                       text=line.split(' - ')[0].strip(),
                                       values=(linea_id,
                                                line.split(' - ')[1].strip()),
                                       tags=(tag,))
        self.help_treeview.tag_configure('Odd.Treeview', background="#ffffff")
        self.help_treeview.tag_configure('Even.Treeview', background="#eaeaea")
    # SELECCIONAR UN GRUPO Y AGREGARLO AL CAMPO DE GRUPO
    def SelectGroup(event):
        item_id = self.help_treeview.selection()
        info = self.help_treeview.item(item_id)
        grupo_id = info['text']
        self.GRUPO = LINE_MANAGER.GetGroup(linea_id,grupo_id)
        self.help_frame.destroy()
    # GROUP WINDOW - GROUP WINDOW - GROUP WINDOW - GROUP WINDOW - 
    self.help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
    self.help_frame.geometry('600x400')
    self.help_frame.title('Ayuda de Grupos')
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
                         text='Ayuda de Grupos',
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
    self.search_help_bar.bind("<Return>",lambda event: SearchGroup())
    self.search_help_bar.bind("<Control-BackSpace>", lambda event: ListGroups())
    # BOTONES TREEVIEW
    # BUSCAR
    search_btn = ctk.CTkButton(self.help_frame,
                               text='Buscar',
                               command= SearchGroup,
                               fg_color=APP_COLOR['main'],
                               hover_color=APP_COLOR['sec'])
    search_btn.grid(row=1,column=2,columnspan=2,sticky='w',padx=5,pady=5)  
    # CANCELAR
    cancel_btn = ctk.CTkButton(self.help_frame,
                               text='Cancelar',
                               command=ListGroups,
                               fg_color=APP_COLOR['red_m'],
                               hover_color=APP_COLOR['red_s'])
    cancel_btn.grid(row=1,column=7,columnspan=2,sticky='w',padx=5,pady=5)
    # TREEVIEW
    self.help_treeview = ttk.Treeview(self.help_frame,
                                 style='Custom.Treeview',
                                 columns=('Linea','Grupo'))
    self.help_treeview.grid(row=2,column=0,sticky='nswe',padx=10,pady=10,rowspan=8,columnspan=9)
    # EVENTO DE SELECCIONAR PRODUCTO
    self.help_treeview.bind("<<TreeviewSelect>>",SelectGroup)
    # CODIGO
    self.help_treeview.heading('#0',text='Código')
    self.help_treeview.column('#0',width=25,anchor='center')
    # LINEA
    self.help_treeview.heading('Linea',text='Línea')
    self.help_treeview.column('Linea',width=100,anchor='center')
    # GRUPO
    self.help_treeview.heading('Grupo',text='Grupo')
    self.help_treeview.column('Grupo',width=100,anchor='center')
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(self.help_frame,
                                 orientation='vertical',
                                 command=self.help_treeview.yview)
    scrollbar.grid(row=2,column=9,sticky='nws',pady=5,rowspan=8)
    self.help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR LOS PROVEEDORES
    ListGroups()
    self.help_frame.wait_window()
    return self.GRUPO