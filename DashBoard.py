import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from CargaProductos import*
from CargaLineasGrupos import*
from CargaProveedores import*
from Database import*
from Inicio import*
import datetime
from threading import Timer
from style import FONTS, APP_COLORS, APPEARANCE_MODE

class MainFrame(ctk.CTkFrame):
    def __init__(self,parent,lockscreen_callback):
        super().__init__(parent)
        
        # ASIGNAR EL CALLBACK PARA LA PANTALLA DE BLOQUEO
        self.lockscreen_callback = lockscreen_callback
        # CREA EL MENU DE BOTONES Y MUESTRA DE PRIMERA INSTANCIA EL MENU DE INVENTARIO
        self.ButtonsFrame()
        self.current_frame = self.InicioFrame()

    # MENU DE BOTONES       
    def ButtonsFrame(self):
        
        # CREA EL FRAME DONDE ESTARAN LOS BOTONES DEL DASHBOARD
        buttons_frame = ctk.CTkFrame(self,corner_radius=0,width=50,fg_color=APP_COLORS[2])
        buttons_frame.pack(side='left',fill='y')
        
        # BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - BOTON INICIO - 
        inic_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inicio_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_inicio_dark.png"))
        inic_btn = ctk.CTkButton(buttons_frame,
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
        invt_btn = ctk.CTkButton(buttons_frame,
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
        fact_btn = ctk.CTkButton(buttons_frame,
                                     text='Facturacion',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=fact_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.FacturacionFrame))
        fact_btn.pack(fill='x',pady=5,side='top')

        # BOTON CUENTAS - BOTON CUENTAS - BOTON CUENTAS - BOTON CUENTAS - BOTON CUENTAS - BOTON CUENTAS - BOTON CUENTAS
        cuentas_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentas_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_cuentas_dark.png"))
        cuentas_btn = ctk.CTkButton(buttons_frame,
                                     text='Cuentas',
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     image=cuentas_btn_image,
                                     corner_radius=0,
                                     compound='left',
                                     anchor='w',
                                     command=lambda: self.SwitchFrame(self.CuentasFrame))
        cuentas_btn.pack(fill='x',pady=5,side='top')

        # BOTON DE BLOQUEAR O CERRAR SESION -  BOTON DE BLOQUEAR O CERRAR SESION - BOTON DE BLOQUEAR O CERRAR SESION 
        lock_btn_image=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_lock_light.png"), size=(30,30),
                                   dark_image=Image.open(r"Recursos\Iconos\btn_lock_dark.png"))
        lockscreen_btn=ctk.CTkButton(buttons_frame,
                                     text='',
                                     image=lock_btn_image,
                                     corner_radius=0,
                                     fg_color=APP_COLORS[2],
                                     hover_color=APP_COLORS[3],
                                     command=lambda: self.lockscreen_callback()
                                     )
        lockscreen_btn.pack(side='bottom',pady=5)

    # INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - INICIO - 
    def InicioFrame(self):
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')


        inicio_frame = Inicio(self.head_frame)
        inicio_frame.pack(expand=True, fill='both')

        return self.head_frame

    # CREAR EL FRAME DE INVENTARIO - CREAR EL FRAME DE INVENTARIO - CREAR EL FRAME DE INVENTARIO - CREAR EL FRAME DE INVENTARIO
    def InventarioFrame(self):

        self.head_frame = ctk.CTkFrame(self,
                                       height=600,
                                       corner_radius=0,
                                       fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')


        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Inventario',
                                bg_color=APP_COLORS[0],
                                text_color=APP_COLORS[1],
                                font=FONTS[0],
                                height=10)
        head_inv.pack(pady=30,padx=40,fill='both',expand=True)

        # PESTANAS - PESTANAS - PESTANAS - PESTANAS - PESTANAS - PESTANAS - PESTANAS - PESTANAS - PESTANAS - 
        tabs = ctk.CTkTabview(self.head_frame,height=800,
                              fg_color=APP_COLORS[0],
                              segmented_button_fg_color=APP_COLORS[0],
                              segmented_button_selected_color=APP_COLORS[2],
                              segmented_button_selected_hover_color=APP_COLORS[3],
                              segmented_button_unselected_color=APP_COLORS[3],
                              segmented_button_unselected_hover_color=APP_COLORS[2],
                              text_color=APP_COLORS[0])
        tabs.pack(expand=True,fill='both')
        tabs.add("Listado de productos")
        tabs.add("Carga de productos")
        tabs.add("Carga de líneas y grupos")
        tabs.add("Carga de proveedores")


        # TAB CARGA DE PRODUCTOS
        carga_productos = CargaProductosProg(tabs.tab("Carga de productos"))
        carga_productos.pack(expand=True,fill='both')

        # TAB CARGA DE LINEAS Y GRUPOS
        carga_lin_gru = LineasGruposProg(tabs.tab("Carga de líneas y grupos"),line_manager=LINE_MANAGER)
        carga_lin_gru.pack(expand=True,fill='both')

        carga_proveedores = ProveedoresProg(tabs.tab("Carga de proveedores"),prov_manager=PROV_MANAGER)
        carga_proveedores.pack(expand=True,fill='both')

        return self.head_frame
    

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

    # CREAR EL FRAME DE CUENTAS - CREAR EL FRAME DE CUENTAS - CREAR EL FRAME DE CUENTAS - CREAR EL FRAME DE CUENTAS
    def CuentasFrame(self):
        self.head_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.head_frame.pack(expand=True,fill='both')

        head_inv = ctk.CTkLabel(self.head_frame,
                                text='Cuentas',
                                bg_color=APP_COLORS[0],
                                font=FONTS[0])
        head_inv.place(x=50,y=40,anchor='nw')
        return self.head_frame
    


    # CAMBIO DE FRAMES
    def SwitchFrame(self,new_frame):
        self.current_frame.destroy()
        self.current_frame = new_frame()