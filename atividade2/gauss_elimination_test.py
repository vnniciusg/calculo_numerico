import unittest
import numpy as np
from gauss_elimination import GaussElimination


class LinearSystemTestCase(unittest.TestCase):
    def test_valid_dimensions(self):
        """
        Test case to ensure matrices have the same dimensions.
        """
        A = np.array([[2, 1], [3, 4]])
        b = np.array([5, 4, 5])
        with self.assertRaises(ValueError):
            GaussElimination(A, b)

    def test_solve1(self):
        """
        Test case to verify complete solution using Gaussian elimination with diagonal pivot.
        """
        A = np.array([[2, 4, 3], [1, 2, -2], [4, 4, 3]])
        b = np.array([1, 11, 3])

        expected_x = np.array([1, 2, -3])

        solver = GaussElimination(A.copy(), b.copy())
        x = solver.solve()

        self.assertTrue(np.allclose(x, expected_x))

    def test_solve2(self):
        """
        Test case to verify complete solution using Gaussian elimination with diagonal pivot.
        """
        A = np.array([[1, 2, 1], [-1, 0, 3], [1, -2, 1]])
        b = np.array([0, 5, 1])

        expected_x = np.array([-0.875, -0.25, 1.375])

        solver = GaussElimination(A.copy(), b.copy())
        x = solver.solve()

        self.assertTrue(np.allclose(x, expected_x))


if __name__ == '__main__':
    unittest.main()
