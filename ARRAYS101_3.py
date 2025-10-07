def sortedSquares(nums):
    newArr = []
    for num in nums : 
        newArr.append(num**2)
     
    newArr.sort()
    return newArr

nums = [-4,-1,0,4,6,7]

print(sortedSquares(nums))