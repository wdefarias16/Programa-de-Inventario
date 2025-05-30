import psycopg2
from psycopg2 import sql

# DETALLES DE CONEXIÓN
DB_NAME = "AppDatabase"
DB_USER = "postgres"
DB_PASSWORD = "admin1234"
DB_HOST = "localhost"
DB_PORT = "5432"

def CreateDatabase():
    try:
        # Abrimos la conexión de forma manual para evitar el bloque de transacción del "with"
        conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, 
                                host=DB_HOST, port=DB_PORT)
        conn.autocommit = True  # Esto es imprescindible para CREATE DATABASE
        
        cursor = conn.cursor()
        # Verificar si la base de datos ya existe
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME])
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"La base de datos '{DB_NAME}' ha sido creada exitosamente.")
            cursor.close()
            conn.close()
            # Inicializar las tablas una vez creada la base de datos
        else:
            print(f"La base de datos '{DB_NAME}' ya existe.")
            cursor.close()
            conn.close()
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {repr(e)}")

def InitTables():
    try:
        # Usamos with para la conexión en InitTables, ya que CREATE TABLE sí se puede ejecutar en un bloque de transacción
        with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                              host=DB_HOST, port=DB_PORT) as conn:
            with conn.cursor() as cursor:
                statements = [
                    # PROVEEDORES
                    """CREATE TABLE proveedores (
                        codigo SERIAL PRIMARY KEY,
                        nombre VARCHAR(255) NOT NULL,
                        contacto VARCHAR(255),
                        direccion1 TEXT,
                        direccion2 TEXT,
                        ciudad VARCHAR(100),
                        telefono VARCHAR(50),
                        celular VARCHAR(50),
                        email VARCHAR(255),
                        rif VARCHAR(50)
                    )""",
                    # LINEAS
                    """CREATE TABLE lineas (
                        codigo SERIAL PRIMARY KEY,
                        nombre VARCHAR(255) NOT NULL
                    )""",
                    # GRUPOS
                    """CREATE TABLE grupos (
                        codigo VARCHAR(10) PRIMARY KEY,
                        linea INT REFERENCES lineas(codigo),
                        nombre VARCHAR(255) NOT NULL,
                        porcentaje1 NUMERIC(10,2),
                        porcentaje2 NUMERIC(10,2),
                        porcentaje3 NUMERIC(10,2)
                    )""",
                    # PRODUCTOS
                    """CREATE TABLE productos (
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
                        existencia INT DEFAULT 0
                    )""",
                    # ROLES DE USUARIO
                    """CREATE TABLE roles (
                        codigo SERIAL PRIMARY KEY,
                        rol VARCHAR(50) UNIQUE NOT NULL
                        )""",
                    # AGREGAR LOS ROLES DE USUARIO
                    """INSERT INTO roles (rol) VALUES 
                        ('Administrador'), 
                        ('Supervisor'), 
                        ('Gerente'), 
                        ('Vendedor')""",
                    # USUARIOS
                    """CREATE TABLE usuarios (
                        codigo SERIAL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        clave VARCHAR(255) NOT NULL,
                        correo VARCHAR(255) UNIQUE,
                        rol INT NOT NULL,
                        estado BOOLEAN DEFAULT TRUE,
                        FOREIGN KEY (rol) REFERENCES roles(codigo) ON DELETE RESTRICT  
                    )""",
                    # ENTRADAS A INVENTARIO
                    """CREATE TABLE entradas_inventario (
                        id SERIAL PRIMARY KEY,
                        num_factura VARCHAR(50) NOT NULL,
                        proveedor VARCHAR(100) NOT NULL,
                        fecha DATE NOT NULL,
                        total NUMERIC(12,2) NOT NULL,
                        iva NUMERIC(5,2) DEFAULT 0,
                        flete NUMERIC(5,2) DEFAULT 0,
                        descuento1 NUMERIC(5,2) DEFAULT 0,
                        descuento2 NUMERIC(5,2) DEFAULT 0,
                        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                        )""",
                    # DETALLES DE ENTRADAS
                    """CREATE TABLE detalle_entrada (
                        id SERIAL PRIMARY KEY,
                        entrada_id INTEGER NOT NULL,
                        codigo VARCHAR(50) NOT NULL,
                        cantidad INTEGER NOT NULL,
                        costo NUMERIC(12,2) NOT NULL,
                        descuento NUMERIC(5,2) DEFAULT 0,
                        neto NUMERIC(12,2) NOT NULL,
                        subtotal NUMERIC(12,2) NOT NULL,
                        FOREIGN KEY (entrada_id) REFERENCES entradas_inventario(id) ON DELETE CASCADE
                        )"""
                ]
                
                for stmt in statements:
                    cursor.execute(stmt)
                conn.commit()
                print("Tablas inicializadas correctamente.")
    except Exception as e:
        print(f"Error al inicializar las tablas: {repr(e)}")

CreateDatabase()
InitTables()
