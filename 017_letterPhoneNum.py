import copy
class Solution:
    def letterCombinations(self, digits):
        dig_dict = {'1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
            '0':""}
        res = []
        temp = [] 
        cnt = 0
        for digit in digits:
            if digit == '1':
                continue
            #print(digit)    
            for letter in dig_dict[digit]:
                print(letter)
                if cnt == 0:
                    res.append(letter)
                else:
                   
                    
                    for item in res:
                        item = item + letter
                        temp.append(item)
                    
            if temp != []:
                res = temp
                temp = []
            #print(res)
            #print(temp)
            #temp = []                       
            cnt = cnt + 1  
        return res




print(Solution().letterCombinations(digits = "23"))  #["ad","ae","af","bd","be","bf","cd","ce","cf"]
#print(Solution().letterCombinations(digits = ""))
#print(Solution().letterCombinations(digits = "2"))
        