
def insertion_sort(array):
    for i in range(len(array)):
        x = array[i]
        j = i

        while j > 0 and array[j-1] > x:
            array[j] = array[j - 1]
            j = j - 1
        array[j] = x
    return array


print(insertion_sort([5,2,9,1,0,2541,-2]))
