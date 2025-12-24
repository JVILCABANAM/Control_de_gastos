import sqlite3
from coneccion import cursor, conexion


def mostrar_gastos():
    try:
        print("\n📊 Mostrando todos los gastos:\n")
        cursor.execute("SELECT * FROM gastos")
        gastos = cursor.fetchall()
        
        if gastos:
            for i, gasto in enumerate(gastos, start=1):
                print(f"  {i}. {gasto}")
        else:
            print("No hay gastos registrados")
    except sqlite3.Error as e:
        print(f" Error al mostrar gastos: {e}")