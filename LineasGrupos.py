from tkinter import messagebox
import json,os

# CLASE DE LINEAS Y GRUPOS - CLASE DE LINEAS Y GRUPOS - CLASE DE LINEAS Y GRUPOS - CLASE DE LINEAS Y GRUPOS - CLASE DE LINEAS Y GRUPOS - 
class LineasGrupos():
    def __init__(self,filename = 'Data/Lineas.json'):
        self.filename = filename
        self.lineas_grupos = {}
        self.Iniciar_File()
# INICIA EL ARCHIVO CON UN VALOR NEUTRAL
    def Iniciar_File(self):
        if not os.path.exists('Data'):
            os.makedirs('Data')
        if not os.path.exists(self.filename):            
                self.lineas_grupos = {
                    "000": {"linea": "sin linea", "grupo":[]}
                }
                self.Save_Lines()
        else:
            self.Load_Lines()
            if "000" not in self.lineas_grupos:
                self.lineas_grupos["000"] = {"linea": "sin linea", "grupo":[]}
                self.Save_Lines()
# CARGAR EL ARCHIVO DE DATOS
    def Load_Lines(self):
    # CREAR LA CARPETA DATA SI NO EXISTE
        if not os.path.exists('Data'):
            os.makedirs('Data')
    # VERIFICAR SI EXISTE EL ARCHIVO DE DATOS / CARGAR EL ARCHIVO DE DATOS
        try:
            with open(self.filename,'r') as file:
                self.lineas_grupos = json.load(file)
        except FileNotFoundError:
            self.lineas_grupos={}
            self.Save_Lines()
        except json.JSONDecodeError as e:
            messagebox.showerror("Error JSON", f"Error al leer el archivo JSON: {e}")
            self.lineas_grupos = {"000": {"linea": "sin linea", "grupo":[]}}
            self.Save_Lines()
# GUARDAR EL ARCHIVO DE DATOS
    def Save_Lines(self):
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(self.filename, 'w') as file:
            json.dump(self.lineas_grupos, file, indent=4)
# RETORNA LOS NOMBRES DE LINEA EN FORMATO (CODIGO - NOMBRE)
    def GetLineNames(self):
        return [f"{codigo} - {info['linea']}" for codigo, info in self.lineas_grupos.items()]
# RETORNA LOS GRUPOS DE UNA LINEA
    def GetGroupNames(self,codigo):
        grupos=[]
        linea = self.lineas_grupos[codigo]
        for grupo in linea['grupo']:
            grupos.append(grupo)
        return grupos    
# AGREGA UNA LINEA A LA BASE DE DATOS
    def Add_Line(self,codigo,linea,grupo=None):
        if codigo in self.lineas_grupos:
            messagebox.showerror('Error',f'El codigo de línea {codigo} ya se encuentra en la base de datos')
            return False
        if grupo is None:
            grupo = []
        self.lineas_grupos[codigo]={'linea': linea,'grupo': grupo}
        self.Save_Lines()
        messagebox.showinfo('Info',f'La linea {codigo} se ha cargado correctamente')
        return True
# MODIFICA UNA LINEA
    def Mod_Linea(self,codigo,linea):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error',f'No se encontro la linea {codigo}.')
        self.lineas_grupos[codigo]['linea'] = linea
        self.Save_Lines()
        messagebox.showinfo('Info',f'La linea {codigo} se editado correctamente')
# ELIMINA UNA LINEA
    def Del_Linea(self,codigo):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error',f'No se encontro la linea {codigo}.')
        del self.lineas_grupos[codigo]
        self.Save_Lines()
        messagebox.showinfo('Info',f'La linea {codigo} ha sido eliminada')
# AGREGA UN GRUPO A LA BASE DE DATOS
    def Add_Group(self,codigo,grupo):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error',f'La línea con codigo {codigo} no existe')
            return False
        self.lineas_grupos[codigo]['grupo'].append(grupo)
        self.Save_Lines()
        messagebox.showinfo('Info',f'El grupo {grupo} se ha cargado correctamente a la linea {codigo}')
        return True
# MODIFICA UN GRUPO
    def Mod_Grupo(self,codigo,nuevo_g,antiguo_g):
        grupos = self.lineas_grupos[codigo]['grupo']
        for i in range(len(grupos)):
            if grupos[i] == antiguo_g:
                grupos[i] = nuevo_g
                break
        self.Save_Lines()
        messagebox.showinfo('Info',f'El grupo {antiguo_g} ha sido modificado a {nuevo_g}')
# ELIMINA UN GRUPO
    def Eliminar_Grupo(self,codigo,grupo):
        grupos = self.lineas_grupos[codigo]['grupo']
        if grupo in grupos:
            grupos.remove(grupo)
        self.Save_Lines()
        messagebox.showinfo('Info',f'El grupo {grupo} ha sido eliminado')
# CHEQUEA SI EL CODIGO DE LINEA PERTENECE A LA ALGUNA PREVIAMENTE CARGADA
    def CheckLine(self,codigo):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error de Línea',f'El codigo {codigo} no pertenece a ninguna linea cargada.')
            return False
        return True
# CHEQUEA SI EL GRUPO PERTENECE A LA LINEA
    def CheckGrupo(self,codigo,grupo):    
        if grupo in self.lineas_grupos[codigo]['grupo']:
            return True
        messagebox.showerror('Error de carga', f'El grupo {grupo} no pertenece a la línea {codigo}.')
        return False