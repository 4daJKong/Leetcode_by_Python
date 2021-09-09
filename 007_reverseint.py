from math import pow
# def reverse(x):      
#     temp = []
#     if x < 0:
#         x = -1 * x
#         sig = -1
#     else:
#         sig = 1        
#     l_x = [int(j) for j in str(x)]
#     n = len(l_x)
#     for i in range(0, n):
#         temp.append(l_x[n-i-1])  
#     temps = [str(k) for k in temp]
#     int_x = sig * int("".join(temps))
#     if -pow(2,31) < int_x < pow(2,31)-1:      
#         return int_x
#     else:
#         return 0

def reverse(x):
    t = abs(x)
    res = 0
    while (t != 0):
        res = 10 * res + t % 10
        t = int(t / 10)
    if (res <= 2**31-1 and res >= -2**31):
        if x >= 0:
            return res
        else: 
            return -res
    else:
        return 0
    
    
  


# the third way is to use str[::-1]


input1 = int(input())
print(reverse(input1))