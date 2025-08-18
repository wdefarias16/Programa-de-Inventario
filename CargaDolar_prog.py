import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from style import FONT, ICONS, APP_COLOR
from DatabaseManager import INVENTARIO,VALOR_DOLAR,FUNCIONES
import datetime
from datetime import date

class CargaDolar(ctk.CTkFrame):
    def __init__(self, parent, GoBack_CB):
        super().__init__(parent)
        self.configure(fg_color=APP_COLOR['white_m'])
        # CALLBACK IR ATRÁS
        self.GoBack_CB = GoBack_CB
        self.validate = self.register(self.ValidateDigit)

        # OBTENER VALOR DOLAR
        self.VALOR_DOLAR = VALOR_DOLAR
        
             
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
    # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   height=70,
                                   fg_color=APP_COLOR['sec'],
                                   corner_radius=0)
        title_frame.place(relx=0.5,rely=0,relwidth=1,anchor='n')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Carga diaria del dólar',
                                   bg_color='transparent',
                                   text_color=APP_COLOR['white_m'],
                                   font=FONT['title_light'])
        title_label.place(relx=0.5,rely=0.5,anchor='center')
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
    # MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - MAIN FRAME - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LOG
        self.log_label = ctk.CTkLabel(self,
                                    text='Nota',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['text'],
                                    height=30,
                                    corner_radius=10,
                                    fg_color=APP_COLOR['gray'])
        self.log_label.place(relx=0.5,rely=0.85,relwidth=0.70,anchor='n')
        # FECHA
        self.fecha_label = ctk.CTkLabel(self,
                                    text='',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45,
                                    corner_radius=2,
                                    fg_color=APP_COLOR['main'])
        self.fecha_label.place(relx=0.10,rely=0.15,anchor='n')
        # FECHA LABEL
        fecha_text_label = ctk.CTkLabel(self,
                                    text='Fecha',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=60,
                                    height=25)
        fecha_text_label.place(relx=0.10,rely=0.11,anchor='n')
        # HORA
        self.hora_label = ctk.CTkLabel(self,
                                    text='',
                                    text_color=APP_COLOR['white'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45,
                                    corner_radius=2,
                                    fg_color=APP_COLOR['main'])
        self.hora_label.place(relx=0.90,rely=0.15,anchor='n')
        # HORA LABEL
        hora_text_label = ctk.CTkLabel(self,
                                    text='Hora',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=60,
                                    height=25)
        hora_text_label.place(relx=0.90,rely=0.11,anchor='n')
        # DOLAR
        self.dolar_label = ctk.CTkLabel(self,
                                    text=f'Bs. {self.VALOR_DOLAR}',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['subtitle_bold'],
                                    width=120,
                                    height=45)
        self.dolar_label.place(relx=0.50,rely=0.15,anchor='n')
        # VALOR ACTUAL
        valor_actual_label = ctk.CTkLabel(self,
                                    text='Valor actual',
                                    text_color=APP_COLOR['gray'],
                                    font=FONT['text'],
                                    width=120,
                                    height=45)
        valor_actual_label.place(relx=0.50,rely=0.20,anchor='n')
        # ACTUALIZAR FECHA Y HORA ACTUALES
        self.GetDate()
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        self.update_dolar_btn = ctk.CTkButton(self,
                                    text='Actualizar',
                                    command = self.UpdateDolarWindow,
                                    font=FONT['text'],
                                    fg_color=APP_COLOR['main'],
                                    hover_color=APP_COLOR['sec'],
                                    width=80,
                                    height=25,
                                    corner_radius=2)
        self.update_dolar_btn.place(relx=0.50,rely=0.30,anchor='n')
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - TREEVIEW - 
        # CONFIGURACION VISUAL DEL TV
        style = ttk.Style()
        style.configure(
            'Custom.Treeview',
            background = APP_COLOR['white_m'],
            foreground = APP_COLOR['black_m'],
            rowheight = 40,
            font = FONT['text'],
            fieldbackground = APP_COLOR['white_m'])
        style.configure(
            'Custom.Treeview.Heading',
            background = APP_COLOR['black_m'],
            foreground = APP_COLOR['black_m'],
            font = FONT['text_light'])
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
        
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
        def ListDolarValues():
            dolars_last_month = INVENTARIO.GetDolarLastMonth()
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
        ListDolarValues()
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
    # FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
# ACTUALIZACION DEL DOLAR
    def UpdateDolarWindow(self):
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

            INVENTARIO.GuardarDolar(fecha,valor_dolar,motivo)

            self.VALOR_DOLAR = valor_dolar
            self.dolar_label.configure(text=f'Bs. {self.VALOR_DOLAR}')

            actualizardolar=FUNCIONES['UpdateDolarValue']
            actualizardolar()
            dolar_window.destroy()
            

        # FRAME 
        dolar_window = ctk.CTkToplevel(self,
                                   fg_color=APP_COLOR['white_m'])
        dolar_window.geometry('600x350')
        dolar_window.title('Editar')
        dolar_window.protocol("WM_DELETE_WINDOW", lambda: None)
        dolar_window.transient(self)
        dolar_window.grab_set()
        dolar_frame = ctk.CTkFrame(dolar_window,
                                corner_radius=0,
                                fg_color=APP_COLOR['white_m'])
        dolar_frame.place(relx=0,rely=0,relheight=1,relwidth=1,anchor='nw')
        # LABELS - LABELS - LABELS - 
        # NUEVO VALOR
        nuevo_valor_label = ctk.CTkLabel(dolar_frame,
                                text='Nuevo valor',
                                text_color=APP_COLOR['gray'],
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
                                fg_color=APP_COLOR['white'],
                                border_color=APP_COLOR['white_m'])
        nuevo_valor_entry.place(relx=0.35,rely=0.20,anchor='nw')
        nuevo_valor_entry.bind("<Return>",lambda event: UpdateDolar())
        nuevo_valor_entry.focus()
        # LOG
        log = ctk.CTkTextbox(dolar_frame,
                                height=80,
                                fg_color=APP_COLOR['white'])
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
    # -----------------------------------------------------------------------------------------------
# VALIDAR ENTRADA DE CARACTERES NUMERICOS
    def ValidateDigit(self,text):
            text = text.replace(".", "", 1)
            if text == '':
                return True
            return text.isdigit()
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------