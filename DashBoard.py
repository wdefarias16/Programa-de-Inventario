import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from CargaProductos_prog import*
from CargaLineasGrupos_prog import*
from CargaProveedores_prog import*
from DatabaseManager import*
from Menu_Inventario import*
from Menu_CuentasPorPagar import*
import datetime
from threading import Timer
from style import FONT, APP_COLORS, ICONS

class DashBoardMenu(ctk.CTkFrame):
    def __init__(self,parent,
                 lockscreen_callback,
                 exit_callback,
                 Inventario_CB,
                 CuentasPorPagar_CB,
                 ProgramasDeUtilidad_CB):
        super().__init__(parent)
    # ASIGNAR EL CALLBACK PARA LA PANTALLA DE BLOQUEO
        self.lockscreen_callback = lockscreen_callback
        self.exit = exit_callback
        self.Inventario_CB = Inventario_CB
        self.CuentasPorPagar_CB = CuentasPorPagar_CB
        self.ProgramasDeUtilidad_CB = ProgramasDeUtilidad_CB
        self.ResizeImage()
    # MAIN FRAME GRID SETUP
        for rows in range(21):
            self.rowconfigure(rows, weight=1, uniform='row')
        for columns in range(21):
            self.columnconfigure(columns, weight=1, uniform='column')
    # BARRA INFERIOR
        self.inf_bar_frame = ctk.CTkFrame(self,
                                          corner_radius=0,
                                          fg_color=APP_COLORS[3])
        self.inf_bar_frame.grid(row=20,column=0,columnspan=21,sticky='nsew')
        
        self.barra_inf_label = ctk.CTkLabel(self.inf_bar_frame,
                                            fg_color=APP_COLORS[3],
                                            text_color=APP_COLORS[0],
                                            text='Programa de gestion')
        self.barra_inf_label.pack(side='left',padx=20)
    # RELOJ
        self.date_time = ctk.CTkLabel(self.inf_bar_frame,
                                      text='',
                                      text_color=APP_COLORS[0],
                                      font=FONT['text_light'],
                                      height=10,
                                      )
        self.date_time.pack(side='right',pady=5,padx=10)
        self.Date_Time()
# FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - 
# INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - 
    # PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - 
    # CREA EL FRAME DONDE ESTARAN LOS BOTONES DEL DASHBOARD
        self.buttons_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[2])
        self.buttons_frame.grid(row=0,rowspan=20,column=0,columnspan=2,sticky='nsew')
        for rows in range(12):
            self.buttons_frame.rowconfigure(rows,weight=1,uniform='row')
        for columns in range(2):
            self.buttons_frame.columnconfigure(columns,weight=1,uniform='column')
        # BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO
        invt_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Inventario',
                                     font=FONT['text'],
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=ICONS['inventory'],
                                     corner_radius=10,
                                     compound='left',
                                     anchor='w',
                                     command=self.Inventario_CB)
        invt_btn.grid(row=0,column=0,columnspan=2,sticky='nswe',padx=15)
        # BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION
        fact_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Facturacion',
                                     font=FONT['text'],
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=ICONS['fact'],
                                     corner_radius=10,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: 0+0)
        fact_btn.grid(row=1,column=0,columnspan=2,sticky='nswe',padx=15)
        # BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - 
        cuentas_xp_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por pagar',
                                     font=FONT['text'],
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=ICONS['cxp'],
                                     corner_radius=10,
                                     compound='left',
                                     anchor='w',
                                     command=self.CuentasPorPagar_CB)
        cuentas_xp_btn.grid(row=2,column=0,columnspan=2,sticky='nswe',padx=15)
        # BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - 
        cuentas_xc_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por cobrar',
                                     font=FONT['text'],
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=ICONS['cxc'],
                                     corner_radius=10,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.CuentasXCFrame))
        cuentas_xc_btn.grid(row=3,column=0,columnspan=2,sticky='nswe',padx=15)
        # BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD -  
        pdutilidad_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Programas de utilidad',
                                     font=FONT['text'],
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=ICONS['proutil'],
                                     corner_radius=10,
                                     compound='left',
                                     anchor='w',
                                     command= self.ProgramasDeUtilidad_CB)
        pdutilidad_btn.grid(row=4,column=0,columnspan=2,sticky='nswe',padx=15)
        # BOTON DE BLOQUEAR O CERRAR SESION -  BOTON DE BLOQUEAR O CERRAR SESION - BOTON DE BLOQUEAR O CERRAR SESION
        lockscreen_btn=ctk.CTkButton(self.buttons_frame,
                                     text='',
                                     image=ICONS['lock'],
                                     corner_radius=10,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=lambda: self.lockscreen_callback()
                                     )
        lockscreen_btn.grid(row=11,column=0,columnspan=1,sticky='nswe',pady=10,padx=5)
        # BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - 
        exit_btn=ctk.CTkButton(self.buttons_frame,
                                     text='',
                                     image=ICONS['exit'],
                                     corner_radius=10,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=self.exit
                                     )
        exit_btn.grid(row=11,column=1,columnspan=1,sticky='nswe',pady=10,padx=5)
    # INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - 
        title_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        title_frame.grid(row=0,rowspan=20,column=2,columnspan=19,sticky='nsew')
        for rows in range(20):
            title_frame.rowconfigure(rows, weight=1, uniform='row')
        for columns in range(20):
            title_frame.columnconfigure(columns, weight=1, uniform='column')

        imagen_logo = Image.open(r"Recursos\Cliente\logo_cliente_resized.png")
        imagen_logo_ctk = ctk.CTkImage(imagen_logo,size=(200,32))

        head = ctk.CTkLabel(title_frame, image=imagen_logo_ctk, text="",fg_color=APP_COLORS[0])
        head.grid(row=8,column=0,rowspan=2,columnspan=20,sticky='nsew')

        
# FUNCION DAR FECHA Y HORA
    def Date_Time(self):
        hora = datetime.datetime.now()
        self.date_time.configure(text=hora.strftime("%d-%m-%Y  |  %H:%M:%S"))
        self.after(1000,self.Date_Time)

    def ResizeImage(self):
        imagen = Image.open(r"Recursos\Cliente\logo_cliente.png")
        width = 200
        ratio = imagen.height / imagen.width
        height = int(width * ratio)
        resized = imagen.resize((width,height))
        resized.save(r"Recursos\Cliente\logo_cliente_resized.png")