class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        l = 2 * numRows - 2
        if l == 0:
            return s
        for i in range (0, numRows):
            temp = i
            while (i < len(s)):
                res = res + s[i]
                if (i % l) != 0 and (i % l) != (numRows - 1):
                    if i + (numRows - temp - 1) * 2 < len(s):
                        res = res + s[i + (numRows - temp - 1) * 2]


                i = i + l 
  

        return res


print(Solution().convert(s = "A", numRows = 1))


#print(Solution().convert(s = "PAYPALISHIRING", numRows = 3)) #PAHNAPLSIIGYIR
#print(Solution().convert(s = "PAYPALISHIRING", numRows = 4)) #PINALSIGYAHRPI
