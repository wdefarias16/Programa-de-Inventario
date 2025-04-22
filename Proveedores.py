from tkinter import messagebox
import json,os

# CLASE PROVEEDORES
class Proveedores():
    def __init__(self,filename = 'Data/Proveedores.json'):
        self.filename = filename
        self.proveedores = {}
        self.Load_Prov()
 # CARGAR EL ARCHIVO DE DATOS
    def Load_Prov(self):
    # CREAR LA CARPETA DATA SI NO EXISTE
        if not os.path.exists('Data'):
            os.makedirs('Data')
    # VERIFICAR SI EXISTE EL ARCHIVO DE DATOS / CARGAR EL ARCHIVO DE DATOS
        try:
            with open(self.filename,'r') as file:
                self.proveedores = json.load(file)
        except FileNotFoundError:
            self.proveedores={}
            self.Save_Prov()
# GUARDAR EL ARCHIVO DE DATOS
    def Save_Prov(self):
        with open(self.filename,'w') as file:
            json.dump(self.proveedores,file,indent=4)
# OBTENER TODOS LOS NOMBRES DE PROVEEDORES EN FORMATO (CODIGO - NOMBRE)
    def GetProvNames(self):
        return [f"{codigo} - {info['proveedor']}" for codigo, info in self.proveedores.items()]
# AGREGAR PROVEEDOR
    def Add_Prov(self,codigo,nombre):
        if codigo in self.proveedores:
            messagebox.showerror('Error',f'El proveedor {codigo} ya se encuentra en la base de datos')
            return False
        self.proveedores[codigo]={'proveedor': nombre}
        self.Save_Prov()
        messagebox.showinfo('Info',f'El proveedor {codigo} se ha cargado correctamente')
        return True