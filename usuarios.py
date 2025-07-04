# programa_CRM_/usuarios.py

import re
from conexion import ConexionMySQL

# Clase Usuario para gestionar el registro y validación de usuarios en el CRM

class Usuario:
    def __init__(self, nombre, apellidos, email, telefono=None, direccion=None):
        self.validar_campos(nombre, apellidos, email)
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.id = self.generar_id()
        self.insertar_en_bd()

    def validar_campos(self, nombre, apellidos, email):
        if not all([nombre.strip(), apellidos.strip(), email.strip()]):
            raise ValueError("Nombre, apellidos y email son obligatorios.")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Formato de email inválido.")

        # Verificar unicidad del email
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            raise ValueError("El email ya está registrado.")
        conexion.cerrar()

    def generar_id(self):
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        total = cursor.fetchone()[0] + 1
        conexion.cerrar()
        return f"USUARIO{total:03d}"

    def insertar_en_bd(self):
        conexion = ConexionMySQL()
        cursor = conexion.obtener_cursor()
        cursor.execute("""
            INSERT INTO usuarios (id, nombre, apellidos, email, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (self.id, self.nombre, self.apellidos, self.email, self.telefono, self.direccion))
        conexion.confirmar()
        conexion.cerrar()
        print(f"Usuario registrado exitosamente con ID: {self.id}")

# Buscar usuarios por email o nombre

class BuscadorUsuario:
    def __init__(self):
        self.db = ConexionMySQL()
        self.cursor = self.db.obtener_cursor()

    def buscar_por_email(self, email):
        self.cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        return self.cursor.fetchone()

    def buscar_por_nombre(self, nombre):
        self.cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", (f"%{nombre}%",))
        return self.cursor.fetchall()

    def cerrar(self):
        self.db.cerrar()

# Obtener listado de usuarios

class ListadoUsuarios:
    def __init__(self):
        self.db = ConexionMySQL()
        self.cursor = self.db.obtener_cursor()

    def obtener_todos(self):
        self.cursor.execute("SELECT id, nombre, apellidos, email, telefono, fecha_registro FROM usuarios")
        return self.cursor.fetchall()

    def cerrar(self):
        self.db.cerrar()
