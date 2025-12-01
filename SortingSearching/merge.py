def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    merged_arr = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            merged_arr.append(left[left_pointer])
            left_pointer += 1
        else:
            merged_arr.append(right[right_pointer])
            right_pointer += 1
    
    if left_pointer == len(left):
        merged_arr.extend(right[right_pointer:])
    else: 
        merged_arr.extend(left[left_pointer:])

    return merged_arr

