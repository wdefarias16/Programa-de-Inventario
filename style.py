import customtkinter as ctk
from PIL import Image

FONTS = [('Roboto light',25),('Roboto light',15),('Roboto light',12),('Roboto',15),('Roboto Bold',25),('Roboto Bold',20)]
APP_COLORS = ['#eaeaea','#1d1d1d','#1c9bac','#166c78',
              '#5d5d5d',"#d4d4d4",'#ffffff','#666666',
              '#31C74A','#D8171D','#810005']
APPEARANCE_MODE = 'light'


cancel_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_cerrar_light.png"), size=(30,30),
                                        dark_image=Image.open(r"Recursos\Iconos\btn_cerrar_dark.png"))
search_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_search_light.png"), size=(30,30),
                                dark_image=Image.open(r"Recursos\Iconos\btn_search_dark.png"))
refresh_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_refresh_light.png"), size=(30,30),
                                dark_image=Image.open(r"Recursos\Iconos\btn_refresh_dark.png"))
trash_icon = ctk.CTkImage(light_image=Image.open(r"Recursos\Iconos\btn_trash_light.png"), size=(30,30),
                                dark_image=Image.open(r"Recursos\Iconos\btn_trash_dark.png"))


ICONS = {
    'cancel':cancel_icon,
    'search':search_icon,
    'refresh':refresh_icon,
    'trash':trash_icon
}


