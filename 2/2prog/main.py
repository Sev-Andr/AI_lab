# a + (n-1)*d
# Дано перший член і різницю арифметичної прогресії. Написати рекурсивну функцію
# для знаходження: знаходження n-го члена прогресії;
def func_rec(a, d, n):
    if n == 1:
        return a
    else:
        return d + func_rec(a, d, n-1)
def func(a, d, n):
    return a + (n - 1) * d

a = 1  # перший член прогресії
d = 2  # різниця прогресії
n = 5  # член прогресії, який потрібно знайти

print("Результат з рекурсією = " + str(func_rec(a, d, n)))  # Виводимо n-й член прогресії
# перевірка((3*x) / (y**4)) - 2*z
print("Результат без рекурсії = " + str(func(a, d, n)))  # Виводимо n-й член прогресії

# У масиві X=(x1,x2,...,xn) поміняти місцями перший і другий негативні елементи, третій і
# четвертий негативні елементи тощо.
def swap_negatives(arr):
    fl = False
    first_min_ind = 0
    for index in range(len(arr)):
        if arr[index] < 0 and fl == False:
            # finding the first minimum
            first_min_ind = index
            fl = True
        elif arr[index] < 0 and fl == True:
            # swap
            arr[index], arr[first_min_ind] = arr[first_min_ind], arr[index]
            # normal value
            fl = False
    return arr

numb = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14]
print("Масив до обробки:\t\t" + str(numb))
result = swap_negatives(numb)
print("Масив після обробки:\t" + str(result))


# Створити функцію сортування в порядку убування.
# Сортування включенням
def descending_insertion_sort(arr):
    # починаємо з другого
    for i in range(1, len(arr)):
        key = arr[i]  # key = наш елемент для якого ми шукаємо місце

        # находимо правильне місце для вставки елемента
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Масив до сортування:", arr)
descending_insertion_sort(arr)
print("Масив після сортування:", arr)

# Створити анонімну функцію для обчислення функції f = ((3x)\(y^4))-2z
f = lambda x, y, z: ((3*x) / (y**4)) - 2*z
result = f(2, 3, 4)
print("Результат = " + str(result))