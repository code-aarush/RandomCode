from merge import merge
import random

def mergeSort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[0 : mid]
    right = arr[mid : len(arr)]
    
    sorted_left = mergeSort(left)
    sorted_right = mergeSort(right)

    return merge(sorted_left, sorted_right) 
    
arr = [random.randint(0,1000) for i in range(100)]

print(mergeSort(arr))
