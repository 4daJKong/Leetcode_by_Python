# def isPalindrome(x):
#     if x >= 0:
#         res = 0
#         t = x
#         while (t != 0):
#             res = 10 * res + t % 10
#             t = int(t / 10)
#         if res == x:
#             return True
#         else:
#             return False
#     else: 
#         return False

def isPalindrome(x):
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False
    res = 0
    while (x > res):
        res = res * 10 + x % 10
        x = int(x / 10)
    return (x == res) or (x == int(res / 10))




while(True):
    input1 = int(input())
    print(isPalindrome(input1))
