import math
import matplotlib.pyplot as plt
def determinant(matrix):
    num_row, num_col = len(matrix), len(matrix[0])
    
    if num_row != num_col:
        return None
    
    if num_row == 1:
        return matrix[0][0]
    
    det = 0
    for c in range(num_col):
        sub_matrix = [[matrix[i][j] for j in range(num_col) if j != c] for i in range(1, num_row)]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    
    return det

def condition_number(matrix):
    det_A = determinant(matrix)
    
    if det_A == 0:
        return float('inf')
    
    inverse_matrix = [[matrix[j][i] / det_A for i in range(len(matrix))] for j in range(len(matrix))]
    
    return abs(determinant(matrix)) * determinant(inverse_matrix)

# Пример использования функции
A = [[4, 2, 1],
     [3, 1, 2],
     [2, 5, 3]]

cond_num = condition_number(A)
print(f"Число обусловленности матрицы: {cond_num}")


# Функция f(x) = 2*x^2 - 5*x + 3
def f(x):
    return 2*x**2 - 5*x + 3

# Производная функции f(x) = 4*x - 5
def df(x):
    return 4*x - 5

# Первое достаточное условие: f(a) * f(b) < 0
def sufficient_condition(a, b):
    return f(a) * f(b) < 0

# Критерий окончания итерационного процесса (анализируем норму разницы)
def stop_criterion(x, x_prev, epsilon):
    return abs(x - x_prev) < epsilon

# Метод итерации - простая итерация
def simple_iteration_method(x0, epsilon):
    x = x0
    x_prev = x
    iterations = 0
    
    while True:
        x = x - f(x) / df(x)
        iterations += 1
        
        if stop_criterion(x, x_prev, epsilon):
            break
            
        x_prev = x
    
    return x, iterations

# Начальные приближения
x0_values = [0.5, 1.5, 2.5]

# Точности
eps_values = [1e-2, 1e-3, 1e-4]

# Результаты для каждой точности и начального приближения
results = {}

for eps in eps_values:
    results[eps] = {}
    for x0 in x0_values:
        root, iterations = simple_iteration_method(x0, eps)
        results[eps][x0] = (root, iterations)

# Графики зависимости количества итераций от нормы разности точного решения и начального приближения


for eps in eps_values:
    for x0 in x0_values:
        diffs = []
        iterations = []
        for i in range(1, 100):
            root, iters = simple_iteration_method(x0, eps)
            diffs.append(abs(root - x0))
            iterations.append(iters)
            x0 += 0.1
        
        plt.figure()
        plt.plot(diffs, iterations)
        plt.title(f"Iterations vs. Difference for epsilon = {eps} and x0 = {x0}")
        plt.xlabel("Difference")
        plt.ylabel("Iterations")
        plt.show()
