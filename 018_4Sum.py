class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)     
        res = []
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k = j + 1           
                l = n - 1             
                while(k < l):
                    
                    temp = []
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        #print(i,j,k,l)
                        
                            
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[k])
                        temp.append(nums[l])
                        res.append(temp)
                        while(k < l and nums[k] == nums[k + 1]):
                            k = k + 1
                        while(k < l and nums[l] == nums[l - 1]):
                            l = l - 1
                        k = k + 1
                        l = l - 1
                        

                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l = l - 1
                    else:
                        k = k + 1        
        return res


print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))  #[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum(nums = [-2,-1,-1,1,1,2,2], target = 0)) #[[-2,-1,1,2],[-1,-1,1,1]]


