class Solution:
    def combinationSum(self, candidates, target):
        result = []
        tmp_list = []
        self.dfs(candidates, tmp_list, target, result)
        return result

    def dfs(self, candidates, path, diff, res):    
    
        if diff == 0:
            res.append(path)
            return
        elif diff < 0:
            return                  
        else:
            for i in range(len(candidates)):   
                self.dfs(candidates[i:], path + [candidates[i]], diff - candidates[i], res)
#有个问题是我把diff == 0 和 diff<0  放到了for 里面，但是结果就不行，不知道为什么

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7)) #[[2,2,3],[7]]
print(Solution().combinationSum(candidates = [2,3,5], target = 8)) #[[2,2,2,2],[2,3,3],[3,5]]
print(Solution().combinationSum(candidates = [2], target = 1)) #[]
print(Solution().combinationSum(candidates = [1], target = 1)) #[[1]]
print(Solution().combinationSum(candidates = [1], target = 2)) #[[1,1]]


   







     

