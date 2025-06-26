import os
import pymysql
import time

class MiTaller:
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                port=3306,
                user="mateo",
                password="1234",
                database="taller_mecanico",
            )
            self.cursor = self.db.cursor()
            print("\n¡Conectado a la base de datos del taller!\n")
        except Exception as e:
            print("No se pudo conectar a la base de datos:", e)
            exit()

    def limpiar(self):
        os.system("cls" if os.name == "nt" else "clear")

    def menu_principal(self):
        print("\n--- Taller Mecánico ---")
        print("1. Clientes")
        print("2. Autos")
        print("3. Mecánicos")
        print("4. Fichas Técnicas")
        print("5. Facturación")
        print("6. Salir")

    def menu_clientes(self):
        print("\n--- Menú Clientes ---")
        print("1. Listar clientes")
        print("2. Agregar cliente")
        print("3. Buscar cliente por DNI")
        print("4. Borrar cliente")
        print("5. Volver")

    def mostrar_clientes(self):
        self.cursor.execute("SELECT * FROM Clientes")
        clientes = self.cursor.fetchall()
        if not clientes:
            print("No hay clientes registrados.")
        else:
            for c in clientes:
                print(f"DNI: {c[0]} | Nombre: {c[1]} {c[2]} | Tel: {c[4]}")
        input("\nPresioná Enter para seguir...")

    def agregar_cliente(self):
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        try:
            self.cursor.execute(
                "INSERT INTO Clientes (DNI, Nombre, Apellido, Direccion, Telefono) VALUES (%s, %s, %s, %s, %s)",
                (dni, nombre, apellido, direccion, telefono),
            )
            self.db.commit()
            print("Cliente guardado!")
        except Exception as e:
            print("Error al guardar cliente:", e)
        input("\nPresioná Enter para seguir...")

    def buscar_cliente(self):
        dni = input("DNI del cliente: ")
        self.cursor.execute("SELECT * FROM Clientes WHERE DNI=%s", (dni,))
        c = self.cursor.fetchone()
        if c:
            print(f"DNI: {c[0]} | Nombre: {c[1]} {c[2]} | Dirección: {c[3]} | Tel: {c[4]}")
        else:
            print("No se encontró ese cliente.")
        input("\nPresioná Enter para seguir...")

    def borrar_cliente(self):
        dni = input("DNI del cliente a borrar: ")
        self.cursor.execute("DELETE FROM Clientes WHERE DNI=%s", (dni,))
        self.db.commit()
        print("Cliente eliminado (si existía).")
        input("\nPresioná Enter para seguir...")

    def menu_autos(self):
        print("\n--- Menú Autos ---")
        print("1. Listar autos")
        print("2. Agregar auto")
        print("3. Buscar auto por patente")
        print("4. Borrar auto")
        print("5. Volver")

    def mostrar_autos(self):
        self.cursor.execute("SELECT * FROM Vehiculos")
        autos = self.cursor.fetchall()
        if not autos:
            print("No hay autos cargados.")
        else:
            for a in autos:
                print(
                    f"Patente: {a[0]} | Dueño: {a[1]} | Marca: {a[2]} | Modelo: {a[3]} | Color: {a[4]}"
                )
        input("\nPresioná Enter para seguir...")

    def agregar_auto(self):
        patente = input("Patente: ")
        dni = input("DNI del dueño: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        try:
            self.cursor.execute(
                "INSERT INTO Vehiculos (Patente, DNI, Marca, Modelo, Color) VALUES (%s, %s, %s, %s, %s)",
                (patente, dni, marca, modelo, color),
            )
            self.db.commit()
            print("Auto guardado!")
        except Exception as e:
            print("Error al guardar auto:", e)
        input("\nPresioná Enter para seguir...")

    def buscar_auto(self):
        patente = input("Patente del auto: ")
        self.cursor.execute("SELECT * FROM Vehiculos WHERE Patente=%s", (patente,))
        a = self.cursor.fetchone()
        if a:
            print(
                f"Patente: {a[0]} | Dueño: {a[1]} | Marca: {a[2]} | Modelo: {a[3]} | Color: {a[4]}"
            )
        else:
            print("No se encontró ese auto.")
        input("\nPresioná Enter para seguir...")

    def borrar_auto(self):
        patente = input("Patente del auto a borrar: ")
        self.cursor.execute("DELETE FROM Vehiculos WHERE Patente=%s", (patente,))
        self.db.commit()
        print("Auto eliminado (si existía).")
        input("\nPresioná Enter para seguir...")

    def menu_mecanicos(self):
        print("\n--- Menú Mecánicos ---")
        print("1. Listar mecánicos")
        print("2. Agregar mecánico")
        print("3. Buscar mecánico por legajo")
        print("4. Borrar mecánico")
        print("5. Volver")

    def mostrar_mecanicos(self):
        self.cursor.execute("SELECT * FROM Mecanicos")
        ms = self.cursor.fetchall()
        if not ms:
            print("No hay mecánicos registrados.")
        else:
            for m in ms:
                print(f"Legajo: {m[0]} | Nombre: {m[1]} {m[2]} | Rol: {m[3]} | Estado: {m[4]}")
        input("\nPresioná Enter para seguir...")

    def agregar_mecanico(self):
        legajo = input("Legajo: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        rol = input("Rol: ")
        estado = input("Estado (+/-): ")
        try:
            self.cursor.execute(
                "INSERT INTO Mecanicos (Legajo, Nombre, Apellido, Rol, Estado) VALUES (%s, %s, %s, %s, %s)",
                (legajo, nombre, apellido, rol, estado),
            )
            self.db.commit()
            print("Mecánico guardado!")
        except Exception as e:
            print("Error al guardar mecánico:", e)
        input("\nPresioná Enter para seguir...")

    def buscar_mecanico(self):
        legajo = input("Legajo del mecánico: ")
        self.cursor.execute("SELECT * FROM Mecanicos WHERE Legajo=%s", (legajo,))
        m = self.cursor.fetchone()
        if m:
            print(f"Legajo: {m[0]} | Nombre: {m[1]} {m[2]} | Rol: {m[3]} | Estado: {m[4]}")
        else:
            print("No se encontró ese mecánico.")
        input("\nPresioná Enter para seguir...")

    def borrar_mecanico(self):
        legajo = input("Legajo del mecánico a borrar: ")
        self.cursor.execute("DELETE FROM Mecanicos WHERE Legajo=%s", (legajo,))
        self.db.commit()
        print("Mecánico eliminado (si existía).")
        input("\nPresioná Enter para seguir...")

    def menu_fichas(self):
        print("\n--- Menú Fichas Técnicas ---")
        print("1. Crear ficha técnica")
        print("2. Ver fichas técnicas")
        print("3. Modificar ficha técnica")
        print("4. Volver")

    def crear_ficha(self):
        id_ficha = input("ID de ficha: ")
        dni = input("DNI del cliente: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        patente = input("Patente: ")
        motivo = input("Motivo ingreso: ")
        fecha = input("Fecha ingreso (YYYY-MM-DD): ")
        try:
            self.cursor.execute(
                "INSERT INTO Ficha_tecnica (id_ficha, dni_cliente, marca, modelo, patente, motivo_ingreso, fecha_ingreso) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (id_ficha, dni, marca, modelo, patente, motivo, fecha),
            )
            self.db.commit()
            print("Ficha técnica guardada!")
        except Exception as e:
            print("Error al guardar ficha técnica:", e)
        input("\nPresioná Enter para seguir...")

    def ver_fichas(self):
        self.cursor.execute("SELECT * FROM Ficha_tecnica")
        fichas = self.cursor.fetchall()
        if not fichas:
            print("No hay fichas técnicas.")
        else:
            for f in fichas:
                print(f)
        input("\nPresioná Enter para seguir...")

    def modificar_ficha(self):
        id_ficha = input("ID de la ficha a modificar: ")
        self.cursor.execute("SELECT * FROM Ficha_tecnica WHERE id_ficha=%s", (id_ficha,))
        ficha = self.cursor.fetchone()
        if not ficha:
            print("No existe esa ficha.")
            input("\nPresioná Enter para seguir...")
            return
        print("¿Qué campo querés cambiar?")
        print("1. Marca\n2. Modelo\n3. Patente\n4. Motivo ingreso\n5. Fecha ingreso\n6. DNI cliente")
        op = input("Opción: ")
        campos = ["marca", "modelo", "patente", "motivo_ingreso", "fecha_ingreso", "dni_cliente"]
        if op in [str(i+1) for i in range(6)]:
            nuevo = input("Nuevo valor: ")
            self.cursor.execute(f"UPDATE Ficha_tecnica SET {campos[int(op)-1]}=%s WHERE id_ficha=%s", (nuevo, id_ficha))
            self.db.commit()
            print("Ficha modificada!")
        else:
            print("Opción inválida.")
        input("\nPresioná Enter para seguir...")

    def menu_facturacion(self):
        print("\n--- Menú Facturación ---")
        print("1. Nueva factura")
        print("2. Anular factura")
        print("3. Ver facturas")
        print("4. Volver")

    def nueva_factura(self):
        dni = input("DNI del cliente: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        monto = input("Monto: ")
        try:
            self.cursor.execute(
                "INSERT INTO Facturacion (DNI_Cliente, Fecha_Factura, Monto, Estado) VALUES (%s, %s, %s, 'Emitida')",
                (dni, fecha, monto),
            )
            self.db.commit()
            print("Factura emitida!")
        except Exception as e:
            print("Error al emitir factura:", e)
        input("\nPresioná Enter para seguir...")

    def anular_factura(self):
        idf = input("ID de la factura a anular: ")
        self.cursor.execute("UPDATE Facturacion SET Estado='Anulada' WHERE id_factura=%s", (idf,))
        self.db.commit()
        print("Factura anulada (si existía).")
        input("\nPresioná Enter para seguir...")

    def ver_facturas(self):
        self.cursor.execute("SELECT * FROM Facturacion")
        facturas = self.cursor.fetchall()
        if not facturas:
            print("No hay facturas.")
        else:
            for f in facturas:
                print(f)
        input("\nPresioná Enter para seguir...")

    def salir(self):
        print("\nChau! Cerrando el taller...")
        self.cursor.close()
        self.db.close()
        exit()


# --- Programa principal ---
taller = MiTaller()
while True:
    taller.limpiar()
    taller.menu_principal()
    op = input("\nElegí una opción: ")
    if op == "1":
        taller.limpiar()
        while True:
            taller.menu_clientes()
            op2 = input("Opción: ")
            if op2 == "1":
                taller.mostrar_clientes()
            elif op2 == "2":
                taller.agregar_cliente()
            elif op2 == "3":
                taller.buscar_cliente()
            elif op2 == "4":
                taller.borrar_cliente()
            elif op2 == "5":
                break
            else:
                print("Opción inválida.")
    elif op == "2":
        taller.limpiar()
        while True:
            taller.menu_autos()
            op2 = input("Opción: ")
            if op2 == "1":
                taller.mostrar_autos()
            elif op2 == "2":
                taller.agregar_auto()
            elif op2 == "3":
                taller.buscar_auto()
            elif op2 == "4":
                taller.borrar_auto()
            elif op2 == "5":
                break
            else:
                print("Opción inválida.")
    elif op == "3":
        taller.limpiar()
        while True:
            taller.menu_mecanicos()
            op2 = input("Opción: ")
            if op2 == "1":
                taller.mostrar_mecanicos()
            elif op2 == "2":
                taller.agregar_mecanico()
            elif op2 == "3":
                taller.buscar_mecanico()
            elif op2 == "4":
                taller.borrar_mecanico()
            elif op2 == "5":
                break
            else:
                print("Opción inválida.")
    elif op == "4":
        taller.limpiar()
        while True:
            taller.menu_fichas()
            op2 = input("Opción: ")
            if op2 == "1":
                taller.crear_ficha()
            elif op2 == "2":
                taller.ver_fichas()
            elif op2 == "3":
                taller.modificar_ficha()
            elif op2 == "4":
                break
            else:
                print("Opción inválida.")
    elif op == "5":
        taller.limpiar()
        while True:
            taller.menu_facturacion()
            op2 = input("Opción: ")
            if op2 == "1":
                taller.nueva_factura()
            elif op2 == "2":
                taller.anular_factura()
            elif op2 == "3":
                taller.ver_facturas()
            elif op2 == "4":
                break
            else:
                print("Opción inválida.")
    elif op == "6":
        taller.salir()
    else:
        print("Opción inválida. Probá de nuevo.")
        time.sleep(1)