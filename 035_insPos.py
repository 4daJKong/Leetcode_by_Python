def searchInsert(nums, target):
    n = len(nums)
    i = 0
    if nums[0] > target:
        return 0
    if nums[n - 1] == target:
        return n - 1
    elif nums[n - 1] < target:
        return n
    for i in range(0, n):
        if nums[i] == target:
            return i   
        if nums[i] < target < nums[i + 1]:
            return i + 1 
#print(int(2 + (2 + 3) / 2))
def searchInsert_demo(nums, target):   
    left = 0
    right = len(nums) 
    if target > nums[-1]:
        return right
    while(left < right):
        mid = int(left + (right - left) / 2)    #or (right + left)/2
        #print(mid)

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1 
                       
    return right

print(searchInsert_demo([1,3,5], 4)) #2


print(searchInsert_demo([1,3,5,6], 5)) #2

print(searchInsert_demo([1,3,5,6], 2)) #1

print(searchInsert_demo([1,3,5,6], 7)) #4

print(searchInsert_demo([1,3,5,6], 0)) #0
