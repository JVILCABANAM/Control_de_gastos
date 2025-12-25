import sqlite3

try:
    conexion = sqlite3.connect("gastos.db")
    cursor = conexion.cursor()
    
    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            nombre_gasto TEXT NOT NULL,
            monto_gasto REAL NOT NULL
        )
    """)
    conexion.commit()
    
    print("✅ Conectado exitosamente a la base de datos")
except sqlite3.Error as e:
    print(f" Error al conectar a la base de datos: {e}")