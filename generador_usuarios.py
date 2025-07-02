# programa_CRM_/generador_usuarios.py

from usuarios import Usuario
from faker import Faker
import random

# Generador de usuarios de prueba utilizando Faker
# Este script crea una cantidad especificada de usuarios con datos aleatorios
class GeneradorUsuarios:
    def __init__(self, cantidad=5):
        self.cantidad = cantidad
        self.faker = Faker('es_ES')
        self.generar_usuarios()

    def generar_usuarios(self):
        for i in range(self.cantidad):
            try:
                nombre = self.faker.first_name()
                apellidos = self.faker.last_name() + " " + self.faker.last_name()
                email = self.faker.unique.email()
                telefono = random.choice([self.faker.phone_number(), None])
                direccion = random.choice([self.faker.address(), None])

                Usuario(nombre, apellidos, email, telefono, direccion)
            except ValueError as e:
                print(f"Error al crear usuario de prueba: {e}")

if __name__ == "__main__":
    GeneradorUsuarios(cantidad=10)