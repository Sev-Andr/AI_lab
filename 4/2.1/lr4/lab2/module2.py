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