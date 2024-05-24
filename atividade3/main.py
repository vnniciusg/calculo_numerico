from typing import List, Tuple
import numpy as np

def least_squares(x_values: List[int], y_values: List[int], new_x: int) -> Tuple[np.ndarray, int] :

    if len(x_values) != len(y_values) or len(x_values) > 5:
        raise Exception('Erro: x_values e y_values devem ter o mesmo tamanho e x_values deve ter no máximo 5 elementos')

    X = np.column_stack([np.ones(len(x_values)), x_values, np.square(x_values)])
    Y = np.array(y_values)


    coefficients = np.linalg.lstsq(X, Y, rcond=None)[0]

    new_y = coefficients[0] + coefficients[1] * new_x + coefficients[2] * new_x ** 2

    return coefficients, round(new_y, 2)


if __name__ == '__main__':
    
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    new_x = 6

    try:
        coefficients, new_y = least_squares(x_values, y_values, new_x)
        print(f'Coeficiente: {coefficients}')
        print(f'Novo valor de y: {new_y:.2f}')
    except Exception as e:
        print(e)