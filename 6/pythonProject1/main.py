import numpy as np
def get_int_input(prompt): # lr3
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Невірний формат. Введіть число.")

N = get_int_input("Введіть кількість рядків для матриці X (Nх4): ")
M = get_int_input("Введіть кількість стовпців для матриці Y (4xM): ")

X = np.random.rand(N, 4)
Y = np.random.rand(4, M)

print("Матриця Х: ")
print(X)
print("Матриця Y: ")
print(Y)

# Обчислення добутку матриць Z = X * Y
Z = np.dot(X, Y)

# Нормалізація стовпців матриці Z
Z_mean = np.mean(Z, axis=0) # axis - для обчислення по стовпчиках
Z_normalized = Z - Z_mean

# Обчислення дисперсії та визначника матриці Z_normalized
variance = np.var(Z_normalized)
if N == 4 and M == 4:
    determinant = np.linalg.det(Z_normalized)
else:
    determinant = "Incorrect matrix values" + "\nВизначник матриці можна обчислити лише для квадратної матриці, тобто матриці з однаковою кількістю рядків і стовпців."

print("Матриця Z_normalized:")
print(Z_normalized)
print("Дисперсія матриці Z_normalized:", variance)
print("Визначник матриці Z_normalized:", determinant)