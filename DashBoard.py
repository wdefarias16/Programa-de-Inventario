import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from prog_CargaProductos import*
from prog_CargaLineasGrupos import*
from prog_CargaProveedores import*
from DatabaseManager import*
from Menu_Inventario import*
from Menu_CuentasPorPagar import*
import datetime
from style import *
from DatabaseManager import GetCurrentUser

class DashBoardMenu(ctk.CTkFrame):
    def __init__(self,parent,
                 lockscreen_callback,
                 exit_callback,
                 Inventario_CB,
                 Facturacion_CB,
                 CuentasPorPagar_CB,
                 ProgramasDeUtilidad_CB):
        super().__init__(parent)
    # ASIGNAR EL CALLBACK PARA LA PANTALLA DE BLOQUEO
        self.lockscreen_callback = lockscreen_callback
        self.exit = exit_callback
        self.Inventario_CB = Inventario_CB
        self.Facturacion_CB = Facturacion_CB
        self.CuentasPorPagar_CB = CuentasPorPagar_CB
        self.ProgramasDeUtilidad_CB = ProgramasDeUtilidad_CB
    
# BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR
# BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR
        self.inf_bar_frame = ctk.CTkFrame(self,
                                          corner_radius=0,
                                          fg_color=APP_COLOR['main'])
        self.inf_bar_frame.place(relx=0.5,rely=0.95,relwidth=1,relheight=0.05,anchor='n')
        user = GetCurrentUser()
        self.barra_inf_label = ctk.CTkLabel(self.inf_bar_frame,
                                            text=f'Winventory v1.0 Beta | {user}',
                                            font=FONT['text'],
                                            fg_color=APP_COLOR['main'],
                                            text_color=APP_COLOR['sec'])
        self.barra_inf_label.pack(side='left',padx=20)
    # RELOJ
        self.date_time = ctk.CTkLabel(self.inf_bar_frame,
                                      text='',
                                      text_color=APP_COLOR['sec'],
                                      font=FONT['text'],
                                      height=10,
                                      )
        self.date_time.pack(side='right',pady=5,padx=10)
        self.Date_Time()
    # -----------------------------------------------------------------------
    # PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL L
    # -----------------------------------------------------------------------
        # FRAME
        self.buttons_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLOR['sec'])
        self.buttons_frame.place(relx=0,rely=0,relwidth=0.20,relheight=0.95,anchor='nw')

        self.logo = LogoLabel(self.buttons_frame, version=1, ancho_deseado=120, fg_color=APP_COLOR['sec'])
        self.logo.place(relx=0.5,rely=0.05,relwidth=0.8,anchor='n')

        # -------------------------------------------------------------------
        # BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVE
        # -------------------------------------------------------------------
        invt_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Inventario',
                                     text_color=APP_COLOR['white_m'],
                                     font=FONT['text'],
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec_s'],
                                     image=ICONS['inventory'],
                                     corner_radius=5,
                                     compound='left',
                                     anchor='w',
                                     command=self.Inventario_CB)
        invt_btn.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.08,anchor='n')
        # -------------------------------------------------------------------
        # BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON F
        # -------------------------------------------------------------------
        fact_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Facturación',
                                     text_color=APP_COLOR['white_m'],
                                     font=FONT['text'],
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec_s'],
                                     image=ICONS['fact'],
                                     corner_radius=5,
                                     compound='left',
                                     anchor='w',
                                     command=self.Facturacion_CB)
        fact_btn.place(relx=0.5,rely=0.33,relwidth=0.9,relheight=0.08,anchor='n')
        # -------------------------------------------------------------------
        # BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS P
        # -------------------------------------------------------------------
        cuentas_xp_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por pagar',
                                     text_color=APP_COLOR['white_m'],
                                     font=FONT['text'],
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec_s'],
                                     image=ICONS['cxp'],
                                     corner_radius=5,
                                     compound='left',
                                     anchor='w',
                                     command=self.CuentasPorPagar_CB)
        cuentas_xp_btn.place(relx=0.5,rely=0.41,relwidth=0.9,relheight=0.08,anchor='n')
        # -------------------------------------------------------------------
        # BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - BOTON CUENTAS
        # -------------------------------------------------------------------
        cuentas_xc_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por cobrar',
                                     text_color=APP_COLOR['white_m'],
                                     font=FONT['text'],
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec_s'],
                                     image=ICONS['cxc'],
                                     corner_radius=5,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.CuentasXCFrame))
        cuentas_xc_btn.place(relx=0.5,rely=0.49,relwidth=0.9,relheight=0.08,anchor='n')
        # -------------------------------------------------------------------
        # BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD - BOTON P
        # -------------------------------------------------------------------
        pdutilidad_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Prgs. de utilidad',
                                     text_color=APP_COLOR['white_m'],
                                     font=FONT['text'],
                                     fg_color=APP_COLOR['sec'],
                                     hover_color=APP_COLOR['sec_s'],
                                     image=ICONS['proutil'],
                                     corner_radius=5,
                                     compound='left',
                                     anchor='w',
                                     command= self.ProgramasDeUtilidad_CB)
        pdutilidad_btn.place(relx=0.5,rely=0.57,relwidth=0.9,relheight=0.08,anchor='n')
        # BOTON DE BLOQUEAR O CERRAR SESION -  BOTON DE BLOQUEAR O CERRAR SESION - BOTON DE BLOQUEAR O CERRAR SESION
        #lockscreen_btn=ctk.CTkButton(self.buttons_frame,
        #                             text='',
        #                             image=ICONS['lock'],
        #                             corner_radius=10,
        #                             fg_color=APP_COLOR['main'],
        #                             hover_color=APP_COLOR['sec'],
        #                             command=lambda: self.lockscreen_callback()
        #                             )
        #lockscreen_btn.grid(row=11,column=0,columnspan=1,sticky='nswe',pady=10,padx=5)
        ## BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - BOTON SALIR - 
        #exit_btn=ctk.CTkButton(self.buttons_frame,
        #                             text='',
        #                             image=ICONS['exit'],
        #                             corner_radius=10,
        #                             fg_color=APP_COLOR['main'],
        #                             hover_color=APP_COLOR['sec'],
        #                             command=self.exit
        #                             )
        #exit_btn.grid(row=11,column=1,columnspan=1,sticky='nswe',pady=10,padx=5)


        
# FUNCION DAR FECHA Y HORA
    def Date_Time(self):
        hora = datetime.datetime.now()
        self.date_time.configure(text=hora.strftime("%d-%m-%Y  |  %H:%M:%S"))
        self.after(1000,self.Date_Time)