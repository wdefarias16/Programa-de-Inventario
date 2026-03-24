import customtkinter as ctk
import os
from PIL import Image
FONT = {
    'title_bold': ('Roboto Bold',25),
    'title_light': ('Roboto light',25),
    'subtitle_bold': ('Roboto Bold',20),
    'subtitle_light': ('Roboto light',20),
    'text': ('Roboto',15),
    'text_bold': ('Roboto Bold',15),
    'text_small': ('Roboto',12),
    'text_light': ('Roboto light',15),
    'text_light_small': ('Roboto light',12),
    'text_big': ('Roboto Bold',40),
    'text_big2': ('Roboto Bold',30),
}
APPEARANCE_MODE = 'light'
APP_COLOR = {
    'main':"#a2ff00",
    'main_s':"#87d400",
    'sec':"#0d5e1c",
    'sec_s':"#0a5418",
    'white_m':'#eaeaea',
    'black_m':'#1d1d1d',
    'white':'#ffffff',
    'black':'#000000',
    'gray':'#5d5d5d',
    'gray_s':"#3d3d3d",
    'light_gray':"#b9b9b9",
    'green_m':'#31C74A',
    'green_s':'#1A832B',
    'red_m':'#D8171D',
    'red_s':'#810005',
}
# ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - 
# ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - 
back_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_back_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_back_dark.png"))
cancel_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cerrar_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_cerrar_dark.png"))
search_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_search_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_search_dark.png"))
refresh_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_refresh_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_refresh_dark.png"))
trash_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_trash_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_trash_dark.png"))
lock_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_lock_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_lock_dark.png"))
exit_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_exit_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_exit_dark.png"))
eye_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_eye_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_eye_dark.png"))
inv_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inventario_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_inventario_dark.png"))
home_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inicio_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_inicio_dark.png"))
fact_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_fact_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_fact_dark.png"))
cuentas_xp_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentas_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_cuentas_dark.png"))
cuentas_xc_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentasPC_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_cuentasPC_dark.png"))
pdutilidad_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_PDUtilidad_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_PDUtilidad_dark.png"))
dolar_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_dolar_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_dolar_dark.png"))
pagomovil_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_pagom_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_pagom_dark.png"))
tarjetadd_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_tdd_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_tdd_dark.png"))
tarjetadc_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_tdc_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_tdc_dark.png"))
ICONS = {
    'cancel':cancel_icon,
    'search':search_icon,
    'refresh':refresh_icon,
    'trash':trash_icon,
    'lock':lock_icon,
    'exit':exit_icon,
    'eye':eye_icon,
    'inventory':inv_icon,
    'home':home_icon,
    'fact':fact_icon,
    'cxp':cuentas_xp_icon,
    'cxc':cuentas_xc_icon,
    'proutil':pdutilidad_icon,
    'dolar':dolar_icon,
    'pagomovil':pagomovil_icon,
    'tdd':tarjetadd_icon,
    'tdc':tarjetadc_icon,
    'back':back_icon,
}





class LogoLabel(ctk.CTkLabel):
    def __init__(self,parent,version,ancho_deseado=200,**kwargs):
        rutas_logos = {
            '1': os.path.join("Recursos", "Cliente", "logo_cliente.png"),
            '2': os.path.join("Recursos", "Cliente", "logo_cliente_v2.png"),
            '3': os.path.join("Recursos", "Cliente", "logo_cliente_v3.png"),
            '4': os.path.join("Recursos", "Cliente", "logo_cliente_v4.png"),
            '5': os.path.join("Recursos", "Cliente", "logo_cliente_v5.png")}
        
        versiones = [1,2,3,4,5]
        for v in versiones:
            if v == version:
                ruta_logo = rutas_logos[str(v)]
            else:
                ruta_logo = os.path.join("Recursos", "Cliente", "logo_cliente.png")
        try:
            img_original = Image.open(ruta_logo)
            ratio = img_original.height / img_original.width
            alto_proporcional = int(ancho_deseado * ratio)

            self.logo_image = ctk.CTkImage(
                light_image=img_original,
                dark_image=img_original,
                size=(ancho_deseado,alto_proporcional)
            )

            super().__init__(parent, image=self.logo_image, text="", **kwargs)

        except Exception as e:
            print(f"Error cargando el logo: {e}")
            super().__init__(parent, text="LOGO NO ENCONTRADO", **kwargs)
