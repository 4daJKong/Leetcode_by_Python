def findLength(A, B):
    n = len(A)
    m = len(B)

    
    dp =  [[0 for k in range(m + 1)] for l in range(n + 1)]
    lm = 0  #length of max in each row 
    
    for i in range (1, n+1):

        for j in range (1, m+1):
            
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                lm = max(lm, dp[i][j])
    return lm




A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(findLength(A,B))