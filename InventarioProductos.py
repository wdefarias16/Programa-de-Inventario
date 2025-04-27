import json,os
from tkinter import messagebox

# CLASE PRODUCTOS - CLASE PRODUCTOS - CLASE PRODUCTOS - CLASE PRODUCTOS - CLASE PRODUCTOS - CLASE PRODUCTOS - CLASE PRODUCTOS - 
class Product():
    def __init__(self,codigo,linea,grupo,proveedor,nombre,precio,cantidad):
        self.codigo = codigo
        self.linea = linea
        self.grupo = grupo
        self.proveedor = proveedor
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
# REGRESA EL DICCIONARIO DE UN PRODUCTO
    def ToDict(self):
        return{
            'codigo':self.codigo,
            'linea':self.linea,
            'grupo':self.grupo,
            'proveedor':self.proveedor,
            'nombre':self.nombre,
            'precio':self.precio,
            'cantidad':self.cantidad
        }
# CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - CLASE INVENTARIO - 
class Inventory():
    def __init__(self,filename = 'Data/Inventario.json'):
        self.filename = filename
        self.inventario = {}
        self.Load_Inventory()
# CARGAR EL ARCHIVO DE DATOS
    def Load_Inventory(self):
        global Inventario
    # CREAR LA CARPETA DATA SI NO EXISTE
        if not os.path.exists('Data'):  
            os.makedirs('Data')
    # VERIFICAR SI EXISTE EL ARCHIVO DE DATOS / CARGAR EL ARCHIVO DE DATOS
        try:
            with open(self.filename,'r') as file:
                self.inventario = json.load(file)
        except FileNotFoundError:
            self.Save_Inventory()
# GUARDAR EL ARCHIVO DE DATOS
    def Save_Inventory(self):
        with open(self.filename,'w') as file:
            json.dump(self.inventario,file,indent=4)
# AGREGAR PRODUCTO
    def AddProduct(self,product):
        if product['codigo'] in self.inventario:
            messagebox.showinfo('Producto existente',f"El producto con el codigo {product['codigo']} ya existe.")
            return
        elif product['codigo'] == '':
            messagebox.showerror('Error',f"Agregue un codigo de producto.")
        else:
            self.inventario[product['codigo']] = product
            self.Save_Inventory()
            messagebox.showinfo('Producto agregado',f"El producto {product['codigo']} ha sido agregado.")
# EDITAR PRODUCTO
    def EditProduct(self,product):
        if product['codigo'] in self.inventario:
            self.inventario[product['codigo']] = product
            self.Save_Inventory()
            messagebox.showinfo('Producto modificado',f"El producto {product['codigo']} ha sido modificado.")
# BORRAR PRODUCTO
    def DelProduct(self,codigo):
        if codigo in self.inventario:
            del self.inventario[codigo]
            self.Save_Inventory()
            messagebox.showinfo('Producto Eliminado',"El producto ha sido Eliminado.")
# OBTENER EL INVENTARIO
    def GetInventory(self):
        return self.inventario
# VERIFICAR EXITENCIA DE CCODIGO
    def CheckCode(self,codigo):
        if codigo not in self.inventario:
            return True
        else:
            messagebox.showerror('Error',f'El codigo {codigo}, ya se encuentra en la base de datos.')
            return False
    def CheckName(self,name):
        if name == '':
            messagebox.showerror('Error',f'Ingrese un nombre de producto')
            return False
        else:
            return True