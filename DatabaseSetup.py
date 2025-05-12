import psycopg2
from psycopg2 import sql

# DETALLES DE CONECCION 
DB_NAME = "AppDatabase"
DB_USER = "postgres"
DB_PASSWORD = "admin1234"
DB_HOST = "localhost"  
DB_PORT = "5432"

# CREAR LA BASE DE DATOS SI NO EXISTE
def CreateDatabase():
    try:
        conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        conn.autocommit = True
        cursor = conn.cursor()

        # CHEQUEAR SI LA DB EXISTE
        cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME])
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")

# SCRIPT SQL PARA CREAR LAS TABLAS
def InitTables():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cursor = conn.cursor()

        create_tables_sql = """
        CREATE TABLE IF NOT EXISTS proveedores (
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
        );
        
        );
        CREATE TABLE grupos (
            codigo SERIAL PRIMARY KEY,
            linea VARCHAR(10) REFERENCES lineas(codigo),
            nombre VARCHAR(255) NOT NULL,
            porcentaje1 NUMERIC(10,2),
            porcentaje2 NUMERIC(10,2),
            porcentaje3 NUMERIC(10,2)
        );
        CREATE TABLE productos (
            codigo VARCHAR(10) PRIMARY KEY,
            linea VARCHAR(10) REFERENCES lines(codigo),
            grupo INT REFERENCES groups(id),
            proveedor VARCHAR(10) REFERENCES suppliers(codigo),
            nombre VARCHAR(255) NOT NULL,
            costo NUMERIC(10,2),
            ubicacion1 VARCHAR(50),
            ubicacion2 VARCHAR(50),
            precio1 NUMERIC(10,2),
            precio2 NUMERIC(10,2),
            precio3 NUMERIC(10,2),
            existencia INT DEFAULT 0
        );
        """

        cursor.execute(create_tables_sql)
        conn.commit()
        print("Tablas inicializadas correctamente.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error inicializando tablas: {e}")

DATABASE_MANAGER = CreateDatabase