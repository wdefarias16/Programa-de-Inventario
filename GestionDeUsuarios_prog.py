import customtkinter as ctk
from tkinter import ttk
from style import FONT,APP_COLOR

class GestionUsuariosProg(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color = APP_COLOR['white_m'])
        self.GoBack_CB = GoBack_CB
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
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
                                   text='Gestión de usuarios',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
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
        self.treeview_main = ttk.Treeview(self,
                                    style='Custom.Treeview',
                                    columns=('Hora','Valor'))
        self.treeview_main.place(relx=0.5,y=300,relwidth=0.70,height=320,anchor='n')
        # DESCRIPCION
        self.treeview_main.heading('#0',text='Fecha')
        self.treeview_main.column('#0', width=100, anchor='w', minwidth=100, stretch=True)
        # CANTIDAD
        self.treeview_main.heading('Hora',text='Hora')
        self.treeview_main.column('Hora', width=100, anchor='center', stretch=True)
        # BOLIVARES
        self.treeview_main.heading('Valor',text='Valor.')
        self.treeview_main.column('Valor', width=100, anchor='w', stretch=True)
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------