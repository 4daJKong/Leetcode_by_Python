import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        #print(s)
        s = re.findall(r'(^[\+\-0]*\d+)\D*', s)
        try:
            res = int(''.join(s))
            #print(res)
            int_max = 2**31 - 1
            int_min = - 2**31
            if res > int_max:
                return int_max
            elif res < int_min:
                return int_min
            else:
                return res
        except:
            return 0

print(Solution().myAtoi("42"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))