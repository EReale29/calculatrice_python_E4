import unittest
from calculatrice import ajouter, soustraire, multiplier, diviser

class TestCalculator(unittest.TestCase):
    def test_ajouter(self):
        self.assertEqual(ajouter(2, 3), 5)
        self.assertEqual(ajouter(-1, 1), 0)
        self.assertEqual(ajouter(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(soustraire(5, 3), 2)
        self.assertEqual(soustraire(1, 1), 0)
        self.assertEqual(soustraire(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(-1, 5), -5)
        self.assertEqual(multiplier(0, 10), 0)

    def test_divide(self):
        self.assertEqual(diviser(6, 3), 2)
        self.assertEqual(diviser(10, 2), 5)
        self.assertEqual(diviser(0, 5), 0)
        self.assertEqual(diviser(5, 0), "Erreur : Division par zéro")

def main():
    unittest.main()

if __name__ == '__main__':
    main()