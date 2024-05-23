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
            # normal
            fl = False
    return arr