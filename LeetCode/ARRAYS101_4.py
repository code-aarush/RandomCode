def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 2
        else:
            i += 1
    
    return(arr)

arr = [3,5,0,6,5,0,3,0,5]

print(duplicateZeros(arr))