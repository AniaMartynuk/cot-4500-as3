import unittest
import numpy as np
from src.main.assignment_3 import euler_method, runge_kutta_method, function

class TestNumericalMethods(unittest.TestCase):
    
    def test_euler_method(self):
        t0, y0, t_end, n = 0, 1, 2, 10
        result = euler_method(function, t0, y0, t_end, n)
        self.assertAlmostEqual(result, 1.2446380979332121, places=5)

    def test_runge_kutta_method(self):
        t0, y0, t_end, n = 0, 1, 2, 10
        result = runge_kutta_method(function, t0, y0, t_end, n)
        self.assertAlmostEqual(result, 1.2513165878879806, places=5)

if __name__ == "__main__":
    unittest.main()
