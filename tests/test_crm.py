# programa_CRM_/tests/test_crm.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from usuarios import Usuario, BuscadorUsuario
from facturas import Factura, FacturasUsuario
import random

class TestCRM(unittest.TestCase):

    def setUp(self):
        # Generar email único por ejecución
        num = random.randint(1000, 9999)
        self.email = f"test{num}@example.com"
        self.nombre = "Test"
        self.apellidos = "User"
        self.telefono = "123456"
        self.direccion = "Calle Falsa 123"
        self.descripcion = "Servicio de prueba"
        self.monto = 100.0
        self.estado = "Pendiente"

    def test_crear_usuario_y_factura(self):
        # Crear usuario
        usuario = Usuario(
            nombre=self.nombre,
            apellidos=self.apellidos,
            email=self.email,
            telefono=self.telefono,
            direccion=self.direccion
        )

        # Verificar que el usuario existe en base de datos
        buscador = BuscadorUsuario()
        resultado = buscador.buscar_por_email(self.email)
        buscador.cerrar()

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[3], self.email)

        # Crear factura
        factura = Factura(
            email_usuario=self.email,
            descripcion=self.descripcion,
            monto=self.monto,
            estado=self.estado
        )

        # Verificar que la factura se asoció correctamente
        facturas = FacturasUsuario(self.email)
        datos_facturas = facturas.obtener_facturas()
        facturas.cerrar()

        self.assertTrue(any(f[2] == self.descripcion and f[4] == self.estado for f in datos_facturas))

if __name__ == "__main__":
    unittest.main()
