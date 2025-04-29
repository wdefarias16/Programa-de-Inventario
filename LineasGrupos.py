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
                self.lineas_grupos = {"001": {"linea": "Linea 1",
                                              "grupos": {"G001": {"nombre_grupo": "Grupo 1",
                                                                  "porcentaje_1": 0.0,
                                                                  "porcentaje_2": 0.0,
                                                                  "porcentaje_3": 0.0}}}}
                self.Save_Lines()
        else:
            self.Load_Lines()
            if "001" not in self.lineas_grupos:
                self.lineas_grupos["001"] = {"001": {"linea": "Linea 1",
                                              "grupos": {"G001": {"nombre_grupo": "Grupo 1",
                                                                  "porcentaje_1": 0.0,
                                                                  "porcentaje_2": 0.0,
                                                                  "porcentaje_3": 0.0}}}}
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
            self.lineas_grupos = {"001": {"linea": "Linea 1",
                                              "grupos": {"G001": {"nombre_grupo": "Grupo 1",
                                                                  "porcentaje_1": 0.0,
                                                                  "porcentaje_2": 0.0,
                                                                  "porcentaje_3": 0.0}}}}
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
    def GetGroupNames(self, codigo):
        lista_grupos = []
        linea_data = self.lineas_grupos.get(codigo, {})
        grupos = linea_data.get("grupos", {})
        for grupo_id, grupo_data in grupos.items():
            nombre_grupo = grupo_data.get("nombre_grupo", "Sin Nombre")
            lista_grupos.append(f"{grupo_id} - {nombre_grupo}")
        return lista_grupos
    def GetPorcentajes(self,linea,grupo):
        porcentajes = self.lineas_grupos[linea]['grupos'][grupo]
        return porcentajes
    
# AGREGA UNA LINEA A LA BASE DE DATOS
    def Add_Line(self,codigo,linea,grupos=None):
        if codigo in self.lineas_grupos:
            messagebox.showerror('Error',f'El codigo de línea {codigo} ya se encuentra en la base de datos')
            return False
        if grupos is None:
            grupos = {}
        self.lineas_grupos[codigo]={'linea': linea,'grupo': grupos}
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
    def Add_Group(self, codigo, grupo_id, nombre_grupo, porcentaje_1, porcentaje_2, porcentaje_3):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error', f'La línea con código {codigo} no existe')
            return False
    
        grupos = self.lineas_grupos[codigo].get('grupos', {})
        if grupo_id in grupos:
            messagebox.showerror('Error', f'El grupo con código {grupo_id} ya existe en la línea {codigo}')
            return False
    
        # Agregar el nuevo grupo
        grupos[grupo_id] = {"nombre_grupo": nombre_grupo,
                            "porcentaje_1": porcentaje_1,
                            "porcentaje_2": porcentaje_2,
                            "porcentaje_3": porcentaje_3}
        self.lineas_grupos[codigo]['grupos'] = grupos
        self.Save_Lines()
        messagebox.showinfo('Info', f'El grupo {grupo_id} - {nombre_grupo} se ha agregado correctamente a la línea {codigo}')
        return True

# MODIFICA UN GRUPO
    def Mod_Grupo(self, codigo,grupo_id,nuevo_nombre,porcentaje_1,porcentaje_2,porcentaje_3):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error', f'La línea con código {codigo} no existe')
            return False
        grupos = self.lineas_grupos[codigo].get('grupos', {})
        if grupo_id not in grupos:
            messagebox.showerror('Error', f'El grupo con código {grupo_id} no existe en la línea {codigo}')
            return False
        grupos[grupo_id]["nombre_grupo"] = nuevo_nombre
        grupos[grupo_id]["porcentaje_1"] = porcentaje_1
        grupos[grupo_id]["porcentaje_2"] = porcentaje_2
        grupos[grupo_id]["porcentaje_3"] = porcentaje_3
        self.Save_Lines()
        messagebox.showinfo('Info', f'El grupo {grupo_id} ha sido modificado correctamente en la línea {codigo}')
        return True
# ELIMINA UN GRUPO
    def Del_Group(self, codigo, grupo_id):
        if codigo not in self.lineas_grupos:
            messagebox.showerror('Error', f'La línea con código {codigo} no existe')
            return False
    
        grupos = self.lineas_grupos[codigo].get('grupos', {})
        if grupo_id not in grupos:
            messagebox.showerror('Error', f'El grupo con código {grupo_id} no existe en la línea {codigo}')
            return False
    
    # Eliminar el grupo
        del grupos[grupo_id]
        self.lineas_grupos[codigo]['grupos'] = grupos  # Actualizamos la estructura de grupos

        self.Save_Lines()
        messagebox.showinfo('Info', f'El grupo {grupo_id} ha sido eliminado correctamente de la línea {codigo}')
        return True

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