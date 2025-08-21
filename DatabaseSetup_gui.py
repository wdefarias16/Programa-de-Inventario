import customtkinter as ctk
import psycopg2
from psycopg2 import sql

# Parámetros de conexión
DB_NAME = "AppDatabase"
DB_USER = "postgres"
DB_PASSWORD = "admin1234"
DB_HOST = "localhost"
DB_PORT = "5432"

# Lista con nombres de tablas por defecto (según el ejemplo original)
default_tables = [
    "proveedores", "lineas", "grupos", "productos",
    "roles", "usuarios", "entradas_inventario", "detalle_entrada"
]

class DatabaseManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Base de Datos")
        self.geometry("800x600")

        # Crear un Tabview para separar la gestión de base de datos y la de tablas.
        self.tabview = ctk.CTkTabview(self, width=780, height=300)
        self.tabview.pack(pady=20, padx=10)
        self.tabview.add("Base de Datos")
        self.tabview.add("Tablas")

        # Configuración de la pestaña "Base de Datos"
        self.setup_db_tab()

        # Configuración de la pestaña "Tablas"
        self.setup_table_tab()

        # Área para mostrar resultados y mensajes (log)
        self.log_box = ctk.CTkTextbox(self, height=200)
        self.log_box.pack(pady=10, padx=10, fill="both", expand=True)
        self.log("Aplicación iniciada.")

    def log(self, message: str):
        """Añade un mensaje al log."""
        self.log_box.configure(state="normal")
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def setup_db_tab(self):
        """Configura la pestaña de gestión de la base de datos."""
        tab = self.tabview.tab("Base de Datos")
        # Botón para crear la base de datos
        self.create_db_button = ctk.CTkButton(tab, text="Crear Base de Datos", command=self.create_database)
        self.create_db_button.grid(row=0, column=0, padx=10, pady=10)

        # Botón para inicializar las tablas (cargar la estructura)
        self.init_tables_button = ctk.CTkButton(tab, text="Inicializar Tablas", command=self.init_tables)
        self.init_tables_button.grid(row=0, column=1, padx=10, pady=10)

        # Botón para eliminar la base de datos
        self.drop_db_button = ctk.CTkButton(tab, text="Eliminar Base de Datos", command=self.drop_database)
        self.drop_db_button.grid(row=0, column=2, padx=10, pady=10)

    def setup_table_tab(self):
        """Configura la pestaña de gestión de tablas (crear, eliminar y editar)."""
        tab = self.tabview.tab("Tablas")

        # --- Sección para crear una nueva tabla ---
        create_frame = ctk.CTkFrame(tab)
        create_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        create_label = ctk.CTkLabel(create_frame, text="Crear Tabla (SQL):")
        create_label.pack(padx=5, pady=5)
        # Caja de texto para comandar SQL (puede ser un CREATE TABLE completo)
        self.create_sql_textbox = ctk.CTkTextbox(create_frame, height=100)
        self.create_sql_textbox.pack(padx=5, pady=5, fill="x")
        self.create_table_button = ctk.CTkButton(create_frame, text="Ejecutar Creación", command=self.create_table_from_text)
        self.create_table_button.pack(padx=5, pady=5)

        # --- Sección para eliminar una tabla existente ---
        delete_frame = ctk.CTkFrame(tab)
        delete_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        delete_label = ctk.CTkLabel(delete_frame, text="Eliminar Tabla:")
        delete_label.pack(padx=5, pady=5)
        self.delete_table_option = ctk.CTkOptionMenu(delete_frame, values=default_tables)
        self.delete_table_option.pack(padx=5, pady=5)
        self.delete_table_button = ctk.CTkButton(delete_frame, text="Eliminar Tabla", command=self.delete_table)
        self.delete_table_button.pack(padx=5, pady=5)

        # --- Sección para editar una tabla (ejecutar comandos ALTER TABLE, etc.) ---
        edit_frame = ctk.CTkFrame(tab)
        edit_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        edit_label = ctk.CTkLabel(edit_frame, text="Editar Tabla (SQL, e.g. ALTER TABLE):")
        edit_label.pack(padx=5, pady=5)
        self.edit_table_option = ctk.CTkOptionMenu(edit_frame, values=default_tables)
        self.edit_table_option.pack(padx=5, pady=5)
        self.edit_sql_textbox = ctk.CTkTextbox(edit_frame, height=100)
        self.edit_sql_textbox.pack(padx=5, pady=5, fill="x")
        self.edit_table_button = ctk.CTkButton(edit_frame, text="Ejecutar Edición", command=self.edit_table)
        self.edit_table_button.pack(padx=5, pady=5)

    def create_database(self):
        """Crea la base de datos si no existe."""
        try:
            conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD,
                                    host=DB_HOST, port=DB_PORT)
            conn.autocommit = True  # Es imprescindible para CREATE DATABASE
            cursor = conn.cursor()
            cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME])
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
                self.log(f"La base de datos '{DB_NAME}' ha sido creada exitosamente.")
            else:
                self.log(f"La base de datos '{DB_NAME}' ya existe.")
            cursor.close()
            conn.close()
        except Exception as e:
            self.log(f"Error al crear la base de datos: {repr(e)}")

    def drop_database(self):
        """Elimina la base de datos de forma segura."""
        try:
            conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD,
                                    host=DB_HOST, port=DB_PORT)
            conn.autocommit = True
            cursor = conn.cursor()
            # Se utiliza DROP DATABASE IF EXISTS para evitar errores si no existe
            cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(DB_NAME)))
            self.log(f"La base de datos '{DB_NAME}' ha sido eliminada exitosamente.")
            cursor.close()
            conn.close()
        except Exception as e:
            self.log(f"Error al eliminar la base de datos: {repr(e)}")

    def init_tables(self):
        """Inicializa (crea) las tablas dentro de la base de datos."""
        try:
            with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                  host=DB_HOST, port=DB_PORT) as conn:
                with conn.cursor() as cursor:
                    statements = [
                        # MASTER TABLE
                        """CREATE TABLE master_table (
                            table_id SERIAL PRIMARY KEY,
                            table_name TEXT UNIQUE NOT NULL
                        )""",
                        '''CREATE TABLE dolar (
                            codigo SERIAL PRIMARY KEY,
                            fecha DATE NOT NULL,
                            tasa DECIMAL(12, 4) NOT NULL,
                            log TEXT,
                            hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )''',
                        # Tabla proveedores
                        """CREATE TABLE IF NOT EXISTS proveedores (
                            codigo SERIAL PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            contacto VARCHAR(255),
                            direccion1 TEXT,
                            direccion2 TEXT,
                            ciudad VARCHAR(100),
                            telefono1 VARCHAR(50),
                            telefono2 VARCHAR(50),
                            celular1 VARCHAR(50),
                            celular2 VARCHAR(50),
                            email VARCHAR(255),
                            rif VARCHAR(50) NOT NULL
                        )""",
                        # Tabla lineas
                        """CREATE TABLE IF NOT EXISTS lineas (
                            codigo SERIAL PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL
                        )""",
                        # Tabla grupos
                        """CREATE TABLE IF NOT EXISTS grupos (
                            codigo VARCHAR(10) PRIMARY KEY,
                            linea INT REFERENCES lineas(codigo),
                            nombre VARCHAR(255) NOT NULL,
                            porcentaje1 NUMERIC(10,2),
                            porcentaje2 NUMERIC(10,2),
                            porcentaje3 NUMERIC(10,2)
                        )""",
                        # Tabla productos
                        """CREATE TABLE IF NOT EXISTS productos (
                            codigo VARCHAR(255) PRIMARY KEY,
                            linea INT REFERENCES lineas(codigo),
                            grupo VARCHAR(10) REFERENCES grupos(codigo),
                            proveedor INT REFERENCES proveedores(codigo),
                            nombre VARCHAR(255) NOT NULL,
                            costo NUMERIC(10,2),
                            ubicacion1 VARCHAR(50),
                            ubicacion2 VARCHAR(50),
                            precio1 NUMERIC(10,2),
                            precio2 NUMERIC(10,2),
                            precio3 NUMERIC(10,2),
                            existencia INT DEFAULT 0,
                            image TEXT
                        )""",
                        # Tabla roles
                        """CREATE TABLE IF NOT EXISTS roles (
                            codigo SERIAL PRIMARY KEY,
                            rol VARCHAR(50) UNIQUE NOT NULL
                        )""",
                        # Insertar roles (agregamos ON CONFLICT DO NOTHING para evitar duplicados)
                        """INSERT INTO roles (rol) 
                           VALUES ('Administrador'), ('Supervisor'), ('Gerente'), ('Vendedor')
                           ON CONFLICT DO NOTHING""",
                        # Tabla usuarios
                        """CREATE TABLE IF NOT EXISTS usuarios (
                            codigo SERIAL PRIMARY KEY,
                            nombre VARCHAR(100) NOT NULL,
                            usuario VARCHAR(100) NOT NULL,
                            clave VARCHAR(255) NOT NULL,
                            opcode INT NOT NULL,
                            correo VARCHAR(255) UNIQUE,
                            rol INT NOT NULL,
                            estado BOOLEAN DEFAULT TRUE,
                            FOREIGN KEY (rol) REFERENCES roles(codigo) ON DELETE RESTRICT 
                        )""",
                        # TABLA CLIENTES
                        """CREATE TABLE IF NOT EXISTS clientes(
                            codigo SERIAL PRIMARY KEY,
                            nombre VARCHAR(100) NOT NULL,
                            id_fiscal VARCHAR(50) NOT NULL,
                            telefono VARCHAR(50),
                            direccion1 TEXT,
                            direccion2 TEXT,
                            ciudad VARCHAR(50),
                            email VARCHAR(100)
                        )""",
                        # TABLA ENTRADAS INVENTARIO
                        """CREATE TABLE IF NOT EXISTS entradas_inventario (
                            id SERIAL PRIMARY KEY,
                            num_factura VARCHAR(50) NOT NULL,
                            proveedor   INT     NOT NULL REFERENCES proveedores(codigo),
                            fecha       DATE    NOT NULL,
                            total       NUMERIC(12,2) NOT NULL,
                            created_at  TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
                        )""",
                        # TABLA DETALLES DE ENTRADA A INVENTARIO
                        """CREATE TABLE IF NOT EXISTS detalle_entrada (
                            id          SERIAL PRIMARY KEY,
                            entrada_id  INTEGER     NOT NULL
                                           REFERENCES entradas_inventario(id) ON DELETE CASCADE,
                            codigo      VARCHAR(255) NOT NULL
                                           REFERENCES productos(codigo),
                            cantidad    INTEGER     NOT NULL,
                            costo       NUMERIC(12,2) NOT NULL,
                            descuento1  NUMERIC(5,2)  DEFAULT 0,
                            descuento2  NUMERIC(5,2)  DEFAULT 0,
                            descuento3  NUMERIC(5,2)  DEFAULT 0,
                            flete       NUMERIC(5,2)  DEFAULT 0,
                            iva         NUMERIC(5,2)  DEFAULT 0,
                            neto        NUMERIC(12,2) NOT NULL,
                            neto_iva    NUMERIC(12,2) NOT NULL,
                            subtotal    NUMERIC(12,2) NOT NULL
                        )""",
                        # TABLA AJUSTES INVENTARIO
                        """CREATE TABLE IF NOT EXISTS ajustes_inventario (
                            id SERIAL PRIMARY KEY,
                            num_documento VARCHAR(50) NOT NULL UNIQUE,
                            log TEXT,
                            fecha DATE NOT NULL
                        )""",
                        # TABLA DETALLES DE AJUSTES A INVENTARIO
                        """CREATE TABLE IF NOT EXISTS detalle_ajustes (
                            id SERIAL PRIMARY KEY,
                            ajuste_id INTEGER NOT NULL
                              REFERENCES ajustes_inventario(id) ON DELETE CASCADE,
                            codigo VARCHAR(255) NOT NULL
                              REFERENCES productos(codigo),
                            cantidad INTEGER NOT NULL,
                            ajuste INTEGER NOT NULL,
                            final INTEGER NOT NULL
                        )""",

                        # INSERT TABLES IN MASTER TABLE
                        """INSERT INTO master_table (table_name)
                        VALUES ('proveedores'),
                               ('lineas'),
                               ('grupos'),
                               ('productos'),
                               ('roles'),
                               ('usuarios'),
                               ('entradas_inventario'),
                               ('detalle_entrada'),
                               ('ajustes_inventario'),
                               ('detalle_ajustes')
                        """
                    ]
                    for stmt in statements:
                        cursor.execute(stmt)
                    conn.commit()
                    self.log("Tablas inicializadas correctamente.")
        except Exception as e:
            self.log(f"Error al inicializar las tablas: {repr(e)}")

    def create_table_from_text(self):
        """Ejecuta el comando SQL ingresado para crear una tabla."""
        sql_command = self.create_sql_textbox.get("1.0", "end").strip()
        if not sql_command:
            self.log("Por favor, ingrese un comando SQL para crear una tabla.")
            return
        try:
            with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                  host=DB_HOST, port=DB_PORT) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_command)
                conn.commit()
            self.log("Tabla creada exitosamente.")
        except Exception as e:
            self.log(f"Error al crear la tabla: {repr(e)}")

    def delete_table(self):
        """Elimina la tabla seleccionada."""
        table_name = self.delete_table_option.get()
        if not table_name:
            self.log("Seleccione una tabla para eliminar.")
            return
        try:
            with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                  host=DB_HOST, port=DB_PORT) as conn:
                with conn.cursor() as cursor:
                    query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table_name))
                    cursor.execute(query)
                conn.commit()
            self.log(f"La tabla '{table_name}' ha sido eliminada exitosamente.")
        except Exception as e:
            self.log(f"Error al eliminar la tabla: {repr(e)}")

    def edit_table(self):
        """Ejecuta el comando SQL ingresado para editar (alterar) la estructura de una tabla."""
        table_name = self.edit_table_option.get()
        sql_command = self.edit_sql_textbox.get("1.0", "end").strip()
        if not table_name or not sql_command:
            self.log("Seleccione una tabla y escriba el comando SQL para editarla.")
            return
        try:
            with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                                  host=DB_HOST, port=DB_PORT) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_command)
                conn.commit()
            self.log(f"Tabla '{table_name}' editada exitosamente.")
        except Exception as e:
            self.log(f"Error al editar la tabla: {repr(e)}")

if __name__ == "__main__":
    app = DatabaseManagerApp()
    app.mainloop()