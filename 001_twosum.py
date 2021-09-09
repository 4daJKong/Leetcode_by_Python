num  = [3,2,4,15]
targets = 6

# def twoSum(nums, target):
#     n = len(nums)
#     order = []
#     for i in range (0, n-1):
#         for j in range (i+1, n):
#             sumTwo = nums[i] + nums[j]
#             if sumTwo == target:
#                 order.append(i)
#                 order.append(j)
#     return order


#using hashmap to reduce time complexity from n^2 to n
def twoSum(nums, target):
    hash_map = {}
    n = len(nums)
    for i in range (0, n):
        t = target - nums[i]
        if t not in hash_map:
            hash_map[nums[i]] = i
            print(hash_map)
        else:
            return [hash_map[t], i]

print(twoSum(num, targets))