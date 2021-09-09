class Solution:
    def generateParenthesis_my(self, n):
        dict_pare = {'(':')'}
       
        list_p = []
        for i in range (2**(2*n)):
            item = bin(i)[2:].zfill(2 * n)
            item = item.replace("0","(")
            item = item.replace("1",")")
            l_s = []
            res = True  
            for i in range(0, 2 * n):
            
                if item[i] in dict_pare:
                    l_s.append(dict_pare[item[i]])
                elif l_s and l_s[-1] == item[i]:
                    l_s.pop() 
                else:
                    res = False                  
            if l_s == [] and res:
                list_p.append(item)
        
        return list_p

    def generateParenthesis(self, n):
        dp = [[] for i in range(n + 1)]
        print(dp)
        dp[0].append('')
        print(dp)
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                print(dp[i])
        return dp[n]

print(Solution().generateParenthesis(n = 3))
# print(Solution().generateParenthesis(n = 1))
# print(Solution().generateParenthesis(n = 2))
# print(Solution().generateParenthesis(n = 4))



"""
class Solution {
public:
    vector<string> generateParenthesis(int n);
};
// dp as binary tree generate
vector<string> Solution::generateParenthesis(int n) {
    vector<vector<string>> dp(n + 1, vector<string>());
    dp[0] = {""};
    for (int i = 1; i <= n; ++i) { // total
        for (int left = 0; left <= i - 1; ++left) { // left tree size
            int right = i - 1 - left;
            for (int l = 0; l < dp[left].size(); ++l) {
                for (int r = 0; r < dp[right].size(); ++r) {
                    dp[i].push_back("(" + dp[left][l] + ")" + dp[right][r]);
                }
            }
        }
    }
    return dp[n];
}
"""