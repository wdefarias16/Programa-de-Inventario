import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from style import FONT, APP_COLORS, ICONS

class MaestroDeTablas_prog(ctk.CTkFrame):
    def __init__(self,parent,GoBack_CB):
        super().__init__(parent)
        # GO BACK CALLBACK
        self.GoBack_CB = GoBack_CB

        # TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - TITLE - 
        # FRAME
        title_frame = ctk.CTkFrame(self,
                                   fg_color=APP_COLORS[3],
                                   corner_radius=0,
                                   height=50)
        title_frame.pack(fill='x')
        # LABEL
        title_label = ctk.CTkLabel(title_frame,
                                   text='Maestro de tablas',
                                   bg_color='transparent',
                                   text_color=APP_COLORS[0],
                                   font=FONT['title_light'])
        title_label.pack(pady=10)
        
        # CREATE THE MAIN MENU
        self.MainMenu()
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    # PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - PROG - 
    def MainMenu(self):
        # PROG FRAME
        self.current_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.current_frame.pack(expand=True,fill='both',side='left')
        self.current_frame.bind("<Return>",lambda event:self.ProductsHelp())

        # GRID SETUP
        ROWS, COLUMNS = 7, 4
        for rows in range(ROWS):
            self.current_frame.rowconfigure(rows,weight=1,uniform='a')
        for columns in range(COLUMNS):
            self.current_frame.columnconfigure(columns,weight=1,uniform='a')
        
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # CREATE TABLE
        create_table_btn = ctk.CTkButton(self.current_frame,
                                         text='Crear una tabla',
                                         command=self.CreateTableFrame,
                                         font=FONT['title_light'],
                                         fg_color=APP_COLORS[2],
                                         hover_color=APP_COLORS[3])
        create_table_btn.grid(row=1,column=1,rowspan=2,columnspan=2,sticky='nswe')
        # MODIFY TABLE
        mod_table_btn = ctk.CTkButton(self.current_frame,
                                         text='Modificar una tabla',
                                         command=self.ModTableFrame,
                                         font=FONT['title_light'],
                                         fg_color=APP_COLORS[2],
                                         hover_color=APP_COLORS[3])
        mod_table_btn.grid(row=4,column=1,rowspan=2,columnspan=2,sticky='nswe')

# CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - 
# CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - CREATE TABLE FRAME - 
    def CreateTableFrame(self):
        def AddColumn():
            # ENTRY
            column_var = tk.StringVar()
            column_entry = ctk.CTkEntry(self.current_frame,
                                        textvariable=column_var,
                                        fg_color=APP_COLORS[6],
                                        border_color=APP_COLORS[2])
            column_entry.grid(row=self.column_entry_row,column=6,sticky='we')
            self.entry_var_list.append(column_var)
            # LABEL
            column_entry_label = ctk.CTkLabel(self.current_frame,
                                              text=f'Columna {self.counter}',
                                              text_color=APP_COLORS[4],
                                              font=FONT['text'])
            column_entry_label.grid(row=self.column_entry_row,column=4,columnspan=2,sticky='e',padx=5)
            # ADD COUNTER
            ColumnCounter()
        # ----------------------------------------------------------------------------
        # ----------------------------------------------------------------------------
        # ADD 1 ROW FOR THE NEXT TIME THAT ADDCOLUMN EXECUTES
        def ColumnCounter():
            self.counter += 1
            self.column_entry_row += 1
        # ----------------------------------------------------------------------------
        # ----------------------------------------------------------------------------
        self.current_frame.destroy()

        self.counter = 1
        # STRING VAR LIST
        self.entry_var_list = []
        # COUNTER FOR GRID ROW
        self.column_entry_row = 6
        
        # PROG FRAME
        self.current_frame = ctk.CTkFrame(self,corner_radius=0,fg_color=APP_COLORS[0])
        self.current_frame.pack(expand=True,fill='both',side='left')
        self.current_frame.bind("<Return>",lambda event:self.ProductsHelp())

        # GRID SETUP
        ROWS, COLUMNS = 20, 16
        for rows in range(ROWS):
            self.current_frame.rowconfigure(rows,weight=1,uniform='a')
        for columns in range(COLUMNS):
            self.current_frame.columnconfigure(columns,weight=1,uniform='a')
        
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - ENTRYS - 
        # TABLE ID
        table_id_entry_var = tk.StringVar()
        table_id_entry = ctk.CTkEntry(self.current_frame,
                                      textvariable=table_id_entry_var,
                                      fg_color=APP_COLORS[6],
                                      border_color=APP_COLORS[2])
        table_id_entry.grid(row=2,column=6,sticky='we')
        # TABLE NAME
        table_name_entry_var = tk.StringVar()
        table_name_entry = ctk.CTkEntry(self.current_frame,
                                      textvariable=table_name_entry_var,
                                      fg_color=APP_COLORS[6],
                                      border_color=APP_COLORS[2])
        table_name_entry.grid(row=3,column=6,columnspan=2,sticky='we')
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - LABELS - 
        # TABLE ID
        table_id_label = ctk.CTkLabel(self.current_frame,
                                      text='ID de tabla',
                                      text_color=APP_COLORS[4],
                                      font=FONT['text'])
        table_id_label.grid(row=2,column=4,columnspan=2,sticky='e',padx=5)
        # TABLE NAME
        table_name_label = ctk.CTkLabel(self.current_frame,
                                        text='Nombre de tabla',
                                        text_color=APP_COLORS[4],
                                        font=FONT['text'])
        table_name_label.grid(row=3,column=4,columnspan=2,sticky='e',padx=5)
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        # BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - BUTTONS - 
        add_column_btn = ctk.CTkButton(self.current_frame,
                                       text='+',
                                       command=AddColumn,
                                       font=FONT['text'],
                                       fg_color=APP_COLORS[2],
                                       hover_color=APP_COLORS[3])
        add_column_btn.grid(row=4,column=9,sticky='nswe')
        # START WITH 1 COLUMN CREATED
        AddColumn()

    

    def ModTableFrame(self):
        pass