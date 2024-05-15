import numpy as np

xi = np.array([0.341, 0.343, 0.345, 0.347, 0.349])
yi = np.array([2.19280, 2.20293, 2.21309, 2.22331, 2.23347])


h = xi[1] - xi[0]

#Первая производная
def first_derivative(yi, h):
    f_prime = [(yi[1] - yi[0]) / h]
    f_prime += [(yi[i+1] - yi[i-1]) / (2*h) for i in range(1, len(yi)-1)]
    f_prime += [(yi[-2] - yi[-3]) / h]
    return f_prime

#Вторая производная
def second_derivative(yi, h):
    f_double = [(yi[i+1] - 2*yi[i] + yi[i-1]) / np.power(h,2) for i in range(1, len(yi)-1)]
    f_double.insert(0, None)
    f_double.append(None)
    return f_double

df = first_derivative(yi, h)
d2f = second_derivative(yi, h)

print("Первая производная:", df)
print("Вторая производная:", d2f[:-1])

