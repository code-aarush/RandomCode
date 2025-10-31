def merge(nums1, m, nums2, n):
    del nums1[m : len(nums1)]
    for num in nums2:
        nums1.append(num)
    nums1.sort()
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))
