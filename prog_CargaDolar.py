import tkinter as tk
import customtkinter as ctk
import datetime
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import ACCOUNTING_MANAGER
from Help_Functions import ValidateAmount
from datetime import date

class CargaDolar(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.validate = self.register(ValidateAmount)
        # OBTENER VALOR DOLAR
        self.DOLAR = ACCOUNTING_MANAGER.GetLastDolarValue()
        self.PARALELO = ACCOUNTING_MANAGER.GetLastDolarParaleloValue()
        
        # -------------------------------------------------------------------------------
        # PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE - PROGRAM TITLE -
        # -------------------------------------------------------------------------------
        self.title_frame = ctk.CTkFrame(self,
                        fg_color=APP_COLOR['main'],
                        corner_radius=0,)
        self.title_frame.place(relx=0.5,rely=0,relwidth=1,relheight=0.1,anchor='n')
        self.title_label = ctk.CTkLabel(self.title_frame,
                        text='Carga del dólar',
                        text_color=APP_COLOR['black_m'],
                        font=FONT['subtitle_bold'])
        self.title_label.place(relx=0.5,rely=0.5,anchor='center')
        # -----------------------------------------------------------------------------
        # BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR - BARRA INFERIOR
        # -----------------------------------------------------------------------------
        self.inf_bar_frame = ctk.CTkFrame(self,
                corner_radius=0,
                fg_color=APP_COLOR['sec'])
        self.inf_bar_frame.place(relx=0, rely=1, relwidth=1, relheight=0.05, anchor='sw')
        # FECHA
        self.fecha_label = ctk.CTkLabel(self.inf_bar_frame,
                                    text='',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['text'],
                                    corner_radius=2,)
        self.fecha_label.pack(side='right',pady=5,padx=10)
        # HORA
        self.hora_label = ctk.CTkLabel(self.inf_bar_frame,
                                    text='',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['text'],
                                    corner_radius=2,)
        self.hora_label.pack(side='right',pady=5,padx=10)
        self.GetDate()
    # -----------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME -
    # -----------------------------------------------------------------------------
        # LABELS - LABELS - LABELS - LABELS - LABELS - 
        # -------------------------------------------------------------------------
        # LOG
        self.log_label = ctk.CTkLabel(self,
                                    text='Dólar',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['text'],
                                    height=30,
                                    corner_radius=10,
                                    fg_color=APP_COLOR['gray'])
        self.log_label.place(relx=0.5,rely=0.85,relwidth=0.70,anchor='n')
        # DOLAR
        self.dolar_label = ctk.CTkLabel(self,
                                    text=f'Bs. {self.DOLAR}',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['subtitle_bold'],
                                    height=45)
        self.dolar_label.place(relx=0.45,rely=0.20,anchor='e')
        # PARALELO
        self.paralelo_label = ctk.CTkLabel(self,
                                    text=f'Bs. {self.PARALELO}',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['subtitle_bold'],
                                    height=45)
        self.paralelo_label.place(relx=0.55,rely=0.20,anchor='w')
        # VALOR ACTUAL DOLAR
        valor_actual_label = ctk.CTkLabel(self,
                                    text='Valor dólar',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['text'],
                                    height=45)
        valor_actual_label.place(relx=0.45,rely=0.25,anchor='e')
        # VALOR ACTUAL PARALELO
        valorparalelo_actual_label = ctk.CTkLabel(self,
                                    text='Valor secundario',
                                    text_color=APP_COLOR['black_m'],
                                    font=FONT['text'],
                                    height=45)
        valorparalelo_actual_label.place(relx=0.55,rely=0.25,anchor='w')
        # ACTUALIZAR FECHA Y HORA ACTUALES
        self.GetDate()
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # ACTUALIZAR DOLAR
        self.update_dolar_btn = ctk.CTkButton(self,
                                    text='Actualizar',
                                    command = self.UpdateDolarWindow,
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['main'],
                                    hover_color=APP_COLOR['sec'],
                                    text_color=APP_COLOR['black_m'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.update_dolar_btn.place(relx=0.45,rely=0.30,anchor='e')
        # ACTUALIZAR PARALELO
        self.update_paralelo_btn = ctk.CTkButton(self,
                                    text='Actualizar',
                                    command = self.UpdateDolarParaleloWindow,
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['main'],
                                    hover_color=APP_COLOR['sec'],
                                    text_color=APP_COLOR['black_m'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.update_paralelo_btn.place(relx=0.55,rely=0.30,anchor='w')
        # VER CARGAS DEL DOLAR
        self.list_dolar_btn = ctk.CTkButton(self,
                                    text='Dolar',
                                    command = self.ListDolarValues,
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['gray'],
                                    hover_color=APP_COLOR['sec'],
                                    text_color=APP_COLOR['black_m'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.list_dolar_btn.place(relx=0.15,rely=0.40,anchor='w')
        # VER CARGAS DEL DOLAR
        self.list_paralelo_btn = ctk.CTkButton(self,
                                    text='Secundario',
                                    command = self.ListDolarParaleloValues,
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['gray'],
                                    hover_color=APP_COLOR['sec'],
                                    text_color=APP_COLOR['black_m'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.list_paralelo_btn.place(relx=0.23,rely=0.40,anchor='w')
        # GO BACK BUTTON
        self.go_back_btn = ctk.CTkButton(self,
                        text='Volver',
                        text_color=APP_COLOR['black_m'],
                        font=FONT['text_small'],
                        fg_color=APP_COLOR['gray'],
                        hover_color=APP_COLOR['main'],
                        command=lambda: self.GoBack_CB())
        self.go_back_btn.place(relx=0, rely=0.1, relwidth=0.1, relheight=0.05, anchor='nw')
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 30,
            font = FONT['text'],
            bordercolor=APP_COLOR['black_m'],
            relief="solid",
            fieldbackground = APP_COLOR['white_m'],)
        self.style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['main'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_bold'])
        self.treeview_main = ttk.Treeview(self,
                                    style='Custom.Treeview',
                                    columns=('Hora','Valor'))
        self.treeview_main.place(relx=0.5,y=480,relwidth=0.70,height=320,anchor='n')
        # DESCRIPCION
        self.treeview_main.heading('#0',text='Fecha')
        self.treeview_main.column('#0', width=100, anchor='w', minwidth=100, stretch=True)
        # CANTIDAD
        self.treeview_main.heading('Hora',text='Hora')
        self.treeview_main.column('Hora', width=100, anchor='center', stretch=True)
        # BOLIVARES
        self.treeview_main.heading('Valor',text='Valor.')
        self.treeview_main.column('Valor', width=100, anchor='w', stretch=True)
        self.ListDolarValues()
    # -----------------------------------------------------------------------------------------------
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # -----------------------------------------------------------------------------------------------
    def ListDolarValues(self):
            dolars_last_month = ACCOUNTING_MANAGER.GetDolarLastMonth()
            for item in self.treeview_main.get_children():
                self.treeview_main.delete(item)
            for i, dolar in enumerate(dolars_last_month):
                hora = str(dolar['hora'])
                hora = hora.split(' ')[1]
                tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
                self.treeview_main.insert("", 'end',
                                           text=dolar['fecha'],
                                           values=(hora,
                                                   f'Bs. {dolar['tasa']}'),
                                           tags=(tag,))
            self.treeview_main.tag_configure('Odd.Treeview', background="#ffffff")
            self.treeview_main.tag_configure('Even.Treeview', background="#eaeaea")
            self.log_label.configure(text='Dólar')
    def ListDolarParaleloValues(self):
            dolars_last_month = ACCOUNTING_MANAGER.GetDolarParaleloLastMonth()
            for item in self.treeview_main.get_children():
                self.treeview_main.delete(item)
            for i, dolar in enumerate(dolars_last_month):
                hora = str(dolar['hora'])
                hora = hora.split(' ')[1]
                tag = "Even.Treeview" if i % 2 == 0 else "Odd.Treeview"  # Alternar tags
                self.treeview_main.insert("", 'end',
                                           text=dolar['fecha'],
                                           values=(hora,
                                                   f'Bs. {dolar['tasa']}'),
                                           tags=(tag,))
            self.treeview_main.tag_configure('Odd.Treeview', background="#ffffff")
            self.treeview_main.tag_configure('Even.Treeview', background="#eaeaea")
            self.log_label.configure(text='Secundario')
# ACTUALIZACION DEL DOLAR
    def UpdateDolarWindow(self):
        # ACTUALIZAR EL DOLAR
        def UpdateDolar():
            fecha = date.today()
            valor_dolar = nuevo_valor_entry_var.get()
            try:
                 float(nuevo_valor_entry_var.get())
            except ValueError:
                 messagebox.showwarning('¡Error!','Error de carga')
                 nuevo_valor_entry_var.set('')
                 nuevo_valor_entry.focus()
            motivo = log.get("1.0","end").strip()

            ACCOUNTING_MANAGER.GuardarDolar(fecha,valor_dolar,motivo)

            self.DOLAR = valor_dolar
            self.dolar_label.configure(text=f'Bs. {self.DOLAR}')
            self.ListDolarValues()
            dolar_window.destroy()
        # ---------------------------------------------- 
        # FRAME 
        # ---------------------------------------------- 
        dolar_window = ctk.CTkToplevel(self)
        dolar_window.geometry('600x350')
        dolar_window.title('Editar')
        dolar_window.protocol("WM_DELETE_WINDOW", lambda: None)
        dolar_window.transient(self)
        dolar_window.grab_set()
        dolar_frame = ctk.CTkFrame(dolar_window,
                                corner_radius=0)
        dolar_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # LABELS - LABELS - LABELS - 
        # NUEVO VALOR
        nuevo_valor_label = ctk.CTkLabel(dolar_frame,
                                text='Nuevo valor',
                                text_color=APP_COLOR['main'],
                                anchor='w',
                                font=FONT['title_bold'])
        nuevo_valor_label.place(relx=0.1,rely=0.2,anchor='nw')
        # LOG
        log_label = ctk.CTkLabel(dolar_frame,
                                text='Motivo de ajuste',
                                text_color=APP_COLOR['gray'],
                                anchor='w',
                                font=FONT['text'])
        log_label.place(relx=0.1,rely=0.4,anchor='nw')
        # ENTRYS - ENTRYS - ENTRYS - 
        # DOLAR
        nuevo_valor_entry_var = tk.StringVar()
        nuevo_valor_entry = ctk.CTkEntry(dolar_frame,
                                width=160,
                                height=40,
                                validate = 'key',
                                validatecommand = (self.validate,'%P'),
                                textvariable=nuevo_valor_entry_var,
                                fg_color=APP_COLOR['white_m'],
                                border_color=APP_COLOR['gray'],
                                text_color=APP_COLOR['black_m'])
        nuevo_valor_entry.place(relx=0.40,rely=0.20,anchor='nw')
        nuevo_valor_entry.bind("<Return>",lambda event: UpdateDolar())
        nuevo_valor_entry.focus()
        # LOG
        log = ctk.CTkTextbox(dolar_frame,
                                height=80,
                                fg_color=APP_COLOR['white'],
                                text_color=APP_COLOR['black_m'])
        log.place(relx=0.5,rely=0.5,anchor='n',relwidth=0.80)
        # BUTTONS - BUTTONS - BUTTONS - 
        exit_button = ctk.CTkButton(dolar_frame,
                                text='',
                                width=20,
                                height=20,
                                image=ICONS['cancel'],
                                command=lambda:dolar_window.destroy(),
                                fg_color=APP_COLOR['red_m'],
                                hover_color=APP_COLOR['red_s'])
        exit_button.place(relx=0.90,rely=0.05,anchor='nw')
    # ACTUALIZAR PARALELO
    def UpdateDolarParaleloWindow(self):
        # ACTUALIZAR EL DOLAR
        def UpdateDolar():
            fecha = date.today()
            valor_dolar = nuevo_valor_entry_var.get()
            try:
                 float(nuevo_valor_entry_var.get())
            except ValueError:
                 messagebox.showwarning('¡Error!','Error de carga')
                 nuevo_valor_entry_var.set('')
                 nuevo_valor_entry.focus()
            motivo = log.get("1.0","end").strip()

            ACCOUNTING_MANAGER.GuardarDolarParalelo(fecha,valor_dolar,motivo)

            self.PARALELO = valor_dolar
            self.paralelo_label.configure(text=f'Bs. {self.PARALELO}')
            self.ListDolarParaleloValues()
            dolar_window.destroy()
        # ---------------------------------------------- 
        # FRAME 
        # ---------------------------------------------- 
        dolar_window = ctk.CTkToplevel(self)
        dolar_window.geometry('600x350')
        dolar_window.title('Editar')
        dolar_window.protocol("WM_DELETE_WINDOW", lambda: None)
        dolar_window.transient(self)
        dolar_window.grab_set()
        dolar_frame = ctk.CTkFrame(dolar_window,
                                corner_radius=0)
        dolar_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # LABELS - LABELS - LABELS - 
        # NUEVO VALOR
        nuevo_valor_label = ctk.CTkLabel(dolar_frame,
                                text='Nuevo valor',
                                text_color=APP_COLOR['main'],
                                anchor='w',
                                font=FONT['title_bold'])
        nuevo_valor_label.place(relx=0.1,rely=0.2,anchor='nw')
        # LOG
        log_label = ctk.CTkLabel(dolar_frame,
                                text='Motivo de ajuste',
                                text_color=APP_COLOR['gray'],
                                anchor='w',
                                font=FONT['text'])
        log_label.place(relx=0.1,rely=0.4,anchor='nw')
        # ENTRYS - ENTRYS - ENTRYS - 
        # DOLAR
        nuevo_valor_entry_var = tk.StringVar()
        nuevo_valor_entry = ctk.CTkEntry(dolar_frame,
                                width=160,
                                height=40,
                                validate = 'key',
                                validatecommand = (self.validate,'%P'),
                                textvariable=nuevo_valor_entry_var,
                                fg_color=APP_COLOR['white_m'],
                                border_color=APP_COLOR['gray'],
                                text_color=APP_COLOR['black_m'])
        nuevo_valor_entry.place(relx=0.40,rely=0.20,anchor='nw')
        nuevo_valor_entry.bind("<Return>",lambda event: UpdateDolar())
        nuevo_valor_entry.focus()
        # LOG
        log = ctk.CTkTextbox(dolar_frame,
                                height=80,
                                fg_color=APP_COLOR['white'],
                                text_color=APP_COLOR['black_m'])
        log.place(relx=0.5,rely=0.5,anchor='n',relwidth=0.80)
        # BUTTONS - BUTTONS - BUTTONS - 
        exit_button = ctk.CTkButton(dolar_frame,
                                text='',
                                width=20,
                                height=20,
                                image=ICONS['cancel'],
                                command=lambda:dolar_window.destroy(),
                                fg_color=APP_COLOR['red_m'],
                                hover_color=APP_COLOR['red_s'])
        exit_button.place(relx=0.90,rely=0.05,anchor='nw')

# MOSTAR LA FECHA Y HORA
    def GetDate(self):
        hora = datetime.datetime.now()
        self.fecha_label.configure(text=hora.strftime("%d/%m/%Y"))
        self.hora_label.configure(text=hora.strftime("%H:%M:%S"))
        self.after(1000,self.GetDate)
    # -----------------------------------------------------------------------------------------------