# TallerDB - Sistema de Gestión de Taller Mecánico

Este proyecto implementa una aplicación de consola en Python para gestionar las operaciones de un taller mecánico, incluyendo la administración de clientes, vehículos, mecánicos, fichas técnicas y facturación. Utiliza MySQL como motor de base de datos y la librería `pymysql` para la conexión.

## Requisitos

* Python 3.7 o superior
* MySQL Server 5.7 o superior
* Biblioteca `pymysql`

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tuusuario/tallerdb.git
   cd tallerdb
   ```

2. **Crear entorno virtual (opcional pero recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate   # Windows
   ```

3. **Instalar dependencias**

   ```bash
   pip install pymysql
   ```

4. **Configurar la base de datos**

   * Iniciar sesión en MySQL:

     ```sql
     mysql -u root -p
     ```
   * Crear la base de datos y tablas necesarias:

     ```sql
     CREATE DATABASE taller_mecanico;
     USE taller_mecanico;

     CREATE TABLE Clientes (
       DNI INT PRIMARY KEY,
       Nombre VARCHAR(100),
       Apellido VARCHAR(100),
       Direccion VARCHAR(255),
       Telefono VARCHAR(50)
     );

     CREATE TABLE Vehiculos (
       Patente VARCHAR(15) PRIMARY KEY,
       DNI INT,
       Marca VARCHAR(50),
       Modelo VARCHAR(50),
       Color VARCHAR(30),
       FOREIGN KEY (DNI) REFERENCES Clientes(DNI)
     );

     CREATE TABLE Mecanicos (
       Legajo VARCHAR(20) PRIMARY KEY,
       Nombre VARCHAR(100),
       Apellido VARCHAR(100),
       Rol VARCHAR(50),
       Estado ENUM('+','-')
     );

     CREATE TABLE Ficha_tecnica (
       id_ficha INT PRIMARY KEY,
       dni_cliente INT,
       marca VARCHAR(50),
       modelo VARCHAR(50),
       patente VARCHAR(15),
       motivo_ingreso TEXT,
       fecha_ingreso DATE,
       FOREIGN KEY (dni_cliente) REFERENCES Clientes(DNI),
       FOREIGN KEY (patente) REFERENCES Vehiculos(Patente)
     );

     CREATE TABLE Facturacion (
       id_factura INT AUTO_INCREMENT PRIMARY KEY,
       DNI_Cliente INT,
       Fecha_Factura DATE,
       Monto DECIMAL(10,2),
       Estado ENUM('Emitida','Anulada'),
       FOREIGN KEY (DNI_Cliente) REFERENCES Clientes(DNI)
     );
     ```

5. **Actualizar credenciales**

   * En el archivo principal, ajustar los parámetros de conexión:

     ```python
     host="localhost",
     port=3306,
     user="<tu_usuario>",
     password="<tu_contraseña>",
     database="taller_mecanico",
     ```

## Uso

Se mostrará un menú principal con las siguientes opciones:

1. **Clientes**

   * Ver todos los clientes
   * Ingresar nuevo cliente
   * Ver cliente específico (por DNI)
   * Eliminar cliente (por DNI)

2. **Vehículos**

   * Ver todos los vehículos
   * Ingresar nuevo vehículo
   * Ver vehículo específico (por patente)
   * Eliminar vehículo (por patente)

3. **Mecánicos**

   * Ver todos los mecánicos
   * Ingresar nuevo mecánico
   * Ver mecánico específico (por legajo)
   * Eliminar mecánico (por legajo)

4. **Ficha Técnica**

   * Crear ficha técnica
   * Consultar ficha técnica (todas o por ID)
   * Modificar ficha técnica (marca, modelo, patente o DNI cliente)

5. **Facturación**

   * Crear factura
   * Anular factura (por ID)
   * Consultar factura (todas o por ID)

6. **Salir**

Para navegar, ingrese el número de opción correspondiente y siga las instrucciones en pantalla.
