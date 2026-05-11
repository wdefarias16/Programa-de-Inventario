# -----------------------------------
# SISTEMA DE GESTION WINVENTORY
# -----------------------------------
import customtkinter as ctk
from tkinter import messagebox
from Login import Login
from style import *
from DatabaseManager import USER_MANAGER, GetCurrentUser
from DashBoard import DashBoardMenu

# -----------------------------------
# MENUS - MENUS - MENUS - MENUS - 
# -----------------------------------
from Menu_Inventario import InventarioMenu
from Menu_CuentasPorPagar import CuentasPorPagarMenu
from Menu_Facturacion import FacturacionMenu
from Menu_ProgramasDeUtilidad import ProgramasDeUtilidadMenu

# -----------------------------------
# PROGRAMAS - PROGRAMAS - PROGRAMAS
# -----------------------------------
# INVENTARIO
from prog_CargaLineasGrupos import LineasGruposProg
from prog_CargaProductos import CargaProductosProg
from prog_AjustesInventario import AjustesInventarioProg
from prog_EntradaInventario import EntradasInventarioProg
# CUENTAS POR PAGAR
from prog_CargaProveedores import ProveedoresProg
# FACTURACION
from prog_Facturacion import FacturacionProg
# UTILIDADES
from prog_GestionDeUsuarios import GestionUsuariosProg
from prog_CargaDolar import CargaDolar

# VENTANA PRINCIPAL (APLICACION)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Winventory v0.1 Beta')
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # INICIALIZAR EL PROGRAMA ACTIVO COMO NONE
        self.current_prog = None
        self.dashboard_activo = False
        self.login_activo = False
        self.side_bar_active = False
        
        # ATAJOS
        # ATAJO CERRAR SESION
        self.winfo_toplevel().bind("<Control-Q>", lambda event: self.CloseSession())
        self.winfo_toplevel().bind("<Control-q>", lambda event: self.CloseSession())
        # ATAJO VOLVER AL DASHBOARD
        self.winfo_toplevel().bind("<F4>", self.F4_Pressed)
        
        # INICIAR EN EL FRAME DE LOGIN
        self.Show_Frame(Login, success_callback=self.LoginSuccess, exit_callback=self.Salir)
        
        # RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN - RUN -
        self.mainloop()
        
    # -----------------------------------------------------------------
    # FUNCION QUE MANEJA TODOS LOS CAMBIOS DE PROGRAMA
    # -----------------------------------------------------------------
    def Show_Frame(self,frame_class,**kwargs):
        # LIMPIAR EL FRAME ACTUAL SI NO EXISTE
        if self.current_prog is not None:
            self.current_prog.destroy()
        if self.side_bar_active:
            self.side_bar_frame.destroy()

        # INSTANCIAR EL NUEVO FRAME
        self.current_prog = frame_class(self,**kwargs)
        self.current_prog.pack(expand=True,fill='both',side=['right'])
        
        # GESTION AUTOMATICA DE ESTADO
        self.dashboard_activo = isinstance(self.current_prog, DashBoardMenu)
        self.login_activo = isinstance(self.current_prog, Login)

        if not self.dashboard_activo and not self.login_activo:
            self.Side_Bar()
            self.side_bar_active = True
            
    # -----------------------------------------------------------------
    # SIDE BAR - SIDE BAR - SIDE BAR - SIDE BAR - SIDE BAR - SIDE BAR - 
    # -----------------------------------------------------------------
    def Side_Bar(self):
        self.side_bar_frame = ctk.CTkFrame(self,
                    fg_color=APP_COLOR['sec'],
                    width=100,
                    corner_radius=0)
        self.side_bar_frame.pack(fill='y',side=['left'])
        
        # BOTONES
        # GO HOME
        self.home_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS['home'],
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.ReturnToDashboard)
        self.home_btn.place(relx=0.5,rely=0.02,relwidth=0.8,anchor='n')
        
        # MENU INVENTARIO
        self.inv_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS.get('box', ICONS.get('user')), # Using a fallback just in case 'box' isn't in your ICONS dict
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.InventarioMenu)
        self.inv_btn.place(relx=0.5,rely=0.38,relwidth=0.8,anchor='center')
        
        # MENU FACTURACION
        self.fact_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS.get('invoice', ICONS.get('m_note')),
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.FacturacionMenu)
        self.fact_btn.place(relx=0.5,rely=0.44,relwidth=0.8,anchor='center')
        
        # MENU CUENTAS POR PAGAR
        self.cxp_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS.get('wallet', ICONS.get('dolar')),
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.CuentasPorPagarMenu)
        self.cxp_btn.place(relx=0.5,rely=0.50,relwidth=0.8,anchor='center')
        
        # MENU UTILIDAD
        self.progutil_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS.get('pdu', ICONS.get('user')),
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.ProgramasUtilidadMenu)
        self.progutil_btn.place(relx=0.5,rely=0.56,relwidth=0.8,anchor='center')
        
        # LOGOUT
        self.logout_btn = ctk.CTkButton(self.side_bar_frame,
            text='',
            image=ICONS.get('lock', ICONS.get('lock')),
            fg_color=APP_COLOR['sec_mid'],
            hover_color=APP_COLOR['sec'],
            text_color=APP_COLOR['black_m'],
            command=self.CloseSession)
        self.logout_btn.place(relx=0.5,rely=0.92,relwidth=0.8,anchor='n')

    # -----------------------------------------------------------------
    # ATAJOS - ATAJOS - ATAJOS - ATAJOS - ATAJOS - ATAJOS - ATAJOS - AT
    # -----------------------------------------------------------------
    def F4_Pressed(self,event):
        if isinstance(self.current_prog,Login):
            return
        if not self.dashboard_activo:
            self.ReturnToDashboard()

    def CloseSession(self):
        self.Logout_User()
        self.LockWindow()

