-- Create the Suppliers table
CREATE TABLE suppliers (
    codigo VARCHAR(10) PRIMARY KEY,
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

-- Create the Lines table
CREATE TABLE lines (
    codigo VARCHAR(10) PRIMARY KEY,
    linea VARCHAR(255) NOT NULL
);

-- Create the Groups table
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    line_code VARCHAR(10) REFERENCES lines(codigo),
    nombre_grupo VARCHAR(255) NOT NULL,
    porcentaje_1 NUMERIC(10,2),
    porcentaje_2 NUMERIC(10,2),
    porcentaje_3 NUMERIC(10,2)
);

-- Create the Products table
CREATE TABLE products (
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
