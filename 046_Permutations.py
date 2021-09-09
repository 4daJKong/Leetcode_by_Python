class Solution:
    def permute(self, nums):
        res = [[]]
     
        for i in range(0, len(nums)):
            tmp3 = res.copy()
            res = []
            for j in range(len(tmp3)):
                tmp1 = tmp3[j].copy()
                #print(tmp1)
                for k in range(len(tmp1) + 1):
                    tmp2 = tmp1.copy()
                    tmp2.insert(k, nums[i])
                    
                    res.append(tmp2)

        return res

    def permute_demo(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            
            # return # backtracking
        for i in range(len(nums)):
            print("i",i,nums[:i], nums[i+1:], path, [nums[i]])
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
           

print(Solution().permute_demo([1,3,5])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

   


# nums = [4,5,6,7,8]

# res = [[]]
# #res = [[5, 4], [4, 5]]
# for i in range(0, len(nums)):
#     tmp3 = res.copy()
#     res = []
#     for j in range(len(tmp3)):
#         tmp1 = tmp3[j].copy()
#         #print(tmp1)
#         for k in range(len(tmp1) + 1):
#             tmp2 = tmp1.copy()
#             tmp2.insert(k, nums[i])
#             #print(tmp2)
#             res.append(tmp2)
# print(res)
# print(len(res))
        



