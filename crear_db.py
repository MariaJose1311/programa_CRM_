# programa_CRM_/crear_db.py

from conexion import ConexionMySQL

class CrearBaseDeDatos:
    def __init__(self):
        self.db = ConexionMySQL()
        self.cursor = self.db.obtener_cursor()
        self.crear_tabla_usuarios()
        self.crear_tabla_facturas()
        self.db.confirmar()
        self.db.cerrar()

    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id VARCHAR(10) PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                apellidos VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                telefono VARCHAR(20),
                direccion VARCHAR(255),
                fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("Tabla 'usuarios' creada o ya existe.")

    def crear_tabla_facturas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS facturas (
                numero VARCHAR(10) PRIMARY KEY,
                usuario_id VARCHAR(10),
                fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
                descripcion TEXT,
                monto FLOAT CHECK (monto > 0),
                estado ENUM('Pendiente', 'Pagada', 'Cancelada'),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
            )
        """)
        print("Tabla 'facturas' creada o ya existe.")

# Ejecutar solo si se llama directamente
if __name__ == "__main__":
    CrearBaseDeDatos()