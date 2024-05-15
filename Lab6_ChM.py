import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функция под интегралом
def f(x):
    return (x + 3) / (x * (x - 2) * (x + 2))

# Точное значение интеграла
exact_value = (1/8) * (7 * np.log(3) - np.log(5) - 6 * np.log(2))

# Метод прямоугольников
def rectangle_method(f, a, b, n, method='mid'):
    h = (b - a) / n
    result = 0
    for i in range(n):
        if method == 'left':
            result += f(a + i * h)
        elif method == 'right':
            result += f(a + (i + 1) * h)
        elif method == 'mid':
            result += f(a + (i + 0.5) * h)
    return result * h

# Метод трапеций
def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Метод Симпсона (парабол)
def simpson_method(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        result += f(a + i * h) * (4 if i % 2 != 0 else 2)
    return result * (h / 3)

# Параметры интегрирования
a, b = 3, 4
n_values = [4, 8, 16, 32, 64]# количество итераций

# Сравнение методов и построение графиков погрешности
errors = {'левый': [], 'правый': [], 'средний': [], 'трапеция': [], 'симпсон': []}
for n in n_values:
    errors['левый'].append(np.abs(rectangle_method(f, a, b, n, 'left') - exact_value))
    errors['правый'].append(np.abs(rectangle_method(f, a, b, n, 'right') - exact_value))
    errors['средний'].append(np.abs(rectangle_method(f, a, b, n, 'mid') - exact_value))
    errors['трапеция'].append(np.abs(trapezoid_method(f, a, b, n) - exact_value))
    errors['симпсон'].append(np.abs(simpson_method(f, a, b, n) - exact_value))


plt.figure(figsize=(12, 7))
for method, error_values in errors.items():
    plt.plot(n_values, error_values, label=f'{method.capitalize()} метод')

plt.xlabel('Количество итераций (n)')
plt.ylabel('Абсолютная ошибка')
plt.legend()
plt.grid(True)
plt.show()
