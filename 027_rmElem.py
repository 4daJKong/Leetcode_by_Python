def removeElement(nums, val):
    n = len(nums)
    i = 0 
    for j in range (0, n):
        if nums[j] != val:
             
            nums[i] = nums[j]
            i = i + 1
                      
    return i




print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
