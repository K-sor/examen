import unittest
from trapezoid import calcular_area, calcular_perimetro

class TestTrapezoidCalculations(unittest.TestCase):

    # Prueba que debería funcionar
    def test_calcular_area_funciona(self):
        # Esta prueba debería pasar porque 8 y 5 son las bases y 4 la altura
        self.assertEqual(calcular_area(8, 5, 4), 26.0)  # (8 + 5) * 4 / 2 = 26

    # Prueba que debería fallar (para mostrar cómo se maneja el error)
    def test_calcular_area_falla(self):
        # Esta prueba debería fallar porque el resultado correcto es 26, no 30
        self.assertEqual(calcular_area(8, 5, 4), 30.0)  # Este valor debería ser incorrecto

    # Prueba de perímetro que debería funcionar
    def test_calcular_perimetro_funciona(self):
        # Esta prueba debería pasar porque el perímetro es 8 + 5 + 6 + 6 = 25
        self.assertEqual(calcular_perimetro(8, 5, 6, 6), 25)

if __name__ == "__main__":
    unittest.main()
