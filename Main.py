import customtkinter as ctk
from DashBoard import*
from Login import*
from CargaProductos import*
from CargaLineasGrupos import*
from CargaProveedores import*
from InventarioMenu2 import*
from EntradaInventarios import*
from style import FONTS, APP_COLORS, APPEARANCE_MODE

# VENTANA PRINCIPAL (APLICACION)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema')
        self.geometry('1000x500')
        self.dashboard_activo = False
    # ATAJOS
        # ATAJO CERRAR SESION
        self.winfo_toplevel().bind("<Control-Q>", self.ctrl_q_callback)
        self.winfo_toplevel().bind("<Control-q>", self.ctrl_q_callback)
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
        self.dashboard=MainFrame(self,
                                 lockscreen_callback = self.LockWindow,
                                 exit_callback = self.Salir,
                                 Inventario_CB=self.InventarioMenu)
        self.dashboard.pack(expand=True, fill='both')
        self.dashboard_activo = True
    def LockWindow(self):
        if not self.dashboard_activo:
            return
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.login_frame = LoginFrame(self, success_callback=self.LoginSuccess)
        self.login_frame.pack(expand=True,fill='both')
# PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO - PROGRAMAS DE INVENTARIO
    # MENU DE INVENTARIO
    def InventarioMenu(self):
        self.dashboard.destroy()
        self.dashboard_activo = False
        self.current_prog = InventarioMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           CargaPro_Prog = self.CargaProductosProg,
                                           Lineas_Prog = self.CargaLineas,
                                           Proveedores_Prog = self.CargaProveedores,
                                           EntradasInv_prog = self.EntradasInventario)
        self.current_prog.pack(expand=True,fill='both')
    def GoBackInventario(self):
        self.current_prog.destroy()
        self.current_prog = InventarioMenu(self,
                                           GoBack_CB = self.ReturnToDashboard,
                                           CargaPro_Prog = self.CargaProductosProg,
                                           Lineas_Prog = self.CargaLineas,
                                           Proveedores_Prog = self.CargaProveedores,
                                           EntradasInv_prog = self.EntradasInventario)
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
    # PROGRAMA DE CARGA DE PROVEEDORES
    def CargaProveedores(self):
        self.current_prog.destroy()
        self.current_prog = ProveedoresProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')
    # ENTRADAS DE INVENTARIO
    def EntradasInventario(self):
        self.current_prog.destroy()
        self.current_prog = EntradasInventarioProg(self,GoBack_CB=self.GoBackInventario)
        self.current_prog.pack(expand=True,fill='both')

# REGRESAR AL DASHBOARD
    def ReturnToDashboard(self):
        self.current_prog.destroy()
        self.dashboard=MainFrame(self,lockscreen_callback = self.LockWindow,
                                 exit_callback = self.Salir,
                                 Inventario_CB=self.InventarioMenu)
        self.dashboard.pack(expand=True, fill='both')
        self.dashboard_activo = True
# SALIR DEL PROGRAMA
    def Salir(self):
        answer = messagebox.askyesno('Salir','¿Está seguro que desea salir de la aplicación?')
        if answer:
            self.quit()
# ATAJOS
    def F4_Pressed(self,event):
        if self.dashboard_activo == False:
            self.ReturnToDashboard()
    def ctrl_q_callback(self, event):
        if self.dashboard_activo:
            self.LockWindow()
# INNICIO DE LA APLICACION
if __name__ == '__main__':
    ctk.set_appearance_mode(APPEARANCE_MODE)
    # EJECUTAR LA APP   
    App()