# conexion.py
import mysql.connector
from mysql.connector import Error

class ConexionMySQL:
    def __init__(
        self,
        host='127.0.0.1',
        user='root',
        password='Majo.bnr13',
        database='crm',
        port=3306
    ):
        try:
            self.conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error en la conexión a MySQL: {e}")

    def obtener_cursor(self):
        return self.conexion.cursor()

    def confirmar(self):
        self.conexion.commit()

    def cerrar(self):
        if self.conexion.is_connected():
            self.conexion.close()