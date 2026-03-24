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

# ---------------------------------------------------------------
# VERIFY OPCODE - VERIFY OPCODE - VERIFY OPCODE - 
# ---------------------------------------------------------------
# VERIFY USER OP CODE
def VerifyOpCode(self):
    result = None
    USER_ROL = None
    USER = USER_MANAGER.GetUser(GetCurrentUser())
    ROLES = USER_MANAGER.GetRoles()
    for rol in ROLES:
        if rol.split(' - ')[0] == str(USER['rol']):
            USER_ROL = rol.split(' - ')[1]
            break
    if USER_ROL != 'Administrador':
        messagebox.showwarning('Gestión de usuarios','Usted no posee las'
        ' credenciales para realizar esta acción.')
        return
    
    # -------------------------------------------------------------------------
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # -------------------------------------------------------------------------
    def VerifyOpCode():
        opcode = opcode_entry_var.get()
        if opcode == USER['opcode']:
            nonlocal result
            result = True
            opcode_window.destroy()
        else:
            messagebox.showwarning('Gestión de usuarios','Código inválido.')
            result = False       
            opcode_window.destroy()
    # -------------------------------------------------------------------------
    # WINDOW - WINDOW - WINDOW - WINDOW - WINDOW - WINDOW - WINDOW - WINDOW - 
    # -------------------------------------------------------------------------
    opcode_window = ctk.CTkToplevel(self)
    opcode_window.geometry('400x200')
    opcode_window.title('Código de operación')
    opcode_window.protocol("WM_DELETE_WINDOW", lambda: None)
    opcode_window.transient(self)
    opcode_window.grab_set()
    opcode_frame = ctk.CTkFrame(opcode_window,
            corner_radius=0)
    opcode_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
    # -------------------------------------------------------------------------
    # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
    # -------------------------------------------------------------------------
    entry_label = ctk.CTkLabel(opcode_frame,
            text='Ingresa tu código de operación',
            font=FONT['text'],
            text_color=APP_COLOR['gray_s'])
    entry_label.place(relx=0.1,rely=0.3,anchor='w')
    info_label = ctk.CTkLabel(opcode_frame,
            text='',
            font=FONT['text'],
            text_color=APP_COLOR['gray'])
    info_label.place(relx=0.1,rely=0.7,anchor='w')
    # -------------------------------------------------------------------------
    # ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - ENTRIES - 
    # -------------------------------------------------------------------------
    opcode_entry_var = ctk.StringVar()
    opcode_entry = ctk.CTkEntry(opcode_frame,
            textvariable=opcode_entry_var,
            width=50,
            fg_color=APP_COLOR['light_gray'],
            border_color=APP_COLOR['light_gray'],
            text_color=APP_COLOR['black_m'])
    opcode_entry.place(relx=0.1,rely=0.5,anchor='w')
    opcode_entry.bind('<Return>',lambda event: VerifyOpCode())
    opcode_entry.focus()
    # -------------------------------------------------------------------------
    # BUTTON - BUTTON - BUTTON - BUTTON - BUTTON - BUTTON - BUTTON - BUTTON - 
    # -------------------------------------------------------------------------
    # EXIT
    exit_button = ctk.CTkButton(opcode_frame,
            text='',
            image= ICONS['cancel'],
            command=opcode_window.destroy,
            width=40,
            fg_color=APP_COLOR['red_m'],
            hover_color=APP_COLOR['red_s'])
    exit_button.place(relx=0.98,rely=0.10,anchor='ne')
    # ACCEPT
    enter_button = ctk.CTkButton(opcode_frame,
            text='Aceptar',
            command=VerifyOpCode,
            fg_color=APP_COLOR['main'],
            text_color=APP_COLOR['black_m'],
            hover_color=APP_COLOR['sec'])
    enter_button.place(relx=0.26,rely=0.5,anchor='w')
    opcode_window.wait_window(opcode_window)
    return result