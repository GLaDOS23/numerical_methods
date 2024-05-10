import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                # для каждой x вычисляем term 
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result += term
    return result

def piecewise_linear_interpolation(x, y, x_interp):
    n = len(x)
    for i in range(n-1):#перебираем все x
        if x_interp >= x[i] and x_interp <= x[i+1]:
            #находим нужный интервал
            #по формуле находим значения функции
            slope = (y[i+1] - y[i]) / (x[i+1] - x[i])
            
            return y[i] + slope * (x_interp - x[i])


def original_function(x):
    return np.sqrt(float(2)**x - float(3)**x)

def mean_absolute_error(arr1, arr2):


  
  if len(arr1) != len(arr2):
    raise ValueError("массивы разные")

  mae = 0

  #  абсолютные погрешности
  for i in range(len(arr1)):
    mae += abs(arr1[i] - arr2[i])

  #сред абсолютная погрешность
  mae /= len(arr1)

  return mae


x_nodes = np.array([-5.0, -4.6, -4.2, -3.8,-3.4, -3.0, -2.6, -2.2, -1.8, -1.4, -1.0])
y_nodes = original_function(x_nodes)


x_interp = np.linspace(x_nodes[0], x_nodes[-1], 100)
y_interp_lagrange = [lagrange_interpolation(x_nodes, y_nodes, xi) for xi in x_interp]
y_interp_linear = [piecewise_linear_interpolation(x_nodes, y_nodes, xi) for xi in x_interp]
y_original = original_function(x_interp)


print("Погрешность полинома Лагранжа: ", mean_absolute_error(y_original,y_interp_lagrange))
print( "Погрешность Кусочно-линейной интерполяции: ",mean_absolute_error(y_original,y_interp_linear))



plt.figure(figsize=(12, 6))
plt.plot(x_interp, y_interp_lagrange, label="Интерполяция полиномом Лагранжа")
plt.plot(x_interp, y_interp_linear, label="Кусочно-линейная интерполяция")
plt.plot(x_interp, y_original, label="Оригинальная функция")
plt.scatter(x_nodes, y_nodes, color='red', label="Узлы интерполяции")
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Интерполяция функции на отрезке')
plt.grid(True)
plt.show()
