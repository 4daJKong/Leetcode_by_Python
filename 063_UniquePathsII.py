class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):                
        m = len(obstacleGrid) #row 
        n = len(obstacleGrid[0]) #col
        #print(m,n)

        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1

        for j in range(n):
            for i in range(m):                            
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        continue            
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                   
        return dp[m - 1][n - 1]


#当计算第一行的时候dp[-1][j]实际上就是最后一行的dp，也就是0.
#同样的，dp[i][-1]实际上是最后一列的dp，但是还没遍历到过，所以也是0.
#总之，虽然dp数组在计算第一行和第一列的时候用到了最后一行最后一列的dp数据，
#但是由于还没有遍历到，那么dp数组实际上是0，所以完全可以省去判断。
    

print(Solution().uniquePathsWithObstacles([[1]])) #0
print(Solution().uniquePathsWithObstacles([[0,1],[1,0]])) #0
print(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]])) #0
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) #2
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]])) #1
print(Solution().uniquePathsWithObstacles([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],
[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],
[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]])) #0        

            




