import random

def bubble(my_arr):
    for i in range(len(my_arr)-1):
        for j in range(len(my_arr) - i -1):
            if my_arr[j] > my_arr[j + 1]:
                my_arr[j], my_arr[j + 1] = my_arr[j + 1], my_arr[j]
            print(my_arr)
    return my_arr

my_arr = [random.randint(0,100) for i in range(10)]
print(my_arr)

bubble(my_arr)
print(my_arr)