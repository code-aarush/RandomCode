def max_consecutive_ones(nums) :
    max_val = 0
    current_val = 0
        
    for num in nums :
        if num == 1 :
            current_val += 1
        else: 
            if current_val > max_val :
                max_val = current_val
                current_val = 0
        
    if current_val > max_val :
        max_val = current_val
        
    return max_val

my_arr = [1,1,0,1,1,1]
print(max_consecutive_ones(my_arr))
