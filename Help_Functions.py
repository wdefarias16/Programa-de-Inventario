import customtkinter as ctk
import tkinter as tk
from tkinter import ttk,messagebox
from style import FONT,APP_COLOR,ICONS
from DatabaseManager import *

# -------------------------------------------------------------------------------
# VALIDATE ENTRIES - VALIDATE ENTRIES - VALIDATE ENTRIES - VALIDATE ENTRIES - 
# -------------------------------------------------------------------------------
# VALIDATE AMOUNT
def ValidateAmount(text):
    text = text.replace(".", "", 1)
    if text == '':
        return True
    return text.isdigit()
# VALIDATE DIGIT ONLY
def ValidateDigit(text):
    text = text.replace("", "", 1)
    if text == '':
        return True
    return text.isdigit()
# VALIDAR TELÉFONO
def ValidatePhone(texto):
        if len(texto) > 7:
            return False
        if texto == '':
            return True
        return texto.isdigit()
# VALIDAR CÉDULA
def ValidateCedula(texto):
        if len(texto) > 8:
            return False
        if texto == '':
            return True
        return texto.isdigit()
# VALIDAR CODIGO
def ValidateCodigo(texto):
        if len(texto) > 3:
            return False
        if texto == '':
            return True
        return texto.isdigit()
# VALIDAR EDAD
def ValidateEdad(texto):
        if len(texto) > 2:
            return False
        if texto == '':
            return True
        return texto.isdigit()
# -------------------------------------------------------------------------------
# VALIDATE USER - VALIDATE USER - VALIDATE USER - VALIDATE USER - 
# -------------------------------------------------------------------------------
def ValidateUser(id):
    user = GetCurrentUser()
    user = USER_MANAGER.GetUser(user)
    if user['rol'] != id:
        messagebox.showwarning('Atención','Usted no posee los permisos para acceder a este módulo.')
        return False
    return True
