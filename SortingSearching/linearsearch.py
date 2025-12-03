def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i]
        else: 
            return "Target not found"
        
target = int(input("Enter the number you want to find: "))
arr = [1,2,3,4,5,6,7,8,9,10]


