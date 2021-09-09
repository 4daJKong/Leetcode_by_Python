class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = []
        for i in range (0, n):
            # if i == 3:
            #     print(res)
            
            temp_odd = []
            temp_even = []
            temp = []
            
            
            j = 0
            temp_odd.append(s[i])
            while (s[i - j] == s[i + j]): 
                if j != 0:
                    temp_odd.append(s[i + j])                   
                    temp_odd.insert(0, s[i - j])
                j = j + 1                
                if (i - j < 0 or i + j >= n):
                    break



            j = 0
            if i + 1 < n and s[i] == s[i + 1]:
                temp_even.append(s[i])
                temp_even.append(s[i + 1])
                while(s[i - j] == s[i + 1 + j]):                   
                    if j != 0:
                        temp_even.insert(0, s[i - j])
                        temp_even.append(s[i + 1 + j])           
                    j = j + 1 
                    if i - j < 0 or i + j + 1 >= n:
                        break

            if len(temp_odd) >= len(temp_even):
                temp = temp_odd
            else:
                temp = temp_even
            if len(temp) > len(res):
                res = temp
        
        return "".join(res)

    def longestPalindrome_demo(self, s: str) -> str:
        res = ''
        n = len(s)
        for i in range(0, n):
            for j in range(n, i, -1):
                if len(res) >= j - i:
                    break
                elif s[i: j] == s[i: j][::-1]:
                    res = s[i: j]
        
        return res




        
print(Solution().longestPalindrome_demo(s = "bananas")) #anana
print(Solution().longestPalindrome_demo(s = "cbaabf")) #baab
print(Solution().longestPalindrome_demo(s = "babad")) 
print(Solution().longestPalindrome_demo(s = "bbbbb"))
print(Solution().longestPalindrome(s = "cbbd")) 
print(Solution().longestPalindrome(s = "a")) 
print(Solution().longestPalindrome(s = "ac")) 
print(Solution().longestPalindrome(s = "abracadabra"))  
print(Solution().longestPalindrome(s = "aba"))
print(Solution().longestPalindrome_demo(s = "abba"))
print(Solution().longestPalindrome_demo(s = "level"))  







    # def longestPalindrome_demo(self, s: str) -> str: 

    #     T = '#'.join('^{}$'.format(s))
    #     # T = s
    #     P = [0] * len(T)
    #     R, C = 0, 0
    #     for i in range(1,len(T) - 1):
    #         if i < R:
    #             P[i] = min(P[2 * C - i], R - i)
            
    #         while T[i+(P[i]+1)] == T[i-(P[i]+1)]:
    #             P[i] += 1
            
    #         if i + P[i] > R:
    #             R, C = i + P[i], i
    #     return P




    
 

