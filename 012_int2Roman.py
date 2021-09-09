class Solution:
    def intToRoman(self, num: int) -> str:
        dict_rom = {5000:'MMMMM',4000:'MMMM',3000:'MMM',2000:'MM',1000:'M',        
        900:'CM',800:'DCCC',700:'DCC',600:'DC',500:'D',400:'CD',300:'CCC',200:'CC',100:'C',
        90:'XC',80:'LXXX',70:'LXX',60:'LX',50:'L',40:'XL',30:'XXX',20:'XX',10:'X',
        9:'IX',8:'VIII',7:'VII',6:'VI',5:'V',4:'IV',3:'III',2:'II',1:'I'}

        list_num = list(str(num))
        n = len(list_num)
        res = ''
        for i in range(n - 1, -1, -1):
            
            factor = 10**(n-i-1)
            #print(list_num[i])
            if  int(list_num[i]) != 0:
                res = dict_rom[int(list_num[i]) * factor] + res       
        return res
    def intToRoman_demo(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        res = ""
        
        for i in d:
            res += (num//i) * d[i]    #9//2 = 4, 10//2 = 5, 7//3 = 2
            num = num % i
        
        return res


print(Solution().intToRoman_demo(10))
print(Solution().intToRoman_demo(3))
print(Solution().intToRoman_demo(101))
# print(Solution().intToRoman(4))
# print(Solution().intToRoman(9))
# print(Solution().intToRoman(58)) #LVIII
# print(Solution().intToRoman(1994)) #MCMXCIV




# one_un = int(num % 10)
# ten_un = int(num / 10 % 10) * 10
# hun_un = int(num / 100 % 10) * 100
# tho_un = int(num / 1000) * 1000


