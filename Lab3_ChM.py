import math


def f(x):
    return math.sqrt(2 - math.sqrt(x + 2)) - x

def df(x):
    return -(1 / (2 * math.sqrt(2 - math.sqrt(x + 2)))) - 1

def newton_method(p0, tolerance):
    p = p0
    iteration = 0
    
    while True:
        p_new = p - f(p) / df(p)
        iteration += 1
        
        if abs(p_new - p) < tolerance:
            break
        
        p = p_new
    
    return p_new, iteration



# задаем требуемую точность
tolerance = 1e-10
#  метод Ньютона
solution, iterations = newton_method(0.5, tolerance)

print("Решение: x =", solution)
print("Количество итераций:", iterations)
print('////////////////////////////////////')
#///////////////


def newton_method2(p0, tolerance, max_iterations):
    p = p0
    iteration = 0
    
    while iteration < max_iterations:
        p_new = p - f(p) / df(p)
        iteration += 1
        
        if abs(p_new - p) < tolerance:
            break
        
        p = p_new
    
    return p_new, iteration

#начальное приближение p0
p0 = 0.5
# задаем требуемую точность
tolerance = 1e-16
#максимальное количество итераций
max_iterations = 1000

# Решаем систему уравнений методом Ньютона
solution, iterations = newton_method2(p0, tolerance, max_iterations)

print("Решение: x =", solution)
print("Количество итераций:", iterations)








import numpy as np


def equation(x):
    return np.sqrt(2 - np.sqrt(x + 2)) - x


def derivative(x):
    return -1 / (2 * np.sqrt(x + 2) * np.sqrt(2 - np.sqrt(x + 2))) - 1



def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return None


lower_bound = -1
upper_bound = 1 

# Поиск корней в пределах
roots = []
for x0 in range(lower_bound, upper_bound + 1):
    if x0 % 10 != 0:
        root = newton_method(equation, derivative, x0)
        if root is not None:
            roots.append(root)

print(f"Корни уравнения: {roots}")

