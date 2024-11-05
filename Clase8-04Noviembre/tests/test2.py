import unittest

def test_isgreater(self):
    self.assertGreater(100,10)


class TestExamples(unittest.TestCase):
    def test_if_true(self):
        # Afirmo que es verdadero, esta prueba va a pasar porque es "true"
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
