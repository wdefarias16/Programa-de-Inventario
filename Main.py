import customtkinter as ctk
from DashBoard import*
from Login import*
from AjustesInventario_prog import*
from CargaProductos_prog import*
from CargaLineasGrupos_prog import*
from CargaProveedores_prog import*
from Facturacion_prog import*
from MaestroDeTablas_prog import*
from Menu_Inventario import*
from Menu_Facturacion import*
from Menu_CuentasPorPagar import*
from Menu_ProgramasDeUtilidad import*
from EntradaInventario_prog import*
from style import APPEARANCE_MODE
import psycopg2
from psycopg2 import sql

DB_NAME = "AppDatabase"
DB_USER = "postgres"
DB_PASSWORD = "admin1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# VENTANA PRINCIPAL (APLICACION)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema')
        self.geometry('1000x500')
        self.dashboard_activo = False
    # ATAJOS
        # ATAJO CERRAR SESION
        self.winfo_toplevel().bind("<Control-Q>", self.CloseSession)
        self.winfo_toplevel().bind("<Control-q>", self.CloseSession)
        # ATAJO VOLVER AL DASHBOARD
        self.winfo_toplevel().bind("<F4>", self.F4_Pressed)
    # INICIAR EN EL FRAME DE LOGIN
        self.login_frame = LoginFrame(self, success_callback=self.LoginSuccess)
        self.login_frame.pack(expand=True,fill='both')
    # INICIALIZAR EL PROGRAMA ACTIVO COMO NONE
        self.current_prog = None

    # RUN
        self.mainloop()
# BLOQUEO Y DESBLOQUEO DE SESION
    def LoginSuccess(self):
        self.login_frame.destroy()
        self.dashboard=DashBoardMenu(self,
                                 lockscreen_callback = self.LockWindow,
                                 exit_callback = self.Salir,
                                 Inventario_CB= self.InventarioMenu,
                                 Facturacion_CB= self.FacturacionMenu,
                                 CuentasPorPagar_CB=self.CuentasPorPagarMenu,
                                 ProgramasDeUtilidad_CB = self.ProgramasUtilidadMenu)
        self.dashboard.pack(expand=True, fill='both')
        self.dashboard_activo = True
    def LockWindow(self):
        if not self.dashboard_activo:
            return
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.login_frame = LoginFrame(self, success_callback=self.LoginSuccess)
        self.login_frame.pack(expand=True,fill='both')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO
# PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO
# PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO
    # MENU DE INVENTARIO
    def InventarioMenu(self):
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.current_prog = InventarioMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           CargaPro_Prog = self.CargaProductosProg,
                                           Lineas_Prog = self.CargaLineas,
                                           EntradasInv_prog = self.EntradasInventario,
                                           AjustesInv_Prog = self.AjustesInventario)
        self.current_prog.pack(expand=True,fill='both')
    def GoBackInventario(self):
        self.current_prog.destroy()
        self.current_prog = InventarioMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           CargaPro_Prog = self.CargaProductosProg,
                                           Lineas_Prog = self.CargaLineas,
                                           EntradasInv_prog = self.EntradasInventario,
                                           AjustesInv_Prog = self.AjustesInventario)
        self.current_prog.pack(expand=True,fill='both')
    # PROGRAMA DE CARGA DE LINEAS Y GRUPOS
    def CargaLineas(self):
        self.current_prog.destroy()
        self.current_prog = LineasGruposProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')
    # PROGRAMA DE CARGA DE PRODUCTOS
    def CargaProductosProg(self):
        self.current_prog.destroy()
        self.current_prog = CargaProductosProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')
    # ENTRADAS DE INVENTARIO
    def EntradasInventario(self):
        self.current_prog.destroy()
        self.current_prog = EntradasInventarioProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')
    # AJUSTES DE INVENTARIO
    def AjustesInventario(self):
        self.current_prog.destroy()
        self.current_prog = AjustesInventarioProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - 
# PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - 
# PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - PROGRAMAS DE FACTURACION - 
    def FacturacionMenu(self):
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.current_prog = FacturacionMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           FacturacionProg = self.FacturacionProg)
        self.current_prog.pack(expand=True,fill='both')
    def GoBackFacturacion(self):
        self.current_prog.destroy()
        self.current_prog = FacturacionMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           FacturacionProg = self.FacturacionProg)
        self.current_prog.pack(expand=True,fill='both')
    def FacturacionProg(self):
        self.current_prog.destroy()
        self.current_prog = FacturacionProg(self,GoBack_CB=self.GoBackFacturacion)
        self.current_prog.pack(expand=True,fill='both')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - 
# PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - 
# PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - PROGRAMAS DE CUENTAS POR PAGAR - 
    # MENU DE CUENTAS POR PAGAR
    def CuentasPorPagarMenu(self):
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.current_prog = CuentasPorPagarMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           Proveedores_Prog = self.CargaProveedores)
        self.current_prog.pack(expand=True,fill='both')
    def GoBackCuentasPP(self):
        self.current_prog.destroy()
        self.current_prog = CuentasPorPagarMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           Proveedores_Prog = self.CargaProveedores)
        self.current_prog.pack(expand=True,fill='both')
    # PROGRAMA DE CARGA DE PROVEEDORES
    def CargaProveedores(self):
        self.current_prog.destroy()
        self.current_prog = ProveedoresProg(self,GoBack_CB=self.GoBackCuentasPP)
        self.current_prog.pack(expand=True,fill='both')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - 
# PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - 
# PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - PROGRAMAS DE UTILIDAD - 
    # PROGRAMAS DE UTILIDAD MENU
    def ProgramasUtilidadMenu(self):
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.current_prog = ProgramasDeUtilidadMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           MaestroDeTablas = self.MaestroDeTablas)
        self.current_prog.pack(expand=True,fill='both')
    # GO BACJ PDU MENU
    def GoBackProgramasUtilidadMenu(self):
        self.current_prog.destroy()
        self.current_prog = ProgramasDeUtilidadMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           MaestroDeTablas = self.MaestroDeTablas)
        self.current_prog.pack(expand=True,fill='both')
    # PROG MAESTRO DE TABLAS
    def MaestroDeTablas(self):
        self.current_prog.destroy()
        self.current_prog = MaestroDeTablas_prog(self,GoBack_CB=self.GoBackProgramasUtilidadMenu)
        self.current_prog.pack(expand=True,fill='both')
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# REGRESAR AL DASHBOARD
# REGRESAR AL DASHBOARD
# REGRESAR AL DASHBOARD
    def ReturnToDashboard(self):
        self.current_prog.destroy()
        self.dashboard=DashBoardMenu(self,
                                 lockscreen_callback = self.LockWindow,
                                 exit_callback = self.Salir,
                                 Inventario_CB=self.InventarioMenu,
                                 Facturacion_CB=self.FacturacionMenu,
                                 CuentasPorPagar_CB=self.CuentasPorPagarMenu,
                                 ProgramasDeUtilidad_CB = self.ProgramasUtilidadMenu)
        self.dashboard.pack(expand=True, fill='both')
        self.dashboard_activo = True
# SALIR DEL PROGRAMA
# SALIR DEL PROGRAMA
# SALIR DEL PROGRAMA
    def Salir(self):
        answer = messagebox.askyesno('Salir','¿Está seguro que desea salir de la aplicación?')
        if answer:
            self.quit()
# ATAJOS
# ATAJOS
# ATAJOS
    def F4_Pressed(self,event):
        if self.dashboard_activo == False:
            self.ReturnToDashboard()
    def CloseSession(self, event):
        if self.dashboard_activo:
            self.LockWindow()
# INNICIO DE LA APLICACION
# INNICIO DE LA APLICACION
# INNICIO DE LA APLICACION
if __name__ == '__main__':
    ctk.set_appearance_mode(APPEARANCE_MODE)
    # EJECUTAR LA APP   
    App()