# conexion.py
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class ConexionMySQL:
    def __init__(self):
        load_dotenv()  # Cargar .env
        try:
            self.conexion = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
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