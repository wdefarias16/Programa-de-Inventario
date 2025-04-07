import customtkinter as ctk
from ProductDataBase import*
from DashBoard import*
from Login import*


fonts = [('Roboto light',25),('Roboto light',15)]
app_colors = ['#eaeaea','#1d1d1d','#1c9bac','#166c78','#5d5d5d']
ctk.set_appearance_mode('light')



# VENTANA PRINCIPAL (APLICACION)
class App(ctk.CTk):
    def __init__(self): 
        super().__init__()

        self.title('Sistema')
        self.geometry('1000x500')
    
        # FRAME DE LOGIN
        self.login_frame = LoginFrame(self, success_callback=self.LoginSuccess)
        self.login_frame.pack(expand=True,fill='both')

        # RUN
        self.mainloop()

    def LoginSuccess(self):
        self.login_frame.destroy()
        self.dashboard=MainFrame(self,lockscreen_callback = self.LockWindow)
        self.dashboard.pack(expand=True, fill='both')

    def LockWindow(self):
        self.dashboard.destroy()
        self.login_frame = LoginFrame(self, success_callback=self.LoginSuccess)
        self.login_frame.pack(expand=True,fill='both')

    def Salir(self):
        pass

if __name__ == '__main__':
    inv = Inventory()
    Load_Inventory()
    
    # INICIALIZAR LOS ARCHIVOS
    ReadUsersData()
    # EJECUTAR LA APP   
    App()