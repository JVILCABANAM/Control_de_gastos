from datetime import datetime
import sqlite3
from coneccion import cursor, conexion


def filtrar_gastos():
    fecha = input("🔍 Ingrese la fecha (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(fecha, "%Y-%m-%d")

        encontrados = False

        cursor.execute("SELECT * FROM gastos WHERE fecha = ?", (fecha,))
        gastos = cursor.fetchall()

        if gastos:
            print(f"\n📊 Gastos encontrados para {fecha}:\n")
            for i, gasto in enumerate(gastos, start=1):
                print(f"  {i}. {gasto}")
                encontrados = True

        if not encontrados:
            print("⚠️  No hay gastos para esa fecha")

    except ValueError:
        print("Error: Formato de fecha inválido. Use el formato YYYY-MM-DD")
    except sqlite3.Error as e:
        print(f"Error al consultar la base de datos: {e}")


def filtrar_suma_gastos_por_fecha():
    fecha = input("🔍 Ingrese la fecha (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(fecha, "%Y-%m-%d")

        encontrados = False
        total = 0

        cursor.execute("SELECT * FROM gastos WHERE fecha = ?", (fecha,))
        gastos = cursor.fetchall()

        if gastos:
            print(f"\n📊 Gastos encontrados para {fecha}:\n")
            for i, gasto in enumerate(gastos, start=1):
                print(f"  {i}. {gasto}")
                encontrados = True
                # Asumiendo que monto_gasto es el índice 2 (tercera columna)
                if len(gasto) >= 3:
                    total += float(gasto[2])

        if encontrados:
            print(f"\n💰 Total de gastos para {fecha}: S/{total:.2f}")
        else:
            print("No hay gastos para esa fecha")

    except ValueError:
        print("Error: Formato de fecha inválido. Use el formato YYYY-MM-DD")
    except sqlite3.Error as e:
        print(f"Error al consultar la base de datos: {e}")


def filtrar_por_rango_de_fechas():
    fecha_inicio = input("📅 Ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("📅 Ingrese la fecha de fin (YYYY-MM-DD): ").strip()

    try:
        fecha_inicio_obj = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin_obj = datetime.strptime(fecha_fin, "%Y-%m-%d")
        
        if fecha_inicio_obj > fecha_fin_obj:
            print("Error: La fecha de inicio debe ser anterior o igual a la fecha de fin")
            return

        encontrados = False
        total = 0

        cursor.execute("SELECT * FROM gastos WHERE fecha BETWEEN ? AND ?", (fecha_inicio, fecha_fin))
        gastos = cursor.fetchall()

        if gastos:
            print(f"\n📊 Gastos encontrados entre {fecha_inicio} y {fecha_fin}:\n")
            for i, gasto in enumerate(gastos, start=1):
                print(f"  {i}. {gasto}")
                encontrados = True
                if len(gasto) >= 3:
                    total += float(gasto[2])

        if encontrados:
            print(f"\n💰 Total de gastos entre {fecha_inicio} y {fecha_fin}: S/{total:.2f}")
        else:
            print(" No hay gastos en el rango de fechas")

    except ValueError:
        print("Error: Formato de fecha inválido. Use el formato YYYY-MM-DD")
    except sqlite3.Error as e:
        print(f" Error al consultar la base de datos: {e}")