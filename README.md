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

   1. **Crear la base de datos**

      ```sql
      CREATE DATABASE IF NOT EXISTS `Taller_Mecanico`;
      USE `Taller_Mecanico`;
      ```

   2. **Crear tablas**

      ```sql
      -- Clientes
      CREATE TABLE IF NOT EXISTS `Clientes` (
          `DNI` VARCHAR(255) PRIMARY KEY,
          `Nombre` VARCHAR(255),
          `Apellido` VARCHAR(255),
          `Direccion` VARCHAR(255),
          `Telefono` VARCHAR(255)
      );

      -- Vehículos
      CREATE TABLE IF NOT EXISTS `Vehiculos` (
          `Patente` VARCHAR(255) PRIMARY KEY,
          `DNI` VARCHAR(255),
          `Marca` VARCHAR(255),
          `Modelo` VARCHAR(255),
          `Color` VARCHAR(255),
          FOREIGN KEY (`DNI`) REFERENCES `Clientes`(`DNI`)
      );

      -- Mecánicos
      CREATE TABLE IF NOT EXISTS `Mecanicos` (
          `Legajo` VARCHAR(255) PRIMARY KEY,
          `Nombre` VARCHAR(255),
          `Apellido` VARCHAR(255),
          `Rol` VARCHAR(255),
          `Estado` VARCHAR(255)
      );

      -- Repuestos
      CREATE TABLE IF NOT EXISTS `Repuestos` (
          `Id` INT PRIMARY KEY,
          `Nombre` VARCHAR(255),
          `Precio` INT,
          `Fabricante` VARCHAR(255)
      );

      -- Reparaciones
      CREATE TABLE IF NOT EXISTS `Reparaciones` (
          `id_reparacion` INT PRIMARY KEY,
          `Fecha_entrada` DATE,
          `Hora_entrada` TIME,
          `Patente` VARCHAR(255),
          `Legajo` VARCHAR(255),
          `DNI` VARCHAR(255),
          FOREIGN KEY (`Patente`) REFERENCES `Vehiculos`(`Patente`),
          FOREIGN KEY (`Legajo`) REFERENCES `Mecanicos`(`Legajo`),
          FOREIGN KEY (`DNI`) REFERENCES `Clientes`(`DNI`)
      );

      -- Relación Mecánico-Reparaciones
      CREATE TABLE IF NOT EXISTS `Mecanico_Reparaciones` (
          `Legajo` VARCHAR(255),
          `id_reparacion` INT,
          PRIMARY KEY (`Legajo`, `id_reparacion`),
          FOREIGN KEY (`Legajo`) REFERENCES `Mecanicos`(`Legajo`),
          FOREIGN KEY (`id_reparacion`) REFERENCES `Reparaciones`(`id_reparacion`)
      );

      -- Ficha técnica
      CREATE TABLE IF NOT EXISTS `Ficha_tecnica` (
          `id_ficha` VARCHAR(255) PRIMARY KEY,
          `dni_cliente` VARCHAR(255),
          `marca` VARCHAR(255) NOT NULL,
          `modelo` VARCHAR(255) NOT NULL,
          `patente` VARCHAR(255) NOT NULL,
          `motivo_ingreso` VARCHAR(255),
          `fecha_ingreso` DATE
      );

      -- Facturación
      CREATE TABLE IF NOT EXISTS `Facturacion` (
          `id_factura` INT PRIMARY KEY AUTO_INCREMENT,
          `DNI_Cliente` VARCHAR(255),
          `Fecha_Factura` DATE,
          `Monto` DECIMAL(10, 2),
          `Estado` ENUM('Emitida', 'Anulada'),
          FOREIGN KEY (`DNI_Cliente`) REFERENCES `Clientes`(`DNI`)
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
