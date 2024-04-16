import numpy
import numpy as np


class GaussElimination:
    def __init__(self, A: numpy.ndarray, b: numpy.ndarray) -> None:
        """
        Initializes the class with the coefficient matrix A and constant terms vector b
        Args:
            A (numpy.ndarray): the coefficient matrix A
            b (numpy.ndarray): the constant terms vector b
        """
        if not A.shape == (len(b), len(b)):
            raise ValueError("matrix A and vector b must have the same dimension (n x n).")
        self.A = A.astype(float)
        self.b = b.astype(float)
        self.n = len(b)

    def forward_elimination(self, augmented_matrix: numpy.ndarray) -> numpy.ndarray:
        """
        Performs forward_elimination step of Gaussian elimination.

        Parameters:
            augmented_matrix (numpy.ndarray): Augmented coefficient matrix.
        Returns:
            augmented_matrix (numpy.ndarray): Augmented coefficient matrix after forward elimination.
        """
        for i in range(self.n):
            max_index = np.argmax(abs(augmented_matrix[i:, i])) + i
            if max_index != i:
                augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]

            for j in range(i+1, self.n):
                ratio = augmented_matrix[j, i] / augmented_matrix[i, i]
                augmented_matrix[j, i:] -= ratio * augmented_matrix[i, i:]

        return augmented_matrix

    def back_substitution(self, augmented_matrix: numpy.ndarray) -> numpy.ndarray:
        """
        Performs back substitution step of Gaussian elimination.

        Parameters:
            augmented_matrix (numpy.ndarray): Augmented coefficient matrix.
        Returns:
            x (numpy.ndarray): Solution vector.
        """
        x = np.zeros(self.n)
        for i in range(self.n-1, -1, -1):
            x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i + 1:self.n], x[i + 1:])) / augmented_matrix[i, i]
        return x

    def solve(self) -> np.ndarray:
        """
        Solves the system of linear equations Ax = b using Gaussian elimination with diagonal pivot
        Returns:
           x (numpy.ndarray): Solution vector.
        """
        augmented_matrix = np.concatenate((self.A, self.b.reshape(self.n, 1)), axis=1)
        augmented_matrix = self.forward_elimination(augmented_matrix)
        x = self.back_substitution(augmented_matrix)
        return x
