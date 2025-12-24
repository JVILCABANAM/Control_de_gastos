
from opciones import mostrar_opciones
from Ingreso_gasto import ingresar_gasto
from mostrar_gastos import mostrar_gastos
from filtrar_gastos import filtrar_gastos, filtrar_suma_gastos_por_fecha, filtrar_por_rango_de_fechas

def main():
    print("💵 BIENVENIDO SISTEMA DE GASTOS 💵")
    
    while True:
        mostrar_opciones()
        opcion = input("👉 Ingrese una opcion: ")

        if opcion == "1":
            ingresar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            filtrar_gastos()
        elif opcion == "4":
            filtrar_suma_gastos_por_fecha()
        elif opcion == "5":
            filtrar_por_rango_de_fechas()
        elif opcion == "6":
            print("👋 Gracias por usar el sistema de gastos 💵")
            break
        else:
            print("Opcion invalida")
        

if __name__ == "__main__":
    main()
