def myPow(x, n):
    return x ** n

#use log func
def myPow_demo(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0 and n > 0:
        return myPow_demo(x * x, n / 2)
    elif n > 0:
        return myPow_demo(x, n - 1) * x
    else:
        return 1 / myPow_demo(x, -n) 



print(myPow_demo(2, 10)) #1024
print(myPow_demo(x = 2.10000, n = 3)) #9.26100
print(myPow_demo(x = 2.00000, n = -2))













# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         elif n % 2 == 0 and n > 0:
#             return self.myPow(x * x, n / 2)
#         elif n > 0:
#             return self.myPow(x, n - 1) * x
#         else:
#             return 1 / self.myPow(x, -n) 