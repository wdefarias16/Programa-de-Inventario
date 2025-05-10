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
        return [f"{codigo} - {info['nombre']}" for codigo, info in self.proveedores.items()]
# OBTENER TODOS LOS PROVEEDORES
    def GetProv(self):
        return self.proveedores
# BUSCAR UN PROVEEDOR POR CODIGO
    def BuscarProv(self,codigo):
        if codigo not in self.proveedores:
            messagebox.showerror('Error de busqueda',f'El proveedor con codigo {codigo} no existe')
        else:
            proveedor = self.proveedores[codigo]
            return proveedor
# BUSCAR PROVEEDORES POR NOMBRES
    def BuscarNombres(self,busqueda):
        resultados = [
        proveedor for proveedor in self.proveedores.values()
        if busqueda in proveedor["nombre"].lower()]
        return resultados
# AGREGAR PROVEEDOR
    def Add_Prov(self,codigo,nombre,contacto='',direccion1='',direccion2='',
                 ciudad='',telefono='',celular='',email='',rif=''):
        if codigo in self.proveedores:
            messagebox.showerror('Error',f'El proveedor {codigo} ya se encuentra en la base de datos')
            return False
        self.proveedores[codigo]={'codigo':codigo,
                                  'nombre': nombre,
                                  'contacto': contacto,
                                  'direccion1':direccion1,
                                  'direccion2':direccion2,
                                  'ciudad':ciudad,
                                  'telefono':telefono,
                                  'celular':celular,
                                  'email':email,
                                  'rif':rif}
        self.Save_Prov()
        messagebox.showinfo('Info',f'El proveedor {codigo} - {nombre} se ha cargado correctamente')
        return True
# MODIFICAR PROVEEDOR
    def Mod_Prov(self,codigo,nombre,contacto='',direccion1='',direccion2='',
                 ciudad='',telefono='',celular='',email='',rif=''):
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea modificar el proveedor {codigo} con estos datos?')
        if answer:
            self.proveedores[codigo]={'nombre': nombre,
                                  'contacto': contacto,
                                  'direccion1':direccion1,
                                  'direccion2':direccion2,
                                  'ciudad':ciudad,
                                  'telefono':telefono,
                                  'celular':celular,
                                  'email':email,
                                  'rif':rif}
            self.Save_Prov()
            messagebox.showinfo('Info',f'El proveedor {codigo} ha sido modificado.')
# ELIMINAR PROVEEDOR
    def Del_Prov(self,codigo):
        answer = messagebox.askyesno('¡Atención!',f'¿Está seguro que desea eliminar el proveedor {codigo}?')
        if answer:
            if codigo in self.proveedores:
                del self.proveedores[codigo]
            self.Save_Prov()
            messagebox.showinfo('Info',f'El proveedor {codigo} ha sido eliminado.')
# CHEQUEAR UN PROVEEDOR
    def ChechProv(self,codigo):
        if codigo in self.proveedores:
            return True
        else:
            messagebox.showerror('Error',f'Agregue un codigo de proveedor válido.')