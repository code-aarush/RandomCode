import random

def selectionSort(myList):
    for i in range (len(myList)):
        min_index = i 
        for j in range(i+1, len(myList)):
            if myList[min_index] > myList[j]:
                min_index = j 
        print(myList)
        myList[i],myList[j] = myList[j], myList[i]
    return myList

myList = [random.randint(0,100) for i in range(10)]
print(selectionSort(myList))