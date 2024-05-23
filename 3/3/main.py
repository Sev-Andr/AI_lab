import random
def proc(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(text)):
        if text[i] == ' ':
            result += str(alphabet.find(text[i + 1]) + 1)
        else:
            result += text[i]
    return result

A = " he thrusts his fists against the posts and still insists he sees the ghosts."
A1 = A.replace("th", "st")
print(A1)
A2 = proc(A1)
print(A2)

print("-" * 20)
# Задаємо матриці X та Y
X = [[random.randint(-10, 10) for i in range(3)] for i in range(5)]
Y = [[random.randint(-10, 10) for i in range(3)] for i in range(5)]

# Заповнюємо Z нулями
Z = [[0]*3 for i in range(5)]

'''
Z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
'''

# Виконання завдання
for i in range(5):
    for j in range(3):
        if abs(Y[i][j]) >= abs(X[i][j]):
            Z[i][j] = Y[i][j]
        else:
            Z[i][j] = X[i][j]

# Вивід результату
print("Матриця X:")
for row in X:
    print(row)
print("\nМатриця Y:")
for row in Y:
    print(row)
print("\nМатриця Z:")
for row in Z:
    print(row)