from collections import Counter
class Solution:
    def permuteUnique(self, nums):
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
                    if  k < len(tmp1) and tmp1[k] == nums[i]: 
                        break  

        return res


    def permuteUnique_demo(self, nums):
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
    def permuteUnique_demo2(self, nums):
        ans = [[]]
        for n in nums:
            print("n",n)
            new_ans = []
            for l in ans:
                print("l",l)
                for i in range(len(l) + 1):
                   
                    new_ans.append(l[:i]+[n]+l[i:])
                    print(l[:i],l[i:])
                    print("new ans",new_ans)
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans

        return ans

     
 

print(Solution().permuteUnique([4,5,5])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permuteUnique([2,2,1,1]))  #[[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
   


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
        



