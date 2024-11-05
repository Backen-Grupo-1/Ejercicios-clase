import unittest
from CalculatorClass import Calculator

class TestSimpleCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()
        print("Hola soy setUpClass")

    #Devuelve la base original limpia
    @classmethod
    def tearDownClass(cls):
        print("Limpieza después de todos los tests")

    def setUp(self):
        print("Hola soy setUp")

    def test_add_two_integers(self):
        self.assertEqual(2,2)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 5), 10)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(2, 0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)

if __name__ == '__main__':
    unittest.main()