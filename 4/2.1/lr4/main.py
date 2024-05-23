from lab2 import *

numb = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14]
print("Масив до обробки:\t\t" + str(numb))
result = module1.swap_negatives(numb)
print("Масив після обробки:\t" + str(result))

arr = [64, 34, 25, 12, 22, 11, 90]
print("Масив до сортування:", arr)
module2.descending_insertion_sort(arr)
print("Масив після сортування:", arr)

# Створити анонімну функцію для обчислення функції f = ((3x)\(y^4))-2z
result = module3.lmbd(2, 3, 4)
print("Результат = " + str(result))