
from datetime import datetime
import sqlite3

from coneccion import cursor, conexion


def ingresar_gasto():
    try:
        nombre_gasto = input("📝 Ingrese el nombre del gasto: ").strip()
        if not nombre_gasto:
            print("❌ Error: El nombre del gasto no puede estar vacío")
            return
        
        monto_gasto = float(input("💰 Ingrese el monto del gasto: "))
        if monto_gasto <= 0:
            print("❌ Error: El monto debe ser mayor a cero")
            return
        
        fecha_input = input("📅 Ingrese la fecha (YYYY-MM-DD) o presione Enter para usar hoy: ").strip()
        
        if fecha_input:
            try:
                fecha_obj = datetime.strptime(fecha_input, "%Y-%m-%d")
                fecha = fecha_obj.strftime("%Y-%m-%d")
            except ValueError:
                print("❌ Error: Formato de fecha inválido. Use el formato YYYY-MM-DD (ejemplo: 2024-01-15)")
                return
        else:
            fecha = datetime.now().strftime("%Y-%m-%d")
            
        cursor.execute("INSERT INTO gastos (fecha, nombre_gasto, monto_gasto) VALUES (?, ?, ?)", (fecha, nombre_gasto, monto_gasto))
        print("Gasto registrado correctamente")
        conexion.commit()
    except ValueError:
        print(" Error: Por favor ingrese un número válido para el monto")
    except sqlite3.Error as e:
        print(f" Error al guardar en la base de datos: {e}")