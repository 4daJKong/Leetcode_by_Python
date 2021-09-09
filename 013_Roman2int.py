# def romanToInt(s):
#     res = 0
#     dict_rom = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#     n = len(s)
#     i = 0
#     while (i < n):
#         t = 0        
#         if i < (n-1) :
#             if dict_rom[s[i]] < dict_rom[s[i+1]]:
#                 t = dict_rom[s[i+1]] - dict_rom[s[i]]
#                 res = res + t
#                 i = i + 2 
#             else:
#                 res = res + dict_rom[s[i]]
#                 i = i + 1
#         else:
#             res = res + dict_rom[s[i]]
#             break                  
#     return res


def romanToInt(s):   
    dict_rom = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res = dict_rom[s[-1]]
    N = len(s)
    for i in range (N - 2, -1, -1):
        if dict_rom[s[i]] < dict_rom[s[i + 1]]:
            res = res - dict_rom[s[i]]
        else:
            res = res + dict_rom[s[i]]
    return res




while (True):

    input1 = input()
    print(romanToInt(input1))
