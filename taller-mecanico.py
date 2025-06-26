import os
import pymysql
import time

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class BaseTaller:
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                port=3306,
                user="mateo",
                password="1234",
                database="taller_mecanico"
            )
            self.cur = self.db.cursor()
            print("Conectado a la base de datos!")
        except Exception as error:
            print("No se pudo conectar:", error)
            quit()

    def mostrar_menu(self):
        limpiar_pantalla()
        print("--- MENU PRINCIPAL ---")
        print("a) Clientes")
        print("b) Autos")
        print("c) Mecánicos")
        print("d) Fichas Técnicas")
        print("e) Facturación")
        print("f) Salir")

    def menu_clientes(self):
        print("1) Listar clientes")
        print("2) Nuevo cliente")
        print("3) Buscar cliente")
        print("4) Borrar cliente")
        print("5) Volver")

    def menu_autos(self):
        print("1) Listar autos")
        print("2) Nuevo auto")
        print("3) Buscar auto")
        print("4) Borrar auto")
        print("5) Volver")

    def menu_mecanicos(self):
        print("1) Listar mecánicos")
        print("2) Nuevo mecánico")
        print("3) Buscar mecánico")
        print("4) Borrar mecánico")
        print("5) Volver")

    def menu_fichas(self):
        print("1) Crear ficha técnica")
        print("2) Ver ficha técnica")
        print("3) Editar ficha técnica")
        print("4) Volver")

    def menu_facturacion(self):
        print("1) Nueva factura")
        print("2) Anular factura")
        print("3) Ver facturas")
        print("4) Volver")

    # CLIENTES
    def ver_clientes(self):
        self.cur.execute("SELECT * FROM Clientes")
        datos = self.cur.fetchall()
        for cli in datos:
            print(cli)
        input("Presione Enter para volver...")

    def agregar_cliente(self):
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        self.cur.execute(
            "INSERT INTO Clientes (DNI, Nombre, Apellido, Direccion, Telefono) VALUES (%s, %s, %s, %s, %s)",
            (dni, nombre, apellido, direccion, telefono)
        )
        self.db.commit()
        print("Cliente guardado!")
        time.sleep(1)

    def buscar_cliente(self):
        dni = input("DNI del cliente: ")
        self.cur.execute("SELECT DNI, Nombre, Apellido, Telefono FROM Clientes WHERE DNI=%s", (dni,))
        cli = self.cur.fetchone()
        if cli:
            print(f"DNI: {cli[0]} | Nombre: {cli[1]} | Apellido: {cli[2]} | Teléfono: {cli[3]}")
        else:
            print("No existe ese cliente.")
        input("Presione Enter para volver...")

    def borrar_cliente(self):
        dni = input("DNI a borrar: ")
        self.cur.execute("DELETE FROM Clientes WHERE DNI=%s", (dni,))
        self.db.commit()
        print("Cliente eliminado!")
        time.sleep(1)

    # AUTOS
    def ver_autos(self):
        self.cur.execute("SELECT * FROM Vehiculos")
        autos = self.cur.fetchall()
        for auto in autos:
            print(auto)
        input("Presione Enter para volver...")

    def agregar_auto(self):
        patente = input("Patente: ")
        dni = input("DNI dueño: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        self.cur.execute(
            "INSERT INTO Vehiculos (Patente, DNI, Marca, Modelo, Color) VALUES (%s, %s, %s, %s, %s)",
            (patente, dni, marca, modelo, color)
        )
        self.db.commit()
        print("Auto guardado!")
        time.sleep(1)

    def buscar_auto(self):
        patente = input("Patente del auto: ")
        self.cur.execute("SELECT Patente, Marca, Modelo FROM Vehiculos WHERE Patente=%s", (patente,))
        auto = self.cur.fetchone()
        if auto:
            print(f"Patente: {auto[0]} | Marca: {auto[1]} | Modelo: {auto[2]}")
        else:
            print("No existe ese auto.")
        input("Presione Enter para volver...")

    def borrar_auto(self):
        patente = input("Patente a borrar: ")
        self.cur.execute("DELETE FROM Vehiculos WHERE Patente=%s", (patente,))
        self.db.commit()
        print("Auto eliminado!")
        time.sleep(1)

    # MECANICOS
    def ver_mecanicos(self):
        self.cur.execute("SELECT * FROM Mecanicos")
        for m in self.cur.fetchall():
            print(m)
        input("Presione Enter para volver...")

    def agregar_mecanico(self):
        legajo = input("Legajo: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        rol = input("Rol: ")
        estado = input("Estado (+/-): ")
        while estado not in ["+", "-"]:
            print("Estado inválido")
            estado = input("Estado (+/-): ")
        self.cur.execute(
            "INSERT INTO Mecanicos (Legajo, Nombre, Apellido, Rol, Estado) VALUES (%s, %s, %s, %s, %s)",
            (legajo, nombre, apellido, rol, estado)
        )
        self.db.commit()
        print("Mecánico guardado!")
        time.sleep(1)

    def buscar_mecanico(self):
        legajo = input("Legajo del mecánico: ")
        self.cur.execute("SELECT Legajo, Nombre, Apellido, Rol, Estado FROM Mecanicos WHERE Legajo=%s", (legajo,))
        m = self.cur.fetchone()
        if m:
            print(f"Legajo: {m[0]} | Nombre: {m[1]} | Apellido: {m[2]} | Rol: {m[3]} | Estado: {m[4]}")
        else:
            print("No existe ese mecánico.")
        input("Presione Enter para volver...")

    def borrar_mecanico(self):
        legajo = input("Legajo a borrar: ")
        self.cur.execute("DELETE FROM Mecanicos WHERE Legajo=%s", (legajo,))
        self.db.commit()
        print("Mecánico eliminado!")
        time.sleep(1)

    # FICHAS TECNICAS
    def crear_ficha(self):
        limpiar_pantalla()
        idf = input("ID ficha: ")
        dni = input("DNI cliente: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        patente = input("Patente: ")
        motivo = input("Motivo ingreso: ")
        fecha = input("Fecha ingreso (YYYY-MM-DD): ")
        try:
            self.cur.execute(
                "INSERT INTO Ficha_tecnica (id_ficha, dni_cliente, marca, modelo, patente, motivo_ingreso, fecha_ingreso) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (idf, dni, marca, modelo, patente, motivo, fecha)
            )
            self.db.commit()
            print("Ficha técnica guardada!")
        except Exception as e:
            print("Error al guardar ficha:", e)
        time.sleep(1)

    def editar_ficha(self):
        limpiar_pantalla()
        idf = input("ID de la ficha a editar: ")
        self.cur.execute("SELECT * FROM Ficha_tecnica WHERE id_ficha=%s", (idf,))
        ficha = self.cur.fetchone()
        if not ficha:
            print("No existe esa ficha.")
            time.sleep(1)
            return
        print("1) Cambiar datos del auto")
        print("2) Cambiar DNI cliente")
        print("3) Cancelar")
        op = input("Opción: ")
        if op == "1":
            campo = input("¿Qué campo? (marca/modelo/patente): ")
            if campo not in ["marca", "modelo", "patente"]:
                print("Campo inválido.")
                return
            nuevo = input(f"Nuevo valor para {campo}: ")
            self.cur.execute(f"UPDATE Ficha_tecnica SET {campo}=%s WHERE id_ficha=%s", (nuevo, idf))
        elif op == "2":
            nuevo = input("Nuevo DNI cliente: ")
            self.cur.execute("UPDATE Ficha_tecnica SET dni_cliente=%s WHERE id_ficha=%s", (nuevo, idf))
        else:
            print("Cancelado.")
            return
        self.db.commit()
        print("Ficha técnica actualizada!")
        time.sleep(1)

    def ver_fichas(self):
        limpiar_pantalla()
        idf = input("ID de ficha (vacío para todas): ")
        if idf.strip() == "":
            self.cur.execute("SELECT * FROM Ficha_tecnica")
            fichas = self.cur.fetchall()
            if not fichas:
                print("No hay fichas.")
            else:
                for f in fichas:
                    print(f)
        else:
            self.cur.execute("SELECT * FROM Ficha_tecnica WHERE id_ficha=%s", (idf,))
            ficha = self.cur.fetchone()
            if ficha:
                print(ficha)
            else:
                print("No existe esa ficha.")
        input("Presione Enter para volver...")

    # FACTURACION
    def nueva_factura(self):
        limpiar_pantalla()
        dni = input("DNI cliente: ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        monto = input("Monto: ")
        estado = "Emitida"
        try:
            self.cur.execute(
                "INSERT INTO Facturacion (DNI_Cliente, Fecha_Factura, Monto, Estado) VALUES (%s, %s, %s, %s)",
                (dni, fecha, monto, estado)
            )
            self.db.commit()
            print("Factura guardada!")
        except Exception as e:
            print("Error al guardar factura:", e)
        time.sleep(1)

    def anular_factura(self):
        limpiar_pantalla()
        idf = input("ID de factura a anular: ")
        self.cur.execute("UPDATE Facturacion SET Estado='Anulada' WHERE id_factura=%s", (idf,))
        if self.cur.rowcount == 0:
            print("No existe esa factura.")
        else:
            self.db.commit()
            print("Factura anulada!")
        time.sleep(1)

    def ver_facturas(self):
        limpiar_pantalla()
        idf = input("ID de factura (vacío para todas): ")
        if idf.strip() == "":
            self.cur.execute("SELECT * FROM Facturacion")
            facturas = self.cur.fetchall()
            if not facturas:
                print("No hay facturas.")
            else:
                for f in facturas:
                    print(f)
        else:
            self.cur.execute("SELECT * FROM Facturacion WHERE id_factura=%s", (idf,))
            f = self.cur.fetchone()
            if f:
                print(f)
            else:
                print("No existe esa factura.")
        input("Presione Enter para volver...")

    def cerrar(self):
        print("Chau! Cerrando todo...")
        self.cur.close()
        self.db.close()
        quit()

# --- PROGRAMA PRINCIPAL ---

def main():
    taller = BaseTaller()
    while True:
        taller.mostrar_menu()
        op = input("Opción: ").lower()
        if op == "a":
            limpiar_pantalla()
            taller.menu_clientes()
            sub = input("Opción: ")
            if sub == "1":
                taller.ver_clientes()
            elif sub == "2":
                taller.agregar_cliente()
            elif sub == "3":
                taller.buscar_cliente()
            elif sub == "4":
                taller.borrar_cliente()
            elif sub == "5":
                continue
        elif op == "b":
            limpiar_pantalla()
            taller.menu_autos()
            sub = input("Opción: ")
            if sub == "1":
                taller.ver_autos()
            elif sub == "2":
                taller.agregar_auto()
            elif sub == "3":
                taller.buscar_auto()
            elif sub == "4":
                taller.borrar_auto()
            elif sub == "5":
                continue
        elif op == "c":
            limpiar_pantalla()
            taller.menu_mecanicos()
            sub = input("Opción: ")
            if sub == "1":
                taller.ver_mecanicos()
            elif sub == "2":
                taller.agregar_mecanico()
            elif sub == "3":
                taller.buscar_mecanico()
            elif sub == "4":
                taller.borrar_mecanico()
            elif sub == "5":
                continue
        elif op == "d":
            limpiar_pantalla()
            taller.menu_fichas()
            sub = input("Opción: ")
            if sub == "1":
                taller.crear_ficha()
            elif sub == "2":
                taller.ver_fichas()
            elif sub == "3":
                taller.editar_ficha()
            elif sub == "4":
                continue
        elif op == "e":
            limpiar_pantalla()
            taller.menu_facturacion()
            sub = input("Opción: ")
            if sub == "1":
                taller.nueva_factura()
            elif sub == "2":
                taller.anular_factura()
            elif sub == "3":
                taller.ver_facturas()
            elif sub == "4":
                continue
        elif op == "f":
            taller.cerrar()
        else:
            print("Opción inválida!")
            time.sleep(1)

if __name__ == "__main__":
    main()
