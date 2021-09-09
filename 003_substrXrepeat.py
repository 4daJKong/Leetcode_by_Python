class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_sub = {}
        n = len(s)
        if n == 1:
            return 1
        left = 0
        len_sub = 0
        for right in range(0, n):
            if s[right] in dict_sub:
                left = max(left, dict_sub[s[right]] + 1)
            len_sub = max(len_sub, right - left + 1)
            dict_sub[s[right]] = right
    
                
        return len_sub

        


print(Solution().lengthOfLongestSubstring(s = "abcabcbb")) #3
print(Solution().lengthOfLongestSubstring(s = "bbbbb"))   #1
print(Solution().lengthOfLongestSubstring(s = "pwwkew"))  #3
print(Solution().lengthOfLongestSubstring(s = "dvdf"))    #3
print(Solution().lengthOfLongestSubstring(s = ""))   #0
print(Solution().lengthOfLongestSubstring(s = " "))   #1
print(Solution().lengthOfLongestSubstring(s ="tmmzuxt")) #5




                
    