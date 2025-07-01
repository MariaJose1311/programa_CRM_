# programa_CRM_/main.py

from usuarios import Usuario
from facturas import Factura

def mostrar_menu():
    print("\n=== SISTEMA DE CRM ===")
    print("1. Registrar nuevo usuario")
    print("2. Buscar usuario")
    print("3. Crear factura para usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Mostrar facturas de un usuario")
    print("6. Resumen financiero por usuario")
    print("7. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n=== REGISTRO DE NUEVO USUARIO ===")
            try:
                nombre = input("Ingrese nombre: ").strip()
                apellidos = input("Ingrese apellidos: ").strip()
                email = input("Ingrese email: ").strip()
                telefono = input("Ingrese teléfono (opcional): ").strip() or None
                direccion = input("Ingrese dirección (opcional): ").strip() or None
                Usuario(nombre, apellidos, email, telefono, direccion)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            print("\n=== CREAR FACTURA ===")
            try:
                email = input("Ingrese email del usuario: ").strip()
                descripcion = input("Ingrese descripción del servicio/producto: ").strip()
                monto = input("Ingrese monto total: ").strip()
                print("Seleccione estado:")
                print("1. Pendiente")
                print("2. Pagada")
                print("3. Cancelada")
                estados = ["Pendiente", "Pagada", "Cancelada"]
                estado_op = input("Estado: ").strip()
                estado = estados[int(estado_op) - 1]
                Factura(email, descripcion, monto, estado)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")

        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
