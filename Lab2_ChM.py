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


A = [[12, 7, 1, 1],
     [4, 8, 3, 1],
     [3, 3, 8, 1],
     [3,1,0,5]]

cond_num = condition_number(A)
print(f"Число обусловленности матрицы: {cond_num}")


#Функция f(x) = 2*x^2 - 5*x + 3
def f(x):
    return 2*x**2 - 5*x + 3

#производная функции f(x) = 4*x - 5
def df(x):
    return 4*x - 5

#первое достаточное условие: f(a) * f(b) < 0
def sufficient_condition(a, b):
    return f(a) * f(b) < 0

#критерий окончания итерационного процесса (анализируем норму разницы)
def stop_criterion(x, x_prev, epsilon):
    return abs(x - x_prev) < epsilon

#Метод итерации - простая итерация
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

#начальные приближения
x0_values = [0.5, 1.5, 2.5]

#точности
eps_values = [1e-2, 1e-3, 1e-4]
#результаты для каждой точности и начального приближения
results = {}
for eps in eps_values:
    results[eps] = {}
    for x0 in x0_values:
        root, iterations = simple_iteration_method(x0, eps)
        results[eps][x0] = (root, iterations)

#графики зависимости количества итераций от нормы разности точного решения и начального приближения
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
        plt.title(f" ε = {eps} и x0 = {x0}")
        plt.xlabel("Нормы разници")
        plt.ylabel("Итерации")
        plt.show()
#/////////////////////////////////////

def simple_iteration(A, b, x0, tol=1e-6, max_iter=100):

    n = len(A)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    x_new[i] -= A[i][j] * x[j]
            x_new[i] += b[i]
            x_new[i] /= A[i][i]
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < tol:
            return x_new
        x = x_new
    return x
#Метод Гаусса-Зейделя

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    for _ in range(max_iter):
        for i in range(n):
            x[i] = b[i]
            for j in range(i):
                x[i] -= A[i][j] * x[j]
            for j in range(i+1, n):
                x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]
        if max([abs(x[i] - x0[i]) for i in range(n)]) < tol:
            return x
        x0 = x
    return x
#Метод Якоби

def jacobi(A, b, x0, tol=1e-6, max_iter=100):

    n = len(A)
    x = x0.copy()
    for _ in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    x_new[i] -= A[i][j] * x[j]
            x_new[i] += b[i]
            x_new[i] /= A[i][i]
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < tol:
            return x_new
        x = x_new
    return x

# Проверка выполнения достаточных условий и критериев сходимости

def check_convergence(A):

    n = len(A)
    for i in range(n):
        row_sum = 0
        for j in range(n):
            if i != j:
                row_sum += abs(A[i][j])
        if abs(A[i][i]) < row_sum:
            return False
    return True
#Ведение расчётов до достижения точности 10^-2, 10^-3, 10^-4

def solve_with_accuracy(A, b, x0, tol, max_iter=100):

    n = len(A)
    x = x0.copy()
    iter_count = 0
    while True:
        iter_count += 1
        x_new = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    x_new[i] -= A[i][j] * x[j]
            x_new[i] += b[i]
            x_new[i] /= A[i][i]
        if max([abs(x_new[i] - x[i]) for i in range(n)]) < tol:
            return x_new, iter_count
        x = x_new
        
        if iter_count >= max_iter:
            return x, iter_count
#Оценка влияния выбора начального приближения на количество итераций

def plot_convergence(A, b, tol, methods):

    n = len(A)
    x_exact = gauss_seidel(A, b, [0] * n, tol=1e-10)  

    norms = [i / 10 for i in range(1, 11)]
    iter_counts = [[0] * len(norms) for _ in range(len(methods))]

    #Итерации по нормам
    for i, norm in enumerate(norms):
        #по методам
        for j, method in enumerate(methods):
            #по начальным приближениям
            for k in range(10):
                x0 = [x_exact[i] + norm * (2 * k - 9) / 10 for i in range(n)]
                _, iter_count = solve_with_accuracy(A, b, x0, tol)
                iter_counts[j][i] += iter_count / 10

    #графики
    for j, method in enumerate(methods):
        print(method,": ", norms)
        plt.plot(norms, iter_counts[j], label=method)
        plt.xlabel("Норма разности точного решения и начального приближения")
        plt.ylabel("Количество итераций")
        plt.legend()
        plt.show()


#A = [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
b = [4, 4, 4,4]
tol = 1e-4
methods = ["Простая итерация", "Метод Гаусса-Зейделя", "Метод Якоби"]

plot_convergence(A, b, tol, methods)

