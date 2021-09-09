class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        srt_nums = sorted(nums)
        
        res = 0
        min3 = float('inf')
        for i in range (0, n - 2):

        
            j = i + 1
            k = n - 1
                   
           
            while (j < k):
                temp = srt_nums[i] + srt_nums[j] + srt_nums[k] 
                if min3 > abs(target - temp):
                    min3 = abs(target - temp)
                    res = temp

                if temp < target:
                    j = j + 1
                    
                elif temp > target:
                    k = k - 1
                else:
                    return target

        return res
    



print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)) #2
print(Solution().threeSumClosest(nums = [1,1,1,1], target = 0)) #3

print(Solution().threeSumClosest(nums =[0,2,1,-3], target = 1)) #0

