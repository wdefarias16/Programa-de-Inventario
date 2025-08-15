import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import INVENTARIO,VALOR_DOLAR
import datetime

class CargaDolar(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB

        # OBTENER VALOR DOLAR
        self.VALOR_DOLAR = VALOR_DOLAR
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
                                   text='Carga diaria del dólar',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LOG
        self.log_label = ctk.CTkLabel(self,
                                    text='Nota',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['text'],
                                    height=30,
                                    corner_radius=10,
                                    fg_color=APP_COLOR['gray'])
        self.log_label.place(relx=0.5,rely=0.85,relwidth=0.70,anchor='n')
        # FECHA
        self.fecha_label = ctk.CTkLabel(self,
                                    text='',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45,
                                    corner_radius=2,
                                    fg_color=APP_COLOR['main'])
        self.fecha_label.place(relx=0.10,rely=0.15,anchor='n')
        # FECHA LABEL
        fecha_text_label = ctk.CTkLabel(self,
                                    text='Fecha',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=60,
                                    height=25)
        fecha_text_label.place(relx=0.10,rely=0.11,anchor='n')
        # HORA
        self.hora_label = ctk.CTkLabel(self,
                                    text='',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45,
                                    corner_radius=2,
                                    fg_color=APP_COLOR['main'])
        self.hora_label.place(relx=0.90,rely=0.15,anchor='n')
        # HORA LABEL
        hora_text_label = ctk.CTkLabel(self,
                                    text='Hora',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=60,
                                    height=25)
        hora_text_label.place(relx=0.90,rely=0.11,anchor='n')
        # DOLAR
        self.dolar_label = ctk.CTkLabel(self,
                                    text=f'Bs. {self.VALOR_DOLAR}',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45)
        self.dolar_label.place(relx=0.50,rely=0.15,anchor='n')
        # VALOR ACTUAL
        valor_actual_label = ctk.CTkLabel(self,
                                    text='Valor actual',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=120,
                                    height=45)
        valor_actual_label.place(relx=0.50,rely=0.20,anchor='n')
        # ACTUALIZAR FECHA Y HORA ACTUALES
        self.GetDate()
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        self.update_dolar_btn = ctk.CTkButton(self,
                                    text='Actualizar',
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['main'],
                                    hover_color=APP_COLOR['sec'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.update_dolar_btn.place(relx=0.50,rely=0.30,anchor='n')
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
                                    columns=('Fecha','Hora','Valor'))
        self.treeview_main.place(relx=0.5,y=480,relwidth=0.70,height=320,anchor='n')
        # CODIGO
        self.treeview_main.heading('#0',text='Cod.')
        self.treeview_main.column('#0', width=50, anchor='center', stretch=True)
        # DESCRIPCION
        self.treeview_main.heading('Fecha',text='Fecha')
        self.treeview_main.column('Fecha', width=100, anchor='w', minwidth=100, stretch=True)
        # CANTIDAD
        self.treeview_main.heading('Hora',text='Hora')
        self.treeview_main.column('Hora', width=100, anchor='center', stretch=True)
        # BOLIVARES
        self.treeview_main.heading('Valor',text='Valor.')
        self.treeview_main.column('Valor', width=100, anchor='center', stretch=True)
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------


    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    def GetDate(self):
        hora = datetime.datetime.now()
        self.fecha_label.configure(text=hora.strftime("%d/%m/%Y"))
        self.hora_label.configure(text=hora.strftime("%H:%M:%S"))
        self.after(1000,self.GetDate)
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------