import customtkinter as ctk
import tkinter as tk
import datetime
from threading import Timer

fonts = [('Roboto light',25),('Roboto light',15)]
app_colors = ['#eaeaea','#1d1d1d','#1c9bac','#166c78','#5d5d5d']



class Inicio(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(bg_color=app_colors[0])

        self.lightmode = True

        title_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=app_colors[0])
        title_frame.pack(expand=True,fill='both')
        title=ctk.CTkLabel(title_frame,
                           text='PROGRAMA DE GESTION Y VENTAS',
                           bg_color='transparent',
                           font=fonts[0])
        title.pack(fill='x')

        buss_name_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=app_colors[0])
        buss_name_frame.pack(expand=True,fill='both')
        buss_name=ctk.CTkLabel(buss_name_frame,
                               text='NOMBRE DE LA EMPRESA',
                               bg_color='transparent',
                               font=fonts[0])
        buss_name.pack(fill='x')

        # WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - WIDGETS - 
        widget_frame = ctk.CTkFrame(self,corner_radius=0,bg_color=app_colors[0])
        widget_frame.pack(fill='x')

        # BOTON SALIR
        exit_btn = ctk.CTkButton(widget_frame,
                                 text='Salir',                                 
                                 fg_color=app_colors[2],
                                 hover_color=app_colors[3])
        exit_btn.pack(side='left',pady=5,padx=5)

        # SWITCH LIGHT MODE

        switch_var = ctk.StringVar(value='on')
        switch = ctk.CTkSwitch(widget_frame,
                               text='',
                               command=self.SwitchLight,
                               variable=switch_var,
                               onvalue='on',
                               offvalue='off')
        switch.pack(side='left',pady=5,padx=5)
        
        # RELOJ
        self.date_time = ctk.CTkLabel(widget_frame,
                                      text='',
                                      font=fonts[1],
                                      height=10,
                                      )
        self.date_time.pack(side='right',pady=5,padx=10)

        
        self.Date_Time()

    def SwitchLight(self):
        if self.lightmode == True:
            ctk.set_appearance_mode('dark')
            self.lightmode = False
        else:
            ctk.set_appearance_mode('light')
            self.lightmode = True

    def Date_Time(self):
        
        hora = datetime.datetime.now()
        self.date_time.configure(text=hora.strftime("%d-%m-%Y %H:%M:%S"))
        self.after(1000,self.Date_Time)



