# programa_CRM_/main.py

from usuarios import Usuario, BuscadorUsuario, ListadoUsuarios
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
        
        elif opcion == "2":
            print("\n=== BUSCAR USUARIO ===")
            print("1. Buscar por email")
            print("2. Buscar por nombre")
            metodo = input("Seleccione método de búsqueda: ").strip()

            buscador = BuscadorUsuario()
            if metodo == "1":
                email = input("Ingrese email: ").strip()
                usuario = buscador.buscar_por_email(email)
                if usuario:
                    print("\n--- USUARIO ENCONTRADO ---")
                    print(f"ID: {usuario[0]}")
                    print(f"Nombre: {usuario[1]} {usuario[2]}")
                    print(f"Email: {usuario[3]}")
                    print(f"Teléfono: {usuario[4] or 'No especificado'}")
                    print(f"Dirección: {usuario[5] or 'No especificado'}")
                    print(f"Fecha de registro: {usuario[6].strftime('%d/%m/%Y')}")
                else:
                    print("No se encontró ningún usuario con ese email.")

            elif metodo == "2":
                nombre = input("Ingrese nombre: ").strip()
                resultados = buscador.buscar_por_nombre(nombre)
                if resultados:
                    print(f"\n--- {len(resultados)} resultado(s) encontrados ---")
                    for u in resultados:
                        print(f"\nID: {u[0]}")
                        print(f"Nombre: {u[1]} {u[2]}")
                        print(f"Email: {u[3]}")
                        print(f"Teléfono: {u[4] or 'No especificado'}")
                        print(f"Dirección: {u[5] or 'No especificado'}")
                        print(f"Fecha de registro: {u[6].strftime('%d/%m/%Y')}")
                else:
                    print("No se encontraron usuarios con ese nombre.")
            else:
                print("Método de búsqueda no válido.")

            buscador.cerrar()

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

        elif opcion == "4":
            print("\n=== LISTA DE USUARIOS ===")
            listado = ListadoUsuarios()
            usuarios = listado.obtener_todos()
            if usuarios:
                for idx, u in enumerate(usuarios, start=1):
                    print(f"\nUsuario #{idx}:")
                    print(f"ID: {u[0]}")
                    print(f"Nombre: {u[1]} {u[2]}")
                    print(f"Email: {u[3]}")
                    print(f"Teléfono: {u[4] or 'No especificado'}")
                    print(f"Fecha de registro: {u[5].strftime('%d/%m/%Y')}")
                print(f"\nTotal de usuarios registrados: {len(usuarios)}")
            else:
                print("No hay usuarios registrados.")

            listado.cerrar()

                elif opcion == "5":
            from facturas import FacturasUsuario

            print("\n=== FACTURAS POR USUARIO ===")
            email = input("Ingrese email del usuario: ").strip()
            try:
                f = FacturasUsuario(email)
                facturas = f.obtener_facturas()

                print(f"\n--- FACTURAS DE {f.usuario[1]} {f.usuario[2]} ---")
                if facturas:
                    total = 0
                    pendiente = 0
                    for idx, fac in enumerate(facturas, start=1):
                        print(f"\nFactura #{idx}:")
                        print(f"Número: {fac[0]}")
                        print(f"Fecha: {fac[1].strftime('%d/%m/%Y %H:%M')}")
                        print(f"Descripción: {fac[2]}")
                        print(f"Monto: ${fac[3]:.2f}")
                        print(f"Estado: {fac[4]}")
                        total += fac[3]
                        if fac[4] == "Pendiente":
                            pendiente += fac[3]

                    print(f"\nTotal de facturas: {len(facturas)}")
                    print(f"Monto total facturado: ${total:.2f}")
                    print(f"Monto pendiente: ${pendiente:.2f}")
                else:
                    print("Este usuario no tiene facturas registradas.")
                f.cerrar()
            except ValueError as e:
                print(f"Error: {e}")


        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
