# def integerBreak_demo(n):

#     dp = [-1] * (n+1)
#     dp[0] = 1
#     for i in range(1, n+1):
#         for j in range(1, i):
#             dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
#     return dp[-1]

def integerBreak(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:   
        dp = [0 for i in range (n - 1)]
        dp[0] = 1 #sum = 2 = 1+1
        dp[1] = 2 #sum = 3 = 1+2

        l = int(n / 2 + n % 2)
        for j in range(4, n + 1):
            for i in range(2, l + 1):           
                t = i * max (j - i, dp[j - i - 2])              
                if t > dp[j - 2]:
                    dp[j - 2] = t
        return dp[j - 2]






