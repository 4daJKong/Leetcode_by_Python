class Solution:
    def uniquePaths_combination(self, m: int, n: int) -> int:      
        res = 1
        prod1 = 1
        prod2 = 1
        for i in range(m - 1, 0, -1):
            prod1 = prod1 * i
        for j in range(m + n -2, n - 1, -1):
            prod2 = prod2 * j
        res = prod2/prod1
        return int(res)

    def uniquePaths(self, m: int, n: int) -> int:   
        dp = [[1 for i in range(m)] for j in range(n)]
        for i in range (1, n):
            for j in range(1, m):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]   
  

print(Solution().uniquePaths(m = 3, n = 7)) #28
print(Solution().uniquePaths(m = 3, n = 2)) #3
print(Solution().uniquePaths(m = 7, n = 3)) #28
print(Solution().uniquePaths(m = 3, n = 3)) #6






