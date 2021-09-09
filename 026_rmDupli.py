def removeDuplicates(nums):
    n = len(nums)
    i = n - 1
    while (i > 0) and (n > 1):
        
        if nums[i] == nums[i - 1]:
            del nums[i]
            n = n - 1
            i = n - 1
        else:
            i = i - 1
    return nums

def removeDuplicates_demo(nums):
    n = len(nums)
    i = 0
    for j in range(1, n):
        #print("i:",nums[i], "j:", nums[j])
        if nums[i] != nums[j]:
            print(nums[i])
            i = i + 1
            print(nums[i])
            print(nums[j])
            nums[i] = nums[j]
            print('s:',nums)
    return i + 1





num1 = [1,1,2]
num2 = [0,0,1,1,1,2,2,3,3,4]
num3 = [1,1]
num4 = [1,2,2,3,4]
# print(removeDuplicates(num1))
# print(removeDuplicates(num2))
# print(removeDuplicates(num3))
# print(removeDuplicates(num4))

# print(removeDuplicates_demo(num1))
# print(removeDuplicates_demo(num2))
# print(removeDuplicates_demo(num3))
print(removeDuplicates_demo(num4))
