# programa_CRM_/facturas.py

from conexion import ConexionMySQL
import datetime

class Factura:
    ESTADOS_VALIDOS = ['Pendiente', 'Pagada', 'Cancelada']

    def __init__(self, email_usuario, descripcion, monto, estado):
        self.usuario_id = self.obtener_id_usuario(email_usuario)
        self.validar_campos(descripcion, monto, estado)
        self.descripcion = descripcion
        self.monto = float(monto)
        self.estado = estado
        self.numero = self.generar_numero()
        self.insertar_en_bd()

    def obtener_id_usuario(self, email):
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        resultado = cursor.fetchone()
        conexion.cerrar()
        if not resultado:
            raise ValueError("El usuario con ese email no existe.")
        return resultado[0]

    def validar_campos(self, descripcion, monto, estado):
        if not descripcion.strip():
            raise ValueError("La descripción es obligatoria.")
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser mayor que cero.")
        except ValueError:
            raise ValueError("El monto debe ser un número válido mayor que cero.")

        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(self.ESTADOS_VALIDOS)}")

    def generar_numero(self):
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("SELECT COUNT(*) FROM facturas")
        total = cursor.fetchone()[0] + 1
        conexion.cerrar()
        return f"FAC{total:03d}"

    def insertar_en_bd(self):
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("""
            INSERT INTO facturas (numero, usuario_id, descripcion, monto, estado)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.numero, self.usuario_id, self.descripcion, self.monto, self.estado))
        conexion.confirmar()
        conexion.cerrar()
        print(f"Factura creada exitosamente con número: {self.numero}")

# Obtener facturas de un usuario específico

class FacturasUsuario:
    def __init__(self, email):
        self.email = email
        self.db = ConexionMySQL()
        self.cursor = self.db.obtener_cursor()
        self.usuario = self.obtener_usuario()

    def obtener_usuario(self):
        self.cursor.execute("SELECT id, nombre, apellidos FROM usuarios WHERE email = %s", (self.email,))
        usuario = self.cursor.fetchone()
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        return usuario

    def obtener_facturas(self):
        self.cursor.execute("""
            SELECT numero, fecha_emision, descripcion, monto, estado
            FROM facturas
            WHERE usuario_id = %s
            ORDER BY fecha_emision
        """, (self.usuario[0],))
        return self.cursor.fetchall()

    def cerrar(self):
        self.db.cerrar()
