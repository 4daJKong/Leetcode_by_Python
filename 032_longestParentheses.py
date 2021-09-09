class Solution:
    def longestValidParentheses(self, s: str) -> int:
        temp_len = 0
        max_len = 0
        start = 0 
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    start = i + 1
                else:
                    stack.pop()
                    if stack == []:
                        temp_len = i - start + 1
                        max_len = max(temp_len, max_len)
                    else:
                        temp_len = i - stack[-1]
                        max_len = max(temp_len, max_len)



 
        return max_len

 
print(Solution().longestValidParentheses(s = "()("))  #2
print(Solution().longestValidParentheses(s = "(())"))  #4
print(Solution().longestValidParentheses(s = "()((())")) #4
print(Solution().longestValidParentheses(s = "(()"))  #2
print(Solution().longestValidParentheses(s = ")()())")) #4
print(Solution().longestValidParentheses(s = "(())())"))
print(Solution().longestValidParentheses(s = "(()())"))
print(Solution().longestValidParentheses(s = ""))


