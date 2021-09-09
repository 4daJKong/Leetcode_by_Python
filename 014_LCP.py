

#only under same order, it can be found the lcp#
def longestCommonPrefix(strs):
    res = ''
    for t in zip(*strs):
        
        if len(set(t)) == 1:
            res = res + t[0]
        else:
            break
    return res


input1 = ['flower','owflow','flight']
input2 = ["dog","racecar","car"]
input3 = ["leetcode", "leet", "lee", "le"]
input4 = ["abcdxyz", "xyzabcd"]
#print(longestCommonPrefix(input3))

#can find all lcp in any order

def findLength(strs):
    ###opq
    res = strs[0]
    seq = 1
    while (seq < len(strs)):
        n = len(res)
        m = len(strs[seq])
        res = ''
        
        dp =  [[0 for k in range(m + 1)] for l in range(n + 1)]
        lm = 0  #length of max in each row 
        
        for i in range (1, n+1):
            t = ''
            for j in range (1, m+1):
                
                if strs[0][i-1] == strs[1][j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    #lm = max(lm, dp[i][j])
                    if dp[i][j] > lm:
                        t =  strs[0][i-1]
                        lm = dp[i][j]
            res = res + t
        seq = seq + 1
        if res == 0:
            break
    return res

print(findLength(input4))
#print(input3[0])