# -------------------------------------------------------------------------------------------------
# BLOQUEO Y DESBLOQUEO DE SESION - BLOQUEO Y DESBLOQUEO DE SESION - BLOQUEO Y DESBLOQUEO DE SESION - 
# -------------------------------------------------------------------------------------------------
    def LoginSuccess(self):
        self.ReturnToDashboard()
        
# -------------------------------------------------------------------------------------------------
# CLOSE SESSION - CLOSE SESSION - CLOSE SESSION - CLOSE SESSION - CLOSE SESSION - CLOSE SESSION - 
# -------------------------------------------------------------------------------------------------
    # DESLOGUEAR USUARIO
    def Logout_User(self):
        user = GetCurrentUser()
        if user:
            USER_MANAGER.ChangeUserStatus(user,False)

    def LockWindow(self):
        self.Show_Frame(
                    Login,
                    success_callback=self.LoginSuccess,
                    exit_callback=self.Salir)
                    
    def Salir(self):
        answer = messagebox.askyesno('Salir','¿Está seguro que desea salir de la aplicación?')
        if not answer:
            return
        self.Logout_User()
        self.quit()

# -------------------------------------------------------------------------------------------------
# RETURN TO DASHBOARD - RETURN TO DASHBOARD - RETURN TO DASHBOARD - RETURN TO DASHBOARD -
# -------------------------------------------------------------------------------------------------
    def ReturnToDashboard(self):
        if self.dashboard_activo:
            return
        self.Show_Frame(
                    DashBoardMenu,
                    lockscreen_callback = self.LockWindow,
                    exit_callback = self.Salir,
                    Inventario_CB=self.InventarioMenu,
                    Facturacion_CB=self.FacturacionMenu,
                    CuentasPorPagar_CB=self.CuentasPorPagarMenu,
                    ProgramasDeUtilidad_CB = self.ProgramasUtilidadMenu)
                    
# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO
# -------------------------------------------------------------------------------------------------
    # MENU DE INVENTARIO
    def InventarioMenu(self):
        self.Show_Frame(
                    InventarioMenu,
                    GoBack_CB = self.ReturnToDashboard,
                    CargaPro_Prog = self.CargaProductosProg,
                    Lineas_Prog = self.CargaLineas,
                    EntradasInv_prog = self.EntradasInventario,
                    AjustesInv_Prog = self.AjustesInventario)
                    
    # PROGRAMA DE CARGA DE LINEAS Y GRUPOS
    def CargaLineas(self):
        self.Show_Frame(LineasGruposProg,GoBack_CB=self.InventarioMenu)
        
    # PROGRAMA DE CARGA DE PRODUCTOS
    def CargaProductosProg(self):
        self.Show_Frame(CargaProductosProg,GoBack_CB=self.InventarioMenu)
        
    # ENTRADAS DE INVENTARIO
    def EntradasInventario(self):
        self.Show_Frame(EntradasInventarioProg,GoBack_CB=self.InventarioMenu)
        
    # AJUSTES DE INVENTARIO
    def AjustesInventario(self):
        self.Show_Frame(AjustesInventarioProg,GoBack_CB=self.InventarioMenu)

# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION
# -------------------------------------------------------------------------------------------------
    # MENU FACTURACION
    def FacturacionMenu(self):
        self.Show_Frame(FacturacionMenu,GoBack_CB = self.ReturnToDashboard,FacturacionProg = self.FacturacionProg)
        
    # FACTURACION
    def FacturacionProg(self):
        self.Show_Frame(FacturacionProg,GoBack_CB=self.FacturacionMenu)

# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR
# -------------------------------------------------------------------------------------------------
    # MENU DE CUENTAS POR PAGAR
    def CuentasPorPagarMenu(self):
        self.Show_Frame(CuentasPorPagarMenu,GoBack_CB = self.ReturnToDashboard,Proveedores_Prog = self.CargaProveedores)
        
    # PROGRAMA DE CARGA DE PROVEEDORES
    def CargaProveedores(self):
        self.Show_Frame(ProveedoresProg,GoBack_CB=self.CuentasPorPagarMenu)

# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD
# -------------------------------------------------------------------------------------------------
    # PROGRAMAS DE UTILIDAD MENU
    def ProgramasUtilidadMenu(self):
        self.Show_Frame(
                    ProgramasDeUtilidadMenu,
                    GoBack_CB = self.ReturnToDashboard,
                    CargaDolar = self.CargaDolar,
                    GestionUsuarios=self.GestionUsuarios)
                    
    # PROG CARGA DOLAR
    def CargaDolar(self):
        self.Show_Frame(CargaDolar,CargaDolarGoBack_CB=self.ProgramasUtilidadMenu)
        
    # PROG GESTION DE USUARIOS
    def GestionUsuarios(self):
        self.Show_Frame(GestionUsuariosProg,GoBack_CB=self.ProgramasUtilidadMenu)


# -------------------------------------------------------------------------------------------------
# INICIO DE LA APLICACION - INICIO DE LA APLICACION - INICIO DE LA APLICACION
# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    ctk.set_appearance_mode(APPEARANCE_MODE)
    # EJECUTAR LA APP   
    App()