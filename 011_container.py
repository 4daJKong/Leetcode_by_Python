class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        res = 0
        for i in range (0, n - 1):
            for j in range(1, n):
                con_hei = min(height[i], height[j])
                res = max(res, con_hei * (j - i)) 

        return res

    def maxArea_demo(self, height) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return res

    def maxArea_demo2(self, height) -> int:
        left = 0 
        right = len(height) - 1
        res = 0
        for width in range(len(height) - 1, 0, -1):
            if height[left] > height[right]:
                res = max(res, width * height[right])
                right = right - 1
            else:
                res = max(res, width * height[left])
                left = left + 1

        return res
        
            

             


print(Solution().maxArea_demo2([1,8,6,2,5,4,8,3,7])) #49
print(Solution().maxArea_demo2([1,1])) #1
print(Solution().maxArea_demo2([4,3,2,1,4])) #16
print(Solution().maxArea_demo2([1,2,1])) #2
