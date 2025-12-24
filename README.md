# 💵 Sistema de Gestión de Gastos Personales

Sistema simple de gestión de gastos personales desarrollado en Python con SQLite.

## 📋 Características

- ✅ **Registro de gastos**: Ingresa gastos con nombre, monto y fecha
- 📊 **Visualización**: Muestra todos los gastos registrados
- 🔍 **Filtrado**: Busca gastos por fecha específica
- 💰 **Suma por fecha**: Calcula el total de gastos de una fecha
- 📅 **Rango de fechas**: Filtra y suma gastos en un rango de fechas

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone <tu-repositorio>

# Navegar al directorio
cd Calculo_gastos
```

## 📦 Requisitos

- Python 3.x
- SQLite3 (incluido en Python)

## 🎯 Uso

```bash
python main.py
```

### Menú de Opciones

1. **Ingresar gasto** - Registra un nuevo gasto
2. **Mostrar gastos** - Lista todos los gastos
3. **Filtrar gastos** - Busca gastos por fecha
4. **Filtrar suma de gastos por fecha** - Total de una fecha específica
5. **Filtrar suma de gastos por rango de fechas** - Total en un rango de fechas
6. **Salir** - Cierra el programa

## 📁 Estructura del Proyecto

```
Calculo_gastos/
├── main.py              # Punto de entrada principal
├── Ingreso_gasto.py     # Función para registrar gastos
├── mostrar_gastos.py    # Función para mostrar gastos
├── filtrar_gastos.py    # Funciones de filtrado y suma
├── coneccion.py         # Conexión a la base de datos
├── opciones.py          # Menú de opciones
└── gastos.db            # Base de datos SQLite (se crea automáticamente)
```


## 📝 Ejemplo de Uso

```
BIENVENIDO SISTEMA DE GASTOS 💵

MENU DE OPCIONES

1. Ingresar gasto
2. Mostrar gastos
3. Filtrar gastos
4. Filtrar suma de gastos por fecha
5. Filtrar suma de gastos por rango de fechas

Ingrese una opcion: 1
Ingrese el nombre del gasto: Supermercado
Ingrese el monto del gasto: 150.50
Ingrese la fecha (YYYY-MM-DD) o presione Enter para usar hoy: 2024-01-15
✓ Gasto 'Supermercado' de S/150.50 registrado correctamente para la fecha 2024-01-15
```

## 🗄️ Base de Datos

La base de datos `gastos.db` se crea automáticamente con la siguiente estructura:

- **fecha**: Fecha del gasto (TEXT)
- **nombre_gasto**: Nombre del gasto (TEXT)
- **monto_gasto**: Monto del gasto (REAL)

## 👨‍💻 Autor

Desarrollado con ❤️ para gestión personal de gastos.

