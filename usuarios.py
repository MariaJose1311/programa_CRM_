# programa_CRM_/usuarios.py

import re
from conexion import ConexionMySQL

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
