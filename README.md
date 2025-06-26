# Taller Mecánico

Este proyecto es una aplicación de consola en Python para la gestión de un taller mecánico. Permite administrar clientes, autos, mecánicos, fichas técnicas y facturación usando una base de datos MySQL.

## Archivos del proyecto

- `taller-mecanico.py`: Código fuente principal de la aplicación.
- `taller_mecanico.sql`: Script SQL para crear la base de datos y las tablas necesarias (proporcionado por el profesor).

## Requisitos

- Python 3.x
- Paquete `pymysql` (para conectarse a MySQL)
- MySQL Server (con la base de datos y tablas ya creadas)

## Instalación de dependencias

Instalá pymysql ejecutando:

```
pip install pymysql
```

## Configuración

1. Asegurate de tener MySQL corriendo y la base de datos creada usando el archivo `taller_mecanico.sql`.
2. Modificá los datos de conexión en `taller-mecanico.py` si es necesario (usuario, contraseña, nombre de la base de datos).

## Uso

Ejecutá el programa desde la terminal:

```
python taller-mecanico.py
```

Seguí las instrucciones del menú para gestionar clientes, autos, mecánicos, fichas técnicas y facturación.

## Menú principal

- Clientes: Ver, agregar, buscar y borrar clientes.
- Autos: Ver, agregar, buscar y borrar autos.
- Mecánicos: Ver, agregar, buscar y borrar mecánicos.
- Fichas Técnicas: Crear, ver y editar fichas técnicas de autos.
- Facturación: Crear, anular y consultar facturas.

---

Hecho por MATEO ULLA, Argentina 🇦🇷
