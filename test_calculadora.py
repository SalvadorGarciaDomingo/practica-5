import unittest
from calculadora import suma
from calculadora import resta
from calculadora import multiplicacion
from calculadora import division


class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(suma(3, 2), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(-1, -1), -2)
        self.assertEqual(suma(258963147, 147852369), 406815516)

    def test_restar(self):
        self.assertEqual(resta(3, 2), 1)
        self.assertEqual(resta(-1, 1), -2)
        self.assertEqual(resta(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicacion(3, 2), 6)
        self.assertEqual(multiplicacion(-1, 1), -1)
        self.assertEqual(multiplicacion(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(division(4, 2), 2)
        self.assertEqual(division(9, -3), -3)
        self.assertEqual(division(0, 2), 0)
        self.assertEqual(division(7, 0), {"message": "No se puede dividir entre 0"})
if __name__ == '__main__':
 unittest.main()