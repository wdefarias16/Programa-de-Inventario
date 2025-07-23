import psycopg2
from tkinter import messagebox

class MasterTable:
    def __init__(self,dbname,user,password,host,port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.ConnectToDB()


    # CONNECT TO DB
    def ConnectToDB(self):
        try:
            self.conn = psycopg2.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )
        except Exception as e:
            messagebox.showerror("Database Connection Error",f"Error conectando a la base de datos: {str(e)}")

    # CREATE TABLE
    def CreateTable(self,table,columns):
        # VALIDATE DB CONNECTION
        if not self.conn:
            messagebox.showerror("Error", "No hay conexión a la base de datos")
            return
        try:
            # SAFE SQL DEFINITION
            columns_sql = ", ".join([f"{key} {value}" for key,value in columns.items()])
            # CREATE TABLE
            with self.conn.cursor() as cur:
                query = f"""CREATE TABLE IF NOT EXISTS {table} ({columns_sql})"""
                cur.execute(query)
                self.conn.commit()
            messagebox.showinfo("Éxito", f"Tabla {table} creada correctamente")
        # FAILED TASK
        except Exception as e:
            self.conn.rollback()
            messagebox.showerror('Error', f"Error al crear la tabla: {str(e)}")