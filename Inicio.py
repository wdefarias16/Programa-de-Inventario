import customtkinter as ctk
import tkinter as tk
import datetime
from threading import Timer
from style import FONTS, APP_COLORS, APPEARANCE_MODE


class Inicio(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(bg_color=APP_COLORS[0])

        self.lightmode = True

        title_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=APP_COLORS[0])
        title_frame.pack(expand=True,fill='both')
        title=ctk.CTkLabel(title_frame,
                           text='PROGRAMA DE GESTION Y VENTAS',
                           bg_color='transparent',
                           font=FONTS[0])
        title.pack(fill='x')

        buss_name_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=APP_COLORS[0])
        buss_name_frame.pack(expand=True,fill='both')
        buss_name=ctk.CTkLabel(buss_name_frame,
                               text='NOMBRE DE LA EMPRESA',
                               bg_color='transparent',
                               font=FONTS[0])
        buss_name.pack(fill='x')

        # WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - 
        widget_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=APP_COLORS[0])
        widget_frame.pack(fill='x')

        # BOTON SALIR
        exit_btn = ctk.CTkButton(widget_frame,
                                 text='Salir',                                 
                                 fg_color=APP_COLORS[2],
                                 hover_color=APP_COLORS[3])
        exit_btn.pack(side='left',pady=5,padx=5)


        
        # RELOJ
        self.date_time = ctk.CTkLabel(widget_frame,
                                      text='',
                                      font=FONTS[1],
                                      height=10,
                                      )
        self.date_time.pack(side='right',pady=5,padx=10)
        self.Date_Time()

    def Date_Time(self):
        hora = datetime.datetime.now()
        self.date_time.configure(text=hora.strftime("%d-%m-%Y %H:%M:%S"))
        self.after(1000,self.Date_Time)