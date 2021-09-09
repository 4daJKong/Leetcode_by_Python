
class Solution:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates, reverse=False)
        result = []
        tmp_list = []
        
        self.dfs(candidates, tmp_list, target, result)
        return result
        


    def dfs(self, candidates, path, diff, res):   
        if diff == 0:
            res.append(path)
            #return
        elif diff < 0:
            return
        else:
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue 
                self.dfs(candidates[i + 1:], path + [candidates[i]], diff - candidates[i], res)


    def combinationSum2_demo(self, candidates, target):
        #dynamic programming but I didn't understand XD#

        # candidates.sort()
        # table = [None] + [set() for i in range(target)]
        # for i in candidates:
        #     if i > target:
        #         break
        #     for j in range(target - i, 0, -1):
        #         table[i + j] |= {elt + (i,) for elt in table[j]}
        #     table[i].add((i,))
        # return list(map(list, table[target]))
        #same like below

        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    #print("prev",prev)
                    dp[t].add(prev + (num,))
                    print(dp)
        return list(map(list, dp[-1]))
        

        




#print(Solution().combinationSum2_demo(candidates = [10,1,2,7,6,1,5], target = 8)) #[[1,1,6],[1,2,5],[1,7],[2,6]]
print(Solution().combinationSum2_demo(candidates = [2,5,2,1,2], target = 5)) #[[1,2,2],[5]]