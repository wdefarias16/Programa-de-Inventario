import json,os
from tkinter import messagebox



# CLASE PRODUCTOS
class Product():
    def __init__(self,codigo,linea,grupo,proveedor,nombre,precio,cantidad):

        self.codigo = codigo
        self.linea = linea
        self.grupo = grupo
        self.proveedor = proveedor
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
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

# CLASE INVENTARIO
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

    def AddProduct(self,product):

        if product['codigo'] in self.inventario:
            messagebox.showinfo('Producto existente',f"El producto con el codigo {product['codigo']} ya existe.")
            return
         
        self.inventario[product['codigo']] = product
        self.Save_Inventory()
        messagebox.showinfo('Producto agregado',f"El producto {product['codigo']} ha sido agregado.")

# OBTENER EL INVENTARIO
    def GetInventory(self):
        return self.inventario