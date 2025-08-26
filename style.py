import customtkinter as ctk
from PIL import Image

FONT = {
    'title_bold': ('Roboto Bold',25),
    'title_light': ('Roboto light',25),
    'subtitle_bold': ('Roboto Bold',20),
    'subtitle_light': ('Roboto light',20),
    'text': ('Roboto',15),
    'text_small': ('Roboto',12),
    'text_light': ('Roboto light',15),
    'text_light_small': ('Roboto light',12),
}

APPEARANCE_MODE = 'light'

APP_COLOR = {
    'main':'#1c9bac',
    'sec':'#166c78',
    'white_m':'#eaeaea',
    'black_m':'#1d1d1d',
    'white':'#ffffff',
    'black':'#000000',
    'gray':'#5d5d5d',
    'green_m':'#31C74A',
    'green_s':'#1A832B',
    'red_m':'#D8171D',
    'red_s':'#810005',
}




# ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - 
# ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - ICONOS - 
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
inv_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_inventario_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_inventario_dark.png"))
fact_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_fact_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_fact_dark.png"))
cuentas_xp_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentas_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_cuentas_dark.png"))
cuentas_xc_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cuentasPC_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_cuentasPC_dark.png"))
pdutilidad_icon=ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_PDUtilidad_light.png"), size=(30,30),
                                    dark_image=Image.open(r"Recursos\Iconos\btn_PDUtilidad_dark.png"))


ICONS = {
    'cancel':cancel_icon,
    'search':search_icon,
    'refresh':refresh_icon,
    'trash':trash_icon,
    'lock':lock_icon,
    'exit':exit_icon,
    'inventory':inv_icon,
    'fact':fact_icon,
    'cxp':cuentas_xp_icon,
    'cxc':cuentas_xc_icon,
    'proutil':pdutilidad_icon,
}