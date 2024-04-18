import unittest
from calculadora import suma
from calculadora import resta
from calculadora import multiplicacion
from calculadora import division
#importamos las funciones de calculadora para hacer las pruebas unitarias

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(suma(3, 2), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)

        #vemos si hay algun problema con numeros negativos , no pruebo valores limite ya que en Python 3 no hay límite de tamaño de estos números.

    def test_restar(self):
        self.assertEqual(resta(3, 2), 1)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(-1, -1), 0)

        #vemos si hay algun problema con numeros negativos y problemas con los signos

    def test_multiplicar(self):
        self.assertEqual(multiplicacion(3, 2), 6)
        self.assertEqual(multiplicacion(-1, 1), -1)
        self.assertEqual(multiplicacion(-1, -1), 1)

        #vemos si hay algun problema con numeros negativos y problemas con los signos

    def test_dividir(self):
        self.assertEqual(division(4, 2), 2)
        self.assertEqual(division(9, -3), -3)
        self.assertEqual(division(0, 2), 0)
        self.assertEqual(division(7, 0), {"message": "No se puede dividir entre 0"})

        #vemos si hay problemas con dividir entre numero negativos, dividir un 0 y dividir entre 0
if __name__ == '__main__':
 unittest.main()