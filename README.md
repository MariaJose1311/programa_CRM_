# programa_CRM_

Un sistema CRM básico por consola en Python que permite la gestión de usuarios y sus facturas asociadas, con conexión a MySQL. Incluye registro, búsqueda, facturación, reportes y más.

## Instalación

```bash
pip install -r requirements.txt
```

## Características

### Registrar usuarios
- Permite registrar nuevos usuarios con nombre, apellidos, email (único), teléfono y dirección.
- Genera un ID automático (USR001, USR002, etc.).
- Valida emails, campos obligatorios y formato.

### Crear facturas
- Permite asociar facturas a usuarios existentes.
- ID autogenerado (FAC001, FAC002, etc.).
- Requiere descripción, monto (> 0), y estado (Pendiente, Pagada, Cancelada).

### Búsqueda de usuarios
- Buscar por email exacto o por nombre parcial.
- Muestra todos los datos del usuario encontrado.

### Mostrar todos los usuarios
- Lista a todos los usuarios registrados con su información básica.

### Mostrar facturas de un usuario
- Muestra todas las facturas asociadas a un usuario, con detalles y totales.

### Resumen financiero
- Resumen por usuario: total facturas, pagadas, pendientes.
- Resumen general: total usuarios, facturas, ingresos totales y pendientes.

## Estructura del Proyecto

```
programa_CRM_/
programa_CRM_/
├── tests/
│   └── test_crm.py
├── main.py                 # Menú principal del sistema
├── usuarios.py             # Clase Usuario + búsquedas y listados
├── facturas.py             # Clase Factura + resúmenes
├── conexion.py             # Clase para conexión con MySQL
├── crear_db.py             # Crea las tablas en la base de datos
├── generador_usuarios.py   # Carga usuarios aleatorios de prueba
├── requirements.txt        # Librerías necesarias
├── setup.py                # Configuración como paquete
├── README.md               # Readme del programa
└── __init__.py             # Archivo de inicialización
```

## Uso

### Ejecutar el sistema
```python

python main.py

# Desde el menú podrás:
'''
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
'''
# Crear las tablas (una sola vez)
python crear_db.py

# Generar usuarios de prueba
python generador_usuarios.py
```

## Desarrollo

1. Clona este repositorio
2. Crea un entorno virtual:
   ```bash
   python -m venv crm_env
   .\crm_env\Scripts\activate  # En Windows
   source crm_env/bin/activate # En Linux/Mac
   ```
3. Instala las dependencias de desarrollo:
   ```bash
   pip install -r requirements.txt
   ```
4. Crea la base de datos MySQL:
   ```sql
   CREATE DATABASE crm;
   ```
5. Ejecuta crear_db.py para crear las tablas.

## Ejecutar Pruebas
Este proyecto incluye pruebas funcionales básicas para verificar el flujo completo (registro de usuario + factura).

1. Asegúrate de tener una base de datos llamada `crm` creada.
2. Ejecuta el siguiente comando desde la raíz del proyecto:

```bash
python -m unittest tests/test_fechas.py
```

## Buenas Prácticas Implementadas

1. **Programación Orientada a Objetos**: Clases para Usuario y Factura.
2. **Validaciones**: Formato de email, campos obligatorios, unicidad.
3. **Autogeneración de IDs**: Secuencias USR001, FAC001, etc.
4. **Separación de responsabilidades**: Módulos independientes por entidad.
5. **Conexión MySQL**: Reutilizable y encapsulada.
6. **Código Limpio**: Clara organización y consistencia.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
