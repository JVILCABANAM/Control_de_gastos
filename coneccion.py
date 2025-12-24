import sqlite3

try:
    conexion = sqlite3.connect("gastos.db")
    cursor = conexion.cursor()
    print("Conectado")
except sqlite3.Error as e:
    print(f" Error al conectar a la base de datos: {e}")