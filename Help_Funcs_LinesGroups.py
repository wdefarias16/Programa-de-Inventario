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
        for i,line in enumerate(outcome):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
            self.line_help_treeview.insert("", 'end',
                                 text=line['codigo'],
                                 values=(line['linea']),
                                 tags=(tag,))
        # Configurar colores para los tags
        self.line_help_treeview.tag_configure('Odd.Treeview', background=APP_COLOR['white'])
        self.line_help_treeview.tag_configure('Even.Treeview', background=APP_COLOR['light_gray'])
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
        self.line_help_treeview.tag_configure('Odd.Treeview', background=APP_COLOR['white'])
        self.line_help_treeview.tag_configure('Even.Treeview', background=APP_COLOR['light_gray'])
    # SELECCIONAR UNA LINEA Y AGREGARLA AL CAMPO DE LINEA
    def SelectLine(event):
        item_id = self.line_help_treeview.selection()
        info = self.line_help_treeview.item(item_id)
        self.LINE = {
            'codigo':info['text'],
            'nombre':info['values'][0]
        }
        self.line_help_frame.destroy()
    # ------------------------------------------------------------------------
    self.line_help_frame = ctk.CTkToplevel(self,fg_color=APP_COLOR['white_m'])
    self.line_help_frame.geometry('800x500')
    self.line_help_frame.title('Ayuda de lineas')
    self.line_help_frame.transient(self)
    self.line_help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
    # ---------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE
    # ---------------------------------------------------------------------
    # FRAME
    title_frame = ctk.CTkFrame(self.line_help_frame,
                    fg_color=APP_COLOR['sec'],
                    corner_radius=0,)
    title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
    title_label = ctk.CTkLabel(title_frame,
                    text='Ayuda de líneas',
                    text_color=APP_COLOR['white_m'],
                    font=FONT['title_bold'])
    title_label.place(relx=0.5,rely=0.5,anchor='center')
    exit_btn = ctk.CTkButton(title_frame,
                    text='',
                    image=ICONS['cancel'],
                    width=30,
                    height=30,
                    text_color=APP_COLOR['black_m'],
                    font=FONT['text_small'],
                    fg_color=APP_COLOR['red_m'],
                    hover_color=APP_COLOR['red_s'],
                    command=lambda: self.line_help_frame.destroy())
    exit_btn.place(relx=0.95,rely=0.5,anchor='center')
    # ---------------------------------------------------------------------
    # TREEVIEW FRAME - TREEVIEW FRAME - TREEVIEW FRAME - TREEVIEW FRAME - T
    # ---------------------------------------------------------------------
    search_label = ctk.CTkLabel(self.line_help_frame,
                text='Busqueda por nombre',
                text_color=APP_COLOR['gray'],
                font=FONT['text'])
    search_label.place(relx=0.075,rely=0.15,anchor='w')
    # BARRA DE BUSQUEDA ENTRY
    self.search_line_bar_var = ctk.StringVar()
    self.search_line_bar = ctk.CTkEntry(self.line_help_frame,
                fg_color=APP_COLOR['light_gray'],
                border_color=APP_COLOR['light_gray'],
                textvariable=self.search_line_bar_var)
    self.search_line_bar.place(relx=0.075,rely=0.22,relwidth=0.2,anchor='w')
    self.search_line_bar.bind("<Return>",lambda event: SearchLine())
    # BOTONES - 
    search_btn = ctk.CTkButton(self.line_help_frame,
                text='',
                width=40,
                height=35,
                image=ICONS['search'],
                command=SearchLine,
                fg_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['black'])
    search_btn.place(relx=0.3,rely=0.22,anchor='w')
    refresh_btn = ctk.CTkButton(self.line_help_frame,
                text='',
                width=40,
                height=35,
                image=ICONS['refresh'],
                command=ListLines,
                fg_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['black'])
    refresh_btn.place(relx=0.36,rely=0.22,anchor='w')

    # CONFIGURACION VISUAL DEL TV
    style = ttk.Style()
    style.theme_use("alt")
    style.configure(
        'Custom.Treeview',
        background = APP_COLOR['white_m'],
        foreground = APP_COLOR['black_m'],
        rowheight = 45,
        font = FONT['text'],
        fieldbackground = APP_COLOR['white'],)
    style.configure(
        'Custom.Treeview.Heading',
        background = APP_COLOR['sec'],
        foreground = APP_COLOR['white_m'],
        font = FONT['subtitle_bold'])
    # TREEVIEW
    self.line_help_treeview = ttk.Treeview(self.line_help_frame,
                                 style='Custom.Treeview',
                                 columns=('Linea'))
    self.line_help_treeview.place(relx=0.5,rely=0.3,relwidth=0.85,relheight=0.60,anchor='n')
    # EVENTO DE SELECCIONAR PRODUCTO
    self.line_help_treeview.bind("<<TreeviewSelect>>",SelectLine)
    # CODIGO
    self.line_help_treeview.heading('#0',text='Código')
    self.line_help_treeview.column('#0',width=25,anchor='center')
    # LINEA
    self.line_help_treeview.heading('Linea',text='Línea')
    self.line_help_treeview.column('Linea',width=100,anchor='center')
    # SCROLLBAR DEL TV
    scrollbar = ctk.CTkScrollbar(self.line_help_frame,
                                 orientation='vertical',
                                 command=self.line_help_treeview.yview)
    scrollbar.place(relx=0.95,rely=0.3,relheight=0.60,anchor='n')
    self.line_help_treeview.configure(yscrollcommand=scrollbar.set)
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
        search = self.search_bar_var.get().lower()
        outcome = LINE_MANAGER.SearchGroupByName(search,line=linea_id)
        for i,group in enumerate(outcome):
            tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"
            self.help_treeview.insert("", 'end',
                                 text=group['codigo'],
                                 values=(group['linea'],
                                         group['grupo']),
                                 tags=(tag,),)  # Asignar el tag a la fila
        self.help_treeview.tag_configure('Odd.Treeview', background=APP_COLOR['white'])
        self.help_treeview.tag_configure('Even.Treeview', background=APP_COLOR['light_gray'])
    # LISTAR PROVEEDORES
    def ListGroups():
        self.search_bar.focus()
        self.search_bar_var.set('')
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
    self.help_frame.geometry('800x500')
    self.help_frame.title('Ayuda de Grupos')
    self.help_frame.transient(self)
    self.help_frame.protocol("WM_DELETE_WINDOW", lambda: None)
    # ---------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE
    # ---------------------------------------------------------------------
    # FRAME
    title_frame = ctk.CTkFrame(self.help_frame,
                    fg_color=APP_COLOR['sec'],
                    corner_radius=0,)
    title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
    title_label = ctk.CTkLabel(title_frame,
                    text='Ayuda de grupos',
                    text_color=APP_COLOR['white_m'],
                    font=FONT['title_bold'])
    title_label.place(relx=0.5,rely=0.5,anchor='center')
    exit_btn = ctk.CTkButton(title_frame,
                    text='',
                    image=ICONS['cancel'],
                    width=30,
                    height=30,
                    text_color=APP_COLOR['black_m'],
                    font=FONT['text_small'],
                    fg_color=APP_COLOR['red_m'],
                    hover_color=APP_COLOR['red_s'],
                    command=lambda: self.help_frame.destroy())
    exit_btn.place(relx=0.95,rely=0.5,anchor='center')
    
    search_label = ctk.CTkLabel(self.help_frame,
                text='Busqueda por nombre',
                text_color=APP_COLOR['gray'],
                font=FONT['text'])
    search_label.place(relx=0.075,rely=0.15,anchor='w')
    # BARRA DE BUSQUEDA ENTRY
    self.search_bar_var = ctk.StringVar()
    self.search_bar = ctk.CTkEntry(self.help_frame,
                fg_color=APP_COLOR['light_gray'],
                border_color=APP_COLOR['light_gray'],
                textvariable=self.search_bar_var)
    self.search_bar.place(relx=0.075,rely=0.22,relwidth=0.2,anchor='w')
    self.search_bar.bind("<Return>",lambda event: SearchGroup())
    # BOTONES - 
    search_btn = ctk.CTkButton(self.help_frame,
                text='',
                width=40,
                height=35,
                image=ICONS['search'],
                command=SearchGroup,
                fg_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['black'])
    search_btn.place(relx=0.3,rely=0.22,anchor='w')
    refresh_btn = ctk.CTkButton(self.help_frame,
                text='',
                width=40,
                height=35,
                image=ICONS['refresh'],
                command=ListGroups,
                fg_color=APP_COLOR['black_m'],
                hover_color=APP_COLOR['black'])
    refresh_btn.place(relx=0.36,rely=0.22,anchor='w')

    # CONFIGURACION VISUAL DEL TV
    style = ttk.Style()
    style.theme_use("alt")
    style.configure(
        'Custom.Treeview',
        background = APP_COLOR['white_m'],
        foreground = APP_COLOR['black_m'],
        rowheight = 45,
        font = FONT['text'],
        fieldbackground = APP_COLOR['white'],)
    style.configure(
        'Custom.Treeview.Heading',
        background = APP_COLOR['sec'],
        foreground = APP_COLOR['white_m'],
        font = FONT['subtitle_bold'])
    # TREEVIEW
    self.help_treeview = ttk.Treeview(self.help_frame,
                                 style='Custom.Treeview',
                                 columns=('Linea','Grupo'))
    self.help_treeview.place(relx=0.5,rely=0.3,relwidth=0.85,relheight=0.60,anchor='n')
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
    scrollbar.place(relx=0.95,rely=0.3,relheight=0.60,anchor='n')
    self.help_treeview.configure(yscrollcommand=scrollbar.set)
    # LISTAR LOS PROVEEDORES
    ListGroups()
    self.help_frame.wait_window()
    return self.GRUPO