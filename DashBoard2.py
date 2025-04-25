import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from CargaProductos import*
from CargaLineasGrupos import*
from CargaProveedores import*
from Database import*
from InventarioMenu import*
import datetime
from threading import Timer
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class MainFrame(ctk.CTkFrame):
    def __init__(self,parent,lockscreen_callback):
        super().__init__(parent)
    # ASIGNAR EL CALLBACK PARA LA PANTALLA DE BLOQUEO
        self.lockscreen_callback = lockscreen_callback
    # MUESTRA EL INICIO
        self.current_frame = self.InicioFrame()
    # BARRA INFERIOR
        self.go_back_frame = ctk.CTkFrame(self)
        self.go_back_frame.pack(side='bottom',fill='x')
        button = ctk.CTkButton(self.go_back_frame,text='Ir atras',command=lambda:self.SwitchFrame(self.InicioFrame))
        button.pack(side='left')
        self.barra_inf_label = ctk.CTkLabel(self.go_back_frame,
                                            text='Programa de gestion')
        self.barra_inf_label.pack(side='left',padx=20)
    # RELOJ
        self.date_time = ctk.CTkLabel(self.go_back_frame,
                                      text='',
                                      font=FONTS[1],
                                      height=10,
                                      )
        self.date_time.pack(side='right',pady=5,padx=10)
        self.Date_Time()
    # COMANDO CERRAR SESION
        self.winfo_toplevel().bind("<Control-Q>", self.ctrl_q_callback)
        self.winfo_toplevel().bind("<Control-q>", self.ctrl_q_callback)
        self.winfo_toplevel().bind("<F4>", self.F4_Pressed)
    def ctrl_q_callback(self, event):
        # Verificamos que el dashboard esté activo consultando el atributo en la App
        if self.master.dashboard_activo:
            self.lockscreen_callback()
    def F4_Pressed(self,event):
        self.SwitchFrame(self.InicioFrame)




# FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - FRAMES - 
# INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - 
    def InicioFrame(self):
    # PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - PANEL LATERAL - 
    # CREA EL FRAME DONDE ESTARAN LOS BOTONES DEL DASHBOARD
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True,fill='both')

        self.buttons_frame = ctk.CTkFrame(self.main_frame,corner_radius=0,width=50,fg_color=APP_COLORS[2])
        self.buttons_frame.pack(side='left',fill='y')
    # BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - 
        inic_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inicio_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_inicio_dark.png"))
        inic_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Inicio',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=inic_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.InicioFrame))
        inic_btn.pack(fill='x',pady=5,side='top')
    # BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO - BOTON INVENTARIO
        inv_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inventario_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_inventario_dark.png"))
        invt_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Inventario',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=inv_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.InventarioFrame))
        invt_btn.pack(fill='x',pady=5,side='top') 
    # BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION - BOTON FACTURACION
        fact_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_fact_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_fact_dark.png"))
        fact_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Facturacion',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=fact_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.FacturacionFrame))
        fact_btn.pack(fill='x',pady=5,side='top')
    # BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - BOTON CUENTAS POR PAGAR - 
        cuentas_xp_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentas_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_cuentas_dark.png"))
        cuentas_xp_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por pagar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=cuentas_xp_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.CuentasXPFrame))
        cuentas_xp_btn.pack(fill='x',pady=5,side='top')
    # BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - BOTON CUENTAS POR COBRAR - 
        cuentas_xp_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Cuentas por cobrar',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.CuentasXCFrame))
        cuentas_xp_btn.pack(fill='x',pady=5,side='top')
    # BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD - BOTON PROGRAMAS DE UTILIDAD -  
        cuentas_xp_btn = ctk.CTkButton(self.buttons_frame,
                                     text='Programas de utilidad',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.ProgrmasUFrame))
        cuentas_xp_btn.pack(fill='x',pady=5,side='top')
    # BOTON DE BLOQUEAR O CERRAR SESION -  BOTON DE BLOQUEAR O CERRAR SESION - BOTON DE BLOQUEAR O CERRAR SESION 
        lock_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_lock_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_lock_dark.png"))
        lockscreen_btn=ctk.CTkButton(self.buttons_frame,
                                     text='',
                                     image=lock_btn_image,
                                     corner_radius=0,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=lambda: self.lockscreen_callback()
                                     )
        lockscreen_btn.pack(side='bottom',pady=5)
    # INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - 
        title_frame = ctk.CTkFrame(self.main_frame,corner_radius=0,bg_color=APP_COLORS[0])
        title_frame.pack(expand=True,fill='both')
        title=ctk.CTkLabel(title_frame,
                           text='PROGRAMA DE GESTION Y VENTAS',
                           bg_color='transparent',
                           font=FONTS[0])
        title.pack(fill='x')

        buss_name_frame = ctk.CTkFrame(self.main_frame,corner_radius=0,bg_color=APP_COLORS[0])
        buss_name_frame.pack(expand=True,fill='both')
        buss_name=ctk.CTkLabel(buss_name_frame,
                               text='NOMBRE DE LA EMPRESA',
                               bg_color='transparent',
                               font=FONTS[0])
        buss_name.pack(fill='x')
    # REGRESAR EL FRAME
        return self.main_frame
# INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - INVENTARIO - 
    def InventarioFrame(self):
        self.Inventario_Menu = InventarioMenu(self)
        self.Inventario_Menu.pack(expand=True,fill='both')
    # REGRESAR EL FRAME
        return self.Inventario_Menu
    

    # CREAR EL FRAME DE FACTURACION - CREAR EL FRAME DE FACTURACION - CREAR EL FRAME DE FACTURACION - CREAR EL FRAME DE FACTURACION
    def FacturacionFrame(self):
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')

        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Facturación',
                                bg_color=APP_COLORS[0],
                                font=FONTS[0])
        head_inv.place(x=50,y=40,anchor='nw')
        return self.head_frame

    # CUENTAS POR PAGAR - CUENTAS POR PAGAR - CUENTAS POR PAGAR - CUENTAS POR PAGAR - CUENTAS POR PAGAR - CUENTAS POR PAGAR - 
    def CuentasXPFrame(self):
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')

        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Cuentas por pagar',
                                bg_color=APP_COLORS[0],
                                font=FONTS[0])
        head_inv.place(x=50,y=40,anchor='nw')
        return self.head_frame
    # CUENTAS POR COBRAR - CUENTAS POR COBRAR - CUENTAS POR COBRAR - CUENTAS POR COBRAR - CUENTAS POR COBRAR - CUENTAS POR COBRAR - 
    def CuentasXCFrame(self):
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')

        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Cuentas por cobrar',
                                bg_color=APP_COLORS[0],
                                font=FONTS[0])
        head_inv.place(x=50,y=40,anchor='nw')
        return self.head_frame
    # PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD -  
    def ProgrmasUFrame(self):        
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')

        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Programas de Utilidad',
                                bg_color=APP_COLORS[0],
                                font=FONTS[0])
        head_inv.place(x=50,y=40,anchor='nw')
        return self.head_frame
    
    # CAMBIO DE FRAMES
    def SwitchFrame(self,frame):
        if self.current_frame is not None:
            self.current_frame.destroy()
        
        new_frame = frame
        self.current_frame = new_frame()


    def Date_Time(self):
        hora = datetime.datetime.now()
        self.date_time.configure(text=hora.strftime("%d-%m-%Y %H:%M:%S"))
        self.after(1000,self.Date_Time)